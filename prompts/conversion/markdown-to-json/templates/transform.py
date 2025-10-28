#!/usr/bin/env python3
"""
Deterministic Markdown → JSON transformer
-----------------------------------------
Runs the "Deterministic v2" prompt against an LLM and writes the JSON to file.

Backends:
  - OpenAI API: set LLM_BACKEND=openai and OPENAI_API_KEY
  - OpenRouter: set LLM_BACKEND=openrouter and OPENROUTER_API_KEY

Required env:
  - MODEL (e.g., "gpt-4o", "gpt-5-2025-08-07", or "openai/gpt-4o" on OpenRouter)
  - For GPT-5: do NOT send temperature/top_p. This script skips them by default.

Optional env:
  - SEED (default: 1234)
  - ALLOW_SAMPLING_PARAMS=1 to include temperature/top_p (useful for non GPT-5 models)
  - TEMPERATURE (default: 1) and TOP_P (default: 1) used only if ALLOW_SAMPLING_PARAMS=1
  - OPENAI_BASE_URL (override OpenAI endpoint)
  - OPENROUTER_BASE_URL (override OpenRouter endpoint)

Usage:
  python transform.py input.md output.json
"""

import os
import sys
import json
import requests

def load_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def strip_code_fence(text: str) -> str:
    s = text.strip()
    if s.startswith("```"):
        first = s.find("\n")
        last = s.rfind("```")
        if first != -1 and last != -1 and last > first:
            s = s[first + 1:last].strip()
    return s

def build_payload(model: str, system_msg: dict, user_prompt_msg: dict, user_md_msg: dict) -> dict:
    payload = {
        "model": model,
        "response_format": {"type": "json_object"},
        "messages": [system_msg, user_prompt_msg, user_md_msg],
        "seed": int(os.environ.get("SEED", "1234")),
    }

    # Only include sampling params if explicitly allowed.
    allow_sampling = os.environ.get("ALLOW_SAMPLING_PARAMS", "0") == "1"

    # GPT-5 models reject custom temperature; keep off unless explicitly allowed.
    is_gpt5 = "gpt-5" in model

    if allow_sampling and not is_gpt5:
        # Safe to include on models that support it.
        if "TEMPERATURE" in os.environ:
            payload["temperature"] = float(os.environ.get("TEMPERATURE", "1"))
        if "TOP_P" in os.environ:
            payload["top_p"] = float(os.environ.get("TOP_P", "1"))
        # Optional repetition knobs (don’t affect randomness)
        if "PRESENCE_PENALTY" in os.environ:
            payload["presence_penalty"] = float(os.environ["PRESENCE_PENALTY"])
        if "FREQUENCY_PENALTY" in os.environ:
            payload["frequency_penalty"] = float(os.environ["FREQUENCY_PENALTY"])

    return payload

def post_chat(url: str, headers: dict, payload: dict) -> requests.Response:
    return requests.post(url, headers=headers, json=payload, timeout=600)

def main():
    if len(sys.argv) < 3:
        print("Usage: python transform.py input.md output.json", file=sys.stderr)
        sys.exit(2)

    input_md = sys.argv[1]
    output_json = sys.argv[2]

    # Load files
    # Expect prompt.md to be in the same directory as this script.
    prompt_path = os.path.join(os.path.dirname(__file__), "prompt.md")
    if not os.path.exists(prompt_path):
        print(f"Missing prompt file: {prompt_path}", file=sys.stderr)
        sys.exit(2)

    prompt = load_text(prompt_path)
    markdown = load_text(input_md)

    # Build messages
    system_msg = {
        "role": "system",
        "content": "You convert Markdown into JSON strictly per the provided instructions. Be mechanical and deterministic."
    }
    user_prompt_msg = {"role": "user", "content": prompt}
    user_md_msg = {
        "role": "user",
        "content": "Here is the Markdown template to convert:\n\n```markdown\n" + markdown + "\n```"
    }

    # Backend selection
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
        base_url = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1")
        url = base_url.rstrip("/") + "/chat/completions"
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    elif backend == "openrouter":
        api_key = os.environ.get("OPENROUTER_API_KEY")
        if not api_key:
            print("Missing OPENROUTER_API_KEY", file=sys.stderr)
            sys.exit(2)
        base_url = os.environ.get("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
        url = base_url.rstrip("/") + "/chat/completions"
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    else:
        print("LLM_BACKEND must be 'openai' or 'openrouter'", file=sys.stderr)
        sys.exit(2)

    # Build payload and call API
    payload = build_payload(model, system_msg, user_prompt_msg, user_md_msg)
    resp = post_chat(url, headers, payload)

    # If the model rejects sampling params with an unsupported_value, retry once without them.
    if resp.status_code == 400 and "unsupported_value" in resp.text:
        # Remove potential sampling keys and retry
        for k in ["temperature", "top_p", "presence_penalty", "frequency_penalty"]:
            payload.pop(k, None)
        resp = post_chat(url, headers, payload)

    if resp.status_code != 200:
        print("API error:", resp.status_code, resp.text[:1200], file=sys.stderr)
        sys.exit(1)

    data = resp.json()
    try:
        content = data["choices"][0]["message"]["content"]
    except Exception:
        print("Unexpected API response format:", json.dumps(data)[:1200], file=sys.stderr)
        sys.exit(1)

    content_str = strip_code_fence(content)

    # Validate JSON
    try:
        obj = json.loads(content_str)
    except json.JSONDecodeError as e:
        # Save raw for debugging
        debug_path = output_json + ".raw.txt"
        with open(debug_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Model did not return valid JSON. Raw saved to:", debug_path, file=sys.stderr)
        print("Decode error:", e, file=sys.stderr)
        sys.exit(1)

    # Write JSON (pretty)
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)

    print("Wrote:", output_json)

if __name__ == "__main__":
    main()
