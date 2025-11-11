# transform.py (v5) -- Transforms a Markdown document into JSON using an LLM

#!/usr/bin/env python3
"""
Deterministic Markdown → JSON transformer (generic, rule-aware)
---------------------------------------------------------------
- Runs a deterministic prompt against an LLM and writes JSON to file.
- Provides an authoritative HINTS block so the model preserves IDs,
  section order, and required/format fields across ANY Markdown doc type.
- Writes sidecars for reproducibility and parity validation.
- Explicitly flags if any section objects contain a 'group' key (schema violation).

Backends:
  - OpenAI API: set LLM_BACKEND=openai and OPENAI_API_KEY
  - OpenRouter: set LLM_BACKEND=openrouter and OPENROUTER_API_KEY

Required env:
  - MODEL (e.g., "gpt-4o", "gpt-5-2025-08-07", or "openai/gpt-4o" on OpenRouter)

Optional env:
  - SEED (default: 1234)
  - ALLOW_SAMPLING_PARAMS=1 to include sampling params (disabled for GPT-5 by default)
  - TEMPERATURE / TOP_P / PRESENCE_PENALTY / FREQUENCY_PENALTY (floats)
  - OPENAI_BASE_URL, OPENROUTER_BASE_URL
  - MAX_TOKENS (int) — caps model output tokens
  - PROMPT_PATH — alternate prompt location (overrides --prompt)
  - HINTS_MODE — "append" (default) | "none"
  - RULES_SIDECAR=1 — write <out>.rules-check.json
  - META_SIDECAR=1  — write <out>.meta.json

Usage:
  python transform.py input.md output.json [--prompt path/to/prompt.md]
"""
import os
import sys
import re
import json
import time
import hashlib
import argparse
from typing import Dict, List, Set, Tuple
import requests

# ---------- Regexes ----------
BACKTICK_ID = re.compile(r'`([A-Z0-9]+(?:-[A-Z0-9]+)+)`')
COMMENT_GROUP = re.compile(r'<!--\s*group:\s*([A-Z0-9]+(?:-[A-Z0-9]+)+)\s*-->')
COMMENT_ID = re.compile(r'<!--\s*([A-Z0-9]+(?:-[A-Z0-9]+)+)\s*-->')
FRONTMATTER = re.compile(r"^---\n(.*?)\n---", re.DOTALL | re.MULTILINE)
HEADING = re.compile(r'^\s*(#{1,6})\s+(.*?)\s*$')

