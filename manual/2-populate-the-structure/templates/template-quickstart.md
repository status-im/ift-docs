| Section                       | Format                 | Required | ID                    |
|:------------------------------|:-----------------------|:---------|:----------------------|
| Title                         | H1                     | Yes      | `QST-PAGE-TITLE`      |
| Subtitle                      | Single bold sentence   | Yes      | `QST-PAGE-SUBTITLE`   |
| Access callout                | Note-type callout      | No       | `QST-ACCESS`.         |
| Callouts                      | Tip, Note, Important, Caution | No  | `QST-CALLOUTS`      |
| Overview                      | Paragraph              | Yes      | `QST-OVERVIEW`        |
| "Before you start" title      | H2                     | No       | `QST-BEFORE-START-001`|
| "Before you start" list       | Bullet list            | No       | `QST-BEFORE-START`    |
| Task title                    | H2                     | Yes      | `QST-TASK-TITLE`      |
| Task intro                    | Paragraph              |    No    | `QST-TASK-INTRO`      |
| Task callout                  | Callout                |    No    | `QST-TASK-CALL`       |
| Task actions                  | Numbered list          |    Yes   | `QST-TASK-STEPS`      |
| Clarifiers                    | Unordered bullets (depth 1) (2) | No | `QST-TASK-BUL`     |
| Code                          | Fenced code block      |    No    | `QST-TASK-CODE`       |
| Screenshot                    | Image                  |    No    | `QST-TASK-IMG`        |
| H4-H6 headings                | -                      | Forbidden| `QST-EXTRA-002`       |
| "Next steps" title            | H2                     | No       | `QST-NEXT-001`        |
| "Next steps" list             | Bullet list            | No       | `QST-NEXT`            |

## Front matter
---
title:
doc_type: # [procedure, concept, reference, quickstart, api]
product: # [storage, blockchain, communication]
topics: []
authors: # GitHub username
owner: ift
doc_version: # increased by one after every update
slug:
---

## Title guidelines <!-- group: QST-PAGE-TITLE -->

- Use a Markdown H1 heading. <!-- QST-PAGE-TITLE-001 -->
- For the title, use the word "Quickstart for" + the name of the project or feature. Do not add other text. For example, "Quickstart for Logos Storage". <!-- QST-PAGE-TITLE-002 -->

## Subtitle guidelines <!-- group: QST-PAGE-SUBTITLE -->

- Single sentence with no links, list items, or formatting. Ends with a period. <!-- QST-PAGE-SUBTITLE-001 -->
- Use bold format. Stay under 120 characters. <!-- QST-PAGE-SUBTITLE-002 -->
- Use imperative verbs to describe the topic's purpose or benefit: *Explore*, *Get started*, *Try*, and so on. <!-- QST-PAGE-SUBTITLE-003 -->
- Adds new value beyond the title. It should not repeat the title or be a rephrased version of it. <!-- QST-PAGE-SUBTITLE-004 -->

**Examples:**

- *Get hands-on with Waku's key capabilities.*
- *Quickly add payments to your project with Stripe.*

## Access callout guidelines <!-- group: QST-ACCESS -->

This note-type callout is exclusively to alert readers about what roles, permissions, or product versions are required to perform the procedure.

- Place it after the title and subtitle, before the overview. <!-- QST-ACCESS-001 -->
- Use the `Note` callout style. <!-- QST-ACCESS-002 -->
- Start with the phrase: *This feature is available to users with...* or *To perform this procedure, you need...* <!-- QST-ACCESS-003 -->
- Focus on required roles, permissions, or product versions only. Don't include any other prerequisite such as knowledge, skills, or tools. <!-- QST-ACCESS-004 -->

**Examples:**

- *This feature is available to admin roles in version 5.0 or later with write permissions on the repository.*
- *This procedure requires contributor roles in version 2.3 or higher and read/write access to the API endpoints.*

## Callouts guidelines <!-- QST-CALLOUTS -->

- Use callouts sparingly in the document and only when necessary to avoid overwhelming the reader. <!-- QST-CALLOUTS-001 -->
- One callout maximum per section <!-- QST-CALLOUTS-002 -->
- Keep callouts concise. <!-- QST-CALLOUTS-003 -->
- Use the appropriate type: `Tip`, `Note`, `Important`, or `Caution`. <!-- QST-CALLOUTS-004 -->

## Overview guidelines <!-- group: QST-OVERVIEW -->

- Describe the product or feature' core purposes and what the user will achieve in this quickstart. <!-- QST-OVERVIEW-001 -->
- Write one or two 50 to 100-word paragraphs. <!-- QST-OVERVIEW-002 -->
-  Avoid lengthy discussions of the product or feature. Link to a [concept](./concept-help-me-to-understand.md) article if you need to provide more information. <!-- QST-OVERVIEW-003 -->
- Link to related documents or headings in the same document to support the reader's gathering of information. <!-- QST-OVERVIEW-004 -->

## "Before you start" (optional) guidelines <!-- group: QST-BEFORE-START -->

- Use the "Before you start" H2 heading for this section. <!-- QST-BEFORE-START-001 -->
- Write a single unordered list including: <!-- QST-BEFORE-START-002 -->
    - The intended audience of this quickstart.
    - Required prior knowledge for using this quickstart.
    - The software or hardware requirements.
- Use noun phrases (For example, "familiarity with Golang"). Don't include verbs such as "learn" or "prepare". <!-- QST-BEFORE-START-003 -->
- Provide [links](../../20-style-the-content/10-links.md) to related content such as installation instructions or articles that provide required knowledge. <!-- QST-BEFORE-START-004 -->
- Don't include the procedure for setting up or installing prerequisites. If you must explain the procedure, link to the corresponding document or resource. <!-- QST-BEFORE-START-005 -->

