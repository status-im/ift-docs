#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OneDoc Markdown → JSON template transformer (LLM-assisted)
- Universal and template-agnostic
- Keeps existing behaviors; only adds safe guards to prevent container 'group' leakage
Usage:
  python3 transform.py INPUT.md OUTPUT.json [--prompt PROMPT.md]
Env:
  LLM_BACKEND=openai|openrouter (default: openai)
  MODEL=<model name>            (required)
  OPENAI_API_KEY                (for LLM_BACKEND=openai)
  OPENROUTER_API_KEY            (for LLM_BACKEND=openrouter)
  # Optional token limits (not set by default):
  MAX_COMPLETION_TOKENS=4096    (OpenAI new param)
  MAX_TOKENS=4096               (legacy param; avoided by default)
  OPENROUTER_MAX_TOKENS=4096    (OpenRouter 'max_tokens')
"""
import os, sys, json, re

# ---------- IO ----------
def load_text(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_text(path: str, content: str) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# ---------- CLI ----------
def parse_args(argv):
    if len(argv) < 3:
        print("Usage: python3 transform.py INPUT.md OUTPUT.json [--prompt PROMPT.md]", file=sys.stderr)
        sys.exit(2)
    input_md = argv[1]
    output_json = argv[2]
    prompt_path = None
    i = 3
    while i < len(argv):
        if argv[i] == "--prompt" and i + 1 < len(argv):
            prompt_path = argv[i+1]
            i += 2
        else:
            print(f"Unknown argument: {argv[i]}", file=sys.stderr)
            sys.exit(2)
    return input_md, output_json, prompt_path

def discover_prompt_path(script_dir: str, cli_prompt: str | None) -> str:
    if cli_prompt:
        if not os.path.exists(cli_prompt):
            print(f"--prompt file not found: {cli_prompt}", file=sys.stderr); sys.exit(2)
        return cli_prompt
    env_prompt = os.environ.get("PROMPT_PATH", "").strip()
    if env_prompt:
        if not os.path.exists(env_prompt):
            print(f"PROMPT_PATH not found: {env_prompt}", file=sys.stderr); sys.exit(2)
        return env_prompt
    for cand in ("md2json-prompt-templates.md", "prompt.md"):
        p = os.path.join(script_dir, cand)
        if os.path.exists(p):
            return p
    print("Prompt file not found. Tried --prompt, PROMPT_PATH, md2json-prompt-templates.md, prompt.md", file=sys.stderr)
    sys.exit(2)

# ---------- Inventory extraction (template-agnostic) ----------
_INV_GROUP = re.compile(r'<!--\s*group:\s*([A-Z0-9][A-Z0-9_-]*)\s*-->', re.IGNORECASE)
_INV_RULE  = re.compile(r'<!--\s*([A-Z0-9][A-Z0-9_-]*)\s*-->', re.IGNORECASE)

def _extract_id_inventory(md_text: str):
    """
    Build inventory of section container IDs and their rule IDs (order-preserving).
    Returns: (sections_map: dict[str, list[str]], all_rule_ids: set[str])
    """
    sections = {}
    allowed = set()
    current = None
    for line in md_text.splitlines():
        g = _INV_GROUP.search(line)
        if g:
            current = g.group(1).strip()
            sections.setdefault(current, [])
            continue
        r = _INV_RULE.search(line)
        if r:
            rid = r.group(1).strip()
            if rid.upper().startswith("GROUP:"):
                continue
            if current:
                sections.setdefault(current, [])
                sections[current].append(rid)
            allowed.add(rid)
    return sections, allowed

def _render_inventory_block(sections: dict, allowed: set) -> str:
    if not sections:
        return ""
    parts = []
    parts.append("### Canonical Rule-ID Inventory (extracted from this Markdown)\n")
    parts.append("Only use the following rule IDs exactly as written. Do **not** invent or rename IDs.\n")
    for sid, rules in sections.items():
        parts.append(f"Section {sid}:")
        if not rules:
            parts.append("- (no explicit rule IDs found)")
        else:
            for rid in rules:
                parts.append(f"- {rid}")
        parts.append("")
    parts.append("If you output a rule not in this list, add it to `validation.unknownRuleIds` (do not synthesize a new ID).")
    return "\n".join(parts)

# ---------- Post-processing helpers ----------
_EX_TAIL = re.compile(r'\((?:for example|e\.g\.)\s*:\s*([^)]+)\)\s*\.?$', re.IGNORECASE)

def _split_examples(txt: str):
    parts = re.split(r'\s*,\s*|\s+or\s+|\s+and\s+', (txt or "").strip())
    return [p.strip().strip('"').strip("'") for p in parts if p.strip()]

def _move_examples_from_description(rule: dict) -> None:
    desc = (rule.get("description") or "").strip()
    moved = []
    m = _EX_TAIL.search(desc)
    if m:
        moved.extend(_split_examples(m.group(1)))
        desc = desc[:m.start()].rstrip()
    m2 = re.search(r'(?i)\bfor\s+example\b[: ,]+(.+)$', desc)
    if m2 and ("," in m2.group(1) or re.search(r'\b(or|and)\b', m2.group(1))):
        moved.extend(_split_examples(m2.group(1)))
        desc = desc[:m2.start()].rstrip()
    rule["description"] = re.sub(r'\s{2,}', ' ', desc).strip()
    if moved:
        ex = rule.get("examples") or []
        for item in moved:
            if item and item not in ex:
                ex.append(item)
        rule["examples"] = ex

def _derive_group_from_id(rule_id: str):
    if not rule_id: return None
    if "FORBID" in rule_id: return "FORBID"
    if "STRUCT" in rule_id: return "STRUCT"
    if "BEHAV" in rule_id:  return "BEHAV"
    return None

def _extract_doc_type(md_text: str) -> str:
    # explicit: doc_type: concept
    m = re.search(r'^\s*doc_type\s*:\s*["\']?\s*([A-Za-z0-9_-]+)\s*["\']?\s*$', md_text, flags=re.MULTILINE)
    if m: return m.group(1).strip()
    # hinted: doc_type: # [concept]
    m2 = re.search(r'^\s*doc_type\s*:\s*#\s*\[([A-Za-z0-9_-]+)\]\s*$', md_text, flags=re.MULTILINE)
    if m2: return m2.group(1).strip()
    return ""

def _strip_container_groups(obj: dict) -> dict:
    """
    Remove 'group' from section containers and forbidden containers universally.
    Does not touch rule-level 'group'.
    """
    try:
        for s in obj.get("sections") or []:
            if isinstance(s, dict):
                s.pop("group", None)
        for fb in obj.get("forbidden") or []:
            if isinstance(fb, dict):
                fb.pop("group", None)
    except Exception:
        pass
    return obj

def _postprocess(obj: dict, markdown_source: str) -> dict:
    # (1) Fill doc_type
    fm = obj.get("frontMatter") or {}
    if fm.get("doc_type") in (None, "", "null"):
        dt = _extract_doc_type(markdown_source)
        if dt:
            fm["doc_type"] = dt
            obj["frontMatter"] = fm

    # (2) Rules: normalize group + move examples; containers: drop group
    for s in obj.get("sections") or []:
        # never keep container group
        s.pop("group", None)
        for r in s.get("rules") or []:
            g = _derive_group_from_id(r.get("id") or "")
            if g:
                r["group"] = g
            _move_examples_from_description(r)

    for fb in obj.get("forbidden") or []:
        # Some models might emit a dict bucket for forbidden; ensure no container group leaks
        if isinstance(fb, dict):
            fb.pop("group", None)
            for r in fb.get("rules") or []:
                g = _derive_group_from_id(r.get("id") or "")
                if g:
                    r["group"] = g
                _move_examples_from_description(r)

    # (3) Validation cleanup and notes
    v = obj.get("validation") or {}
    msgs = []
    for msg in (v.get("groupViolations") or []):
        if re.match(r'^Section\s+(\S+)\s+marked BEHAV but contains container constraints$', msg or ""):
            continue
        m = re.match(r'^Unknown group token in rule ID\s+(.+?)\s+\(set to BEHAV\)$', msg or "")
        if m and _derive_group_from_id(m.group(1)):
            continue
        msgs.append(msg)
    v["groupViolations"] = msgs

    # Drop NO_SECTION_TABLE if Markdown actually has the overview table header
    if re.search(r'^\|\s*Section\s*\|', markdown_source, flags=re.MULTILINE):
        v["notes"] = [n for n in (v.get("notes") or []) if n != "NO_SECTION_TABLE"]

    # (4) Unknown rule IDs report (inventory-based, generic)
    try:
        inv_sections, inv_allowed = _extract_id_inventory(markdown_source)
    except Exception:
        inv_sections, inv_allowed = ({}, set())
    if inv_allowed:
        unknown = []
        for s in obj.get('sections') or []:
            for r in (s.get('rules') or []):
                rid = r.get('id')
                if rid and rid not in inv_allowed:
                    unknown.append(rid)
        v['unknownRuleIds'] = sorted(list(dict.fromkeys(unknown)))
    obj["validation"] = v

    # (5) Final defensive strip
    obj = _strip_container_groups(obj)
    return obj

# ---------- Backends ----------
def _call_openai(model: str, messages: list[str|dict]) -> str:
    try:
        from openai import OpenAI
    except Exception as e:
        raise RuntimeError("OpenAI SDK not available; set LLM_BACKEND=openrouter or install openai>=1.x") from e
    if not os.environ.get("OPENAI_API_KEY"):
        raise RuntimeError("Missing OPENAI_API_KEY")
    client = OpenAI()
    base_kwargs = dict(model=model, messages=messages, temperature=0, top_p=1,
                       seed=int(os.environ.get("SEED", "1234")))
    # Optional token limits (opt-in)
    mct = os.environ.get("MAX_COMPLETION_TOKENS")
    mt  = os.environ.get("MAX_TOKENS")
    def _create(kwargs):
        return client.chat.completions.create(**kwargs).choices[0].message.content
    if mct:
        try:
            kw = dict(base_kwargs); kw["max_completion_tokens"] = int(mct); return _create(kw)
        except Exception as e:
            if "max_completion_tokens" not in str(e): raise
    if mt:
        try:
            kw = dict(base_kwargs); kw["max_tokens"] = int(mt); return _create(kw)
        except Exception as e:
            if "max_tokens" not in str(e): raise
    return _create(base_kwargs)

def _call_openrouter(model: str, messages: list[str|dict]) -> str:
    import requests
    base = os.environ.get("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("Missing OPENROUTER_API_KEY")
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    body = {"model": model, "messages": messages, "temperature": 0, "top_p": 1,
            "seed": int(os.environ.get("SEED", "1234"))}
    if os.environ.get("OPENROUTER_MAX_TOKENS"):
        try:
            body["max_tokens"] = int(os.environ["OPENROUTER_MAX_TOKENS"])
        except Exception:
            pass
    resp = requests.post(f"{base}/chat/completions", headers=headers, json=body, timeout=600)
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"]

# ---------- Main ----------
def main():
    input_md, output_json, cli_prompt = parse_args(sys.argv)
    if not os.path.exists(input_md):
        print(f"Input Markdown not found: {input_md}\nCWD: {os.getcwd()}", file=sys.stderr); sys.exit(2)

    script_dir = os.path.dirname(__file__)
    prompt_path = discover_prompt_path(script_dir, cli_prompt)

    prompt = load_text(prompt_path)
    markdown = load_text(input_md)

    # Build messages
    inv_sections, inv_allowed = _extract_id_inventory(markdown)
    inventory_block = _render_inventory_block(inv_sections, inv_allowed)
    system_msg = {"role": "system", "content": "Convert Markdown into JSON strictly per the provided instructions. Be mechanical and deterministic."}
    user_prompt_msg = {"role": "user", "content": prompt}
    user_md_msg = {"role": "user", "content": "Here is the Markdown template to convert:\n\n```markdown\n" + markdown + "\n```"}
    inventory_msg = {"role": "user", "content": inventory_block} if inventory_block else None
    messages = [m for m in [system_msg, user_prompt_msg, user_md_msg, inventory_msg] if m]

    backend = os.environ.get("LLM_BACKEND", "openai").lower()
    model = os.environ.get("MODEL")
    if not model:
        print("Missing MODEL environment variable.", file=sys.stderr); sys.exit(2)

    # Call LLM
    try:
        if backend == "openrouter":
            content = _call_openrouter(model, messages)
        else:
            content = _call_openai(model, messages)
    except Exception as e:
        print(f"LLM call failed: {e}", file=sys.stderr); sys.exit(3)

    # Extract JSON block
    m = re.search(r'```json\s*(\{.*?\})\s*```', content, flags=re.DOTALL)
    if not m:
        write_text(output_json + ".raw.txt", content)
        print(f"LLM did not return JSON. See {output_json}.raw.txt", file=sys.stderr)
        sys.exit(3)
    content_str = m.group(1)

    # Parse JSON
    try:
        obj = json.loads(content_str)
    except Exception as e:
        write_text(output_json + ".bad.json", content_str)
        print(f"Could not parse JSON block. Wrote {output_json}.bad.json\n{e}", file=sys.stderr)
        sys.exit(3)

    # Post-process (includes final group strip)
    obj = _postprocess(obj, markdown)

    # Write JSON
    write_text(output_json, json.dumps(obj, ensure_ascii=False, indent=2))
    print(f"Wrote: {output_json}")

if __name__ == "__main__":
    main()
