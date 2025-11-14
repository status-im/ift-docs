# Run Markdown → JSON conversion via API script

**Purpose**

Convert a OneDoc Markdown procedure template into machine-readable JSON using a deterministic prompt and a pinned model.

**Outputs**

- A single JSON file that follows the shared schema.
- A `.raw.txt` file (only when the model returns non-JSON), for debugging.

**Files in this folder**

- `md2json-prompt-templates.md`:  deterministic prompt (do not edit without bumping the version).
- `transform.py`:  API runner script.
- `<your-template>.md`:  the Markdown template to convert.

---

## Part A:  Set up the environment

1. **Install Python 3.10+**

   Verify:

   ```bash
   python3 --version
   ```

   If not installed, download from [python.org](https://www.python.org/downloads/) or use a package manager.

2. **Create a virtual environment**

   ```bash
   python3 -m venv .venv
   ```

   If you have multiple Python versions, you may need to use the absolute path to Python 3.10+, for example:

   ```bash
   /usr/local/bin/python3.10 -m venv .venv
   ```

   > **Note:** Name the virtual environment folder `.venv`; it's included in `.gitignore`.

3. **Activate the virtual environment**

   * macOS/Linux:

     ```bash
     source .venv/bin/activate
     ```

   * Windows (PowerShell):

     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```

   > **Note:** To activate the Python virtual environment in Visual Studio Code, open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`), type `Python: Select Interpreter`, and choose the interpreter from the `.venv` folder. If the option to choose the interpreter does not appear, install the Microsoft Python extension for Visual Studio Code.

4. **Install dependencies**

   ```bash
   pip install requests
   ```

5. **Verify repository files are present**

   Change to the working directory at prompts/conversion/markdown-to-json/templates and ensure `md2json-prompt-templates.md` and `transform.py` are in the directory.

---

## Part B:  Configure the API backend

Choose **one** backend option and set the environment variables.

### Option 1:  OpenAI API

1. **Export required variables**

   * macOS/Linux:

     ```bash
     export LLM_BACKEND=openai
     export OPENAI_API_KEY=<YOUR_KEY>
     export MODEL=gpt-5
     # export TEMPERATURE=0 OpenAI GPT-5 doesn't support custom temperature
     # export TOP_P=1 OpenAI GPT-5 doesn't support custom top_p
     export SEED=1234
     # Optional: export OPENAI_BASE_URL=https://api.openai.com/v1
     export RULES_SIDECAR=1
     ```

   * Windows (PowerShell):

     ```powershell
     $env:LLM_BACKEND="openai"
     $env:OPENAI_API_KEY="<YOUR_KEY>"
     $env:MODEL="gpt-5"
     # $env:TEMPERATURE="0" OpenAI GPT-5 doesn't support custom temperature
     # $env:TOP_P="1" OpenAI GPT-5 doesn't support custom top_p
     $env:SEED="1234"
     # Optional: $env:OPENAI_BASE_URL="https://api.openai.com/v1"
     $env:RULES_SIDECAR="1"
     ```

2. **Pin the model**

   Use a single, agreed model string (for example, `gpt-5`) across all tests.

### Option 2:  OpenRouter

1. **Export required variables**

   - macOS/Linux:

     ```bash
     export LLM_BACKEND=openrouter
     export OPENROUTER_API_KEY=<YOUR_KEY>
     export MODEL=openai/gpt-5
     # export TEMPERATURE=0  OpenAI GPT-5 doesn't support custom temperature
     # export TOP_P=1 OpenAI GPT-5 doesn't support custom top_p
     export SEED=1234
     # Optional: export OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
     export RULES_SIDECAR=1
     ```

   - Windows (PowerShell):

     ```powershell
     $env:LLM_BACKEND="openrouter"
     $env:OPENROUTER_API_KEY="<YOUR_KEY>"
     # $env:MODEL="openai/gpt-5" OpenAI GPT-5 doesn't support custom temperature
     $env:TEMPERATURE="0"
     # $env:TOP_P="1" OpenAI GPT-5 doesn't support custom top_p
     $env:SEED="1234"
     # Optional: $env:OPENROUTER_BASE_URL="https://openrouter.ai/api/v1"
     $env:RULES_SIDECAR="1"
     ```

