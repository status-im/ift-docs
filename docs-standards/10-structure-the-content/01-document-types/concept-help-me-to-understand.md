# Concept - Help me to understand

> **Note:**
> 
> You can find the concept template [here](../../../templates/concept/template-concept.md).

Concept topics build the mental model behind a feature or product. They explain the "why" so users can understand the purpose and benefits of the feature.

For example, a user starting with Waku might need to understand the concept of "Waku nodes" before they can effectively use the Waku protocol.

> **Note:**
>
>  A list of frequently asked questions (FAQs) falls under the concept category.

Concepts provide non-procedural information that complements other topic types, such as procedure or reference topics, but never replaces or duplicates them.

## When to use a concept topic

Create a concept topic whenever readers must understand background knowledge before:

- Using a feature or product
- Implementing an integration
- Choosing between alternative options
- Troubleshooting non-obvious behavior

## Writing a concept topic

### Filenames

Check out the [file names and location rules](../../../CONTRIBUTING.md#file-names-and-location-rules) for more information.

### General rules

- Target for documents between 900 and 1 500 words. Split longer ideas into separate concept topics.
- Replace dense prose with lists and tables to improve readability.
- Richly link to related topics, especially procedure and reference topics.
- Include diagrams or images to illustrate complex ideas or workflows.

> **Tip:**
>
> In Visual Studio Code, use the [Live Word Count](https://marketplace.visualstudio.com/items?itemName=Taptic.live-word-count) extension ↗  that is part of the recommended repository extensions.

## Concept topic structure

| #   | Element                | Format                              | Required   | Depends on         |
|-----|------------------------|-------------------------------------|------------|--------------------|
| 1   | [Title](#title)                  | H1                                  | Yes        | -                  |
| 2   | [Subtitle](#subtitle)               | H4                                  | Yes        | Title              |
| 3   | [Admonition](#admonition)             | Information admonition              | No         | -                  |
| 4   | [Introduction](#introduction)           | Paragraph                           | Yes        | -                  |
| 5   | [Diagram or image](#diagram-or-image)       | Mermaid chart or image             | No         | Introduction       |
| 6   | [Use case example](#use-case-example)       | Paragraph                           | No         | Introduction       |
| 7   | [Comparison](#comparison)             | Paragraph, list, table              | No         | Introduction       |
| 8   | [The basics](#the-basics) heading   | H2                                  | Yes        | -                  |
| 9   | [The basics](#the-basics) list      | Unordered list                      | Yes        | [The basics](#the-basics) H2    |
| 10  | [H2 section](#h2-h4-sections) title       | H2                                  | Yes        | -                  |
| 11  | [H2 section](#h2-h4-sections) content     | Paragraph, list, table, code block  | Yes        | H2 section title   |
| 12  | [H3 section](#h2-h4-sections) title       | H3                                  | No         | H2 section         |
| 13  | [H3 section](#h2-h4-sections) content     | Paragraph, list, table, code block  | No         | H3 section title   |
| 14  | [H4 section](#h2-h4-sections) title       | H4                                  | No         | H3 section         |
| 15  | [H4 section](#h2-h4-sections) content     | Paragraph, list, table, code block  | No         | H4 section title   |
| 16  | [H5-H6 section](#h2-h4-sections)      | -                                   | Forbidden  | -                  |
| 17  | [Further reading](#further-reading)  | -                                   | Forbidden  | -                  |

### Title

Concepts titles should explain, not instruct. They should be descriptive and concise (no more than 60 characters), indicating the main idea of the concept.

Follow these when writing a concept title:

1. Use cue words such as "Guide to", "About", "Understand", "FAQ" or "Introduction to". Do not use active verbs like "Learn" or "How to".
2. For verbs, use the base form over the gerund form. For example, use "Understand" instead of "Understanding".
3. Start with "About" to signal background reading. Avoid gerunds that look like procedures.
4. Use the "FAQ:" prefix for question compilations. Don't phrase FAQs as tasks.
5. When none of the cue words fit, choose a concise noun phrase.

| Rule | Usage     | Example                          |
|------|-----------|----------------------------------|
| 1    | **Correct**   | Guide to RLN rate limiting         |
|      | Incorrect     | RLN rate limiter                   |
| 2    | **Correct**   | Understand Codex API limits        |
|      | Incorrect     | Understanding Codex API limits     |
| 3    | **Correct**   | About Waku GossipSub relay         |
|      | Incorrect     | Running Waku GossipSub relay       |
| 4    | **Correct**   | FAQ: Codex billing                 |
|      | Incorrect     | Billing with Codex                 |
| 5    | **Correct**   | Waku message encryption layers     |
|      | Incorrect     | Encrypt messages in Waku           |

### Subtitle

One short, imperative sentence that (a) defines the topic in plain language and (b) states the primary benefit or outcome. It answers the reader’s silent question, "Why should I care?".

Guidelines:

- Single sentence with no links, list items, or formatting. Ends with a period.
- Stay under 120 characters / 20 words.
- Use imperative verbs to describe the topic's purpose or benefit: Learn, Explore, Understand, Discover, and so on.
- Adds new value beyond the title. It should not repeat the title or be a rephrased version of it.

Examples:

- *Understand Waku’s peer-to-peer protocol for private, censorship-resistant messaging.*
- *Learn how Codex provides real-time blockchain data through a single API.*

### Admonition

This information-type admonition is exclusively to alert readers about who can use this feature. For example, a feature is only available to specific application role or using a specific tool or interface.

Example: *This feature is available to users with the **Admin** role in the application.*

### Introduction

Start with one or two lead sentences in a single paragraph that explains the concept, its purpose, and its relevance. This should be concise and engaging, ideally no more than 50 words.

Using one paragraph per idea, explain the concept's main points. If necessary, provide context or background information to help readers understand the concept.

### Diagram or image

Include a diagram or image that illustrates the concept. This could be a flowchart, screenshot, or any visual aid that helps clarify the topic.

### Use case example

Provide a concrete, real-world scenario for the product feature. It answers the reader's silent question, "How can I use this feature in my work?" Use a bullet list format to present multiple use cases clearly.

Example: *For example, you can configure custom environment variables so they are set every time you open a codespace, and you can ensure that temporary files are retained when the codespace stops.*

### Comparison

Use this section to compare other options and alternatives. This is specially useful when the concept has different implementations. Use a list or table format to clearly present the differences.

### 'The basics' section

It should provide a high-level overview of the concept, covering the most important takeaways without going into too much detail.

Use the "The basics" H2 heading for this section and an unordered list to present the key points. Each point should be a concise statement that captures the essence of the concept.

Example:

- *Codespaces are fully managed, cloud-based development environments you can spin up in seconds.*
- *They run in containers that match your repository’s configuration, so every contributor gets the same setup.*  
- *You connect from your browser, VS Code, or the JetBrains Gateway. No local installation required.*

### H2-H4 sections

Headings structure the content into logical sections. Use H2 for key concepts, H3 for subconcepts, and H4 for further subdivisions if necessary.

Each heading level answers one question:

| Heading | Answers the question...                                         | Content to include                                                                                           |
| ------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| H2  | What is the main concept I need to understand first?           | The core concept (e.g., Architecture, Security Model, Lifecycle).                                            |
| H3  | What are the key components or behaviors of this concept?      | (Optional) Sub-concepts that relate only to the parent H2.                                                   |
| H4  | Are there specific details or edge cases within this subtopic? | (Optional) Use when an H3 contains two distinct or unrelated pieces of information that need further splitting.|

Quick decision tree for section headings:

```markdown
Need to add a section?
├─ Is it a brand-new core concept?             → H2
├─ Is it part of an existing H2 concept?       → H3
└─ Is it a detail that splits an H3 concept?   → H4 (and only if unavoidable)
```

General rules for headings:

- One heading = one concept. Don't mix two ideas under the same heading.
- Start with a paragraph before you add lists or tables.
- When possible, limit the document depth to H3.
- Stop at H4. Deeper levels (H5, H6) are forbidden.
- Arrange H2 sections from general to specific, or from most important to least important.
- If you add an H3, at least one sibling H3 must follow or the split is unnecessary.

Example:

```markdown
## Architecture
{ Paragraph }

### Components
- Compute host  
- Container image  
- Virtual file system  

### Networking
{ Paragraph }

#### Port forwarding rules   <-- only because Networking had two separate cases
{ Paragraph }
```

### Further reading

This section is forbidden in concept topics. Instead, link to related procedure or reference topics within the content.

---

*Examples adapted from GitHub Docs (CC BY 4.0). See [Attributions](/ATTRIBUTIONS.md) for details.*
