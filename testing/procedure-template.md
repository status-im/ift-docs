| Section                        | Format                              | Required  | ID                       |
|:-------------------------------|:------------------------------------|:----------|:------------------------|
| Title                          | H1                                  | Yes       | `PROC-PAGE-TITLE-001`   |
| Subtitle                       | Single bold sentence                | Yes       | `PROC-PAGE-TITLE-002`   |
| Access callout                 | Note-type callout                   | No        | `PROC-ACCESS-001`       |
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

## Front matter

---
title:
doc_type: # [procedure, concept, reference, quickstart, api]
product: # [codex, nomos, waku]
topics: []
steps_layout: # [flat|sectioned]
authors: # GitHub username
owner: ift
doc_version: # increased by one after every update
slug:
---

## Title (H1) guidelines <!-- PROC-PAGE-TITLE-001 -->

- Use Markdown H1 headings and aim for 50 to 60 characters; 80 characters maximum. <!-- PROC-PAGE-TITLE-003 -->
- Start with an action verb in the imperative form. Don't use the *-ing* form of the verb. <!-- PROC-PAGE-TITLE-004 -->
- Capitalize only the first word and any proper nouns (sentence-style capitalization). <!-- PROC-PAGE-TITLE-005 -->
- Focus on the result, not on the task. Emphasize the desired outcome, rather than describing the specific actions involved. For example, instead of "Install Node.js and create a project directory", use "Set up a local development environment for Node.js". <!-- PROC-PAGE-TITLE-006 -->
- Include the action and the object/context (what/where/how). <!-- PROC-PAGE-TITLE-007 -->
- Avoid one- or two-word titles and empty verbs like *make*, *manage*, or *put*. <!-- PROC-PAGE-TITLE-008 -->
- Don't use punctuation marks, such as colons, semicolons, or dashes, except for the required `Step {n}:` prefix. <!-- PROC-PAGE-TITLE-009 -->

Examples:

	| Usage   | Example                                 |
	|:--------|:----------------------------------------|
	| **Use** | Create a codespace from a template      |
	| Avoid   | Creating a codespace from a template    |
	| **Use** | Use source control in your codespace    |
	| Avoid   | Use source control                      |
	| **Use** | Collaborate with others in a codespace  |
	| Avoid   | Set up a live share session             |

## Subtitle guidelines <!-- PROC-PAGE-TITLE-002 -->

- Single sentence with no links, list items, or formatting. Ends with a period. <!-- PROC-PAGE-TITLE-010 -->
- Use bold format. Stay under 120 characters. <!-- PROC-PAGE-TITLE-011 -->
- Use imperative verbs to describe the document purpose or benefit: *Learn*, *Explore*, *Understand*, *Discover*, *Create*, *Follow*, *Try*, and other action verbs. <!-- PROC-PAGE-TITLE-012 -->
- Adds new value beyond the title. It should not repeat the title or be a rephrased version of it. <!-- PROC-PAGE-TITLE-013 -->

Examples:

- **Title**: *Quickstart for GitHub Actions* / **Subtitle**: *Try out the core features of GitHub Actions in minutes.*
- **Title**: *Create a pull request* / **Subtitle**: *Create a pull request to propose and collaborate on changes to a repository.*

## Access callout guidelines <!-- PROC-ACCESS-001 -->

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
- Keep them concise. <!-- PROC-CALLOUTS-003 -->
- Use the appropriate type: `Tip`, `Note`, `Important`, or `Caution`. <!-- PROC-CALLOUTS-004 -->

## Introduction guidelines

Every procedure requires an introduction that provides context and helps readers understand the procedure's purpose and scope. The introduction includes these sections, each one represented by a paragraph, list, or table:

- [Overview guidelines](#overview-guidelines)
- [Decisions guidelines (optional)](#decisions-guidelines-optional)
- [Limits guidelines (optional)](#limits-guidelines-optional)
- [Impact guidelines (optional)](#impact-guidelines-optional)
- [Prerequisites guidelines (optional)](#prerequisites-guidelines-optional)

**Examples:**

For an example of a procedure introduction, check out the [procedure example](./procedure-example.md).

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

## `What to expect` guidelines <!-- group: PROC-EXPECT -->

- Use `What to expect` H2 Markdown heading for this section <!-- PROC-EXPECT-001 -->
- Write a single unordered list with three bullet points that summarize the key results of the procedure. <!-- PROC-EXPECT-002 -->
- Aim for one sentence per bullet point, maximum two short sentences. <!-- PROC-EXPECT-003 -->
- Present the items in order from most important to least important. <!-- PROC-EXPECT-004 -->

**Examples:**

For an example, check out the [procedure example](./procedure-example.md).

## Procedural structure <!-- group: PROC-STRUCT-PATTERN -->

- Choose exactly one layout per article: `flat` or `sectioned`. Do not mix. <!-- PROC-STRUCT-PATTERN-001 -->
- Don't use subtasks. Split into additional H2 task groups or use the sectioned layout instead. <!-- PROC-STRUCT-PATTERN-002 -->

> **Note**
>
> See [Steps structure: flat vs. sectioned](./procedure.md#steps-structure-flat-vs-sectioned) for guidance.

### Procedure layout: flat <!-- group: PROC-STRUCT-FLAT -->

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

### Title (H2) guidelines <!-- group: PROC-TASK-TITLE -->

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
