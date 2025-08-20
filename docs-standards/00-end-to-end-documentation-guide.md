# End-to-end documentation guide

This guide is for the subject-matter experts (SMEs) who contribute to our products: the developers, infrastructure engineers, and other technical contributors responsible for designing and implementing features. It is written for technical experts who need to produce clear, effective documentation for the solutions they create, but who are not professional technical writers.

Our core assumption is that the primary barrier to writing documentation is not a lack of willingness, but the lack of a clear and repeatable process. This guide provides that process. It is designed to remove ambiguity, eliminate "blank page" anxiety, and provide a predictable workflow to create high-quality documentation consistently.

## How this guide is organized

This document provides a high-level overview of the documentation workflow, presented as a sequence of four distinct stages: designing the information, populating the content structure, validating the design, and integrating into the overall structure. It is designed to be a map that you can use to navigate the process from an initial idea to a final, published document.

This document does not contain exhaustive details. Instead, it functions as a central hub, providing direct links to the specific templates, checklists, writing rules, and external tools required to complete each step of the process. You can use it as a quick reference to find the resources you need for a specific task.

## The documentation workflow

This guide provides an end-to-end overview of the documentation process, from initial analysis to final integration. Use it to understand each part of the workflow and how they connect.

## Stage 1: Designing the information

| Element | Description |
|:--------|:------------|
| Description | Identify the reader’s goal, perform a guided task analysis, and decompose the goal into core information blocks (Concept, Procedure, Reference, Troubleshooting). Organize these blocks into a structural blueprint. |
| Goal | Define scope and structure before writing, ensuring alignment with the reader’s goal. |
| Input | Feature code, user stories, and any other existing documentation. |
| Output | A content organization plan (blueprint) that specifies what documents are needed and how information will be structured. |
| Tools | - Task analysis template<br>- Information block organization rules |

```mermaid
flowchart LR
    %% Main flow
    A[Reader's goal] -->|Task analysis| B((1 Task analysis))
    B --> C[Identify information blocks]
    C --> D[Concept]
    C --> E[Procedure]
    C --> F[Reference]
    C --> G[Troubleshooting]
    C -->|Organize| H((2 Organize))
    H --> I[Structural blueprint]

    %% Supporting tools
    J[Task analysis template] --> B
    K[Block organization rules] --> H

    %% Questions
    J -.-> JA["A: 'How do I break down the reader's goal?'"]
    K -.-> KB["B: 'How do I organize the information?'"]

    %% Styling
    style B fill:#fdd,stroke:#333,stroke-width:1px
    style H fill:#fdd,stroke:#333,stroke-width:1px
    style JA fill:#bbf,stroke:#333,stroke-width:1px
    style KB fill:#bbf,stroke:#333,stroke-width:1px
```

## Stage 2: Populating the content structure

| Element | Description |
|:--------|:------------|
| Description | Translate the blueprint into a "good-enough" first draft by filling predefined templates with content drawn from technical sources. Use canonical examples and, where useful, LLMs to assist in generating text. |
| Goal | Produce a "good-enough" first draft that matches the designed structure and reduces ambiguity in what needs to be written. |
| Input | Structural blueprint from Stage 1, technical notes, repository content, templates, and examples. |
| Output | A structured "good-enough" draft of the required document(s). |
| Tools | - Templates<br>- Canonical examples<br>- Writing rules<br>- Custom prompts for LLM assistance |

```mermaid
flowchart LR
%% Stage 2 (Populating the content structure)

subgraph S1[ ]
  direction LR
  Stage1[Stage&nbsp;1]:::stage
  SB[Structural blueprint]:::artifact
  Stage1 -. from Stage 1 .-> SB
end

T["Standardized templates"]:::artifact --> CP
W["Writing rules"]:::artifact --> CP
I["Core technical information (notes&nbsp;+&nbsp;repos)"]:::artifact --> CP
X["Canonical examples"]:::artifact --> CP
SB --> CP

CP[[Custom prompts]]:::prompt --> LLM
LLM[(LLM)]:::process --> GD["Good-enough first draft"]:::output

%% Styles
classDef artifact fill:#FFF7D6,stroke:#333,stroke-width:1px;          %% pale yellow
classDef prompt  fill:#E3F2FF,stroke:#333,stroke-width:1px;           %% pale blue, distinct shape
classDef process fill:#EFEFEF,stroke:#333,stroke-width:1px;
classDef output  fill:#FFFFFF,stroke:#333,stroke-width:1px;
classDef stage   fill:#FFFFFF,stroke-dasharray:3 3,stroke:#777;       %% dotted outline for Stage 1 box
```

## Stage 3: Validating the design

| Element | Description |
|:--------|:------------|
| Description | Improve and refine the draft through self-review, applying checklists, writing rules, and linters. Incorporate additional content as needed. Submit the draft in a GitHub pull request, where SMEs review for technical accuracy and confirm that the content effectively supports the user. |
| Goal | Ensure the documentation is accurate, complete, and structured according to the design. |
| Input | "good-enough" draft from Stage 2. |
| Output | Reviewed and refined documentation, technically validated and structurally consistent. |
| Tools | - Review checklists<br>- Writing rules<br>- Linters<br>- GitHub pull request review |

```mermaid
flowchart LR
    subgraph Stage3["Stage 3: Review & Refinement"]
        GD["Good-enough first draft"] --> SR["Self-review"] --> SD["Second draft"] --> SME["SME review"] --> FC["Final content"]

        %% Supporting tools feeding into Self-review
        RC["Review checklist"] --> SR
        WR["Writing rules"] --> SR
        Lint["Linter"] --> SR

        %% Pull request connected to SME review
        PR["Pull request"] -.-> SME
    end

    %% Dotted line from Stage 2
    Stage2["Stage 2"] -.-> GD

    classDef main fill:#fff,stroke:#333,stroke-width:2px
    classDef support fill:#eef,stroke:#333,stroke-dasharray: 3 3
    classDef review fill:#fdd,stroke:#c33,stroke-width:2px
    classDef stage fill:#ddd,stroke:#333,stroke-dasharray: 5 5

    class GD,SD,FC main
    class RC,WR,Lint,PR support
    class SR,SME review
    class Stage2 stage
```

## Stage 4: Integrating into the overall structure

| Element | Description |
|:--------|:------------|
| Description | Add the approved document to the documentation site. Use the content model to define its location and relationship to other content in the table of contents. |
| Goal | Make the documentation organized, discoverable, and connected to related content. |
| Input | Reviewed and approved documentation from Stage 3. |
| Output | Published documentation, integrated into the overall structure. |
| Tools | - Content model<br>- Documentation publishing platform |

```mermaid
flowchart LR
    subgraph Stage4["Stage 4: Integration & Publication"]
        FC["Final content"] --> INT["Integration (Stage 6)"] --> TOC
        CM["Content model"] --> INT

        %% Docs site as neutral container holding Table of contents
        subgraph DOCSITE["Docs. site"]
            TOC["Table of contents"]
        end
    end

    %% Show link from Stage 3
    STAGE3["Stage 3"] -.-> FC

    classDef main fill:#fff,stroke:#333,stroke-width:2px
    classDef support fill:#eef,stroke:#333,stroke-dasharray: 3 3
    classDef stage fill:#fdd,stroke:#c33,stroke-width:2px
    classDef container fill:#fff,stroke:#333,stroke-dasharray: 3 3

    class FC,TOC main
    class CM support
    class INT stage
    class DOCSITE container
    class STAGE3 support
```