2. **Allow temperature/top_p defaults**

   For GPT-5 or other model variants that do not support custom sampling parameters, do not set `TEMPERATURE` or `TOP_P`. If the model supports them, set `TEMPERATURE=0`, `TOP_P=1`, and `ALLOW_SAMPLING_PARAMS=1`.

3. **Pin the model**

   Use a single, agreed model string (for example, `gpt-5`) across all tests.

---

## Part C:  Convert Markdown to JSON

1. **Place your Markdown input**

   Put the file (for example, `procedure-template-flat.md`) in the same folder as `transform.py`.

2. **Change to the working folder**

   ```bash
   cd prompts/conversion/markdown-to-json/templates
   ```

3. **Run the transformer**

   ```bash
   python3 transform.py <template-name>.md out.json --prompt <prompt-name>.md
   ```

   If your virtual Python environment and script are in different directories, use absolute paths. For example:

   ```bash
   /home/user/.venv/bin/python3 /logos-docs/prompts/conversion/markdown-to-json/templates/transform.py <template-name>.md out.json --prompt <prompt-name>.md
   ```

   > **Note:** Depending on the model, the script task may take several minutes to complete.

4. **Confirm success**
   The script prints:

   ```
   Wrote: out.json
   ```

   > **Note:** As a reference, the procedure template conversion requires about 7 000 input tokens and 17 000 output tokens (USD 0.18 as of October 2025 with GPT-5).

---

## Part D:  Validate and review the output

1. **Validate JSON syntax**

     ```bash
     python3 -m json.tool out.json > /dev/null && echo "JSON OK"
     ```

     This should complete without errors.

2. **Review validation fields**

   Open `out.json` and, under the `validation` key, inspect:

   - `validation.missingRuleIds`
   - `validation.duplicateRuleIds`
   - `validation.groupViolations`
   - `validation.forbiddenViolations`
   - `validation.notes`

   Open `out.json.rules-check.json` and inspect the end of the file for:

   - `missing_in_json`: rule IDs not found in the JSON output.
   - `extra_in_json`: rule IDs found in the JSON output but not in the Markdown.
   - `description_leaks_examples`: rules where the description might be out of the `examples` key.

3. **Save JSON output**

   Rename the output file. Use the same name as the original Markdown file but with `.json` extension. For example:

   ```bash
   mv out.json procedure-template.json
   ```

---

## Part E:  Commit the results

1. **Clean up previous outputs**

   ```bash
   rm out.json prompt.md *.raw.txt
   ```

2. **Add files to git**

   ```bash
   git add procedure-template.json
   ```

2. **Commit with a clear message**

   ```bash
   git commit -S -m "Convert procedure-template.md to JSON using deterministic prompt"
   ```

3. **Push changes**

   ```bash
   git push
   ```

---

## Part F:  Troubleshoot common issues

1. **401/403 errors (authorization)**

   - Verify `OPENAI_API_KEY` or `OPENROUTER_API_KEY`.
   - Confirm `LLM_BACKEND` and `MODEL` values.

2. **Non-JSON response**

   - The script writes `<output>.raw.txt`. Open it to inspect server output.
   - Re-run after fixing environment variables.

3. **Different outputs across users**

   - Confirm everyone uses the **same** prompt, `MODEL`, `TEMPERATURE=0`, `TOP_P=1`, and `SEED=1234`.
   - Keep the original prompt immutable. If you revise it, bump the version in the filename and in commit messages.

4. **Network or proxy issues**

   - If your org uses a proxy, set the standard `HTTP_PROXY`/`HTTPS_PROXY` variables before running.

5. **Model name errors**

   - Use a single pinned model string that exists on your backend. Do not use “auto” aliases.

---

## Notes

- Keep inputs (`.md`) and outputs (`.json`) in the repository to allow diffs and audits.
- Do not change default sampling parameters. Always use `TEMPERATURE=0`, `TOP_P=1` (if supported by your model), and a fixed `SEED`.