<<<<<<< HEAD
| Section                        | Format                        | Required  | ID                      |
|:-------------------------------|:------------------------------|:----------|:------------------------|
| Title                          | H1                            | Yes       | `PROC-TITLE`            |
| Subtitle                       | Single bold sentence          | Yes       | `PROC-SUBTITLE`         |
| Access callout                 | Note-type callout             | No        | `PROC-ACCESS`           |
| Callouts                       | Tip, Note, Important, Caution | No        | `PROC-CALLOUTS`         |
| Overview                       | Paragraph                     | Yes       | `PROC-OVERVIEW`         |
| Decisions                      | Paragraph, list, table        | No        | `PROC-DECISIONS`        |
| Limits                         | Paragraph, list, table        | No        | `PROC-LIMITS`           |
| Impact                         | Paragraph, list, table        | No        | `PROC-IMPACT`           |
| Prerequisites                  | Paragraph, list               | No        | `PROC-PREREQ`           |
| "What to expect"               | List                          | Yes       | `PROC-EXPECT`           |
| Procedure layout               | Flat or sectioned             | Yes       | `PROC-STRUCT-PATTERN`   |
| FAQ / Troubleshooting          | Paragraph, list, H3           | No        | `PROC-EXTRA`            |
| Forbidden content              | -                             | Forbidden | `PROC-FORBID`            |
=======
| Section                        | Format                              | Required  | ID                      |
|:-------------------------------|:------------------------------------|:----------|:------------------------|
| Title                          | H1                                  | Yes       | `PROC-PAGE-TITLE`       |
| Subtitle                       | Single bold sentence                | Yes       | `PROC-PAGE-SUBTITLE`    |
| Access callout                 | Note-type callout                   | No        | `PROC-ACCESS`           |
| Callouts                       | Tip, Note, Important, Caution       | No        | `PROC-CALLOUTS`         |
| Overview                       | Paragraph                           | Yes       | `PROC-OVERVIEW`         |
| Decisions                      | Paragraph, list, table              | No        | `PROC-DECISIONS`        |
| Limits                         | Paragraph, list, table              | No        | `PROC-LIMITS`           |
| Impact                         | Paragraph, list, table              | No        | `PROC-IMPACT`           |
| Prerequisites                  | Paragraph, list                     | No        | `PROC-PREREQ`           |
| "What to expect" heading       | H2                                  | Yes       | `PROC-EXPECT-001`       |
| "What to expect" list          | Unordered list                      | Yes       | `PROC-EXPECT-002`       |
| Procedure layout               | Flat or sectioned                   | Yes       | `PROC-STEPS-PATTERN-001`|
| FAQ / Troubleshooting title    | H2                                  | No        | `PROC-EXTRA-001`        |
| FAQ / Troubleshooting content  | Paragraph, list, H3                 | No        | `PROC-EXTRA-002`        |
| H4-H6 headings                 | -                                   | Forbidden | `PROC-FORBID-001`       |
| Further reading                | -                                   | Forbidden | `PROC-FORBID-002`       |
>>>>>>> 543f454 ((#47) Move files to new repo structure)

## Front matter

---
title:
doc_type: # [procedure, concept, reference, quickstart, api]
product: # [storage, blockchain, communication]
topics: []
steps_layout: # [flat|sectioned]
authors: # GitHub username
owner: ift
doc_version: # increased by one after every update
slug:
---

<<<<<<< HEAD
## Title <!-- group: PROC-TITLE -->

- Use Markdown H1 headings. <!-- PROC-STRUCT-TITLE-H1 -->
- Aim for 50 to 60 characters; 80 characters maximum. <!-- PROC-BEHAV-TITLE-LENGTH-50-80 -->
- Start with an action verb in the imperative form. Don't use the *-ing* form of the verb. <!-- PROC-BEHAV-TITLE-IMPERATIVE -->
- Capitalize only the first word and any proper nouns (sentence-style capitalization). <!-- PROC-BEHAV-TITLE-SENTENCE-CASE -->
- Focus on the outcome, not the mechanics. Prefer results over lists of actions. For example, instead of "Install Node.js and create a project directory", use "Set up a local development environment for Node.js". <!-- PROC-BEHAV-TITLE-OUTCOME-FOCUSED -->
- Include the action and the object/context (what/where/how) so the goal is unambiguous. <!-- PROC-BEHAV-TITLE-ACTION-OBJECT -->
- Avoid one- or two-word titles and empty verbs like *make*, *manage*, or *put*. <!-- PROC-BEHAV-TITLE-NO-EMPTY-VERBS -->
- Don't use punctuation marks, such as colons, semicolons, or dashes. <!-- PROC-BEHAV-TITLE-NO-PUNCT -->
=======
## Title guidelines <!-- group: PROC-PAGE-TITLE -->

- Use Markdown H1 headings and aim for 50 to 60 characters; 80 characters maximum. <!-- PROC-PAGE-TITLE-001 -->
- Start with an action verb in the imperative form. Don't use the *-ing* form of the verb. <!-- PROC-PAGE-TITLE-002 -->
- Capitalize only the first word and any proper nouns (sentence-style capitalization). <!-- PROC-PAGE-TITLE-003 -->
- Focus on the result, not on the task. Emphasize the desired outcome, rather than describing the specific actions involved. For example, instead of "Install Node.js and create a project directory", use "Set up a local development environment for Node.js". <!-- PROC-PAGE-TITLE-004 -->
- Include the action and the object/context (what/where/how). <!-- PROC-PAGE-TITLE-005 -->
- Avoid one- or two-word titles and empty verbs like *make*, *manage*, or *put*. <!-- PROC-PAGE-TITLE-006 -->
- Don't use punctuation marks, such as colons, semicolons, or dashes, except for the required `Step {n}:` prefix. <!-- PROC-PAGE-TITLE-007 -->
>>>>>>> 543f454 ((#47) Move files to new repo structure)

Examples:

	| Usage   | Example                                 |
	|:--------|:----------------------------------------|
	| **Use** | Create a codespace from a template      |
	| Avoid   | Creating a codespace from a template    |
	| **Use** | Use source control in your codespace    |
	| Avoid   | Use source control                      |
	| **Use** | Collaborate with others in a codespace  |
	| Avoid   | Set up a live share session             |

<<<<<<< HEAD
## Subtitle <!-- group: PROC-SUBTITLE -->

- Use a Markdown H4 for the subtitle placed right under the H1. <!-- PROC-STRUCT-SUBTITLE-H4 -->
- One sentence only; no links, lists, or inline formatting. <!-- PROC-BEHAV-SUBTITLE-SINGLE-SENTENCE -->
- Do not end with a period. <!-- PROC-BEHAV-SUBTITLE-NO-PERIOD -->
- Stay under 120 characters (approx. 20 words). <!-- PROC-BEHAV-SUBTITLE-LENGTH-120 -->
- Use an imperative/base-form verb that states the purpose or benefit (for example: *Get started*, *Explore*, *Try*). <!-- PROC-BEHAV-SUBTITLE-IMPERATIVE -->
- Add new value beyond the title; don’t repeat or rephrase the H1. <!-- PROC-BEHAV-SUBTITLE-ADDS-VALUE -->

Examples:

- **Title**: *Quickstart for GitHub Actions* / **Subtitle**: *Try out the core features of GitHub Actions in minutes*
- **Title**: *Create a pull request* / **Subtitle**: *Create a pull request to propose and collaborate on changes to a repository*

## Access callout (optional) <!-- group: PROC-ACCESS -->

This note-type callout is exclusively to alert readers about what roles, permissions, or product versions are required to perform the procedure.

- Place it after the title and subtitle, before the introduction. <!-- PROC-STRUCT-ACCESS-AFTER-SUBTITLE -->
- Use the `Note` callout style. <!-- PROC-STRUCT-ACCESS-NOTE-STYLE -->
- Use label-led, scannable content (no explanations). <!-- PROC-BEHAV-ACCESS-LABELED -->
- Include permissions (software role or permission level). <!-- PROC-BEHAV-ACCESS-PERMISSIONS -->
- Include product (product version or edition), if applicable. <!-- PROC-BEHAV-ACCESS-PRODUCT -->
- If multiple permissions/products apply, use commas. <!-- PROC-BEHAV-ACCESS-LIST-IF-MANY -->
- Do not include knowledge, skills, or required tools. <!-- PROC-BEHAV-ACCESS-SCOPE-ONLY -->
- Omit the callout entirely if no permission/product constraints exist. <!-- PROC-STRUCT-ACCESS-OMIT-IF-EMPTY -->

**Example:**

  > **Note**
  >
  > - **Permissions**: Node operators, Site operators
  > - **Product**: Waku v1.4.0 or later

## Callouts <!-- PROC-CALLOUTS -->

- Use callouts sparingly and avoid placing them consecutively. <!-- PROC-STRUCT-CALLOUTS-NOT-CONSECUTIVE -->
- One callout maximum per section <!-- PROC-STRUCT-CALLOUTS-PER-SECTION-ONE -->
- Keep each callout concise (≤ 2 short sentences). If the content needs a list or multiple paragraphs, move it into the body under a heading. <!-- PROC-BEHAV-CALLOUTS-CONCISE -->
- Ensure the callout content is directly relevant to the nearby task or decision point. <!-- PROC-BEHAV-CALLOUTS-RELEVANT -->
- Use the appropriate type: `Tip`, `Note`, `Important`, or `Caution`. <!-- PROC-BEHAV-CALLOUTS-TYPE -->
- Do **not** include full procedural steps or long prerequisite checklists inside callouts. Put steps in the main flow; keep prerequisite lists in "Before you start." <!-- PROC-BEHAV-CALLOUTS-NO-STEPS -->
- For the allowed callout types and when to use them, see the [writing rules](../../3-validating-design/writing-rules/README.md). <!-- PROC-BEHAV-CALLOUTS-TYPES-REFER-STYLEGUIDE -->

**Example:**

> **Note:**
> Keep container resources within the documented limits to avoid throttling.

## Intro

Every procedure requires an introduction that provides context and helps readers understand the procedure's purpose and scope. The introduction includes these sections, each one represented by a paragraph, list, or table:

- [Overview](#overview)
- [Decisions (optional)](#decisions-optional)
- [Limits (optional)](#limits-optional)
- [Impact (optional)](#impact-optional)
- [Prerequisites (optional)](#prerequisites-optional)
=======
## Subtitle guidelines <!-- group: PROC-PAGE-SUBTITLE -->

- Single sentence with no links, list items, or formatting. Ends with a period. <!-- PROC-PAGE-SUBTITLE-001 -->
- Use bold format. Stay under 120 characters. <!-- PROC-PAGE-SUBTITLE-002 -->
- Use imperative verbs to describe the document purpose or benefit: *Learn*, *Explore*, *Understand*, *Discover*, *Create*, *Follow*, *Try*, and other action verbs. <!-- PROC-PAGE-SUBTITLE-003 -->
- Adds new value beyond the title. It should not repeat the title or be a rephrased version of it. <!-- PROC-PAGE-SUBTITLE-004 -->

Examples:

- **Title**: *Quickstart for GitHub Actions* / **Subtitle**: *Try out the core features of GitHub Actions in minutes.*
- **Title**: *Create a pull request* / **Subtitle**: *Create a pull request to propose and collaborate on changes to a repository.*

## Access callout guidelines <!-- group: PROC-ACCESS -->

This note-type callout is exclusively to alert readers about what roles, permissions, or product versions are required to perform the procedure.

- Place it after the title and subtitle, before the introduction. <!-- PROC-ACCESS-002 -->
- Use the `Note` callout style. <!-- PROC-ACCESS-003 -->
- Start with the phrase: *This feature is available to users with...* or *To perform this procedure, you need...* <!-- PROC-ACCESS-004 -->
- Focus on required roles, permissions, or product versions only. Don't include any other prerequisite such as knowledge, skills, or tools. <!-- PROC-ACCESS-005 -->

**Examples:**

- *This feature is available to admin roles in version 5.0 or later with write permissions on the repository.*
- *This procedure requires contributor roles in version 2.3 or higher and read/write access to the API endpoints.*

## Callouts guidelines <!-- PROC-CALLOUTS -->

- Use callouts sparingly in the document and only when necessary to avoid overwhelming the reader. <!-- PROC-CALLOUTS-001 -->
- One callout maximum per section <!-- PROC-CALLOUTS-002 -->
- Keep callouts concise. <!-- PROC-CALLOUTS-003 -->
- Use the appropriate type: `Tip`, `Note`, `Important`, or `Caution`. <!-- PROC-CALLOUTS-004 -->

## Introduction guidelines

Every procedure requires an introduction that provides context and helps readers understand the procedure's purpose and scope. The introduction includes these sections, each one represented by a paragraph, list, or table:

- [Overview guidelines](#overview-guidelines)
- [Decisions guidelines (optional)](#decisions-guidelines-optional)
- [Limits guidelines (optional)](#limits-guidelines-optional)
- [Impact guidelines (optional)](#impact-guidelines-optional)
- [Prerequisites guidelines (optional)](#prerequisites-guidelines-optional)
>>>>>>> 543f454 ((#47) Move files to new repo structure)

**Examples:**

For an example of a procedure introduction, check out the [procedure example](./procedure-example.md).

<<<<<<< HEAD
### Overview <!-- group: PROC-OVERVIEW -->

- Write a 50–100 word paragraph explaining what this procedure covers, why it matters, and when to use it. <!-- PROC-BEHAV-OVERVIEW-LENGTH-50-100 -->
- Add context that the heading doesn’t provide; do not restate the heading. <!-- PROC-BEHAV-OVERVIEW-NO-REPEAT -->
- State where it applies and who the intended audience is. <!-- PROC-BEHAV-OVERVIEW-AUDIENCE-SCOPE -->
- (Optional) Give one concrete real-world scenario in a single sentence. <!-- PROC-BEHAV-OVERVIEW-EXAMPLE-ONE -->
- Use at most one short alert only if it prevents confusion; otherwise keep this section free of callouts. <!-- PROC-BEHAV-OVERVIEW-ALERT-SPARING -->

### Decisions (optional) <!-- group: PROC-DECISIONS -->

- Summarize decisions the reader must make **before** starting (for example, CLI vs. GUI). <!-- PROC-BEHAV-DECISIONS-PURPOSE -->
- Use a list for simple choices; use a compact table for multi-factor comparisons. <!-- PROC-BEHAV-DECISIONS-FORM -->
- Focus on actionable factors: performance, complexity, cost, prerequisites, and limitations. <!-- PROC-BEHAV-DECISIONS-FACTORS -->
- State trade-offs explicitly (for example, "A is faster but less secure"). <!-- PROC-BEHAV-DECISIONS-TRADEOFFS -->
- Give clear guidance (for example, "Choose A if you need X; choose B if you need Y"). <!-- PROC-BEHAV-DECISIONS-GUIDANCE -->
- If the decision space is complex, link to a dedicated decision guide. <!-- PROC-BEHAV-DECISIONS-LINK -->

### Limits (optional) <!-- group: PROC-LIMITS -->

- Describe constraints as a short paragraph; use a list/table only if it improves scanning. <!-- PROC-BEHAV-LIMITS-FORMAT -->
- Cover quotas, rate limits, timeouts, eventual consistency, and destructive side effects. <!-- PROC-BEHAV-LIMITS-COVERAGE -->
- If a constraint is critical to success or safety, surface it with a single concise callout (see Callouts). <!-- PROC-BEHAV-LIMITS-ALERT-CRITICAL -->
- If useful, mention a workaround or mitigation strategy. <!-- PROC-BEHAV-LIMITS-MITIGATION -->
- Link to a dedicated "Limitations" page if details are lengthy. <!-- PROC-BEHAV-LIMITS-LINK -->

### Impact (optional) <!-- group: PROC-IMPACT -->

- A paragraph, list, or table. <!-- PROC-BEHAV-IMPACT-FORMAT -->
- Highlight side effects and risks (for example, data exposure, downtime, irreversible actions). <!-- PROC-BEHAV-IMPACT-RISKS -->
- Note required privileges or safer alternatives when relevant. <!-- PROC-BEHAV-IMPACT-PRIVS-ALTS -->
- Use a single concise callout for critical security impacts; link out for details. <!-- PROC-BEHAV-IMPACT-ALERT-CRITICAL -->

### Prerequisites (optional) <!-- group: PROC-PREREQ -->

- List only the technical setup needed to run the procedure (software, versions, tools, configuration). <!-- PROC-BEHAV-PREREQ-SCOPE -->
- Don’t include roles, permissions, or product variants here; put those in the [access callout](#access-callout-guidelines). <!-- PROC-BEHAV-PREREQ-NO-ROLES -->
- Prefer a single bullet list of noun phrases; keep it brief and link to install/setup instructions as needed. <!-- PROC-BEHAV-PREREQ-LIST-NOUNS -->

## "What to expect" <!-- group: PROC-EXPECT -->

- Use a Markdown H2 with the exact text "What to expect". <!-- PROC-STRUCT-EXPECT-H2-TEXT -->
- Place this section after the introduction and before the first task section. <!-- PROC-STRUCT-EXPECT-POSITION -->
- Include exactly one unordered list with three items (no code blocks or callouts here). <!-- PROC-STRUCT-EXPECT-UL-THREE -->
- Write one complete sentence per bullet (two short sentences max), and end sentences with a period. <!-- PROC-BEHAV-EXPECT-SENTENCE-1-2 -->
- Use parallel wording in each bullet (same grammatical shape), focused on outcomes users will have after completing the procedure (for example, "You can ..."). <!-- PROC-BEHAV-EXPECT-PARALLEL-OUTCOME -->
- Order items from most important to least important. <!-- PROC-BEHAV-EXPECT-PRIORITY -->
- Avoid links unless you must point to headings in the same page. <!-- PROC-BEHAV-EXPECT-LINKS-INTERNAL -->
=======
### Overview guidelines <!-- group: PROC-OVERVIEW -->

- A 50 to 100-word paragraph that explains what the procedure is about, its purpose, and its relevance. <!-- PROC-OVERVIEW-001 -->
- Mention where it applies and who it is for. <!-- PROC-OVERVIEW-002 -->
- Provide a concrete, real-world scenario for the product feature. <!-- PROC-OVERVIEW-003 -->
- Link to related documents or headings in the same document to assist the reader in gathering information. <!-- PROC-OVERVIEW-004 -->
- Only add a short `Note` alert if it prevents confusion; otherwise keep the overview free of alerts. <!-- PROC-OVERVIEW-005 -->

### Decisions guidelines (optional) <!-- group: PROC-DECISIONS -->

- A paragraph, list, or table that outlines any decisions the reader needs to make before starting the procedure. For example, choosing between CLI or GUI installation methods. <!-- PROC-DECISIONS-001 -->
- Use a list for simple comparisons or a table for more complex ones. <!-- PROC-DECISIONS-002 -->
- Focus on key decision factors, such as performance, complexity, cost, prerequisites, and limitations. <!-- PROC-DECISIONS-003 -->
- Highlight trade‑offs clearly. For example, "Option A is faster but less secure" or "Option B adds encryption overhead". <!-- PROC-DECISIONS-004 -->
- Provide real-world guidance. For example, "Choose A if you need X, choose B if you care about Y". <!-- PROC-DECISIONS-005 -->
- For complex decisions, link to a separate heading or dedicated decision-making guide. <!-- PROC-DECISIONS-006 -->

### Limits guidelines (optional) <!-- group: PROC-LIMITS -->

- A paragraph, list, or table that describes any limitations related to the procedure. For example, "Initial cache warm-up can take up to 60 minutes". <!-- PROC-LIMITS-001 -->
- Consider quotas, rate limits, timeouts, eventual consistency, or destructive side effects. <!-- PROC-LIMITS-002 -->
- Use callouts for critical constraints. <!-- PROC-LIMITS-003 -->
- If applicable, mention any workarounds or mitigation strategies. <!-- PROC-LIMITS-004 -->
- For complex limitations, link to a separate heading or dedicated limitations guide. <!-- PROC-LIMITS-005 -->

### Impact guidelines (optional) <!-- group: PROC-IMPACT -->

- A paragraph, list, or table that highlights potential impacts of performing the procedure. For example, when completing the procedure can potentially expose sensitive information. <!-- PROC-IMPACT-001 -->
- Call out risks, required privileges, and safer alternatives. <!-- PROC-IMPACT-002 -->
- Use callouts for critical security impacts. <!-- PROC-IMPACT-003 -->
- For complex security considerations, link to a separate heading or dedicated security guide. <!-- PROC-IMPACT-004 -->

### Prerequisites guidelines (optional) <!-- group: PROC-PREREQ -->

- A paragraph or list that describes technical setup (software, tools, config) needed to run the procedure. For example, "You must have at least Python 3.14 to complete this procedure." <!-- PROC-PREREQ-001 -->
- Don't include roles, permissions, knowledge, or product versions here. Put those in the [access callout](#access-callout-guidelines) at the top.<!-- PROC-PREREQ-002 -->

## "What to expect" guidelines <!-- group: PROC-EXPECT -->

- Use "What to expect" H2 Markdown heading for this section <!-- PROC-EXPECT-001 -->
- Write a single unordered list with three bullet points that summarize the key results of the procedure. <!-- PROC-EXPECT-002 -->
- Aim for one sentence per bullet point, maximum two short sentences. <!-- PROC-EXPECT-003 -->
- Present the items in order from most important to least important. <!-- PROC-EXPECT-004 -->
>>>>>>> 543f454 ((#47) Move files to new repo structure)

**Examples:**

Check out the [procedure example](./procedure-example.md).

## Procedural structure <!-- group: PROC-STRUCT-PATTERN -->

<<<<<<< HEAD
- Choose exactly one layout per article: `flat` or `sectioned`. Do not mix. <!-- PROC-STRUCT-PATTERN-ONE-LAYOUT -->
- Don’t use subtasks. Split into additional H2 tasks (flat) or use the sectioned layout instead. <!-- PROC-STRUCT-PATTERN-NO-SUBTASKS -->
=======
- Choose exactly one layout per article: `flat` or `sectioned`. Do not mix. <!-- PROC-STRUCT-PATTERN-001 -->
- Don't use subtasks. Split into additional H2 task groups or use the sectioned layout instead. <!-- PROC-STRUCT-PATTERN-002 -->
>>>>>>> 543f454 ((#47) Move files to new repo structure)

> **Note**
>
> See [Steps structure: flat vs. sectioned](./procedure.md#steps-structure-flat-vs-sectioned) for guidance.

### Procedure layout: flat <!-- group: PROC-STRUCT-FLAT -->

<<<<<<< HEAD
| Element      | Format                              | Required | ID                        | Rules              |
|:-------------|:------------------------------------|:---------|:--------------------------|:-------------------|
| Task title   | H2                                  | Yes      | `PROC-STRUCT-FLAT-TITLE`  | PROC-TASK-TITLE    |
| Task intro   | Paragraph                           | No       | `PROC-STRUCT-FLAT-INTRO`  | PROC-TASK-INTRO    |
| Task callout | Callout                             | No       | `PROC-STRUCT-FLAT-CALLOUT`| PROC-TASK-CALLOUTS |
| Steps list   | Numbered list or checkboxes (1)     | Yes      | `PROC-STRUCT-FLAT-STEPS`  | PROC-TASK-STEP     |
| Clarifiers   | Bullets under a step (depth 1) (2)  | No       | `PROC-STRUCT-FLAT-CLAR`   | PROC-TASK-CLAR     |
| Code         | Fenced code block under the step (3)| No       | `PROC-STRUCT-FLAT-CODE`   | PROC-TASK-CODE     |
| Screenshot   | Image under the step (3)            | No       | `PROC-STRUCT-FLAT-IMG`    | PROC-TASK-IMG      |

(1) Use checkboxes only for unordered or long-running tasks. Numbered lists are the default for procedures.  
(2) Use a short bullet list for clarifiers or alternatives. Do not create numbered sub-steps.  
(3) Nest code and images inside the list item they clarify (indent so they are children of the preceding step).

> **Note:**
>
> The "Rules" column points to the shared rule group that governs this element (see [Procedure guidelines](#procedure-guidelines)).

### Procedure layout: sectioned <!-- group: PROC-STRUCT-SEC -->

| Element (per step) | Format                              | Required | ID                        | Rules              |
|:-------------------|:------------------------------------|:---------|:--------------------------|:-------------------|
| Step title         | H2 `Step {n}: …`                    | Yes      | `PROC-STRUCT-SEC-TITLE`   | PROC-TASK-TITLE    |
| Step intro         | Paragraph                           | No       | `PROC-STRUCT-SEC-INTRO`   | PROC-TASK-INTRO    |
| Step callout       | Callout                             | No       | `PROC-STRUCT-SEC-CALLOUT` | PROC-TASK-CALLOUTS |
| Step list          | Numbered list or checkboxes (1)     | Yes      | `PROC-STRUCT-SEC-STEPS`   | PROC-TASK-STEP     |
| Clarifiers         | Bullets under a step (depth 1) (2)  | No       | `PROC-STRUCT-SEC-CLAR`    | PROC-TASK-CLAR     |
| Code               | Fenced code block under the step (3)| No       | `PROC-STRUCT-SEC-CODE`    | PROC-TASK-CODE     |
| Screenshot         | Image under the step (3)            | No       | `PROC-STRUCT-SEC-IMG`     | PROC-TASK-IMG      |

(1) Use checkboxes only for unordered or long-running tasks. Numbered lists are the default for procedures.  
(2) Use a short bullet list for clarifiers or alternatives. Do not create numbered sub-steps.  
(3) Nest code and images inside the list item they clarify (indent so they are children of the preceding step).

Additional structural constraints:

- The first section title must be `Step 1:` and subsequent section titles must increment by 1. <!-- PROC-STRUCT-SEC-ORDER-ASC -->
- Each "Step {n}" section contains exactly one ordered list of actions. <!-- PROC-STRUCT-SEC-ONE-OL -->

> **Note**
>
> The "Rules" column points to the shared rule group that governs this element (see [Procedure guidelines](#procedure-guidelines)).

## Procedure

Use these guidelines for both flat and sectioned procedure layouts. <!-- PROC-BEHAV-GUIDE-APPLIES-BOTH -->

### Task/Step Title <!-- group: PROC-TASK-TITLE -->

- Procedure section titles are Markdown H2 headings. <!-- PROC-STRUCT-TASK-H2 -->
- In the sectioned layout, prefix with `Step {n}:` starting at 1 and incrementing by 1. <!-- PROC-STRUCT-SEC-H2-STEP-PREFIX -->
- Aim for 50–60 characters; 80 max. <!-- PROC-BEHAV-TASK-TITLE-LENGTH-50-80 -->
- Start with an imperative verb; avoid the -ing form. <!-- PROC-BEHAV-TASK-TITLE-IMPERATIVE -->
- Use sentence case (capitalize only the first word and proper nouns). <!-- PROC-BEHAV-TASK-TITLE-SENTENCE-CASE -->
- Avoid empty verbs (make, manage, put). <!-- PROC-BEHAV-TASK-TITLE-NO-EMPTY-VERBS -->
- Avoid one- or two-word titles. <!-- PROC-BEHAV-TASK-TITLE-NO-ONE-TWO-WORD -->
- Don’t use punctuation marks in titles (colons, semicolons, dashes) except in the sectioned layout (`Step {n}:`). <!-- PROC-BEHAV-TASK-TITLE-NO-PUNCT -->

### Task/Step intro (optional) <!-- group: PROC-TASK-INTRO -->

- Write 1–2 short sentences that provide context. <!-- PROC-BEHAV-TASK-INTRO-BRIEF -->
- Do not repeat the task title wording. <!-- PROC-BEHAV-TASK-INTRO-NO-REPEAT -->
- Add cross-references here, not inside steps. <!-- PROC-BEHAV-TASK-INTRO-LINKS -->

### Task/Step callout (optional) <!-- group: PROC-TASK-CALLOUTS -->

- Use one callout after the intro for important notes, warnings, or tips. <!-- PROC-STRUCT-TASK-CALLOUTS-AFTER-INTRO -->
- Do not place callouts between steps. <!-- PROC-STRUCT-TASK-CALLOUTS-NO-BETWEEN-STEPS -->
- One callout maximum per task. <!-- PROC-STRUCT-TASK-CALLOUTS-PER-TASK-ONE -->

### Steps list guidelines <!-- group: PROC-TASK-STEP -->

- Use a numbered list when the task is completed in one go. <!-- PROC-BEHAV-TASK-STEP-ORDERED-ONEGO -->
- Use checkboxes when steps are unordered or spread over time. <!-- PROC-BEHAV-TASK-STEP-CHECKBOX-UNORDERED -->
- Start each step with an imperative verb; avoid -ing forms. <!-- PROC-BEHAV-TASK-STEP-IMPERATIVE -->
- One step = one user action (combine only trivial actions). <!-- PROC-BEHAV-TASK-STEP-ONE-ACTION -->
- Author ordered lists with `1.` for every item (1, 1, 1 …). <!-- PROC-STRUCT-TASK-STEP-OL-ONE -->
- Aim for 2–7 steps. Split if longer. <!-- PROC-BEHAV-TASK-STEP-COUNT-2-7 -->
- Avoid one-step tasks. <!-- PROC-BEHAV-TASK-STEP-NO-ONE -->
- When adding paragraphs, images, or code under a step, insert a blank line and indent so they are children of that step. <!-- PROC-STRUCT-TASK-STEP-NESTING -->
- Bold UI elements (buttons, menus, options). <!-- PROC-BEHAV-TASK-STEP-UI-BOLD -->
- Use inline code for commands, filenames, paths, and output. <!-- PROC-BEHAV-TASK-STEP-CODE-INLINE -->
- Don’t use external links in steps; only same-page anchors. <!-- PROC-BEHAV-TASK-STEP-LINKS-INTERNAL -->
- For UI paths, put location before action. <!-- PROC-BEHAV-TASK-STEP-LOCATION-FIRST -->
- For conditions, write the result first, then the condition. <!-- PROC-BEHAV-TASK-STEP-RESULT-THEN-CONDITION -->

### Task/Step Clarifiers (optional) <!-- group: PROC-TASK-CLAR -->

- Don't use numbered substeps beneath a step (nested ordered lists). <!-- PROC-STRUCT-TASK-CLAR-NO-ORDERED -->
- Use bullets for subactions, such as clarifiers or alternatives. <!-- PROC-STRUCT-TASK-CLAR-BULLETS -->
- Limit clarifiers to 2–4 items in one level. <!-- PROC-BEHAV-TASK-CLAR-COUNT-2-4 -->

### Task/Step code (optional) <!-- group: PROC-TASK-CODE -->

Follow the code rules in the Style Guide. <!-- PROC-BEHAV-TASK-CODE-REFER-STYLEGUIDE -->

**Example:**

1. Do this thing...

```bash
gh workflow run build --repo org/repo
```

### Task/Step screenshot (optional) <!-- group: PROC-TASK-IMG -->

See the [writing rules] for screenshots (../../3-validating-design/writing-rules/README.md). <!-- PROC-BEHAV-TASK-SHOT-REFER-STYLEGUIDE -->

## FAQ / Troubleshooting (optional) <!-- group: PROC-EXTRA -->

- Use an H2 Markdown heading for this section. <!-- PROC-STRUCT-EXTRA-H2 -->
- Place this section after the final procedure section and before "Next steps" (if present). <!-- PROC-STRUCT-EXTRA-POSITION -->
- Begin with "Troubleshooting {topic}" for error resolution or "Frequently asked questions" for question-based content. <!-- PROC-BEHAV-EXTRA-TITLE-PATTERN -->
- Use paragraphs, lists, or H3 headings for the content. <!-- PROC-STRUCT-EXTRA-ALLOWED-BLOCKS-H3 -->
- If you use H3 question headings, write them in sentence case and end with a question mark. <!-- PROC-BEHAV-EXTRA-H3-QUESTION-FORM -->
- Use "Frequently asked questions" instead of "FAQ" alone. <!-- PROC-BEHAV-EXTRA-TERM-FAQ -->
- For longer or complex cases, create a separate FAQ or Troubleshooting (concept) article and link to it. <!-- PROC-BEHAV-EXTRA-SPLIT-IF-LONG -->

## Forbidden content <!-- group: PROC-FORBID -->

- Do not use H4–H6 headings. <!-- PROC-STRUCT-FORBID-H4-H6 -->
- Do not include a "Further reading" section or links to other related topics at the end of the document. <!-- PROC-BEHAV-FORBID-NO-FURTHER-READING -->
=======
| Element       | Format                          | Required | ID                        | Rules           |
|:--------------|:--------------------------------|:---------|:--------------------------|:----------------|
| Task title    | H2                              | Yes      | `PROC-STRUCT-FLAT-TITLE`  | PROC-TASK-TITLE |
| Task intro    | Paragraph                       | No       | `PROC-STRUCT-FLAT-INTRO`  | PROC-INTRO      |
| Task callout  | Callout                         | No       | `PROC-STRUCT-FLAT-CALL`   | PROC-CALL       |
| Steps list    | Numbered list or checkboxes (1) | Yes      | `PROC-STRUCT-FLAT-STEPS`  | PROC-STEP       |
| Clarifiers    | Unordered bullets (depth 1) (2) | No       | `PROC-STRUCT-FLAT-BUL`    | PROC-BUL        |
| Code          | Fenced code block               | No       | `PROC-STRUCT-FLAT-CODE`   | PROC-CODE       |
| Screenshot    | Image                           | No       | `PROC-STRUCT-FLAT-IMG`    | PROC-SHOT       |

(1) Use checkboxes only for unordered or long-running tasks. Numbered lists are the default for procedures.
(2) Use a short bullet list for clarifiers or alternatives. Do not create numbered sub-steps.

> **Note:**
>
> The `Rules` column points to the shared rule group that governs this element (see [Procedure guidelines](#procedure-guidelines)).

### Procedure layout: sectioned <!-- group: PROC-STRUCT-SEC -->

| Element (per step) | Format                          | Required | ID                      | Rules           |
| :----------------- | :------------------------------ | :------: | :---------------------- | :---------------|
| Step title         | H2 `Step {n}:`                  |    Yes   | `PROC-STRUCT-SEC-TITLE` | PROC-TASK-TITLE |
| Step intro         | Paragraph                       |    No    | `PROC-STRUCT-SEC-INTRO` | PROC-INTRO      |
| Step callout       | Callout                         |    No    | `PROC-STRUCT-SEC-CALL`  | PROC-CALL       |
| Step actions       | Numbered list                   |    Yes   | `PROC-STRUCT-SEC-STEPS` | PROC-STEP       |
| Clarifiers         | Unordered bullets (depth 1) (2) |    No    | `PROC-STRUCT-SEC-BUL`   | PROC-BUL        |
| Code               | Fenced code block               |    No    | `PROC-STRUCT-SEC-CODE`  | PROC-CODE       |
| Screenshot         | Image                           |    No    | `PROC-STRUCT-SEC-IMG`   | PROC-SHOT       |

(1) Use a short bullet list for clarifiers or alternatives. Do not create numbered sub-steps.

> **Note:**
>
> The `Rules` column points to the shared rule group that governs this element (see [Procedure guidelines](#procedure-guidelines)).

## Procedure guidelines

Use these guidelines for both flat and sectioned procedure layouts. <!-- PROC-GUIDE-001 -->

### Title guidelines <!-- group: PROC-TASK-TITLE -->

- Procedure section titles are Markdown H2 headings. <!-- PROC-TASK-TITLE-LEVEL-H2 -->
- In the sectioned layout, prefix with `Step {n}:` starting at 1 and incrementing by 1. <!-- PROC-TASK-TITLE-STEP-H2 -->
- Aim for 50–60 characters; 80 max. <!-- PROC-TASK-TITLE-LEN -->
- Start with an imperative verb; avoid the *-ing* form. <!-- PROC-TASK-TITLE-VOICE -->
- Use sentence case (capitalize only the first word and proper nouns). <!-- PROC-TASK-TITLE-CASE -->
- Avoid empty verbs (*make*, *manage*, *put*). <!-- PROC-TASK-TITLE-VERB-SPECIFIC -->
- Avoid one- or two-word titles. <!-- PROC-TASK-TITLE-NO-2WORD -->
- Don’t use punctuation marks in titles (colons, semicolons, dashes) except in the sectioned layout (`Step {n}:`). <!-- PROC-TASK-TITLE-NO-PUNCT -->

### Task introduction (optional) guidelines <!-- group: PROC-INTRO -->

- Write 1–2 short sentences that provide context. <!-- PROC-INTRO-BRIEF -->
- Do not repeat the task title wording. <!-- PROC-INTRO-NO-REPEAT -->
- Add cross-references here, not inside steps. <!-- PROC-INTRO-LINKS -->

### Task callout (optional) guidelines <!-- group: PROC-CALL -->

- Use one callout after the intro for important notes, warnings, or tips. <!-- PROC-CALL-ONCE -->
- Do not place callouts between steps. <!-- PROC-CALL-NO-BETWEEN -->
- One callout maximum per task. <!-- PROC-CALL-ONE -->

### Steps list guidelines <!-- group: PROC-STEP -->

- Use a numbered list when the task is completed in one go. <!-- PROC-STEP-LIST-ORDERED -->
- Use checkboxes when steps are unordered or spread over time. <!-- PROC-STEP-LIST-CHECKBOX -->
- Start each step with an imperative verb; avoid *-ing* forms. <!-- PROC-STEP-VERB -->
- One step = one user action (combine only trivial actions). <!-- PROC-STEP-ONE-ACTION -->
- All steps must use number `1` (1, 1, 1, ... instead of 1, 2, 3, ...) <!-- PROC-STEP-ALL-ONE -->
- Aim for 2–7 steps. Split if longer. <!-- PROC-STEP-RANGE -->
- Avoid one-step tasks. <!-- PROC-STEP-NO-ONE -->
- When adding paragraphs, images, or code under a step, insert a blank line and indent to align with the first text after the list marker. <!-- PROC-STEP-BLOCKS -->
- Bold UI elements (buttons, menus, options). <!-- PROC-STEP-UI-BOLD -->
- Use inline code for commands, filenames, paths, and output. <!-- PROC-STEP-CODE-INLINE -->
- Don’t use external links in steps; only same-page anchors. <!-- PROC-STEP-LINKS-INTERNAL -->
- For UI paths, put location before action. <!-- PROC-STEP-LOC-FIRST -->
- For conditions, write the result first, then the condition. <!-- PROC-STEP-RESULT-FIRST -->

### Clarifiers (optional) guidelines <!-- group: PROC-BUL -->

- Don't use numbered substeps beneath a step (nested ordered lists). <!-- PROC-BUL-NOSUBTASK -->
- Use bullets for subactions, such as clarifiers or alternatives. <!-- PROC-BUL-BULLETS -->
- Limit clarifiers to 2–4 items in one level. <!-- PROC-BUL-LIMIT -->

### Task code (optional) guidelines <!-- group: PROC-CODE -->

Follow the code rules in the Style Guide. <!-- PROC-CODE-LINK -->

**Example:**

	1. Do this thing...

	```bash
	gh workflow run build --repo org/repo
	```

### Task screenshot (optional) guidelines <!-- group: PROC-SHOT -->

Follow the Screenshots rules in the Style Guide. <!-- PROC-SHOT-LINK -->

## FAQ / Troubleshooting guidelines (optional) <!-- group: PROC-EXTRA -->

- Use H2 Markdown heading for this section. <!-- PROC-EXTRA-001 -->
- Begin with "Troubleshooting [topic]" for error resolution or "Frequently asked questions" for query-based content. <!-- PROC-EXTRA-003 -->
- Use paragraphs, lists, or H3 headings for content. <!-- PROC-EXTRA-002 -->
- Use "Frequently asked questions" instead of "FAQ" alone. <!-- PROC-EXTRA-004 -->
- For longer FAQ or complex troubleshooting scenarios, create a separate FAQ or Troubleshooting (concept) article instead. <!-- PROC-EXTRA-005 -->

## Extra content guidelines (forbidden) <!-- group: PROC-FORBID -->

- Do not use H4-H6 headings. <!-- PROC-FORBID-001 -->
- Do not include a "Further reading" section or links to other related topics at the end of the document. <!-- PROC-FORBID-002 -->
>>>>>>> 543f454 ((#47) Move files to new repo structure)
