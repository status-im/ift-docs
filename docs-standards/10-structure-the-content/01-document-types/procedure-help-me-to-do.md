# Procedure - Help me to do

> ℹ️ **Note:**
>
> For the template associated to this topic, see [procedure template](../../../templates/procedure/procedure-template.md).

A procedure describes how to complete an action using a series of steps. Procedures help users use and discover your product. These are the main characteristics of procedures:

- Two parts make up the procedure. The first part includes reference (non-procedural) information, while the second part includes procedural information.
- A procedure explains a single task and, if necessary, additional subtasks. If the task is complex, consider splitting it into different procedures or group them into a guide.
- For tasks that may cause an error (for example, changing a password, choosing a user name, or sending crypto), consider adding a Common questions section at the end of the article, with answers to the most common issues. If the list of possible errors for a specific task is too long, use a FAQ (concept) article instead.
- If the user can complete the procedure in one go, use a numbered list to describe the steps. Use checkboxes if the user can't complete the procedure in one go or the steps don't follow a particular order.
- Non-procedural information in a procedure must follow these rules. If any rule fails, move the information to a separate [concept](./concept-help-me-to-understand.md) article. In the non-procedural part of the procedure document, provide a summary and link to the concept article.

    | Check   | Rule                                                                                                                   |
    |:--------|:-----------------------------------------------------------------------------------------------------------------------|
    | (R1) Scope     | The information only answers: **what** the quickstart or task does, **why** it matters, and **when** to use it. |
    | (R2) Length    | The information is no longer than 150 words or two short paragraphs.                                            |
    | (R3) Structure | The information doesn't contain H3 headings, tables, or diagrams.                                               |
    | (R4) Reuse     | The information doesn't appear in other documents.                                                              |
    | (R5) Blocking  | Omitting the information would cause immediate failure of the described tasks.                                  |

## Procedure structure