> ⚙️ **Example:**
>
> Before you begin, make sure you have:
>
> - A basic understanding of [Ethereum](https://ethereum.org/en/developers/docs/intro-to-ethereum/) ↗ concepts
> - Knowledge of how to work with Python virtual environments
> - A machine running Ubuntu Linux with the following minimum requirements:
>   - 4 GB memory
>   - 2 TB SSD
>   - Linux 64-bit

## Task guidelines: <!-- group: QST-TASK -->

- Choose two or three tasks that are essential, quick to complete, and provide immediate value to the user. <!-- QST-TASK-001 -->
    - The first task is usually about setting up or installing the product or feature. However, if setup requires more than seven steps, create a separate installation guide and direct readers to it in the [Before you start](#before-you-start-section) section. <!-- QST-TASK-002 -->
    - For the other task(s), focus on the core functionalities of the product or feature. <!-- QST-TASK-003 -->

### Task title guidelines <!-- group: QST-TASK-TITLE -->

- Task titles are Markdown H2 headings. <!-- QST-TASK-TITLE-LEVEL-H2 -->
- Don’t include numbering in the title. <!-- QST-TASK-HEADING -->
- Aim for 50–60 characters; 80 max. <!-- QST-TASK-TITLE-LEN -->
- Start with an imperative verb; avoid the *-ing* form. <!-- QST-TASK-TITLE-VOICE -->
- Use sentence case (capitalize only the first word and proper nouns). <!-- QST-TASK-TITLE-CASE -->
- Avoid empty verbs (*make*, *manage*, *put*). <!-- QST-TASK-TITLE-VERB-SPECIFIC -->
- Avoid one- or two-word titles. <!-- QST-TASK-TITLE-NO-2WORD -->
- Don’t use punctuation marks in titles (colons, semicolons, dashes). <!-- QST-TASK-TITLE-NO-PUNCT -->

> ⚙️ **Example:**
>
> - *Run a Waku node*
> - *Connect to the Codex network*
> - *Configure system admin access*

### Task introduction guidelines (optional) <!-- group: QST-TASK-INTRO -->

- Write 1–2 short sentences that provide context. <!-- QST-TASK-INTRO-BRIEF -->
- Do not repeat the task title wording. <!-- QST-TASK-INTRO-NO-REPEAT -->
- Add cross-references here, not inside steps. <!-- QST-TASK-INTRO-LINKS -->

### Task callout guidelines (optional) <!-- group: QST-TASK-CALL -->

- Use one callout after the intro for important notes, warnings, or tips. <!-- QST-TASK-CALL-ONCE -->
- Do not place callouts between steps. <!-- QST-TASK-CALL-NO-BETWEEN -->
- One callout maximum per task. <!-- QST-TASK-CALL-ONE -->

### Task steps guidelines:

- Use a numbered list. <!-- QST-TASK-STEP-LIST-ORDERED -->
- Start each step with an imperative verb; avoid *-ing* forms. <!-- QST-TASK-STEP-VERB -->
- One step = one user action (combine only trivial actions). <!-- QST-TASK-STEP-ONE-ACTION -->
- All steps must use number `1` (1, 1, 1, ... instead of 1, 2, 3, ...) <!-- QST-TASK-STEP-ALL-ONE -->
- Aim for 2–7 steps. Split if longer. <!-- QST-TASK-STEP-RANGE -->
- Avoid one-step tasks. <!-- QST-TASK-STEP-NO-ONE -->
- When adding paragraphs, images, or code under a step, insert a blank line and indent to align with the first text after the list marker. <!-- QST-TASK-STEP-BLOCKS -->
- Bold UI elements (buttons, menus, options). <!-- QST-TASK-STEP-UI-BOLD -->
- Use inline code for commands, filenames, paths, and output. <!-- QST-TASK-STEP-CODE-INLINE -->
- Don’t use external links in steps; only same-page anchors. <!-- QST-TASK-STEP-LINKS-INTERNAL -->
- For UI paths, put location before action. <!-- QST-TASK-STEP-LOC-FIRST -->
- For conditions, write the result first, then the condition. <!-- QST-TASK-STEP-RESULT-FIRST -->

### Clarifiers guidelines (optional) <!-- group: QST-TASK-BUL -->

- Don't use numbered substeps beneath a step (nested ordered lists). <!-- QST-TASK-BUL-NOSUBTASK -->
- Use bullets for subactions, such as clarifiers or alternatives. <!-- QST-TASK-BUL-BULLETS -->
- Limit clarifiers to 2–4 items in one level. <!-- QST-TASK-BUL-LIMIT -->

### Task code guidelines (optional) <!-- group: QST-TASK-CODE -->

Follow the code rules in the Style Guide. <!-- QST-TASK-CODE-LINK -->

**Example:**

    1. Do this thing...

    ```bash
    gh workflow run build --repo org/repo
    ```

### Task screenshot guidelines (optional) <!-- group: QST-TASK-SHOT -->

Follow the Screenshots rules in the Style Guide. <!-- QST-TASK-SHOT-LINK -->

## `Next steps` guidelines (optional) <!-- group: QST-NEXT -->

- Use the "Next steps" H2 heading for this section. <!-- QST-NEXT-001 -->
- Write a bullet list of links to articles about other tasks that the users can try after completing the quickstart. <!-- QST-NEXT-002 -->
- Write at most three articles. <!-- QST-NEXT-003 -->
- Consider a logical connection from the current quickstart that can act as a basis for users' next learning. <!-- QST-NEXT-004 -->

## Extra content guidelines <!-- group: QST-EXTRA -->

- The entire quickstart should be about 1 200 words long. <!-- QST-EXTRA-001 -->
- Do not use H4-H6 headings. <!-- QST-EXTRA-002 -->
