# Procedure - Help me to do

> ℹ️ **Note:**
>
> For the template associated to this topic, see [procedure template](../../../templates/procedure/procedure-template.md).

A procedure topic describes how to complete an action using a series of steps. Procedures help users use and discover your product. These are the main characteristics of procedures:

- Two parts make up the procedure. The first part includes reference (non-procedural) information, while the second part includes procedural information.
- A procedure explains a single task and, if necessary, additional subtasks. If the task is complex, consider splitting it into different procedure documents.
- For tasks that may cause an error (for example, changing a password, choosing a user name, or sending crypto), consider adding a Common questions section at the end of the article, with answers to the most common issues. If the list of possible errors for a specific task is too long, use a FAQ (concept) article instead.
- If the user can complete the procedure in one go, use a numbered list to describe the steps. Use checkboxes if the user can't complete the procedure in one go or the steps don't follow a particular order.
- Non-procedural information in a procedure (for example, the introduction and context sections, and the descriptions in the task section) must follow these rules. If any rule fails, move the information to a separate [concept](./concept-help-me-to-understand.md) article. In the non-procedural part of the procedure document, provide a summary and link to the concept article.

    | Check   | Rule                                                                                                                   |
    |:--------|:-----------------------------------------------------------------------------------------------------------------------|
    | (R1) Scope     | The information only answers: **what** the quickstart or task does, **why** it matters, and **when** to use it. |
    | (R2) Length    | The information is no longer than 150 words or two short paragraphs.                                            |
    | (R3) Structure | The information doesn't contain H3 headings, tables, or diagrams.                                               |
    | (R4) Reuse     | The information doesn't appear in other documents.                                                              |
    | (R5) Blocking  | Omitting the information would cause immediate failure of the described tasks.                                  |

## Procedure structure

