# Quickstart

A quickstart helps your users to start using your product as quickly as possible. It reduces users' onboarding time, giving them the confidence to start working with the product right away.

A quickstart is more than just an installation guide. Along with helping users set up the product or feature, it should also guide them to try at least one core functionality.

You need at least one quickstart for each product. If the product is complex, you can create multiple quickstarts for different features or tasks.

## Quickstart structure

```markdown
# {Quickstart title}

[...]

## Before you start

- {Prerequisite 1}
- {Prerequisite 2}
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

## Next steps"
- {Link to related guide 1}
- {Link to related guide 2}
- {Link to related guide 3}
```

## Quickstart resources

| Resource | Description | When to use it |
| :------- | :---------- | :------------- |
| [Quickstart blueprint]() | A visual representation of the quickstart structure and flow. | Use it in task analysis to organize H1 and H2 Markdown headings |
| [Quickstart template](./quickstart-template.md) | A Markdown template with the quickstart structure and basic rules. | Use it to create new quickstart documents. |
| [Quickstart JSON schema](./quickstart-template.json) | A JSON schema that defines the structure and rules for quickstart documents. | Use it to create new quickstart documents with the help of an LLM. |
