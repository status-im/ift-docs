# Populate the structure

In this phase, you turn the blueprint from Phase 1 (the H1 and H2 headings outline) into a first draft. You can do this manually or with LLM assistance.

- Human-made: You write the draft directly using the writing rules, document templates, and canonical examples as reference.
- LLM-assisted: You use a language model to help generate the draft based on the blueprint and other inputs.

At the end of this phase, you should have a complete first draft of the document, ready for review and refinement in Phase 3.

```mermaid
flowchart TD
    %% Global style for left-aligned nodes
    classDef leftAlign text-align:left,white-space:pre-wrap;

    %% Title
    title["**SME technical documentation authoring paths**"]

    %% Split paths
    subgraph manual_path["**Human-made path**"]

        C1["*Components:*

--
• Blueprint from Phase 1
• Information sources
• Writing rules (Markdown)
• Document templates (Markdown)
• Canonical examples
• Preflight validator (quick structural checks)
• Front matter + rule-ID conventions"]

        D1["*Process:*

--
SME writes draft directly using the writing rules, templates, and canonical examples as reference."]
    end

    subgraph llm_path["**LLM-assisted path**"]
        C2["*Components::*

--
Human-made path components PLUS:
• Prompt templates
• Machine-readable template schema (JSON)
• Binary rules in JSON
• Generator scripts
• Model/runtime config + API credentials
• Safety rails for executable content"]
        E2["*Process:*

--
Generator scripts slice the job, call the LLM with JSON schema constraints, merge output into Markdown template, and run preflight validation."]
    end

    %% Phase 3
    F["**Phase 3: Full validation**"]

    %% Connections
    title --> C1
    title --> C2
    C1 --> D1
    C2 --> E2
    D1 --> F
    E2 --> F

    %% Apply left alignment to all nodes
    class title,B,C1,D1,C2,E2,F leftAlign
```
