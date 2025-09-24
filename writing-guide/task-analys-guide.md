# Task analysis step-by-step guide

This template helps you perform a task analysis for documenting a software feature. It is designed for developers with access to the code, notes, and other materials as input sources.

> **Info:**
>
> For more information on task analysis, see the [Task Analysis](task-analysis.md) overview.

The result of task analysis is a content organization plan (blueprint) that specifies the documents you need to explain a certain feature, and how the information is structured within those documents.

## Step 1: Decompose developer's goal

**Objective:**
Define the developer's high-level objective and break it down all its constituent parts. This is a rapid, unfiltered "brain dump" of what tasks (procedures) the developer needs to perform and what contextual information (concepts and references) they need to know.

### High-level developer's goal
[Write a one-sentence description of the overall objective for using this feature. Example: "Deploy the coaching-service to production."]

### Brainstormed list of tasks and elements

1. Write a rough, unordered list of all the tasks the developer must perform.
2. Add to the list any contextual information they need to know (concepts) or look up (references).
3. After listing, prefix each item with:

   - `(P)` for procedures (tasks the developer performs).
   - `(C)` for concepts (background explanations, like "what are the env vars for the database?").
   - `(R)` for references (lookups, like "list of error codes").
   - `(T)` for troubleshooting (issues like "common deployment failures").

> **Note:**
>
>After you identify the tasks (procedures the developer needs to perform), identifying the contextual information (concepts and references) becomes easier.

**Tips for this step:**

- Draw from code: Look for functions, scripts, configs, or APIs that imply user actions or knowledge needs.
- Ask: What must a developer do step-by-step? What background do they need? What quick facts or error info would help?
- Don't think in documents yet, and don't worry about order, phrasing, or completeness yet

**Example:**

If the goal is "Deploy the `coaching-service`", your final brainstormed list might look like this:

- build the docker thing (P)
- run the deployment script (P)
- what are the env vars for the database (C)
- diagram of how it connects to the API (C)
- common deployment failures (T)
- list of error codes (R)
- install `kubectl` (P)
- push image to ACR (P)

## 2. Annotate procedural tasks

**Objective:** For each (P) item from [Step 1](#step-1-decompose-developers-goal), add context by answering guiding questions. This enriches the procedures and uncovers potential (C), (R), and (T) items overlooked in the previous step.

Go through each (P) item one by one (skip non-(P) items). For each, answer the questions below based on the code/notes. If a question reveals new items, add them to your list from [Step 1](#step-1-decompose-developers-goal).

| Question | Example |
|:---------|:--------|
| What are the prerequisites? | Before the developer even attempts this step, what must be true?</br>What tools must be installed?</br>What access rights or permissions must they have? |
| Are there any cautions? | Is this action irreversible?</br>Could it cause data loss or a security vulnerability if done incorrectly?</br>Is there a risk of service downtime? |
| Is there an important note or tip? | Is there a non-obvious best practice here?</br>Is there a common mistake that will cause the process to fail?</br>Can I provide a list of common error codes to help in troubleshooting? |
| Can I provide ready-to-use code snippets? | Can I make this step easier by providing a code snippet that the developer can copy and paste? |

The output of this step is an enriched version of the original task list with additional context.

**Tips for this step:**

- Use code to identify prerequisites (for example, required libraries) and cautions (for example, side effects in functions).
- Look for comments or logs in the code that suggest notes or tips.
- If annotations suggest broader explanations, flag them as potential (C) or (R) expansions.

> **Note:**
>
> At this step, you are not thinking in documents or heading levels yet, but on the information building blocks that will eventually form those documents.

**Example:**

1. Before (from [Step 1](#step-1-decompose-developers-goal))

	- build the docker thing (P)

2. After

	- build the docker thing (P)
		- Prerequisites: Docker must be installed and running. Developer must have access to the Docker CLI. Developer must have permissions to build images.
		- Cautions: Building a Docker image can take a long time and consume a lot of resources. Ensure that the Dockerfile is optimized to avoid unnecessary layers.
		- Note or tip: Use multi-stage builds to keep the final image size small. A common mistake is to forget to `.dockerignore` files that shouldn't be included in the image.
		- Code snippets: Provide a basic Dockerfile snippet to get started.

## 3. Name the tasks

This is the step where you transform the rough descriptions of your procedural tasks into clean and consistent titles. These titles become the headings (`##` or `###`) that users scan to find relevant information quickly.

To name each task, use the procedure naming conventions outlined in the [Documentation Standards](link-needed).

Example:
| Task name from step #1       | Standardized task name                       |
|:-----------------------------|:---------------------------------------------|
| build the docker thing (P)   | Build the Docker image                       |
| run the deployment script (P)| Deploy your application                      |
| install kubectl (P)          | Install kubectl CLI                          |
| push image to ACR (P)        | Push Docker image to Azure Container Registry |

## 4. Group related headings

This is the step where you take all the refined building blocks from the previous step and organize them into a final and coherent set of documents.

This process has two parts:



Your goal is to combine the tasks you identified in step 3 into logical groups that represent documents. A document can be the result of a single task or a collection of related tasks.