# Copilot instructions (repository-wide)

## Purpose

Make successful docs PRs on the first try by using the repo’s own bootstrap → lint → links → build pipeline. These instructions apply to Copilot Chat, the coding agent, and PR review.

## What this repo is

- Docs-first repository. Primary content under `docs/`.  
- Config at repo root: `.vale.ini` + `vale/`, `.markdownlint.*` (or remark config), `.cspell.json`, `lychee.*`, optional site generator config (`mkdocs.yml` or Docusaurus files).  
- Use **Makefile** targets or **package.json** scripts when present. Avoid calling underlying CLIs directly.

## Operational checklist (before proposing a PR)

1) Bootstrap  
   - If `Makefile` has a bootstrap target: `make bootstrap`  
   - Else if `package.json` exists: `npm ci`  
   - If Python tooling is used: create venv, `pip install -r requirements.txt`

2) Lint  
   - Markdown: `make lint-md` or `npm run lint:md`  
   - Prose/style (Vale): `make lint-prose` or `npm run lint:prose`  
   - Spelling (cspell): `make lint-spell` or `npm run lint:spell`  
   - Links (lychee): `make lint-links` or `npm run lint:links`

3) Build / Preview (only if site generator is configured)  
   - MkDocs: `mkdocs build` (local preview: `mkdocs serve`)  
   - Docusaurus: `npm run build` (local preview: `npm run start`)

4) Stop if any step fails. Fix locally, re-run, then open the PR.

## Guardrails for docs edits

- Keep front matter and any HTML-comment rule IDs intact.  
- For procedures, use Markdown numbered lists; put paragraphs, code, and images **under** the correct list item (blank line + indent).  
- Use relative links for internal references; update inbound links if a file moves.  
- If adding code blocks or screenshots, follow the Style Guide documents in the repo (do not restate rules here).  
- Keep changes small and scoped; preserve technical accuracy and author voice.

## Scope

Markdown files under content under `/docs/**`.

## PR review behavior

- Re-run the same pipeline locally before pushing fixes.  
- When moving or renaming files, update navigation/sidebars (if applicable) and re-run link checks.

## Source of truth

- Prefer repo scripts. If a script is missing, consult the config files at repo root for tool flags and rules. Do not duplicate Style-Guide content here.
