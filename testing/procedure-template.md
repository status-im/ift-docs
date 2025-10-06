# Procedure template <!-- This is an informative header. Replace it with your procedure title -->

## Procedure structure <!-- This is an informative header. Remove it before merging your content. -->

| Element                        | Format                         | Required | ID                   |
|:-------------------------------|:-------------------------------|:---------|:---------------------|
| Title                          | H1                             | Yes      | `PROC-TITLE-001`     |
| Subtitle                       | H4                             | Yes      | `PROC-TITLE-002`     |
| Access prerequisites admonition| Info-type admonition           | No       | `PROC-PREREQ-001`    |
| Overview                       | Paragraph                      | Yes      | `PROC-INTRO-001`     |
| Decisions                      | Paragraph, list, table         | No       | `PROC-INTRO-002`   |
| Limits / Behaviors             | Paragraph, list, table         | No       | `PROC-INTRO-003`   |
| Security / Impact              | Paragraph, list, table         | No       | `PROC-INTRO-004`|
| "What to expect" heading       | H2                             | Yes      | `PROC-EXPECT-001`    |
| "What to expect" list          | Unordered list                 | Yes      | `PROC-EXPECT-002`    |
| Admonition                     | Admonition                     | No       | `PROC-EXPECT-003`    |
| Task title                     | H2                             | Yes      | `PROC-TASK-001`      |
| Task intro                     | Paragraph                      | No       | `PROC-TASK-002`      |
| Steps list                     | Numbered list or checkboxes    | Yes      | `PROC-TASK-003`      |
| Step screenshot                | Screenshot                     | No       | `PROC-TASK-004`      |
| Task admonition                | Admonition                     | No       | `PROC-TASK-005`      |
| Subtask title                  | H3                             | No       | `PROC-TASK-006`      |
| Subtask intro                  | Paragraph                      | No       | `PROC-TASK-007`      |
| Subtask steps list             | Numbered list or checkboxes    | No       | `PROC-TASK-008`      |
| Subtask step screenshot        | Screenshot                     | No       | `PROC-TASK-009`      |
| Subtask admonition             | Admonition                     | No       | `PROC-TASK-010`      |
| FAQ / Troubleshooting title    | H2                             | No       | `PROC-EXTRA-001`     |
| FAQ / Troubleshooting content  | Paragraph, list                | No       | `PROC-EXTRA-002`     |
| H5-H6 section                  | -                              | Forbidden| `PROC-EXTRA-003`     |
| Further reading                | -                              | Forbidden| `PROC-EXTRA-004`     |

## Front matter <!-- This is an informative header. Remove it before merging your content. -->

---
title: 
doc_type: 
product: 
topics: []
authors: # GitHub user name
owner: ift
doc_version: # increased by one after every update
slug: 
---

## Title guidelines <!-- This is an informative header. Remove it before merging your content. --> <!-- `PROC-TITLE-001` -->

- **Keep it short and to the point**. Use Markdown H1 headings and aim for 50 to 60 characters; 80 characters maximum. <!-- `PROC-TITLE-003` -->
- **Use the imperative form**. Start the title with an action verb in the imperative form. Don't use the *-ing* form of the verb. <!-- `PROC-TITLE-004` -->
- **Use sentence case capitalization**. Capitalize only the first word and any proper nouns. <!-- `PROC-TITLE-005` -->
- **Focus on the result, not on the task**. Emphasize the desired outcome, rather than listing or describing the specific actions or steps involved. For example, instead of "Install Node.js and create a project directory", use "Set up a local development environment for Node.js". <!-- `PROC-TITLE-006` -->
- **Be specific and descriptive**. Include the action and the object/context (what/where/how). Avoid one- or two-word titles and empty verbs like *make*, *manage*, or *put*. <!-- `PROC-TITLE-007` -->
- **Avoid using punctuation marks**. Don't use colons, semicolons, or dashes. <!-- `PROC-TITLE-008` -->