| #  | Element                                                          | Format                 | Required |
|:---|:-----------------------------------------------------------------|:-----------------------|:---------|
| 1  | [Title](#title)                                                  | H1                     | Yes      |
| 2  | [Subtitle](#subtitle)                                            | H4                     | Yes      |
| 3  | [Admonition](#admonition-optional)                               | Information admonition | No       |
| 4  | [Introduction](#introduction)                                    | Paragraph              | Yes      |
| 5  | [Example](#example-(optional))                                   | Paragraph              | No       |
| 6  | ["What to expect"](#what-to-expect-section-optional) heading     | H2                     | No       |
| 7  | ["What to expect"](#what-to-expect-section-optional) content     | Bullet list            | No       |
| 8  | [Task Admonition 1](#task-admonition-1-optional)                 | Admonition             | No       |
| 9  | ["Before you start"](#before-you-start-section-optional) heading | H2                     | No       |
| 10 | ["Before you start"](#before-you-start-section-optional) content | Bullet list            | No       |
| 11 | [Task](#task-heading) heading                                    | H2                     | Yes      |
| 12 | [Task](#task-introduction-optional) introduction                 | Paragraph              | No       |
| 13 | [Task](#task-steps) steps                                        | Numbered list          | Yes      |
| 14 | [Task code sample or image](#code-sample-or-image-optional)      | Code block or image    | No       |
| 15 | [Task admonition 2](#task-admonition-2-optional)                 | Admonition             | No       |
| 16 | [Subtask](#subtask-heading-optional) heading                     | H3                     | No       |
| 17 | [Subtask](#subtask-steps-optional) steps                         | Numbered list          | No       |
| 18 | ["Common questions"](#common-questions-section-optional) heading | H2                     | No       |
| 19 | ["Common questions"](#common-questions-section-optional) content | Paragraph              | No       |

### Title

Guidelines:

- Focus on the result, not on the task.
- Start the title with an action verb in the imperative form. Don't use the -ing form of the verb.
- A title should contain the name of the action and how or where the action occurs. Avoid using titles with one or two words.
- Be specific on the task's goal and, if possible, avoid empty verbs like make, manage, or put.

| Rule | Usage         | ⚙️ Example                            |
|:-----|:--------------|:--------------------------------------|
| 1    | **Correct**   | *Access the API with a token*         |
|      | Incorrect     | *Create an API token*                 |
| 2    | **Correct**   | *Run a Nwaku node*                    |
|      | Incorrect     | *Running a Nwaku node*                |
| 3    | **Correct**   | *Configure your notification settings*|
|      | Incorrect     | *Notifications*                       |
| 4    | **Correct**   | *Set up admin access*                 |
|      | Incorrect     | *Manage admin access*                 |

### Subtitle

One short, imperative sentence that describes the task users perform and the outcome they can expect.

Guidelines:

- Single sentence with no links, list items, or formatting. Ends with a period.
- Use H4 format. Stay under 120 characters / 20 words.
- Use imperative verbs to describe the topic's purpose or benefit.
- Adds new value beyond the title. It should not repeat the title or be a rephrased version of it.

> ⚙️ **Example:**
> 
> - *Customize GitHub Copilot Chat responses to match your personal preferences.*
> - *Work in a codespace using your browser, Visual Studio Code, or in a command shell.*

### Admonition (optional)

This information-type [admonition](../../20-style-the-content/12-admonitions.md) is exclusively to alert readers about who can use this feature and shouldn't be used for any other information. For example, a feature is only available to specific application role or using a specific tool or interface.

> ⚙️ **Example:**
>
> *You can only upload files using the desktop app.*

### Introduction

This section explains what the task is and why it matters, providing background information that may be helpful for understanding the task.

Guidelines:
- This section doesn't use a heading.
- Start with one or two lead sentences in a single paragraph that explains what the task is and why it matters. This lead should be concise and engaging, ideally no more than 50 words.
- If the background information requires more than three sentences, move the content to a separate section after the introduction and use a H2 heading.
- Link to related topics or headers in the same document to support the reader's gathering of information.

### Example (optional)

An example explaining the functionality in context. The example answers "why it matters."

Guidelines:
- This section is part of the introduction and doesn't use a heading.
- The example should be concise, using one paragraph.

### "What to expect" section (optional)

Guidelines:

- Describe expected results after completing the task.
- Write a bullet list.
- Link to related topics or headers in the same document to support the reader's gathering of information.

> ⚙️ **Example:**
>
> - Burning tokens is an irreversible blockchain transaction that requires to pay a [network fee (gas fee)](./understand-network-fees).
> - After burning a token, the existing holders keep their tokens, but the token's total supply decreases.
> - You can burn a certain amount of tokens or all the remaining tokens.

### Task admonition 1 (optional)

This admonition provides general notes, tips, or warnings about the task that users should know before starting the task.

> ⚙️ **Example:**
>
> *When you delete an item, the system permanently removes it. Make sure you only delete items that you no longer need*

### "Before you start" section (optional)

This section provides:

- The intended audience for this document. If you include this information in the [admonition](#admonition-optional) under the subtitle, you can still repeat it here to make sure readers are aware of the document's relevance.
- The basic knowledge that you expect users to have before performing the task.
- The software or hardware requirements for the task.

Guidelines:

- Use the "Before you start" H2 heading for this section.
- Only include prerequisites that are specific to the procedure document. Include general prerequisites in the "Before your start" section of the product installation guide.
- Start the section with "Before you begin, make sure you have..."
- After the starting sentence, write a single bullet list of noun phrases or a short paragraph if there's only one prerequisite.
- Don't include verbs such as "learn" or "prepare".
- Provide [links](../../20-style-the-content/10-links.md) to related content such as installation instructions or articles that provide required knowledge.

> ⚙️ **Example:**
>
> Before you begin, make sure you have the admin level access permission.


> ⚙️ **Example:**
>
> Before you begin, make sure you have:
>
> - A basic understanding of [Ethereum](https://ethereum.org/en/developers/docs/intro-to-ethereum/) ↗ concepts
> - Proficiency with the command line
> - A machine running Ubuntu Linux with the following minimum requirements:
>   - 4 GB memory
>   - 2 TB SSD
>   - Linux 64-bit

### Task section

Use this section to describe what users need to do. 

Guidelines:

- If your procedure topic involves a complex task, break it down into different logical subtasks with each subtask consisting of one or more related steps. 
- Describe the most straightforward steps of the tasks.
- Follow the [UI elements guidelines](../../20-style-the-content/11-ui-elements.md) to describe the user interactions with the UI.

#### Task heading

Guidelines:

- The H2 heading is the same with the document title.
- Don’t include “Task:” “Subtask:” or numbering in the heading.
- Use H3 headings for each subtask.
- Avoid H4 headings. Deeper levels (H5, H6) are forbidden. If you need more levels, reorganize the content into more tasks or subtasks.

#### Task introduction (optional)

Guidelines:

- Optionally, include a short introduction paragraph to provide context or required knowledge for the task.
- Don't repeat the title information. For example, if the task title is "Search for a contact using the Status display name," don't introduce the task with "To search for a contact using the Status display name [...]"

#### Task steps

Guidelines:

- Include a short description for each step, even when it contains a code sample.
- In the first step, tell the user where to start.
- Provide examples of sample output, such as return data, a message, so that the users can validate whether they perform the step correctly or not.
- Use one step for each user action. It's OK to combine simple actions into a single step.
- Limit the procedure to a maximum of seven steps. If you need more steps to explain the task, create a subtask.
- Use words consistently when describing user actions. For example, if you use *remove* in one step, don't use *clear*, *empty* or another synonym in a different step.
- Don't use sublists inside lists; instead, use a new list on a subtask.
- Use a period at the end of each step (check [Punctuation](../../20-style-the-content/05-punctuation-and-symbols.md) for more information).
- Write the result of the action first, then the condition for the result.

    | Usage      | Example                                                                 |
    |:-----------|:------------------------------------------------------------------------|
    | **Correct**   | Your Codex node announces itself to other network participants after you specify a public IP address. |
    | Incorrect     | After specifying a public IP address, your Codex node announces itself to other network participants. |
    | **Correct**   | To run a node, you must have the `nwaku` binary.                     |
    | Incorrect     | You must have the `nwaku` binary to run a node.                      |

- Don't use links in procedural steps, except when you need to reference a related subtask in the same article. You can use links in the optional paragraph before the steps.

> ⚙️ **Example:**
>
> ## Handle files using Codex Vault
>
> You can use Codex Vault, a GUI web application, to manage your files on the Codex testnet. Once you have your Codex node running using the installer, you can access the Codex Vault at https://app.codex.storage ↗.
>
> ### Upload files
>
> 1. Open Codex Vault in your browser.
> 1. In the Upload section, drag and drop your file or click **Upload** to choose it.
> 1. Back up the file CID for download.
>
> ### Download files
> 1. Open Codex Vault in your browser.
> 1. In the Download section, enter the CID of the file you want to download.
> 1. Click **Download**.

#### Code sample or image (optional)

This section is part of the task steps and doesn't use a heading. 

Use less than two images or code samples per step. If you need more, the step needs splitting. Make sure your code samples and images are up-to-date, functional, and relevant to the task. For more tips, check out [code](../../20-style-the-content/13-code.md) and [images](../../30-work-with-media/02-images.md) guidelines.

> ℹ️ **Note:**
>
> When you use a code sample or image, it should be indented under the step description so that it's visually grouped with that step.

#### Task admonition 2 (optional)

This admonition provides notes, tips, or warnings about the result of the task or subtask.

Place the admonition after the task or subtask, unless it contains critical information for a specific step. In that case, you can place it directly within the task steps.

#### Subtask heading (optional)

Refer to the [task heading](#task-heading) section for guidelines.

#### Subtask steps (optional) 

Refer to the [task steps](#task-steps) section for guidelines.

### "Common questions" section (optional)

This section addresses common questions or concerns related to the procedure.

Guidelines:
- Use the "Common questions" H2 heading for this section.
- Write each entry as a single question followed by a single answer.
- If the answer requires more than 150 words or two short paragraphs, move it to a separate [concept](./concept-help-me-to-understand.md) article and link to it.

> ⚙️ **Example:**
>
> **What data has GitHub Copilot been trained on?**
>
> GitHub Copilot is powered by generative AI models developed by GitHub, OpenAI, and Microsoft. It has been trained on natural language text and source code from publicly available sources, including code in public repositories on GitHub.
>
> **What languages, IDEs, and platforms does GitHub Copilot support?**
>
> GitHub Copilot is trained on all languages that appear in public repositories. For each language, the quality of suggestions you receive may depend on the volume and diversity of training data for that language.

---
*Examples adapted from GitHub Docs (CC BY 4.0). See [Attributions](/ATTRIBUTIONS.md) for details.*
