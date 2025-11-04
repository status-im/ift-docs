# Markdown → JSON template conversion (v4)

**Task**  
Convert the attached OneDoc **Markdown template** into a **machine-readable JSON** using the schema below. Be mechanical, not creative. **Do not paraphrase.** The output must be **one JSON object only** (in a fenced ```json code block), with keys emitted in the schema order.

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
````

---

## 0) Hints block contract (authoritative IDs)

You will receive a **machine-readable hints block** (JSON) that includes:

* `section_ids_from_table`: ordered list of section IDs from the top table.
* `sections_table`: ordered objects `{id, title, required, format}` from the table.
* `rule_ids_exact`: **ordered** list of rule IDs detected from rule lines (not headings). This list is **authoritative**.

**Rules:**

* Emit **all** rule objects for every ID in `rule_ids_exact`, in order.
* If a rule ID appears **more than once** in `rule_ids_exact`, suffix the **second and subsequent** occurrences with `-DUP-1`, `-DUP-2`, etc.
* Do **not** emit any rule ID that is not in `rule_ids_exact`, except synthesized `AUTO` IDs when a rule line lacks an ID (see 4).
* Use `sections_table` to set each section’s `id`, `title`, `required`, and `format` **verbatim**.

---

## Deterministic Extraction Rules

### 1) Front matter

* If the Markdown has YAML front matter, parse it into `frontMatter`.
* For absent fields, set `null` or `[]` per schema.
* Do not invent values.

### 2) Section table → sections

* Use the **section/table** at the top (if present) to derive:

  * `sections[i].title`
  * `sections[i].required` (map **Yes → "required"**, **No → "optional"**; if explicitly forbidden → **"forbidden"**)
  * `sections[i].format` (copy **verbatim**; if absent → `null`)
  * `sections[i].id` (copy **verbatim** from the table ID column)

* **Ordering**: sections appear in **table order**; if no table, use **first appearance** order.

### 3) IDs and comments (precise)

* Keep IDs in JSON; remove only the HTML comment markers from visible strings.
* Do **not** parse IDs inside fenced code blocks as metadata.
* For section headings that carry inline `<!-- SECTION-ID -->` comments, treat those as **section IDs**, not rule IDs.

### 4) Rule objects (one rule line → one rule)

* Create **one rule object per rule line** that carries an ID comment.
* If a rule line has **no ID**, create a **deterministic synthetic ID**:

  * `"<SECTION-ID>-AUTO-" + zero_padded(index_in_section)` (e.g., `PROC-EXPECT-AUTO-01`)
  * Add a marker to `validation.missingRuleIds` as `"SECTION:<SECTION-ID> ITEM:<index>"`.

* Preserve the **order** of rule lines.

### 5) Group semantics (container vs. rule)

* **Section `group`**:
  **"STRUCT"** if the section has container constraints (presence/position/heading/cardinality/format), else **"BEHAV"**.

* **Rule `group`**: precedence by ID token:

  1. contains `FORBID` → `"FORBID"`
  2. contains `STRUCT` → `"STRUCT"`
  3. contains `BEHAV` → `"BEHAV"`
  4. otherwise `"BEHAV"` and add: `"Unknown group token in rule ID <ID> (set to BEHAV)"`.

### 6) Duplicate IDs (use the hints list counts)

* Only create `-DUP-n` IDs when the **same base ID** appears multiple times in `rule_ids_exact`.
* The **first** occurrence: base ID.
* The **second** → `-DUP-1`; third → `-DUP-2`, etc.
* Record the base ID once in `validation.duplicateRuleIds`.

### 7) Forbidden rules

* Any rule with `FORBID` in the ID goes under top-level `"forbidden"`, grouped by the nearest section `id` (or parent if defined).
* Keep the rule’s `"group": "FORBID"`.
* If an entire section is forbidden, set `required: "forbidden"` and list bullets under `"forbidden"`.

### 8) String normalization (no paraphrasing)

* For `title`, `description`, and non-code example text:

  * Trim edges; collapse internal runs of whitespace to one space.
  * Preserve punctuation and case.

* Preserve **code** (inline & fenced) **verbatim**.

### 9) Description vs. Examples (strict separation)

For each **rule object**, use `{ id, group, description, examples }`:

* **description**: one concise, normative sentence **without** example or contrastive lead-ins:
  *“for example”, “e.g.”, “instead of … use …”, “rather than …”* must **not** appear in `description`.

* **examples**: array of **0–2** short strings (**≤160 chars** each):

  * Extract explicit example lines/blocks under the same section (including under an “Examples” label).
  * Convert *“instead of X, use Y”* or *“use Y rather than X”* into:

    * `"Bad: X"`
    * `"Good: Y"`

  * Convert table/callout/code examples into short strings; keep inline/backtick code verbatim.
  * **Do not fabricate numbering** in examples. If the source shows a leading numeral, you may keep it; otherwise, emit plain strings.
  * If no examples exist, set `"examples": []`.

* **No duplication**: `description` must not restate or summarize example text.

### 10) Required/format fields

* `required`: **"required"**, **"optional"**, or **"forbidden"** as mapped from the table.
* `format`: copy **verbatim** from the table; or `null` when absent.

### 11) Canonical ordering and key order

* **sections**: table order (else appearance order).
* **rules** within a section: appearance order.
* **forbidden.rules**: appearance order.
* Emit object keys **exactly** in the schema order.

### 12) Validation metadata (fixed messages)

Populate arrays (can be empty). Use **fixed strings** only:

* `missingRuleIds`: `"SECTION:<SECTION-ID> ITEM:<index>"`
* `duplicateRuleIds`: base duplicate ID (once).
* `groupViolations`:

  * `"Unknown group token in rule ID <ID> (set to BEHAV)"`
  * `"Section <SECTION-ID> marked BEHAV but contains container constraints"`

* `forbiddenViolations`: concrete findings (e.g., `"Found forbidden heading level H4 in section <SECTION-ID>"`)
* `notes`: source locations/flags (e.g., `"SOURCE:<input>:<line>"`, `"NO_SECTION_TABLE"`, `"NO_FRONT_MATTER"`)

### 13) No dynamic or invented data

* Do **not** include timestamps, UUIDs, environment info, or undocumented fields.
* Unknown values → `null` (or `[]`) as per schema.

### 14) Output contract

* **Respond with a single JSON object only**, inside a ```json fenced block.
* **No prose** before or after.
* If the Markdown is missing or unparsable, still return a valid schema object with empty arrays/`null`s and a note in `validation.notes`.

---

## Acceptance Checklist (self-verify before returning)

* [ ] All section IDs exactly match the table (`sections_table`) with correct `title`, `required`, `format`.
* [ ] Every ID in `rule_ids_exact` produced as a rule object (order preserved).
* [ ] `-DUP-n` suffixes **only** when the same ID repeats in `rule_ids_exact`.
* [ ] No rule IDs invented (except synthesized `AUTO` for missing IDs).
* [ ] Descriptions contain **no** example/contrastive language.
* [ ] Examples: **0–2 items**, each **≤160 chars**; Bad/Good pairs for contrastive forms.
* [ ] Code preserved verbatim; no fabricated numbering in examples.
* [ ] Deterministic ordering and schema key order respected.
* [ ] `validation.*` populated with fixed strings only.