Examples:

	| Usage   | Example                                 |
	|:--------|:----------------------------------------|
	| **Use** | Create a codespace from a template      |
	| Avoid   | Creating a codespace from a template    |
	| **Use** | Use source control in your codespace    |
	| Avoid   | Use source control                      |
	| **Use** | Collaborate with others in a codespace  |
	| Avoid   | Set up a live share session             |

## Subtitle guidelines <!-- This is an informative header. Remove it before merging your content. --> <!-- `PROC-TITLE-002` -->

- Single sentence with no links, list items, or formatting. Ends with a period. <!-- `PROC-TITLE-009` -->
- Use H4 format. Stay under 120 characters / 20 words. <!-- `PROC-TITLE-010` -->
- Use imperative verbs to describe the document purpose or benefit: *Learn*, *Explore*, *Understand*, *Discover*, *Create*, *Follow*, *Try*, and other action verbs. <!-- `PROC-TITLE-011` -->
- Adds new value beyond the title. It should not repeat the title or be a rephrased version of it. <!-- `PROC-TITLE-012` -->

Examples:

- **Title**: *Quickstart for GitHub Actions* / **Subtitle**: *Try out the core features of GitHub Actions in minutes.*
- **Title**: *Create a pull request* / **Subtitle**: *Create a pull request to propose and collaborate on changes to a repository.*

## Access prerequisites admonition guidelines <!-- This is an informative header. Remove it before merging your content. --> <!-- `PROC-PREREQ-001` -->

This information-type admonition is exclusively to alert readers about what roles, permissions, or product versions are required to perform the procedure.

- Place it after the title and subtitle, before the introduction. <!-- `PROC-PREREQ-002` -->
- Use the **Info** admonition style. <!-- `PROC-PREREQ-003` -->
- Start with the phrase: *This feature is available to users with...* or *To perform this procedure, you need...* <!-- `PROC-PREREQ-004` -->
- Focus on required roles, permissions, or product versions only. Don't include any other prerequisite such as knowledge, skills, or tools. <!-- `PROC-PREREQ-005` -->

**Examples:**

- *This feature is available to admin roles in version 5.0 or later with write permissions on the repository.*
- *This procedure requires contributor roles in version 2.3 or higher and read/write access to the API endpoints.*

## Introduction guidelines <!-- This is an informative header. Remove it before merging your content. --> <!-- `PROC-INTRO-001` -->

Every procedure requires an introduction. The introduction provides context and helps readers understand the purpose and scope of the procedure. The introduction includes these sections, each one represented by a paragraph, list, or table.:

- **Overview**: A concise paragraph that explains what the procedure is about, its purpose, and its relevance. Aim for 50 to 100 words. Link to related topics or headers in the same document to support the reader's gathering of information. <!-- `PROC-INTRO-005` -->
- **Decisions** (optional): A paragraph, list, or table that outlines any decisions the reader needs to make before starting the procedure. This could include choosing between different methods, tools, or configurations. <!-- `PROC-INTRO-006` -->
- **Limits / Behaviors** (optional): A paragraph, list, or table that describes any limitations or expected behaviors related to the procedure. This helps set expectations and avoid confusion during execution. <!-- `PROC-INTRO-007` -->
- **Security / Impact** (optional): A paragraph, list, or table that highlights any security considerations or potential impacts of performing the procedure. This is crucial for ensuring that readers are aware of any risks or precautions they need to take. <!-- `PROC-INTRO-008` -->

**Examples:**


- Start with one or two lead sentences in a single paragraph that explains the concept, its purpose, and its relevance. This lead should be concise and engaging, ideally no more than 50 words.
- After the lead, explain the concept's main points using one paragraph per idea.
- If necessary, provide context or background information to help readers understand the concept.
- Link to related topics or headers in the same document to support the reader's gathering of information.

