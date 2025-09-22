# Task analysis

## What is task analysis?

Good documentation helps people to get things done. Task analysis is the process of figuring out what those "things" are.

Task analysis takes place before you start writing documentation. By analyzing the tasks the developers need to perform, you create a clear structure for your documentation, focus on what's important, and avoid writing unnecessary content.

> **Tip:**
>
> Task analysis forces you to stop and think about the developer's goals before writing the correct approach. It shifts the focus from "what I know" to "what the developer needs to do".

The result of task analysis is a content organization plan (blueprint) that specifies the documents you need to explain a certain feature, and how the information is structured within those documents.

## Why is task analysis important?

The quality of your task analysis determines the quality of your documentation and the time it takes to write it. It is safe to say that the more time you spend on task analysis, the less time you will spend on writing. On average, professional technical writers don't spend more than 15-20% of their time writing. This is only possible because they use task analysis to know exactly what to write.

This guide provides a step-by-step approach to task analysis for developer documentation, with only the necessary background information to help you get started.

> **Info:** 
>
> Task analysis for user and developer documentation share the same principles and goals but differ in important details. This guide focuses on developer documentation.

## Task analysis in the documentation process

Task analysis is a foundational step in the documentation workflow. As outlined in this guide's intro, it fits into [Stage 1: Design the information](#link-needed), as illustrated in this diagram:

```mermaid
flowchart LR
    subgraph S1["Stage 1: Design the information"]
        RG([Reader's goal]):::artifact --> TA["Task analysis<br/>👉 You are here"]:::action

        TA:::here

        %% Information blocks cluster
        TA --> IB["Identify information blocks"]:::main
        IB --> Cpt["Concept"]:::main
        IB --> Proc["Procedure"]:::main
        IB --> Ref["Reference"]:::main
        IB --> Troub["Troubleshooting"]:::main

        IB --> ORG["Organize"]:::action --> SB([Structural blueprint]):::artifact

        %% Supporting tools (solid links, their own style)
        TAT["Task analysis template"]:::tool --> TA
        BOR["Block organization rules"]:::tool --> ORG

        %% Questions (dashed links)
        Q1["A: 'How do I break down the reader’s goal?'"]:::support -.-> TAT
        Q2["B: 'How do I organize the information?'"]:::support -.-> BOR
    end

    %% Styles
    classDef main fill:#fff,stroke:#333,stroke-width:2px
    classDef artifact fill:#FFF7D6,stroke:#333,stroke-width:2px
    classDef action fill:#fdd,stroke:#c33,stroke-width:2px
    classDef tool fill:#e0ffe0,stroke:#333,stroke-width:2px
    classDef support fill:#eef,stroke:#333,stroke-dasharray:3 3
    classDef here fill:#ffeb3b,stroke:#f57c00,stroke-width:3px
```

## Task analysis steps

Task analysis consists of four differentiated steps:

