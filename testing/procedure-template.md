# Procedure template

## Non-procedural structure

| Element                        | Format                       | Required | ID                 |
|:-------------------------------|:-----------------------------|:---------|:-------------------|
| Title                          | H1                           | Yes      | `PROC-TITLE-001`   |
| Subtitle                       | H4                           | Yes      | `PROC-TITLE-002`   |
| Access prerequisites admonition| Info-type admonition         | No       | `PROC-PREREQ-001`  |
| Overview                       | Paragraph                    | Yes      | `PROC-OVERVIEW`    |
| Admonition                     | Info admonition              | No       | `PROC-OVERVIEW-005`|
| Decisions                      | Paragraph, list, table       | No       | `PROC-DECISIONS`   |
| Limits                         | Paragraph, list, table       | No       | `PROC-LIMITS`      |
| Impact                         | Paragraph, list, table       | No       | `PROC-IMPACT`      |
| "What to expect" heading       | H2                           | Yes      | `PROC-EXPECT-001`  |
| "What to expect" list          | Unordered list               | Yes      | `PROC-EXPECT-002`  |
| Procedure layout               | Flat or sectioned            | Yes      | `PROC-STEPS-PATTERN-001` |
| FAQ / Troubleshooting title    | H2                           | No       | `PROC-EXTRA-001`   |
| FAQ / Troubleshooting content  | Paragraph, list              | No       | `PROC-EXTRA-002`   |
| H5-H6 section                  | -                            | Forbidden| `PROC-EXTRA-003`   |
| Further reading                | -                            | Forbidden| `PROC-EXTRA-004`   |

## Front matter

---
title:
doc_type: # [procedure, concept, reference, quickstart, api]
product: # [codex, nomos, waku]
topics: []
authors: # GitHub username
owner: ift
doc_version: # increased by one after every update
slug:
---

## Title guidelines <!-- PROC-TITLE-001 -->

- **Keep it short and to the point**. Use Markdown H1 headings and aim for 50 to 60 characters; 80 characters maximum. <!-- PROC-TITLE-003 -->
- **Use the imperative form**. Start the title with an action verb in the imperative form. Don't use the *-ing* form of the verb. <!-- PROC-TITLE-004 -->
- **Use sentence case capitalization**. Capitalize only the first word and any proper nouns. <!-- PROC-TITLE-005 -->
- **Focus on the result, not on the task**. Emphasize the desired outcome, rather than listing or describing the specific actions or steps involved. For example, instead of "Install Node.js and create a project directory", use "Set up a local development environment for Node.js". <!-- PROC-TITLE-006 -->
- **Be specific and descriptive**. Include the action and the object/context (what/where/how). Avoid one- or two-word titles and empty verbs like *make*, *manage*, or *put*. <!-- PROC-TITLE-007 -->
- **Avoid using punctuation marks**. Don't use colons, semicolons, or dashes. <!-- PROC-TITLE-008 -->

Examples:

	| Usage   | Example                                 |
	|:--------|:----------------------------------------|
	| **Use** | Create a codespace from a template      |
	| Avoid   | Creating a codespace from a template    |
	| **Use** | Use source control in your codespace    |
	| Avoid   | Use source control                      |
	| **Use** | Collaborate with others in a codespace  |
	| Avoid   | Set up a live share session             |

## Subtitle guidelines <!-- PROC-TITLE-002 -->

- Single sentence with no links, list items, or formatting. Ends with a period. <!-- PROC-TITLE-009 -->
- Use H4 format. Stay under 120 characters / 20 words. <!-- PROC-TITLE-010 -->
- Use imperative verbs to describe the document purpose or benefit: *Learn*, *Explore*, *Understand*, *Discover*, *Create*, *Follow*, *Try*, and other action verbs. <!-- PROC-TITLE-011 -->
- Adds new value beyond the title. It should not repeat the title or be a rephrased version of it. <!-- PROC-TITLE-012 -->

Examples:

