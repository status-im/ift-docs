# Concept template

<!-- 🚨 Important: Remove all Markdown comments before publishing the topic. -->

<!--
Element reference table

| #   | Element                | Format                 | Required   | Depends on         |
|:----|:-----------------------|:-----------------------|:-----------|:-------------------|
| 1   | Title                  | H1                     | Yes        | -                  |
| 2   | Subtitle               | H4                     | Yes        | Title              |
| 3   | Admonition             | Information admonition | No         | -                  |
| 4   | Introduction           | Paragraph              | Yes        | -                  |
| 5   | Diagram or image       | Mermaid/image          | No         | Introduction       |
| 6   | Use case example       | Paragraph, list        | No         | Introduction       |
| 7   | Comparison             | Paragraph, list, table | No         | Introduction       |
| 8   | `The basics` heading   | H2                     | Yes        | -                  |
| 9   | `The basics` list      | Unordered list         | Yes        | `The basics` H2    |
| 10  | H2 section title       | H2                     | Yes        | -                  |
| 11  | H2 section content     | Paragraph, others      | Yes        | H2 section title   |
| 12  | H3 section title       | H3                     | No         | H2 section         |
| 13  | H3 section content     | Paragraph, others      | No         | H3 section title   |
| 14  | H4 section title       | H4                     | No         | H3 section         |
| 15  | H4 section content     | Paragraph, others      | No         | H4 section title   |
| 16  | H5-H6 section          | -                      | Forbidden  | -                  |
| 17  | Further reading        | -                      | Forbidden  | -                  |

-->

<!-- Fill out the front matter with the topic information -->

---
title: ''
version: ''
---

# { Title }

<!--
Guidelines:

- Concept titles should be descriptive and concise (no more than 60 characters), indicating the main idea of the concept.
- Use cue words such as `Guide to`, `About`, `Understand`, `FAQ`, or `Introduction to`. Do not use active verbs like `Learn` or `How to`.
- For verbs, use the base form over the gerund form. For example, use `Understand` instead of `Understanding`.
- Start with `About` to signal background reading. Avoid gerunds that look like procedures.
- Use the `FAQ:` prefix for question compilations. Don't phrase FAQs as tasks.
- When none of the cue words fit, choose a concise noun phrase.

> ⚙️ **Examples:**
>
> - `Guide to RLN rate limiting`
> - `Understand Codex API limits`
> - `About Waku GossipSub relay`
> - `FAQ: Codex billing and usage`

> ℹ️ **Note:**
> 
> For more information and examples, check out the [concept title](../../docs-standards/10-structure-the-content/concept-help-me-to-understand.md#title) standards.
-->

#### { Subtitle }

<!--
Guidelines:

- Single sentence with no links, list items, or formatting. Ends with a period.
- Use H4 format. Stay under 120 characters / 20 words.
- Use imperative verbs to describe the topic's purpose or benefit: *Learn*, *Explore*, *Understand*, *Discover*, and so on.
- Adds new value beyond the title. It should not repeat the title or be a rephrased version of it.

> ⚙️ **Example:**
>
>- *Understand Waku’s peer-to-peer protocol for private, censorship-resistant messaging.*
>- *Learn how Codex provides real-time blockchain data through a single API.*

> ℹ️ **Note:**
>
> For more information, check out the [concept subtitle](../../docs-standards/10-structure-the-content/01-document-types/concept.md#subtitle) standards.
-->

(Optional){ Admonition }

<!--
This information-type admonition is exclusively to alert readers about who can use this feature and shouldn't be used for any other information. For example, a feature is only available to specific application role or using a specific tool or interface.

> ⚙️ **Example:**
>
> *This feature is available to users with the **Admin** role in the application.*

> ℹ️ **Note:**
>
> For more information, check out [Admonitions](../../docs-standards/20-style-the-content/12-admonitions.md)
-->

{ Introduction }

<!--
Guidelines:

- Start with one or two lead sentences in a single paragraph that explains the concept, its purpose, and its relevance. This lead should be concise and engaging, ideally no more than 50 words.
- After the lead, explain the concept's main points using one paragraph per idea.
- If necessary, provide context or background information to help readers understand the concept.
- Link to related topics or headers in the same document to support the reader's gathering of information.

> ℹ️ **Note:**
>
> For examples, check out [concept introduction](../../docs-standards/10-structure-the-content/concept-help-me-to-understand.md#introduction) standards and [concept example](./concept-example.md).
-->

(Optional){ Diagram or image }

<!--
- Use one diagram or image per concept. If you need two, the concept needs splitting or the second visual belongs to alater H2 section.
- To show an architecture, flow, or process, use a Mermaid diagram.
- For UI or CLI outputs, when the interface itself is the concept, use a screenshot or image.
- For simple relationships, use a Mermaid diagram. Even two boxes and an arrow is clearer than prose.

> ℹ️ **Note:**
>
> For more information, check out the [diagrams](../../30-work-with-media/03-diagrams.md#mermaid-diagrams) and [screenshots](../../30-work-with-media/02-screenshots.md) information.
-->

(Optional) { Use case example}

<!--
Provide a concrete, real-world scenario for the product feature. It answers the reader's silent question, "How can I use this feature in my work?" Use a bullet list format to present multiple use cases clearly.

> ⚙️ **Example:**
>
> *For example, you can configure custom environment variables so they are set every time you open a codespace, and you can ensure that temporary files are retained when the codespace stops.*
-->

(Optional){ Comparison }

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

## `The basics` section

<!--
Guidelines:

- Use `The basics` H2 heading for this section.
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
> For more information, check out the [`The basics` section](../../docs-standards/10-structure-the-content/concept-help-me-to-understand.md#the-basics-section) in the docs standards.
-->

## { Section H2 title }

<!--
Headings guidelines:

- One heading = one concept. Don't mix two ideas under the same heading.
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

(Optional){ Screenshot }

<!--
> ℹ️ **Note:**
>
> For more information, check out [Screenshots](../../docs-standards/30-work-with-media/02-screenshots.md)
-->

(Optional){ Code }

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

(Optional){ Screenshot }

(Optional){ Code }

(Optional) ### { Section H3 title }

<!-- **Second H3**
If you add an H3, at least one sibling H3 must follow or the split is unnecessary.
-->

(Optional) ### { Section H4 title }

{ Key idea description }

(Optional){ Screenshot }

(Optional){ Code }

(Optional) ### { Section H4 title }

<!--
Stop at H4. Deeper levels (H5, H6) are forbidden.
-->

{ Key idea description }

(Optional){ Screenshot }

(Optional){ Code }