1. [Decompose developer's goal](#decompose-developers-goal)
2. [Annotate procedural tasks](#annotate-procedural-tasks)
3. [Name the tasks](#name-the-tasks)
4. [Group related tasks](#group-related-tasks)

This table and diagram summarizes the process:

| # | Step | Description | Outcome |
|:-:|:-----|:------------|:--------|
| 1 | [Decompose developer's goal](#decompose-developers-goal) | Define the developer's high-level objective and break it down into constituent parts. | A rough, unordered list of tasks (procedures), concepts, and references. |
| 2 | [Annotate procedural tasks](#annotate-procedural-tasks) | Add context to each procedural task by identifying prerequisites, cautions, notes, and code snippets. | An enriched version of the original task list with additional context. |
| 3 | [Name the tasks](#name-the-tasks) | Transform rough descriptions of procedural tasks into clear and consistent H1 and H2 titles using the [docs standards](link-needed). | A list of standardized task names that can be used as document headings. |
| 4 | [Group related headings](#group-related-headings) | Organize the headings into logical groups representing the structure of the document. | A structured outline of one or more documents reflecting the relationships between tasks. |

### 1. Decompose developer's goal

In this step, you define the developer's high-level objective and break it down all its constituent parts. This is a rapid, unfiltered "brain dump" of what tasks (procedures) the developer needs to perform to achieve this goal and what contextual information (concepts and references) they need to be aware of.

How to do this:

- The key here is quantity over quality. Aim to generate as many tasks and contextual elements as possible.
- Don't think in documents yet, and don't worry about correct phrasing or order.
- Don't try to organize the information.
- Write the tasks as a rough unordered list of short phrases.
- After the list is complete, label each item with (P) for procedure, (C) for concept, or (R) for reference.

> **Note:** After you identify the tasks (procedures the developer needs to perform), identifying the contextual information (concepts and references) becomes easier. For example, if you identify "run the deployment script" as a required task, adding a list of error codes the script might return becomes a requirement.

Example:

If the goal is "Deploy the `coaching-service`", your final brainstormed list might look like this:

- build the docker thing (P)
- run the deployment script (P)
- what are the env vars for the database (C)
- diagram of how it connects to the API (C)
- need to explain the caching strategy (C)
- list of error codes (R)
- install kubectl (P)
- push image to ACR (P)

> **Note:**
>
> At this stage, you are not thinking in documents or heading levels yet, but on the information building blocks that will eventually form those documents.

### 2. Annotate procedural tasks

This step is about adding context to the procedural tasks you identified in step 1. For each task, identify the developer's immediate questions and needs at the very moment they perform that step. To do this effectively, ask yourself these guiding questions for each procedural task on your list:

| Question | Example |
|:---------|:--------|
| What are the prerequisites? | Before the developer even attempts this step, what must be true?</br>What tools must be installed?</br>What access rights or permissions must they have? |
| Are there any cautions? | Is this action irreversible?</br>Could it cause data loss or a security vulnerability if done incorrectly?</br>Is there a risk of service downtime? |
| Is there an important note or tip? | Is there a non-obvious best practice here?</br>Is there a common mistake that will cause the process to fail?</br>Can I provide a list of common error codes to help in troubleshooting? |
| Can I provide ready-to-use code snippets? | Can I make this step easier by providing a code snippet that the developer can copy and paste? |

The output of this step is not a new document, but an enriched version of the original task list with additional context.

Example:

1. Before

	- build the docker thing (P)

2. After

	- build the docker thing (P)
		- Prerequisites: Docker must be installed and running. Developer must have access to the Docker CLI. Developer must have permissions to build images.
		- Cautions: Building a Docker image can take a long time and consume a lot of resources. Ensure that the Dockerfile is optimized to avoid unnecessary layers.
		- Note or tip: Use multi-stage builds to keep the final image size small. A common mistake is to forget to `.dockerignore` files that shouldn't be included in the image.
		- Code snippets: Provide a basic Dockerfile snippet to get started.

### 3. Name the tasks

This is the step where you transform the rough descriptions of your procedural tasks into clean and consistent titles. These titles become the headings (`##` or `###`) that users scan to find relevant information quickly.

To name each task, use the procedure naming conventions outlined in the [Documentation Standards](link-needed).

Example:
| Task name from step #1       | Standardized task name                       |
|:-----------------------------|:---------------------------------------------|
| build the docker thing (P)   | Build the Docker image                       |
| run the deployment script (P)| Deploy your application                      |
| install kubectl (P)          | Install kubectl CLI                          |
| push image to ACR (P)        | Push Docker image to Azure Container Registry |

### 4. Group related headings

This is the step where you take all the refined building blocks from the previous step and organize them into a final and coherent set of documents.

This process has two parts:



Your goal is to combine the tasks you identified in step 3 into logical groups that represent documents. A document can be the result of a single task or a collection of related tasks.