- **Title**: *Quickstart for GitHub Actions* / **Subtitle**: *Try out the core features of GitHub Actions in minutes.*
- **Title**: *Create a pull request* / **Subtitle**: *Create a pull request to propose and collaborate on changes to a repository.*

## Access prerequisites admonition guidelines <!-- PROC-PREREQ-001 -->

This information-type admonition is exclusively to alert readers about what roles, permissions, or product versions are required to perform the procedure.

- Place it after the title and subtitle, before the introduction. <!-- PROC-PREREQ-002 -->
- Use the **Info** admonition style. <!-- PROC-PREREQ-003 -->
- Start with the phrase: *This feature is available to users with...* or *To perform this procedure, you need...* <!-- PROC-PREREQ-004 -->
- Focus on required roles, permissions, or product versions only. Don't include any other prerequisite such as knowledge, skills, or tools. <!-- PROC-PREREQ-005 -->

**Examples:**

- *This feature is available to admin roles in version 5.0 or later with write permissions on the repository.*
- *This procedure requires contributor roles in version 2.3 or higher and read/write access to the API endpoints.*

## Introduction guidelines

Every procedure requires an introduction that provides context and helps readers understand the procedure's purpose and scope. The introduction includes these sections, each one represented by a paragraph, list, or table:

- [Overview guidelines](#overview-guidelines)
- [Decisions guidelines (optional)](#decisions-guidelines-optional)
- [Limits guidelines (optional)](#limits-guidelines-optional)
- [Impact guidelines (optional)](#impact-guidelines-optional)

**Examples:**

For an example, check out [concept example](./concept-example.md).

### Overview guidelines <!-- group: PROC-OVERVIEW -->

- A 50 to 100-word paragraph that explains what the procedure is about, its purpose, and its relevance. <!-- PROC-OVERVIEW-001 -->
- Mention where it applies and who it is for. <!-- PROC-OVERVIEW-002 -->
- Provide a concrete, real-world scenario for the product feature. <!-- PROC-OVERVIEW-003 -->
- Link to related documents or headings in the same document to assist the reader in gathering information. <!-- PROC-OVERVIEW-004 -->
- Use the **Info** admonition style to highlight important notes or warnings related to the procedure. <!-- PROC-OVERVIEW-005 -->

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
- Use admonitions for critical constraints. <!-- PROC-LIMITS-003 -->
- If applicable, mention any workarounds or mitigation strategies. <!-- PROC-LIMITS-004 -->
- For complex limitations, link to a separate heading or dedicated limitations guide. <!-- PROC-LIMITS-005 -->

### Impact guidelines (optional) <!-- group: PROC-SECURITY -->

- A paragraph, list, or table that highlights potential impacts of performing the procedure. For example, when completing the procedure can potentially expose sensitive information. <!-- PROC-SECURITY-001 -->
- Call out risks, required privileges, and safer alternatives. <!-- PROC-SECURITY-002 -->
- Use admonitions for critical security impacts. <!-- PROC-SECURITY-003 -->
- For complex security considerations, link to a separate heading or dedicated security guide. <!-- PROC-SECURITY-004 -->

## `What to expect` guidelines <!-- group: PROC-EXPECT -->

- Use `What to expect` H2 Markdown heading for this section <!-- PROC-EXPECT-001 -->
- Write a single unordered list with three bullet points that summarize the key results of the procedure. <!-- PROC-EXPECT-002 -->
- Present the items in order from most important to least important. <!-- PROC-EXPECT-003 -->
- Aim for one sentence per bullet point, maximum two short sentences. <!-- PROC-EXPECT-004 -->

**Examples:**

For an example, check out [concept example](./concept-example.md).

## Procedural structure

- Choose exactly one layout per article: `flat` or `sectioned`. Do not mix. <!-- PROC-STEPS-PATTERN-001 -->

> **Information**
>
> See [Steps structure: flat vs. sectioned](./procedure.md#steps-structure-flat-vs-sectioned) for guidance.

### Procedure layout: flat <!-- group: PROC-STEPS-FLAT -->

| Element | Format | Required | ID |
|:--------|:-------|:---------|:---|
| Steps list | Numbered list or checkboxes | Yes | `PROC-STEPS-FLAT-001` |
| Step clarifiers | Unordered list | No | `PROC-STEPS-FLAT-002` |
| Step code | Fenced code block | No | `PROC-STEPS-FLAT-003` |
| Step screenshot | Image | No | `PROC-STEPS-FLAT-004` |

### Procedure layout: sectioned <!-- group: PROC-STEP-SEC -->

| Element | Format | Required | ID |
|:--------|:-------|:---------|:---|
| Section title | H2: `Step {n}` | Yes | `PROC-STEP-SEC-001` |
| Section intro | Paragraph | No | `PROC-STEP-SEC-002` |
| Section actions | Ordered list | Yes | `PROC-STEP-SEC-003` |
| Section clarifiers | Unordered list | No | `PROC-STEP-SEC-004` |
| Section code | Fenced code block | No | `PROC-STEP-SEC-005` |
| Section screenshot | Image | No | `PROC-STEP-SEC-006` |

## Task guidelines <!-- group: PROC-TASK -->

Every task requires:

- [Title](#title-guidelines)
- [Introduction](#task-introduction-optional-guidelines) (Optional)
- [Steps list](#steps-list-guidelines)
- [Screenshot](#task-screenshot-optional-guidelines) (Optional)
- [Admonition](#task-admonition-optional-guidelines) (Optional)
- [Subtasks](#subtask-guidelines-optional) (Optional)

### Title guidelines <!-- PROC-TASK-001 -->

- Use H2 Markdown heading for task titles. <!-- PROC-TASKTITLE-001 -->

### Task introduction (optional) guidelines <!-- PROC-TASKINTRO-002 -->

- One or two short sentences that provide context for the task. <!-- PROC-TASKINTRO-001 -->
- Link to other headings in the same document here, not in the task steps. <!-- PROC-TASKINTRO-002 -->
- Avoid repeating details from the task title. For example, if the task title is "Create a codespace from a template," do not start the introduction with "To create a codespace from a template..." <!-- PROC-TASKINTRO-003 -->

### Task admonition (optional) guidelines <!-- PROC-TASK-005 -->

- If necessary, use a single admonition after the task introduction to highlight important notes, warnings, or tips related to the task. <!-- PROC-TASKADM-001 -->
- Do not use admonitions between steps. <!-- PROC-TASKADM-002 -->

### Steps list guidelines <!-- group: PROC-STEP -->

- Use a numbered list when the task can be completed in one go. <!-- PROC-STEP-LIST-ORDERED -->
- Use checkboxes when steps are unordered or spread over time. <!-- PROC-STEP-LIST-CHECKBOX -->
- Start each step with an imperative verb; avoid -ing forms. <!-- PROC-STEP-VERB-IMPERATIVE -->
- Aim for 2–7 steps; split if more are needed. <!-- PROC-STEP-COUNT-2-7 -->
- Avoid one-step tasks; merge or rethink scope. <!-- PROC-STEP-NO-ONE -->
- Bold UI elements (buttons, menus, options). <!-- PROC-STEP-UI-BOLD -->
- Use inline code for commands, filenames, paths, output. <!-- PROC-STEP-CODE-INLINE -->
- Don’t use external links inside steps; only same-page anchors. <!-- PROC-STEP-LINKS-INTERNAL -->
- One step = one user action (combine only trivial actions). <!-- PROC-STEP-ONE-ACTION -->
- For UI locations, write location before action. <!-- PROC-STEP-LOCATION-FIRST -->
- Write the result first, then the condition. <!-- PROC-STEP-RESULT-THEN-CONDITION -->

### Task screenshot (optional) guidelines <!-- PROC-TASK-004 -->



### Subtask guidelines (optional) <!-- group: PROC-SUBTASK -->

<!-- **Second H3**
If you add an H3, at least one sibling H3 must follow or the split is unnecessary.
-->

