# Procedure

A procedure is a goal-oriented document that describes how to complete an action using a series of steps. Procedures help readers use and discover your project features and are the core of our user documentation. These are the main characteristics of procedures:

- Two parts make up a procedure. The first part includes reference (non-procedural) information, while the second part includes procedural information.
- Non-procedural descriptions must be short and to the point. If the functionality requires further discussion, use an additional [concept article](#concept-help-me-to-understand).
- A procedure explains one or more related tasks and, if necessary, additional subtasks. If a task is complex, consider splitting it into different procedures documents.
- For tasks that may cause an error (for example, changing a password, choosing a username, or sending crypto), consider adding a *Common questions* section at the end of the article, with answers to the most common issues. If the list of possible errors for a specific task is too long, use a linked Troubleshooting or [FAQ](#concept-help-me-to-understand) (concept) article instead.

## Steps structure: flat vs. sectioned

In a procedure document, the steps can be organized in two different ways: flat or sectioned. You must choose one of these structures and apply it consistently throughout the document.

In a flat structure, all steps are presented in a single, continuous list. This layout is straightforward and easy to follow, making it ideal for simple procedures with a limited number of steps. Here is an example of a flat structure:

```markdown
# {Procedure title}

[...]

## Task A

1. {Step 1}
2. {Step 2}
	- {Clarifier / Option 1}
	- {Clarifier / Option 2}
3. {Step 3}
[...]

## Task B

1. {Step 1}
2. {Step 2}
3. {Step 3}
[...]
```

In a sectioned structure, steps are grouped into distinct sections, each with its own H2 heading and set of steps. This layout is useful for complex procedures that involve multiple tasks or require additional context. Here is an example of a sectioned structure:

```markdown
# {Procedure title}

[...]

## Step 1: {Step title}

1. {Step 1}
2. {Step 2}
	- {Clarifier / Option 1}
	- {Clarifier / Option 2}
3. {Step 3}
[...]

## Step 2: {Step title}

1. {Step 1}
2. {Step 2}
3. {Step 3}
[...]
```

Choose flat structure for simple procedures with a limited number of steps, and sectioned structure for complex procedures that involve multiple tasks or require additional context. Either way, actions themselves remain numbered lists or checkboxes.

## Procedure resources

| Resource | Description | When to use it |
| :------- | :---------- | :------------- |
| [Procedure blueprint]() | A visual representation of the procedure structure and flow. | Use it in task analysis to organize H1 and H2 Markdown headings |
| [Procedure template]() | A Markdown template with the procedure structure and basic rules. | Use it to create new procedure documents. |
| [Procedure JSON schema]() | A JSON schema that defines the structure and rules for procedure documents. | Use it to create new procedure documents with the help of an LLM. |