| #  | Element                                                       | Format                 | Required |
|:---|:--------------------------------------------------------------|:-----------------------|:---------|
| 1  | [Title](#title)                            | H1                     | Yes      |
| 2  | [Subtitle](#subtitle)                                         | H4                     | Yes      |
| 3  | [Admonition](#admonition-optional)                            | Information admonition | Yes      |
| 4  | ["Overview"](#overview) heading                               | H2                     | Yes      |
| 5  | ["Overview"](#overview) content                               | Paragraph              | Yes      |
| 6  | ["Before you start"](#before-you-start-section) heading       | H2                     | No       |
| 7  | ["Before you start"](#before-you-start-section) content       | Bullet list            | No       |
| 8  | [Task 1](#task-heading) heading                               | H2                     | Yes      |
| 9  | [Task 1](#task-steps) steps                                   | Numbered list          | Yes      |
| 10 | [Task 1 code sample or image](#code-sample-or-image-optional) | Code block or image    | No       |
| 11 | [Task 1 subtask](#task-subtask-heading-optional) heading      | H3                     | No       |
| 12 | [Task 1 subtask](#task-subtask-steps-optional) steps          | Numbered list          | No       |
| 13 | [Task 2](#task-2-heading) heading                             | H2                     | Yes      |
| 14 | [Task 2](#task-2-steps) steps                                 | Numbered list          | Yes      |
| 15 | ["Next steps"](#next-steps-optional) heading                  | H2                     | No       |
| 16 | ["Next steps"](#next-steps-optional) content                  | Bullet list            | No       |

### Title

Guidelines:

- Focus on the result, not on the task.
- Start the title with an action verb in the imperative form. Don't use the -ing form of the verb.
- A title should contain the name of the action and how or where the action occurs. Avoid using titles with one or two words.
- Be specific on the task's goal and, if possible, avoid empty verbs like make, manage, or put.

| Rule | Usage         | ⚙️ Example                        |
|:-----|:--------------|:---------------------------------|
|  1   | **Correct**   | *     |
|      | Incorrect     | *           |
|  2   | **Correct**   | *    |
|      | Incorrect     | * |
|  3   | **Correct**   | *Configure your notifications settings*     |
|      | Incorrect     | *Notifications*   |
|  4   | **Correct**   | *Set up admin access*             |
|      | Incorrect     | *Manage admin access*             |

### Subtitle

One short, imperative sentence that describes the task users perform and the outcome they can expect.

Guidelines:

- Single sentence with no links, list items, or formatting. Ends with a period.
- Use H4 format. Stay under 120 characters / 20 words.
- Use imperative verbs to describe the topic's purpose or benefit: *Explore*, *Get started*, *Try*, and so on.
- Adds new value beyond the title. It should not repeat the title or be a rephrased version of it.

> ⚙️ **Example:**
> 
> - *.*
> - *e.*

### Admonition (optional)

This information-type [admonition](../../20-style-the-content/12-admonitions.md) is exclusively to alert readers about who can use this feature and shouldn't be used for any other information. For example, a feature is only available to specific application role or using a specific tool or interface.

> ⚙️ **Example:**
>
> *This feature .*

### Introduction

Guidelines:

A brief discussion of the functionality and its relationship with other functionalities.
The introduction answers the "what is this"

### Example

An example explaining the functionality in context.
The example answers "why it matters."

### What to expect (optional)

Guidelines:

- Write a bullet list of expected results after completing the task.
- 

### Admonition

This admonition provides general notes, tips, or warnings about the task.

> ⚙️ **Example:**
>
> *This feature .*

### Task section

Use this section to describe what users need to do. 

Guidelines:

- If you introduce the task with a sentence (this is optional; see Procedure structure), don't repeat the title information. For example, if the task title is "Search for a contact using the Status display name," don't introduce the task with "To search for a contact using the Status display name [...]"
- If your quickstart involves a complex task, break it down into different logical subtasks with each subtask consisting of one or more related steps. 
- Describe the most straightforward steps of the tasks.
Follow the UI elements guidelines to describe the user interactions.

#### Task heading

Guidelines:

- Don’t include “Task,” “Subtask,” or numbering in the heading.
- Focus on the result, not on the task.
- Start the title with an action verb in the imperative form. Don't use the -ing form of the verb.
- Use H2 headings for each task.
- Use H3 headings for each subtask.
- Avoid H4 headings. Deeper levels (H5, H6) are forbidden. If you need more levels, reorganize the content into more tasks or subtasks.

> ⚙️ **Example:**
>
> - *Run a Waku node*
> - *Connect to the Codex network*
> - *Configure system admin access*

#### Task steps

Guidelines:
In the first step, tell the user where to start.
- Optionally, include an introduction paragraph to provide context or required knowledge for the task.
- Include a short description for each step, even when it contains a code sample.
- Provide examples of sample output, such as return data, a message, so that the users can validate whether they perform the step correctly or not.
- Use one step for each user action. It's OK to combine simple actions into a single step.
- Limit the procedure to a maximum of seven steps. If you need more steps to explain the task, create a subtask.
Use words consistently when describing user actions. For example, if you use remove in one step, don't use clear, empty or another synonym in a different step.
- Use a period at the end of each step (check the Punctuation section for more information).

> ⚙️ **Example:**
>
> ## Manage files using Codex Vault
>
> You can use Codex Vault, a GUI web application, to manage your files on the Codex testnet. Once you have your Codex node running using the installer, you can access the Codex Vault at https://app.codex.storage.
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

> ℹ️ **Note:**
>
> For additional tips on writing tasks, see [Procedure docs standards](procedure-help-me-to-do.md
).

#### Code sample or image (optional)

This section is part of the task steps and doesn't use a heading. 

Use less than two images or code samples per step. If you need more, the step needs splitting. Make sure your code samples and images are up-to-date, functional, and relevant to the task. For more tips, check out [code](../../20-style-the-content/13-code.md) and [images](../../30-work-with-media/02-images.md) guidelines.

> ℹ️ **Note:**
>
> When you use a code sample or image, it should be indented under the step description so that it's visually grouped with that step.

#### Task subtask heading (optional) 

Refer to the [task heading](#task-heading) section for guidelines.

#### Task subtask steps (optional) 

Refer to the [task steps](#task-steps) section for guidelines.

#### Task 2 heading

Refer to the [task heading](#task-heading) for guidelines.

#### Task 2 steps 

Refer to the [task steps](#task-steps) section for guidelines.

...

#### Task n heading (optional) 

Refer to the [task heading](#task-heading) for guidelines.

#### Task n steps (optional) 

Refer to the [task steps](#task-steps) section for guidelines.

### Common questions title

Common questions subtitle

Common questions paragraph

---
*Examples adapted from GitHub Docs (CC BY 4.0). See [Attributions](/ATTRIBUTIONS.md) for details.*
