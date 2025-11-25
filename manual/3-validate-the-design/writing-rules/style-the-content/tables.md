# Tables

Tables provide a simple way to summarize information. Use a table instead of [bullet lists](./06-bullet-lists.md) when you need to describe the elements on the list.

- Bullet list example (incorrect):

  There are four types of items:

  - **Item 1** <br>Item 1 description
  - **Item 2** <br>Item 2 description
  - **Item 3** <br>Item 3 description
  - **Item 4** <br>Item 4 description

- Table format example (**correct**):

    | Item   | Description          |
    |:-------|:---------------------|
    | Item 1 | Item 1 description |
    | Item 2 | Item 2 description |
    | Item 3 | Item 3 description |
    | Item 4 | Item 4 description |

You can also use tables to compare the available options across different elements.

    | Features   | Desktop | Mobile | Web |
    |:-----------|:--------|:-------|:----|
    | Feature A  |   ✅    |   ✅   |     |
    | Feature B  |   ✅    |        |     |
    | Feature C  |         |   ✅   | ✅  |

> ✨ **Tip:**
>
> You can use links in tables except if the table is part of a procedural step.

Use the following guidelines when using periods in a table for punctuation:

- End every complete sentence inside tables with a period.
- Use periods when there are multiple sentences in one table cell.
- Keep table columns parallel. If one item in a column is a complete sentence, all items in that column should end with a period, even if they are a single word. This rule applies to each column individually, not across the entire table.

## Formatting tables

When formatting tables in Markdown, follow these guidelines:

- Do not format tables using HTML. Using `<br />` tags for line breaks inside table is okay.
- Use colons (`:`) to align columns. For example, `|:---|` aligns the column to the left, `|:---:|` centers it, and `|---:|` aligns it to the right.
- In tables with small widths (less than 100 characters), format them with extra spaces for better readability. For example:

  Right alignment:

    | Item   | Description          |
    |:-------|:---------------------|
    | Item 1 | Item 1 description.  |
    | Item 2 | Item 2 description.  |

  Wrong alignment:

    | Item | Description         |
    |:---|:----------|
    |Item 1|Item 1 description|
    |Item 2|Item 2 description|

- In tables with larger widths (more than 100 characters), left-align everything, don't use extra spaces, and use only three dashes in the header. For example:

  Right alignment:

    | Item | Description |
    |:---|:---|
    | Item 1 | This is a longer description for Item 1 that exceeds the typical width of a standard table cell. |
    | Item 2 | This is a longer description for Item 2 that exceeds the typical width of a standard table cell. |

  > 📒 **Note:**
  >
  > In long-width tables, using extra dashes in the header makes it harder to understand the table structure.

  Wrong alignment:

    | Item   | Description                                                                                      |
    |:-------|:-------------------------------------------------------------------------------------------------|
    | Item 1 | This is a longer description for Item 1 that exceeds the typical width of a standard table cell. |
    | Item 2 | This is a longer description for Item 2 that exceeds the typical width of a standard table cell. |

- Keep one space between the pipe (`|`) and the content in each cell for better readability. For example:

  Correct:

    | Item   | Description          |
    |:-------|:---------------------|
    | Item 1 | Item 1 description.  |
    | Item 2 | Item 2 description.  |

  Incorrect:

    |Item  |Description        |
    |:-----|:------------------|
    |Item 1|Item 1 description.|
    |Item 2|Item 2 description.|
