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

**Objective:**
Refine the rough (P) items into clear, scannable titles suitable for documentation headings ("#" or "##" Markdown levels).

This is the step where you transform the rough descriptions of your procedural tasks into clean and consistent titles. These titles become the Markdown headings (H1 or H2) that users scan to find relevant information quickly.

To name each task, use the procedure naming conventions outlined in the [Documentation Standards](link-needed).

**Tips for this step:**
- Scan code for precise terms (e.g., function names become part of headings like "Call the `deployService()` function").
- Aim for 5-10 words max per title. Ensure it's searchable (e.g., include keywords from notes).

**Example:**

| Item name from steps 1 and 2       | Standardized task name                       |
|:-----------------------------|:---------------------------------------------|
| build the docker thing (P)   | Build the Docker image                       |
| run the deployment script (P)| Deploy your application                      |
| install kubectl (P)          | Install kubectl CLI                          |
| push image to ACR (P)        | Push Docker image to Azure Container Registry |

## 4. Group related headings

The technical documents that describe your software feature have all a main title (Markdown H1 heading) and a set of related subheadings (Markdown H2 headings). This is the step where you combine the tasks you identified in step 3 into logical groups that represent documents blueprints.

> **Note:**
>
> The headings combination rules described here minimize subjective judgment on content organization, and replace it with simple rules.

Organizing headers is like doing laundry. You start with a messy pile of clothes (your headers) and the first job is to sort them: lights with lights, darks with darks, warm‑wash items with warm, and so on. In the same way, you separate Procedures, Concepts, References, and Troubleshooting, and then apply extra rules: some clothes can be washed together (related procedures in one doc), but special items like a bulky blanket (a long reference list) or a delicate fabric (a risky task like "Delete user") need their own separate wash (their own doc).

### 4.1 General groping and splitting rules

1. Each document has one main topic

If your top three headers sound like three different topics (for example, "Build the Docker image", "Install kubectl CLI", and "Push Docker image to Azure Container Registry"), then you need three different documents.

2. Use a maximum of seven H2 headings per document

- Beyond seven H2 headings, you have too much information for one document. Split it into two or more documents.
- Below two H2 headings, you have too little information for a document. Combine it with another document.

3. Risky or destructive tasks get their own document

For example, "Delete user account" or "Reset configuration database" go in their own document, and not in combination with other tasks.

### 4.2 Rules for "helpers" 

"Helpers" are supporting content that can appear in any main information type. They are not the main information type but provide context or support to the main information type. Some examples are:

- A short "before you start" intro in a procedure.
- A quick list of command options or configuration settings in a larger procedure.
- A "known issues" or "common errors" section at the end of a procedure.

4. Always start a procedure document with at least one concept block that works as an introduction.

- For a single introduction block, the document name in H1 is the heading. Single introduction blocks don't need their own H2 heading.
- For two introduction blocks, use an H2 heading for the second block.

```mermaid

```

5. Small helpers stay in line with the document they support. Large helpers get their own document.
6. If a helper is needed by multiple documents, it gets its own document, independent of its size.

### 4.3 Expansion rule for "helpers"

4. 

5. Keep troubleshooting helpers last.

- In a procedure doc, small troubleshooting sections (for example, "Common errors") go at the end of the document.
- Big troubleshooting sections (long list of errors or more than one troubleshooting heading) get their own document.

Workflow review

Answer these three questions to ensure your grouping is effective:

- Do you have at least one Quick Start or Concept document that introduces the feature?
- Do you have at least one Concept document for background information?
- Do you have a Reference or Troubleshooting document, separted or inline into a concept, procedure, or quick start document?

If your answer is "not sure" or "no" to all of these questions, your grouping is incomplete.

