# Concept

Concept articles describe a product's functionality. They provide technical context, explain architecture, or clarify processes. Concept topics help users understand the "why" and "what" behind a product or feature, rather than the "how" (which is covered in procedures).

For example, a user minting an NFT may not be interested in understanding the interactions with the Ethereum blockchain. For this user, a procedure explaining how to mint an NFT is sufficient. Others, however, may wish to understand this process in more detail, so a concept article on minting NFTs satisfies their curiosity.

Concepts provide non-procedural information that complements other topic types, such as [procedure]() or [reference]() topics, but never replaces or duplicates them.

Logos documentation aims to guide users in completing tasks and exploring the technical stack features and functionalities. Therefore, concept topics are not as common as procedural topics.

> 📒 **Note:**
>
> A list of frequently asked questions (FAQs) falls under the concept category.

## When to write a concept article

Write a concept article when:

- There is a new product feature that users need to understand before using it.
- You are writing a long intro for a procedure to explain background context.
- The new product feature involves important constraints or trade-offs that users must understand to avoid mistakes.
- There is an important context behind a design decision. For example, "Why we use asynchronous processing for bulk operations."

## Concept articles vs. procedure introductions

Every procedure requires an introduction that provides context and helps readers understand the procedure's purpose and scope. However, if the context is complex and requires more than a brief explanation, consider creating a separate concept article instead of expanding the procedure introduction.

Here's how to decide between a procedure introduction and a concept article:

| **Write a concept article if...** | **Write a procedure intro if...** |
| :-------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------- |
| The explanation exceeds 3 paragraphs | The context fits in 1-3 paragraphs |
| The same information appears in 3+ procedures | It's unique to this specific procedure |
| Users might want to read it without following steps (for example, during evaluation) | Users only need it while performing these exact steps |
| It requires diagrams, examples, or deep technical details | It's brief context-setting without needing examples |

Reusability is the key factor. If you find yourself writing the same context in multiple procedures, you should create a concept article and link to it from the procedure introductions.

> 📒 **Note:**
>
> A procedure article always includes an introduction that provides context for the task. Even if you determine that a concept article is necessary, you must still include a brief introduction in the procedure article, summarizing the concept and linking to the full concept article for more information.
