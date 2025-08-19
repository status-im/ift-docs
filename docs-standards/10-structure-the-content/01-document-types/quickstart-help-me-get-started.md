# Quickstart - Help me get started

> ℹ️ **Note:**
>
> For the template associated to this topic, see [quickstart template](../../../templates/quickstart/quickstart-template.md).

A quickstart helps your users to start using your product as quickly as possible. It reduces users' onboarding time, giving them the confidence to start working with the product right away.

A quickstart is more than just an installation guide. Along with helping users set up the product or feature, it should also guide them to try at least one core functionality.

You need at least one quickstart for each product. If the product is complex, you can create multiple quickstarts for different features or tasks.

## Write a quickstart

### Filenames

Check out the [file names and location rules](../../../CONTRIBUTING.md#file-names-and-location-rules) for more information.

### General rules

- The entire quickstart should be about 1 200 words long.
- Include at least one task for users to try the core functionality of the product or feature.
- A quickstart isn’t about explaining every detail, but about helping users quickly accomplish something with your product. For information such as alternative methods or considerations when completing a task, link to a separate [procedure](./procedure-help-me-to-do.md) article.
- Non-procedural information in a quickstart must follow these rules. If any rule fails, move the information to a separate [concept](./concept-help-me-to-understand.md) article. In the quickstart, provide a summary and link to the concept article.

    | Check   | Rule                                                                                                         |
    |:--------|:------------------------------------------------------------------------------------------------------------|
    | (R1) Scope     | Only answers: **what** the quickstart or task does, **why** it matters, and **when** to use it.      |
    | (R2) Length    | No longer than 150 words or two short paragraphs.                                                     |
    | (R3) Structure | Does not contain H3 headings, tables, or diagrams.                                                    |
    | (R4) Reuse     | Unique and does not appear in other documents.                                                        |
    | (R5) Blocking  | Omitting the information would cause immediate failure of the described tasks.                        |

## Quickstart structure

| #  | Element                                                                 | Format                     | Required |
|:---|:-----------------------------------------------------------------------|:---------------------------|:--------:|
| 1  | [Title](#title) — "Quickstart"                                         | H1                         | Yes      |
| 2  | [Subtitle](#subtitle)                                                  | H4                         | Yes      |
| 3  | [Admonition](#admonition-optional)                                     | Information admonition     | Yes      |
| 4  | ["Overview" heading](#overview)                                        | H2                         | Yes      |
| 5  | ["Overview" content](#overview)                                        | Paragraph                  | Yes      |
| 6  | ["Before you start" heading](#before-you-start-section)                | H2                         | No       |
| 7  | ["Before you start" content](#before-you-start-section)                | Bullet list                | No       |
| 8  | [Task 1 heading](#task-heading)                                        | H2                         | Yes      |
| 9  | [Task 1 steps](#task-steps)                                            | Numbered list              | Yes      |
| 10 | [Task 1 code sample or image](#code-sample-or-image-optional)          | Code block or image        | No       |
| 11 | [Task 1 subtask heading](#task-subtask-heading-optional)               | H3                         | No       |
| 12 | [Task 1 subtask steps](#task-subtask-steps-optional)                   | Numbered list              | No       |
| 13 | [Task 2 heading](#task-2-heading)                                      | H2                         | No       |
| 14 | [Task 2 steps](#task-2-steps)                                          | Numbered list              | No       |
| 15 | ["Next steps" heading](#next-steps-optional)                           | H2                         | No       |
| 16 | ["Next steps" content](#next-steps-optional)                           | Bullet list                | No       |

### Title

Quickstart titles use only the word “Quickstart” with no additional information.

### Subtitle

One short, imperative sentence that expresses the product's or feature's purpose and emphasizes the ease of use.

Guidelines:

- Single sentence with no links, list items, or formatting. Ends with a period.
- Use H4 format. Stay under 120 characters / 20 words.
- Use imperative verbs to describe the topic's purpose or benefit: *Explore*, *Get started*, *Try*, and so on.
- Adds new value beyond the title. It should not repeat the title or be a rephrased version of it.

> ⚙️ **Example:**
> 
> - *Get hands-on with Waku’s key capabilities.*
> - *Quickly add payments to your project with Stripe.*

### Admonition (optional)

This information-type [admonition](../../20-style-the-content/12-admonitions.md) is exclusively to alert readers about who can use this feature and shouldn't be used for any other information. For example, a feature is only available to specific application role or using a specific tool or interface.

> ⚙️ **Example:**
>
> *This feature is available to users with the **Admin** role in the application.*

### Overview

Guidelines:

- Use the "Overview" H2 heading for this section.
- Start with a brief discussion of this product or feature and its core purposes. Then describe what the user can accomplish in this quickstart.
- The overview should be one or a maximum of two paragraphs. Use an additional [concept](./concept-help-me-to-understand.md) article if you need to provide more information.
- Link to related topics to support the reader's gathering of information.

### "Before you start" section

This section provides:

- The intended audience for this document. If you include this information in the [admonition](#admonition-optional) under the subtitle, you can still repeat it here to make sure readers are aware of the document's relevance.
- The basic knowledge that you expect users to have before using this quickstart.
- The software or hardware requirements for the quickstart.

Guidelines:

- Use the "Before you start" H2 heading for this section.
- Write a single bullet list.
- Provide [links](../../20-style-the-content/10-links.md) to related content such as installation instructions or articles that provide required knowledge.
- Setting up or installing prerequisites is not part of a quickstart. If you must explain the procedure and it takes less than three steps, include it in the [task](#task-section) where you describe setting up your product.

> ⚙️ **Example:**
> 
> - Learn the basics of [Ethereum](https://ethereum.org/en/developers/docs/intro-to-ethereum/) ↗. 
> - Learn how to use the command line.
> - Prepare a machine running Ubuntu Linux with the following requirements:
>   - 4 GB memory
>   - 2 TB SSD
>   - Linux 64-bit

### Task section

Use this section to describe what users need to do. 

Guidelines:

- Choose two or three tasks that are essential, quick to complete, and provide immediate value to the user. 
    - The first task is usually about setting up or installing the product or feature. However, if setup is complex, create a separate installation guide and direct readers to it in the [Before you start](#before-you-start-section) section.
    - For the other task(s), focus on the core functionalities of the product or feature.
- If your quickstart involves a complex task, break it down into different logical subtasks with each subtask consisting of one or more related steps. 
- Describe the most straightforward steps of the tasks.

#### Task heading

Guidelines:

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

- Optionally, include an introduction paragraph to provide context or required knowledge for the task.
- Include a short description for each step, even when it contains a code sample.
- Provide examples of sample output, such as return data, a message, so that the users can validate whether they perform the step correctly or not.
- Include one action in a step.
- Limit the procedure to a maximum of seven steps. If you need more steps to explain the task, create a subtask.

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

### Next steps (optional)

Guidelines:

- Use the "Next steps" H2 heading for this section.
- Use a bullet list to provide at most three links to articles about other tasks that the users can try after completing the quickstart. 
- Consider a logical connection from the current quickstart that can act as a basis for your users' next learning.

---

*Examples adapted from GitHub Docs (CC BY 4.0). See [Attributions](/ATTRIBUTIONS.md) for details.*
