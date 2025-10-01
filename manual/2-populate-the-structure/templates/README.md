# Templates

This directory contains templates to create new technical documents for Logos. Templates help maintain consistency and save time when creating similar types of content.

- [Quickstart template](./quickstart-template.md)
- [Concept template](./concept-template.md)
- [Procedure template](./procedure-template.md)
- [Reference template](./reference-template.md)

## Using templates

Templates are Markdown files. To use a template, copy the desired template content and paste it into your new document. Then, fill in the relevant sections with your content.

> **Note:**
>
> Your content should follow the structure and guidelines provided in the template. Don't modify the template to fit your content. If you need to update a template, send a pull request with your changes following the [contribution guidelines](../../CONTRIBUTING.md).

## Guided vs. minimal templates

The templates in this section use a guided approach, providing detailed instructions and examples to help you structure your content effectively.

Unlike minimal templates, which offer only basic headings and leave much of the structure up to the author, guided templates are dense with content and may feel overwhelming at first. This initial density is intentional: it makes expectations explicit, prevents omissions, and typically shortens drafting and review time.
 
The rationale for using guided templates instead of minimal templates is twofold:

1. **Reduce context switching**: Minimize the need for authors to jump between resources (e.g., writing rules and examples) while drafting. Guided templates provide instructions and examples in one place.
2. **Support inexperienced authors**: SMEs are typically not trained as technical writers. For highly technical content that is not frequently updated, guided templates are the most effective way to help inexperienced authors produce complete and clear documentation.
This diagram illustrates this situation:

```mermaid
%%{init: {
  "theme": "base",
  "themeVariables": {
    "fontFamily": "Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto",
    "fontSize": "14px",
    "primaryTextColor": "#0f172a",
    "lineColor": "#94a3b8"
  },
  "flowchart": { "curve": "basis", "nodeSpacing": 50, "rankSpacing": 60 }
}}%%
flowchart LR
  %% Groups
  subgraph Inputs
    direction TB
    A{Doc<br/>complexity?}:::decision
    B{Writer<br/>experience?}:::decision
    E{Update<br/>frequency?}:::decision
  end

  subgraph Recommendation
    direction TB
    C([Lightweight<br/>template]):::good
    D([Feature-rich<br/>template]):::strong
  end

  %% Flows
  A -- High --> B
  A -- Low --> C
  B -- New --> D
  B -- Experienced --> C
  E -- Often --> C
  E -- Rare --> D

  %% (Optional) layout hint to keep Inputs aligned
  A -. Align -.-> E

  %% Styles
  classDef decision fill:#eff6ff,stroke:#3b82f6,stroke-width:1.5px,color:#0f172a;
  classDef good fill:#ecfdf5,stroke:#10b981,stroke-width:1.5px,color:#064e3b;
  classDef strong fill:#f5f3ff,stroke:#8b5cf6,stroke-width:1.5px,color:#2e1065;

  %% Link accents (green to "Lightweight", purple to "Feature-rich")
  linkStyle 1,3,4 stroke:#10b981,stroke-width:1.5px;
  linkStyle 2,5 stroke:#8b5cf6,stroke-width:1.5px;
```
