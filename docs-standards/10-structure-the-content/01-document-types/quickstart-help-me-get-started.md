# Quickstart - Help me get started

> ℹ️ **Note:**
>
> For the template associated to this topic, see [quickstart template](../../../templates/quickstart/quickstart-template.md).

A quickstart focuses on the primary aspects of the product or feature, helping your users to start using your product as quickly as possible. It reduces users' onboarding time and gives them the feeling that the product is easy to use.

You need at least one quickstart for each product. If the product is complex, you can create multiple quickstarts for different features or tasks.

## Write a quickstart

### Filenames

Check out the [file names and location rules](../../../CONTRIBUTING.md#file-names-and-location-rules) for more information.

### General rules

- The entire quickstart should be about 1 000 words long.
- Lengthy quickstarts can overwhelm users. Consider condensing or removing steps or tasks.
- Keep descriptions brief and focused. For more in-depth information, link to a separate article.

## Quickstart structure

| #   | Element                                              | Format                        | Required |
|:----|:-----------------------------------------------------|:------------------------------|:---------|
| 1   | [Title](#title)                                      | H1                            | Yes      |
| 2   | [Subtitle](#subtitle)                                | H4                            | Yes      |
| 3   | [Overview](#overview) heading                        | H2                            | Yes      |
| 4   | [Overview](#overview) content                        | Paragraph                     | Yes      |
| 5   | [Before you start](#before-you-start) heading        | H2                            | No       |
| 6   | [Before you start](#before-you-start) content        | Bullet list                   | No       |
| 7   | [Setup](#setup-optional) heading                     | H2                            | No       |
| 8   | [Setup](#setup-optional) content                     | Numbered list                 | No       |
| 9   | [Task 1 heading](#task-heading)                      | H2                            | Yes      |
| 10  | [Task 1 steps](#task-steps)                          | Numbered list                 | Yes      |
| 11  | [Task 1 code sample or image](#code-sample-or-image-optional) | Code block or image  | No       |
| 12  | [Task 1 subtasks](#task-heading)                     | H3 headings and numbered list | No       |
| 13  | [Next steps](#next-steps-optional) heading           | H2                            | No       |
| 14  | [Next steps](#next-steps-optional) content           | Bullet list                   | No       |

### Title

Quickstart titles follow the format of "Quickstart for {feature/product name}".

### Subtitle

One short, imperative sentence that expresses the quickstart's purpose and emphasizes the ease of use.

Guidelines:

- Single sentence with no links, list items, or formatting. Ends with a period.
- Use H4 format. Stay under 120 characters / 20 words.
- Use imperative verbs to describe the topic's purpose or benefit: *Explore*, *Get started*, *Try*, and so on.
- Adds new value beyond the title. It should not repeat the title or be a rephrased version of it.

> ⚙️ **Example:**
> 
> - *Try out the core features of Waku in minutes.*
> - *Quickly add payments to your project with Stripe.*

### Overview

Guidelines:

- Start with a brief discussion of this product or feature and its core purposes. Then describe what the user can accomplish in this quickstart.
- The overview should be concise. Use an additional [concept](./concept-help-me-to-understand.md) article if you need to provide more information.
- Link to related topics to support the reader's gathering of information.

### "Before you start" section

This section provides the following information:

- The intended audience for this document.
- The basic knowledge that you expect the user to have before using this quickstart.
- The software or hardware requirements for the quickstart.

Guidelines:

- Use "Before you start" H2 heading for this section.
- Write a single bullet list.
- Provide [links](../../20-style-the-content/10-links.md) to related content such as installation instructions or articles that provide required knowledge.
- Setting up or installing prerequisites is not part of a quickstart. If you must explain the procedure, use the [Setup](#setup-optional) section.

> ⚙️ **Example:**
> 
> - Learn the basics of [Ethereum](https://ethereum.org/en/developers/docs/intro-to-ethereum/) ↗. 
> - Learn how to use the command line.
> - Prepare a machine running Ubuntu Linux with the following requirements:
>   - 4 GB memory
>   - 2 TB SSD
>   - Linux 64-bit

### Setup (optional)

Include this section if the product or prerequisites are installed or configured at the same time by the person running the quickstart.

Describe the simplest steps using a numbered list. If more detail is needed, create a separate [procedure](procedure-help-me-to-do.md) article and link to it.

> ℹ️ **Note:** 
>
> For additional tips on writing a procedure, see [Procedure docs standards](procedure-help-me-to-do.md
).

#### Setup heading:

Guidelines:

- Use imperative verbs to describe the section's purpose: *Install*, *Configure*, *Set up* and so on.
- Use H2 headings for each setup requirement.

> ⚙️ **Example:**
> 
> - *Build an nwaku node*
> - *Sign up for GitHub Copilot*

### Task section

Use this section to describe what users need to do. 

Guidelines:

- Choose two or three tasks that are essential, quick to complete, and provide immediate value to the user. 
- If your quickstart involves a complex task, break it down into different logical subtasks with each subtask consisting of one or more related steps. 

#### Task heading

Guidelines:

- Focus on the result, not on the task.
- Start the title with an action verb in the imperative form. Don't use the -ing form of the verb.
- Use H2 headings for each task.
- Use H3 headings for each subtask.

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

Use one image or code sample per step. If you need two, the step needs splitting. Make sure your code samples and images are up-to-date, functional, and relevant to the task. For more tips, check out [code](../../20-style-the-content/13-code.md) and [images](../../30-work-with-media/02-images.md) guidelines.

> ℹ️ **Note:**
>
> When you use a code sample or image, it should be indented under the step description so that it's visually grouped with that step.

### Next steps (optional)

In this section, use a bullet list to provide links to articles about other tasks that the users can try after completing the quickstart. Consider a logical connection from the current quickstart that can act as a basis for your users' next learning.

---

*Examples adapted from GitHub Docs (CC BY 4.0). See [Attributions](/ATTRIBUTIONS.md) for details.*
