--- #1


--- #2

Unified, AI-ready framework for IFT's user documentation

--- #3

# Current Documentation Pain Points

- **Fragmented toolchain**: Multiple documentation tools and workflows lead to inefficiencies.
- **Uneven content quality**: Inconsistent documentation standards across projects.
- **Unclear onboarding**: New contributors struggle to understand where to start.
- **Missing key information**: Important concepts are often buried or not documented at all.
- **Lack of standards**: No unified structure for documentation, making it hard for writers to write and users to browse the docs.
- **Diluted ownership**: Docs are treated as a side task, with no clear accountability.

--- #4

# Proposed Solution: Unified Documentation Framework

image

--- #5

# What means "Unified Platform"?

Consolidate all user-facing documentation for IFT projects onto a single, AI-native platform, specifically GitBook, to provide a central access point for users.

image

--- #6

# What means "Unified workflow"?

Establish a standardized workflow for creating and updating documentation using a "docs-as-code" model, with content stored in a single GitHub monorepository, to improve quality and facilitate contributions.

--- #7

# Federated ownership model

Define clear roles and responsibilities, including a project lead (technical writer) and dedicated documentation owners within each IFT unit, to ensure accountability for content creation and maintenance.

Documentation owners will continue to report to their respective team leads, ensuring that writers for each team are managed by their own team and not by the project lead. This federated model aims to avoid a centralized "IFT Docs" department.

--- #8

# Project phases

| Phase                                                                       | Main steps                                                       |
| :-------------------------------------------------------------------------: | :--------------------------------------------------------------: |
| *Authoring and review stay in the old system with no changes*               |                                                                  |
| 0\. Project documentation (I) and kick-off ⬥                                | Project documentation, approval, licensing, and repository setup |
| 1\. GitBook and domain config. ⬥                                            | GitBook deployment and configuration. Domain setup.              |
| 2\. Monorepo setup ⬥                                                        | GitHub configuration                                             |
| 3\. Project documentation (II) ⬥                                            | Style guide and templates                                        |
| 4\. Pilot migration ⭑                                                       | Content migration, scripting, manual updates, and auditing       |
| 5\. Pilot review ⭑                                                          | Content clean-up and review                                      |
| 6\. Feedback and adjust ⭑                                                   | Gather feedback, update workflows                                |
| *Authoring and review continue in the new system only*                      |                                                                  |
| 7\. Project documentation (III) ⬥                                           | Style guide and templates updates                                |
| 8\. Linter implementation ⬥                                                 | Write VALE linter rules and linter implementation                |
| 9\. Project documentation (IV) ⬥                                            | Training materials                                               |
| 10\. Training and mentoring ⭑                                               | Training and mentoring the IFT unit documentation owner          |
| *OneDoc project closure and documentation project handover to the IFT unit* |                                                                  |

⬥ Once only
⭑ Once per IFT unit

--- #9

# Out of scope

- Adapting existing docs ⭑ -- Update the existing documentation to follow standards
- Implementing analytics ⭑ -- Configure GitBook analytics, prioritizing users' privacy

⭑ Once per IFT unit

While phases 11 and 12 are outside the direct scope of this project, we will provide the necessary support to facilitate their implementation.

--- #10

# Where we are

| #  | Phase                              | State | Progress |
|----|------------------------------------|:-----:|:--------:|
| 1  | Project plan and kick-off          | 🟡    | 🟩🟩🟩⬜⬜ |
| 2  | GitBook and domain setup           | ⚪    | ⬜⬜⬜⬜⬜ |
| 3  | Repo scaffold                      | 🟡    | 🟩🟩🟩⬜⬜ |
| 4  | Style guide and templates (v1)     | 🟡    | 🟩⬜⬜⬜⬜ |
| 5  | Pilot migration                    | ⚪    | ⬜⬜⬜⬜⬜ |
| 6  | Pilot review                       | ⚪    | ⬜⬜⬜⬜⬜ |
| 7  | Feedback and adjustments           | ⚪    | ⬜⬜⬜⬜⬜ |
| 8  | Style guide and templates (v2)     | ⚪    | ⬜⬜⬜⬜⬜ |
| 9  | Linter implementation              | ⚪    | ⬜⬜⬜⬜⬜ |
| 10 | Training materials                 | ⚪    | ⬜⬜⬜⬜⬜ |
| 11 | Training and mentoring             | ⚪    | ⬜⬜⬜⬜⬜ |

Legend: 🟢 Done 🟡 In progress ⚪ Not started 🔴 Blocked

--- #11

# Risks and asks

| Risk                                                             | Likelihood | Mitigation |
| :--------------------------------------------------------------- | :--------: | :--------: |
| Unit leads declined to participate (R1)                          | 🟡          | TBD        |
| Workload underestimated for a single writer as project lead (R2) | 🔴          | TBD        |
| Hidden technical debt in legacy docs (R3)                        | 🔴          | ✅          |
| Executive sponsor changes / funding cut (R4)                     | ⚪          | TBD        |
| Veto on SaaS hosting or non-Open Source solution (R5)            | 🟡          | ✅          |
| Access to docs broken during migration (R6)                      | 🟢          | ✅          |
| A single GitHub repo / GitBook server becomes a bottleneck (R7)  | 🟢          | ✅          |
| Status and Keycard docs not migrated (R8)                        | 🟡          | TBD        |