> ℹ️ **Note:**
>
> For examples, check out [concept introduction](../../docs-standards/10-structure-the-content/concept-help-me-to-understand.md#introduction) standards and [concept example](./concept-example.md).
-->


(Optional) { Use case example }

<!--
Provide a concrete, real-world scenario for the product feature. It answers the reader's silent question, "How can I use this feature in my work?" Use a bullet list format to present multiple use cases clearly.

> ⚙️ **Example:**
>
> *For example, you can configure custom environment variables so they are set every time you open a codespace, and you can ensure that temporary files are retained when the codespace stops.*
-->

(Optional) { Comparison }

<!--
Guidelines:

- Use a list for simple comparisons or a table for more complex ones.
- Focus on key decision factors, such as performance, complexity, cost, prerequisites, and limitations.
- Use direct language in short sentences so different options are easy to scan.
- Highlight trade‑offs clearly. For example, "Option A is faster but less secure" or "Option B adds encryption overhead".
- Provide real-world guidance. For example, "Choose A if you need X, choose B if you care about Y".

> ⚙️ **Example:**
>
> | Feature             | Relay                                         | RLN Relay                                         |
> |:--------------------|:----------------------------------------------|:--------------------------------------------------|
> | Spam protection     | None – all peers can flood messages           | Enforces per-peer rate limits, economic penalties |
> | Privacy impact      | Neutral – standard Pub/Sub propagation        | Neutral – preserves Relay’s anonymity properties  |
> | Resource guarantees | Relies on network-level quotas, no enforcement| Stronger resilience due to rate limiting          |

> ℹ️ **Note:**
>
> For more information, check out the [comparison section](../../docs-standards/10-structure-the-content/concept-help-me-to-understand.md#comparison) in the docs standards.
-->

## `What to expect` section

<!--
Guidelines:

- Use `What to expect` H2 heading for this section.
- Write a single unordered list with three bullet points that summarize the concept.
- Order the points from most important to least important.
- Aim for one sentence per bullet point, maximum two very short ones.

> ⚙️ **Example:**
>
>- *Codespaces are fully managed, cloud-based development environments you can spin up in seconds.*
>- *They run in containers that match your repository’s configuration, so every contributor gets the same setup.*  
>- *You connect from your browser, VS Code, or the JetBrains Gateway. No local installation required.*

> ℹ️ **Note:**
>
> For more information, check out the [`What to expect` section](../../docs-standards/10-structure-the-content/concept-help-me-to-understand.md#the-basics-section) in the docs standards.
-->

## { Section H2 title }

<!--
Headings guidelines:

- One heading = one idea. Don't mix two ideas under the same heading.
- Arrange H2 sections from general to specific, or from most important to least important.
- Start with a paragraph before you add lists or tables.
- When possible, limit the document depth to H3.
- Stop at H4. Deeper levels (H5, H6) are forbidden.
- If you add an H3, at least one sibling H3 must follow or the split is unnecessary.

> ℹ️ **Note:**
>
> For more information, check out the [Using headings to organize content](../../docs-standards/10-structure-the-content/concept-help-me-to-understand.md#using-headings-to-organize-content) in the docs standards.
-->

{ Key idea description }

(Optional) { Screenshot }

<!--
> ℹ️ **Note:**
>
> For more information, check out [Screenshots](../../docs-standards/30-work-with-media/02-screenshots.md)
-->

(Optional) { Code }

<!--
> ℹ️ **Note:**
>
> For more information, check out [Code](../../docs-standards/20-style-the-content/13-code.md)
-->

(Optional) ### { Section H3 title }

<!-- **First H3**
H3 is used to break down the main H2 section into smaller, more manageable parts. Use it to provide additional details or sub-sections that are relevant to the main section.
-->

{ Key idea description }

(Optional) { Screenshot }

(Optional){ Code }

(Optional) ### { Section H3 title }

<!-- **Second H3**
If you add an H3, at least one sibling H3 must follow or the split is unnecessary.
-->

(Optional) ### { Section H4 title }

{ Key idea description }

(Optional) { Screenshot }

(Optional) { Code }

(Optional) ### { Section H4 title }

<!--
Stop at H4. Deeper levels (H5, H6) are forbidden.
-->

{ Key idea description }

(Optional) { Screenshot }

(Optional){ Code }
