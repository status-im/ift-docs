# Markdown → JSON template conversion (v2)

**Task**
Convert the attached OneDoc **Markdown procedure template** into a **machine-readable JSON** using the schema below. Be mechanical, not creative. **Do not paraphrase.** The output must be **one JSON object only** (in a fenced ```json code block), with keys emitted in the schema order.

**Consumers**: preflight validator (structure), linter (behavior), and an LLM (examples/context).

---

## JSON Schema (use as-is)

```json
{
  "documentName": "string",
  "docVersion": "string|null",
  "frontMatter": {
    "title": "string|null",
    "doc_type": "string|null",
    "product": "string|null",
    "topics": ["string"],
    "steps_layout": "flat|sectioned|null",
    "authors": ["string"],
    "owner": "string|null",
    "slug": "string|null"
  },
  "sections": [
    {
      "id": "RULE-ID",
      "group": "STRUCT|BEHAV",
      "title": "string",
      "required": "required|optional|forbidden",
      "format": "string|null",
      "rules": [
        {
          "id": "RULE-ID",
          "group": "STRUCT|BEHAV",
          "description": "string",
          "examples": []
        }
      ],
      "examples": []
    }
  ],
  "forbidden": [
    {
      "id": "RULE-ID",
      "rules": [
        {
          "id": "RULE-ID",
          "group": "STRUCT|BEHAV|FORBID",
          "description": "string"
        }
      ]
    }
  ],
  "validation": {
    "missingRuleIds": [],
    "duplicateRuleIds": [],
    "groupViolations": [],
    "forbiddenViolations": [],
    "notes": []
  }
}
```

---

## Deterministic Extraction Rules

### 1) Front matter

- If the Markdown has YAML front matter, parse it into `frontMatter`.
- For absent fields, set `null` or `[]` per schema.
- Do not invent values.

### 2) Section table → sections

- Use the **section/table** at the top (if present) to derive:

  - `sections[i].title`
  - `sections[i].required` (map **Yes → "required"**, **No → "optional"**; if an entire section is explicitly forbidden, set **"forbidden"**)
  - `sections[i].format` (copy **verbatim**; if absent → `null`)
  - `sections[i].id` (from the section’s HTML comment ID if present; otherwise derive a stable ID from the table’s ID column if it holds IDs; else synthesize as in Rule 6)
- **Ordering**: sections appear in **table order**; if no table, use **first appearance** order in the document.



#### 2a) Concept template specifics (H2/H3 containers)

- Concept templates may define container sections like `H2 section` (`CONC-H2-SECTION`) and `H3 section` (`CONC-H3-SECTION`). Treat these as normal sections with their own rules.
- If an older concept table splits H2/H3 into “title” and “content” rows (e.g., `CONC-H2_TITLE`, `CONC-H2_CONTENT`) but the body defines a single `H2 section` with ID `CONC-H2-SECTION`, then **prefer the body heading with its ID** and do **not** invent separate title/content sections.
- Use the table primarily for **ordering** and for the **required/format** fields. For section IDs, prefer the **heading’s HTML comment**; if absent, fallback to the table’s ID column.
- Result: one `H2 section` and one `H3 section` entry in JSON, each with its rule bullets collected from their corresponding body sections.
### 3) IDs and comments (precise)

- **Goal**: keep the ID in JSON, remove only the **HTML comment** from human-visible strings.
- Use this regex for lines that carry an ID comment:

```
^(?P<body>.*?)\s*<!--\s*(?:group:\s*)?(?P<id>[A-Z0-9\-:]+)\s*-->\s*$
```

- Assign `id = <captured id>`.
- For `title`/`description`, use `body` **verbatim** (apply whitespace normalization below).
- **Do not parse IDs inside fenced code blocks** as metadata; treat them as code content.

### 4) Rule objects (one bullet → one rule)

- In each section, create **one rule object per bullet** (or numbered item) that has an ID comment.
- If a bullet has **no ID comment**, create a **deterministic synthetic ID**:

  - `"<SECTION-ID>-AUTO-" + zero_padded(index_in_section)` (e.g., `PROC-EXPECT-AUTO-01`)
  - Add the **missing original** marker to `validation.missingRuleIds` as `"SECTION:<SECTION-ID> ITEM:<index>"`.

- **Ordering**: rules remain in **appearance order**.

### 5) Group semantics (container vs. rule)

- **Section `group` (container classification):**

  - Set to **"STRUCT"** if the section has any container constraints (presence/position/heading text/cardinality/format) that the preflight must enforce.
  - Else set to **"BEHAV"**.

- **Rule `group` (individual check):**

  - Derive from the rule ID **token** using this precedence:

    1. If the ID contains `FORBID` → `"FORBID"`
    2. Else if it contains `STRUCT` → `"STRUCT"`
    3. Else if it contains `BEHAV` → `"BEHAV"`
    4. Else set to `"BEHAV"` and append a fixed message to `validation.groupViolations`:
       `"Unknown group token in rule ID <ID> (set to BEHAV)"`

- A section can host both STRUCT and BEHAV rules; the section’s `group` does **not** constrain the rule list.

- **Rendering note:** A section’s JSON `title` is a **label**, not a guaranteed visible heading. Only render a visible heading if there’s an explicit STRUCT rule permitting or requiring it (for example, `*-RENDER-HEADING`). If a section has a STRUCT rule like `*-NO-HEADING`, or parent-level guidance that children render inline, do **not** output a visible heading; integrate the content under the parent.

### 6) Duplicate IDs

- If the **same rule ID** appears more than once:

  - Keep the **first** as-is.
  - For subsequent duplicates, suffix: `"-DUP-" + n` (n = 1, 2, …) in the emitted `id`.
  - Record the **base** duplicate in `validation.duplicateRuleIds` once: the original ID string.

### 7) Forbidden rules

- Any rule whose ID contains `FORBID` goes under the top-level `"forbidden"` array, grouped by a parent `id` if such a parent is defined; otherwise use the nearest section’s ID as the grouping `id`.
- The rule objects inside `"forbidden"` must keep their `"group"` as `"FORBID"`.
- If the Markdown explicitly forbids an entire section, set that section’s `required: "forbidden"` **and** list the specific bullets under `"forbidden"`.

### 8) String normalization (no paraphrasing)

- For `title`, `description`, and non-code example text:

  - Trim leading/trailing whitespace.
  - Collapse internal runs of whitespace to a single space.
  - Preserve punctuation and case.

- **Preserve code** (inline and fenced) **verbatim** (no whitespace collapsing inside code).

### 9) Examples

- Only capture content explicitly under an “Examples” label or clearly delimited example blocks **within the same section**. If none → `examples: []`.
- Keep code fences and inline code **verbatim**.

### 10) Required/format fields

- `required`: **"required"**, **"optional"**, or **"forbidden"** as defined in Rule 2/7.
- `format`: copy the **table text verbatim**; if not specified → `null`.

### 11) Canonical ordering and key order

- **sections**: table order → else appearance order.
- **rules**: appearance order within section.
- **forbidden.rules**: appearance order.
- Emit object keys **exactly** in the schema order (top-level and nested). JSON objects are unordered by spec, but keep this order for stable diffs.

### 12) Validation metadata (fixed messages)

Populate all arrays (can be empty). Use **fixed strings** only:

- `missingRuleIds`: entries like `"SECTION:<SECTION-ID> ITEM:<index>"`.
- `duplicateRuleIds`: the base duplicate ID string (once per duplicated base).
- `groupViolations`:

  - `"Unknown group token in rule ID <ID> (set to BEHAV)"`
  - `"Section <SECTION-ID> marked BEHAV but contains container constraints"`

- `forbiddenViolations`: concrete findings, e.g.,

  - `"Found forbidden heading level H4 in section <SECTION-ID>"`

- `notes`: source locations and brief flags, e.g.,

  - `"SOURCE:<filename or input>:<line>"`, `"NO_SECTION_TABLE"`, `"NO_FRONT_MATTER"`

### 13) No dynamic or invented data

- Do **not** include timestamps, UUIDs, environment info, or undocumented fields.
- If a value is unknown, set `null` (or `[]`) as per the schema.

### 14) Output contract

- **Respond with a single JSON object only**, inside a ```json fenced block.
- **No prose** before or after.
- If the Markdown is missing or unparsable, still return a valid schema object with empty arrays/`null`s and a note in `validation.notes` (e.g., `"NO_INPUT"` or `"PARSE_ERROR"`).

---

## Acceptance Checklist (self-verify before returning)

- [ ] Every rule bullet → a rule object (IDs present or synthesized).
- [ ] All `<!-- RULE-ID -->` comments stripped from visible strings but captured in `id`.
- [ ] Section `group` reflects container constraints; rule `group` from ID tokens.
- [ ] `required` and `format` mapped from the table; `null` when absent.
- [ ] Examples captured only where explicitly marked; code preserved verbatim.
- [ ] Deterministic ordering and schema key order respected.
- [ ] `validation.*` populated with fixed messages; no freeform prose.
- [ ] Output is one JSON object in a ```json code block, with nothing else.
