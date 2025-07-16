# Concept template

<!-- Important: Remove all Markdown comments before publishing the topic. -->

<!--
Element reference table

| #   | Element                                   | Format                        | Required   | Depends on            |
|:----|:------------------------------------------|:------------------------------|:-----------|:----------------------|
| 1   | [Title](#title)                           | H1                            | Yes        | -                     |
| 2   | [Subtitle](#subtitle)                     | H4                            | Yes        | Title                 |
| 3   | [Admonition](#admonition)                 | Information admonition        | No         | -                     |
| 4   | [Introduction](#introduction)             | Paragraph                     | Yes        | -                     |
| 5   | [Diagram or image](#diagram-or-image)     | Mermaid diagram or image      | No         | Introduction          |
| 6   | [Use case example](#use-case-example)     | Paragraph, list               | No         | Introduction          |
| 7   | [Comparison](#comparison)                 | Paragraph, list, table        | No         | Introduction          |
| 8   | [`The basics`](#the-basics) heading       | H2                            | Yes        | -                     |
| 9   | [`The basics`](#the-basics) list          | Unordered list                | Yes        | `The basics` H2       |
| 10  | [H2 section](#h2-h4-sections) title       | H2                            | Yes        | -                     |
| 11  | [H2 section](#h2-h4-sections) content     | Paragraph, others             | Yes        | H2 section title      |
| 12  | [H3 section](#h2-h4-sections) title       | H3                            | No         | H2 section            |
| 13  | [H3 section](#h2-h4-sections) content     | Paragraph, others             | No         | H3 section title      |
| 14  | [H4 section](#h2-h4-sections) title       | H4                            | No         | H3 section            |
| 15  | [H4 section](#h2-h4-sections) content     | Paragraph, others             | No         | H4 section title      |
| 16  | [H5-H6 section](#h2-h4-sections)          | -                             | Forbidden  | -                     |
| 17  | [Further reading](#further-reading)       | -                             | Forbidden  | -                     |

-->

---
title: ''
version: ''
---

# { Title }

<!--
Concept titles guidelines:

- Concepts titles should be concise and descriptive, ideally no more than 60 characters, and avoid any confusion with procedures.
- Do not start with an action verb, do not use "how to" or "what is" in the title, and do not use the -ing form of verbs.
- Words like "guide", "understand", or "about" are commonly used in titles.

Some good examples for titles include:

- "Data privacy best practices"
- "Introduction to machine learning"
- "Understand cloud computing"
- "FAQ: Import data from Discord"

👉 For more information, check out [Concepts](../style-guide/concepts.md#title)
-->

#### { Subtitle }

<!--
One sentence that (a) defines the topic in plain language and (b) states the primary benefit or outcome. It answers the reader’s silent question, "Why should I care?".

Example: "You can configure custom environment variables so they are set every time you open a codespace, and you can ensure that temporary files are retained when the codespace stops."

👉 For more information, check out [Concepts](../style-guide/concepts.md#subtitle)
-->

(Optional){ Admonition }

<!--
This information-type admonition is exclusively to alert readers about who can use this feature. For example, a feature is only available to specific application role or using a specific tool or interface.

Example: "This feature is available to users with the **Admin** role in the application."

👉 For more information, check out [Admonitions](../style-guide/concepts.md#admonition)
-->

{ Introduction }

<!--
Start with a lead sentence or paragraph that explains the concept, its purpose, and its relevance. This should be concise and engaging, ideally no more than 50 words.

For example, "A webhook is a real-time HTTP callback that GitHub fires when repository events occur. You register an endpoint, select events, and GitHub delivers JSON payloads to your service within seconds."
-->

(Optional){ Diagram }

<!--
Use this section to include a diagram that visually represents the concept. This can help readers quickly grasp the main idea or flow of the concept.

If possible, usa a [Mermaid chart](https://mermaid-js.github.io/mermaid/#/) to create diagrams. If you need to use an image, place the image in the parent folder with the same name as the topic and include the alt-text image description.

👉 For more information, check out [Diagrams](../style-guide/working-with-media.md#diagrams)
-->

{ Use case }

<!--
Provide a concrete, real-world scenario for the product feature. It answers the reader's silent question, "How can I use this feature in my work?" Use a bullet list format to present multiple use cases clearly.

Example: "For example, you can configure custom environment variables so they are set every time you open a codespace, and you can ensure that temporary files are retained when the codespace stops."
-->

(Optional){ Comparison }

<!--
Use this section to compare other options and alternatives. This is specially useful when the concept has multiple implementations or approaches. Use a list or table format to clearly present the differences.
-->

## { Section H2 title }

{ Description }

(Optional){ Screenshot }

<!--
Guidelines:

- Use the .webp format for screenshots.
- Use a descriptive name for the screenshot. For example, "install-via-cli.webp".
- Include the alt-text image description.
- Place the screenshot in the parent folder with the same name as the topic. For example, if the topic name is "install-the-connector-via-the-cli.md", the screenshot should exist in a folder with the same name, "install-the-connector-via-the-cli".

👉 For more information, check out [Screenshots](../style-guide/working-with-media.md#screenshots)
-->

(Optional){ Code }

<!--
👉 For more information, check out [Code](../style-guide/working-with-media.md#code)
-->

(Optional) ### { Section H3 title }

<!--
H3 is used to break down the main H2 section into smaller, more manageable parts. Use it to provide additional details or sub-sections that are relevant to the main section.
-->

{ Description }

(Optional){ Screenshot }

(Optional){ Code }

(Optional) ### { Section H4 title }

<!--
H4 is the last header level you can use. Use it to provide additional details or sub-sections that are relevant to the main section.
-->

{ Description }

(Optional){ Screenshot }

(Optional){ Code }