# ---------- IO helpers ----------
def read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_text(path: str, text: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def strip_json_fence(s: str) -> str:
    s2 = s.strip()
    if s2.startswith("```"):
        i = s2.find("\n")
        j = s2.rfind("```")
        if i != -1 and j != -1 and j > i:
            return s2[i+1:j].strip()
    return s2

# ---------- Markdown parsing (hints) ----------
def parse_frontmatter_keys(md: str) -> List[str]:
    m = FRONTMATTER.search(md)
    if not m:
        return []
    block = m.group(1)
    keys: List[str] = []
    for line in block.splitlines():
        ls = line.strip()
        if not ls or ls.startswith("#"):
            continue
        if ":" in ls:
            k = ls.split(":", 1)[0].strip()
            if k:
                keys.append(k)
    return keys

def parse_section_table(md: str) -> List[Dict[str, str]]:
    """
    Returns ordered list:
      [{"id": "PROC-TITLE", "title": "Title", "required": "Yes|No|Forbidden", "format": "H1"}, ...]
    """
    lines = md.splitlines()
    table_lines: List[str] = []
    in_table = False
    for line in lines:
        if line.strip().startswith("|"):
            table_lines.append(line.rstrip())
            in_table = True
            continue
        if in_table:
            if not line.strip().startswith("|"):
                break
            table_lines.append(line.rstrip())
    # Remove alignment rows like | --- |
    rows = [r for r in table_lines if not re.match(r'^\|\s*:?-', r)]
    if not rows:
        return []
    def split_row(r: str) -> List[str]:
        return [c.strip() for c in r.strip("|").split("|")]
    header = split_row(rows[0])
    data = [split_row(r) for r in rows[1:]]
    result: List[Dict[str, str]] = []
    for cols in data:
        if len(cols) < 4:
            continue
        title, fmt, req, id_cell = cols[:4]
        m = BACKTICK_ID.search(id_cell)
        sid = m.group(1) if m else id_cell.strip()
        result.append({
            "id": sid,
            "title": title,
            "required": req,
            "format": fmt or ""
        })
    return result

def extract_rule_ids_exact(md: str) -> List[str]:
    """
    Returns ordered list of rule IDs from rule lines (NOT headings).
    Duplicates preserved (for -DUP-n expectation).
    """
    ids: List[str] = []
    for m in COMMENT_ID.finditer(md):
        token = m.group(1)
        # locate the full source line containing the comment
        line_start = md.rfind("\n", 0, m.start())
        line_end = md.find("\n", m.end())
        if line_start == -1:
            line_start = 0
        else:
            line_start += 1
        if line_end == -1:
            line_end = len(md)
        line = md[line_start:line_end]
        if "group:" in line:
            continue  # skip group markers
        if HEADING.match(line):
            continue  # skip section headings
        ids.append(token)
    return ids

def map_groups_to_headings(md: str) -> Dict[str, str]:
    """
    Returns {"PROC-OVERVIEW": "Overview", ...} using the nearest preceding heading text
    for each <!-- group: TOKEN -->.
    """
    lines = md.splitlines()
    last_heading_text = ""
    heading_by_line: Dict[int, str] = {}
    for i, line in enumerate(lines):
        hm = HEADING.match(line)
        if hm:
            text = re.sub(r"\s*<!--.*?-->\s*", "", hm.group(2)).strip()
            last_heading_text = text
        heading_by_line[i] = last_heading_text
    groups: Dict[str, str] = {}
    for i, line in enumerate(lines):
        for g in COMMENT_GROUP.findall(line):
            groups[g] = heading_by_line.get(i, "") or ""
    return groups

# ---------- HTTP + payload ----------
def build_messages(prompt: str, markdown: str, hints: Dict) -> List[Dict]:
    system_msg = {
        "role": "system",
        "content": (
            "You convert Markdown into JSON strictly per the provided instructions. "
            "Be mechanical and deterministic. Do not invent fields. Preserve every UPPERCASE rule id verbatim."
        ),
    }
    user_prompt = {"role": "user", "content": prompt}
    user_md = {
        "role": "user",
        "content": "Here is the Markdown document to convert:\n\n```markdown\n" + markdown + "\n```",
    }
    msgs = [system_msg, user_prompt, user_md]
    if os.environ.get("HINTS_MODE", "append") != "none" and hints:
        msgs.append({
            "role": "user",
            "content": (
                "Authoritative hints for determinism (use; do not echo):\n\n"
                "```json\n" + json.dumps(hints, ensure_ascii=False, indent=2) + "\n```"
            ),
        })
    return msgs

def build_payload(model: str, messages: List[Dict]) -> Dict:
    payload = {
        "model": model,
        "response_format": {"type": "json_object"},
        "messages": messages,
        "seed": int(os.environ.get("SEED", "1234")),
    }
    allow_sampling = os.environ.get("ALLOW_SAMPLING_PARAMS", "0") == "1"
    is_gpt5 = "gpt-5" in model
    if allow_sampling and not is_gpt5:
        if "TEMPERATURE" in os.environ:
            payload["temperature"] = float(os.environ["TEMPERATURE"])
        if "TOP_P" in os.environ:
            payload["top_p"] = float(os.environ["TOP_P"])
        if "PRESENCE_PENALTY" in os.environ:
            payload["presence_penalty"] = float(os.environ["PRESENCE_PENALTY"])
        if "FREQUENCY_PENALTY" in os.environ:
            payload["frequency_penalty"] = float(os.environ["FREQUENCY_PENALTY"])
    if "MAX_TOKENS" in os.environ:
        try:
            payload["max_tokens"] = int(os.environ["MAX_TOKENS"])
        except ValueError:
            pass
    return payload

def detect_backend():
    backend = os.environ.get("LLM_BACKEND", "openai").lower()
    model = os.environ.get("MODEL")
    if not model:
        print("Missing MODEL environment variable.", file=sys.stderr)
        sys.exit(2)
    if backend == "openai":
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            print("Missing OPENAI_API_KEY", file=sys.stderr)
            sys.exit(2)
        base = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1")
        url = base.rstrip("/") + "/chat/completions"
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    elif backend == "openrouter":
        api_key = os.environ.get("OPENROUTER_API_KEY")
        if not api_key:
            print("Missing OPENROUTER_API_KEY", file=sys.stderr)
            sys.exit(2)
        base = os.environ.get("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
        url = base.rstrip("/") + "/chat/completions"
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    else:
        print("LLM_BACKEND must be 'openai' or 'openrouter'", file=sys.stderr)
        sys.exit(2)
    return model, url, headers

def post_chat(url: str, headers: Dict, payload: Dict) -> requests.Response:
    return requests.post(url, headers=headers, json=payload, timeout=600)

def retryable_post(url: str, headers: Dict, payload: Dict, attempts: int = 3) -> requests.Response:
    last = None
    for i in range(attempts):
        resp = post_chat(url, headers, payload)
        if resp.status_code == 200:
            return resp
        if resp.status_code == 400 and "unsupported_value" in resp.text:
            for k in ("temperature", "top_p", "presence_penalty", "frequency_penalty"):
                payload.pop(k, None)
            last = resp
            continue
        if resp.status_code >= 500 or resp.status_code in (408, 429):
            time.sleep(1.5 * (i + 1))
            last = resp
            continue
        last = resp
        break
    return last if last is not None else resp

# ---------- Sidecars (parity + metadata) ----------
def _collect_json_ids(obj: Dict) -> Tuple[List[str], List[str]]:
    sections = []
    rules = []
    for s in obj.get("sections", []) or []:
        sid = s.get("id")
        if isinstance(sid, str):
            sections.append(sid)
        for r in s.get("rules", []) or []:
            rid = r.get("id")
            if isinstance(rid, str):
                rules.append(rid)
    for blk in obj.get("forbidden", []) or []:
        for r in blk.get("rules", []) or []:
            rid = r.get("id")
            if isinstance(rid, str):
                rules.append(rid)
    return sections, rules

def _expected_rule_ids_with_dups(rule_ids_exact: List[str]) -> List[str]:
    counts: Dict[str, int] = {}
    out: List[str] = []
    for rid in rule_ids_exact:
        c = counts.get(rid, 0)
        if c == 0:
            out.append(rid)
        else:
            out.append(f"{rid}-DUP-{c}")
        counts[rid] = c + 1
    return out

def _examples_quality(obj: Dict) -> Dict[str, List[str]]:
    leaks = []
    too_many = []
    too_long = []
    ex_pat = re.compile(r"\b(for example|e\.g\.|instead of|rather than)\b", re.IGNORECASE)
    for s in obj.get("sections", []) or []:
        # flag schema violation: section-level 'group'
        if isinstance(s, dict) and "group" in s:
            leaks.append(f"SECTION_HAS_GROUP:{s.get('id')}")
        for r in s.get("rules", []) or []:
            rid = r.get("id", "")
            desc = r.get("description", "") or ""
            exs = r.get("examples", []) or []
            if ex_pat.search(desc):
                too_many.append(f"DESC_LEAKS:{rid}")
            if isinstance(exs, list) and len(exs) > 2:
                too_many.append(f"EX_GT2:{rid}")
            for x in exs:
                if isinstance(x, str) and len(x) > 160:
                    too_long.append(rid)
    return {
        "schema_section_has_group": [x.replace("SECTION_HAS_GROUP:", "") for x in leaks if x.startswith("SECTION_HAS_GROUP:")],
        "description_leaks_examples": [x.replace("DESC_LEAKS:", "") for x in too_many if x.startswith("DESC_LEAKS:")],
        "examples_count_gt2": [x.replace("EX_GT2:", "") for x in too_many if x.startswith("EX_GT2:")],
        "examples_item_gt160chars": too_long,
    }

def _sections_table_mismatches(obj: Dict, sections_table: List[Dict[str, str]]) -> List[Dict]:
    want_by_id = {s["id"]: s for s in sections_table}
    got_by_id = {s.get("id"): s for s in obj.get("sections", []) or []}
    mismatches = []
    for sid, want in want_by_id.items():
        got = got_by_id.get(sid)
        if not got:
            mismatches.append({"type": "section_missing_in_json", "id": sid})
            continue
        # title
        if (got.get("title") or "") != (want["title"] or ""):
            mismatches.append({"type": "title_mismatch", "id": sid, "want": want["title"], "got": got.get("title")})
        # required mapping (Yes/No/Forbidden → required/optional/forbidden)
        got_req = got.get("required")
        got_req_norm = {"required": "Yes", "optional": "No", "forbidden": "Forbidden"}.get(got_req, got_req)
        if got_req_norm != want["required"]:
            mismatches.append({"type": "required_mismatch", "id": sid, "want": want["required"], "got": got_req})
        # format
        if (got.get("format") or "") != (want.get("format") or ""):
            mismatches.append({"type": "format_mismatch", "id": sid, "want": want.get("format", ""), "got": got.get("format", "")})
    return mismatches

def write_rules_sidecar(base_out: str, md: str, obj: Dict) -> None:
    sections_table = parse_section_table(md)
    section_ids_from_table = [s["id"] for s in sections_table]
    rule_ids_exact = extract_rule_ids_exact(md)

    json_section_ids, json_rule_ids = _collect_json_ids(obj)
    expected_rule_ids = _expected_rule_ids_with_dups(rule_ids_exact)

    missing_sections = sorted(set(section_ids_from_table) - set(json_section_ids))
    extra_sections = sorted(set(json_section_ids) - set(section_ids_from_table))

    missing_rules = [rid for rid in expected_rule_ids if rid not in json_rule_ids]
    extra_rules = [rid for rid in json_rule_ids if rid not in expected_rule_ids]

    quality = _examples_quality(obj)
    sections_mismatches = _sections_table_mismatches(obj, sections_table)

    report = {
        "sections": {
            "expected_from_table": section_ids_from_table,
            "json_section_ids": json_section_ids,
            "missing_in_json": missing_sections,
            "extra_in_json": extra_sections,
            "table_mismatches": sections_mismatches,
        },
        "rules": {
            "expected_from_rule_ids_exact": expected_rule_ids,
            "json_rule_ids": json_rule_ids,
            "missing_in_json": missing_rules,
            "extra_in_json": extra_rules,
        },
        "quality": quality,
    }
    write_text(base_out + ".rules-check.json", json.dumps(report, ensure_ascii=False, indent=2))

def write_meta_sidecar(base_out: str, meta: Dict) -> None:
    write_text(base_out + ".meta.json", json.dumps(meta, ensure_ascii=False, indent=2))

# ---------- Main ----------
def main():
    ap = argparse.ArgumentParser(description="Deterministic Markdown→JSON transformer (generic, rule-aware)")
    ap.add_argument("input_md", help="Path to input Markdown file")
    ap.add_argument("output_json", help="Path to output JSON file")
    ap.add_argument("--prompt", dest="prompt_path", help="Path to prompt.md (defaults to ./prompt.md)")
    args = ap.parse_args()

    prompt_path = os.environ.get("PROMPT_PATH") or args.prompt_path or os.path.join(os.path.dirname(__file__), "prompt.md")
    if not os.path.exists(prompt_path):
        print(f"Missing prompt file: {prompt_path}", file=sys.stderr)
        sys.exit(2)

    prompt = read_text(prompt_path)
    markdown = read_text(args.input_md)
    md_hash = sha256(markdown)

    # Hints
    fm_keys = parse_frontmatter_keys(markdown)
    sections_table = parse_section_table(markdown)
    section_ids_from_table = [s["id"] for s in sections_table]
    rule_ids_exact = extract_rule_ids_exact(markdown)
    group_headings = map_groups_to_headings(markdown)

    hints = {
        "md_sha256": md_hash,
        "front_matter_keys": fm_keys,
        "sections_table": sections_table,
        "section_ids_from_table": section_ids_from_table,
        "rule_ids_exact": rule_ids_exact,
        "group_headings": group_headings,
        "notes": [
            "Use rule_ids_exact as the authoritative list of rule IDs to emit.",
            "Only emit -DUP-n for the second+ occurrences of the same base ID in rule_ids_exact.",
            "Do not emit any rule ID not present in rule_ids_exact, except synthesized AUTO IDs for missing rule lines."
        ],
    }

    # Build and send request
    model, url, headers = detect_backend()
    messages = build_messages(prompt, markdown, hints)
    payload = build_payload(model, messages)
    resp = retryable_post(url, headers, payload, attempts=3)
    if not resp or resp.status_code != 200:
        status = resp.status_code if resp else "no_response"
        body = (resp.text[:1400] if resp and hasattr(resp, "text") else "")
        print("API error:", status, body, file=sys.stderr)
        sys.exit(1)

    data = resp.json()
    try:
        content = data["choices"][0]["message"]["content"]
    except Exception:
        print("Unexpected API response:", json.dumps(data)[:1400], file=sys.stderr)
        sys.exit(1)

    content_json = strip_json_fence(content)
    try:
        obj = json.loads(content_json)
    except json.JSONDecodeError as e:
        raw_path = args.output_json + ".raw.txt"
        write_text(raw_path, content)
        print("Model did not return valid JSON. Raw saved to:", raw_path, file=sys.stderr)
        print("Decode error:", e, file=sys.stderr)
        sys.exit(1)

    # Write main JSON
    write_text(args.output_json, json.dumps(obj, ensure_ascii=False, indent=2))
    print("Wrote:", args.output_json)

    # Sidecars
    base = args.output_json
    if os.environ.get("RULES_SIDECAR", "1") == "1":
        write_rules_sidecar(base, markdown, obj)
    if os.environ.get("META_SIDECAR", "1") == "1":
        meta = {
            "model": model,
            "backend": os.environ.get("LLM_BACKEND", "openai"),
            "seed": int(os.environ.get("SEED", "1234")),
            "prompt_path": os.path.abspath(prompt_path),
            "input_md_path": os.path.abspath(args.input_md),
            "output_json_path": os.path.abspath(args.output_json),
            "md_sha256": md_hash,
        }
        write_meta_sidecar(base, meta)

if __name__ == "__main__":
    main()