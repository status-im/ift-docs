---
theme: dracula
transition: slide-left
title: OneDoc Project Briefing
author: campo@ift
browserExporter: 
download: true
exportFilename: ift-onedoc-project-briefing
export:
    format: pdf
---

# OneDoc project briefing

Unified, AI-ready framework for IFT's user documentation

--- 

# OneDoc project goal

<div class="mt-20 text-3xl">
	To unify IFT's user-facing documentation on an AI-native platform (GitBook) with a "docs-as-code" workflow and clear roles, ensuring consistent, high-quality, and easily discoverable documentation to encourage greater developer adoption and contributions.
</div>

<div class="absolute right-30px bottom-30px">
	<SlideCurrentNo /> / <SlidesTotal />
</div>

---

# Current documentation pain points

- **Fragmented toolchain:** Multiple documentation tools and workflows lead to inefficiencies
- **Uneven content quality:** Inconsistent documentation quality across projects
- **Unclear onboarding:** New contributors struggle to understand where to start
- **Missing key information:** Important concepts are often buried or not documented at all
- **Lack of standards:** Lack of structure makes docs hard to write, maintain, and browse
- **Diluted ownership:** Docs are treated as a side task, with no clear accountability

<div class="absolute right-30px bottom-30px">
	<SlideCurrentNo /> / <SlidesTotal />
</div>

---

# Proposed solution: Unified documentation framework

<div class="flex justify-center items-center h-full">
  <img src="/Users/campo/Documents/repos/ift-docs/project/media/unified-documentation-framework-dark.png" class="max-h-96" />
</div>

<div class="absolute right-30px bottom-30px">
	<SlideCurrentNo /> / <SlidesTotal />
</div>

---

# 1/ What means **Unified platform**?

<div class="mt-20 text-3xl">
	Consolidate all user-facing documentation for IFT projects onto a single, AI-native platform, specifically GitBook, to provide a central access point for users.
</div>

<div class="absolute right-30px bottom-30px">
	<SlideCurrentNo /> / <SlidesTotal />
</div>

---

# 2/ What means **Standardized workflow**?

<div class="mt-20 text-3xl">
	Establish a standardized workflow for creating and updating documentation using a "docs-as-code" model, with all content stored in a single GitHub monorepo, to align methods and facilitate contributions.
</div>

<div class="absolute right-30px bottom-30px">
	<SlideCurrentNo /> / <SlidesTotal />
</div>

---

# 3/ What means **Clear ownership**?

<div class="mt-10 text-3xl">
	Federated ownership model
</div>

<div class="mt-5 text-xl">
	Define clear roles and responsibilities, including a project team (technical writers) and dedicated documentation owners within each IFT project, to ensure accountability for content creation and maintenance.
</div>

<div class="mt-5 text-xl">
	Documentation owners continue reporting to their respective team leads, and not the project team, ensuring that writers fully integrate and align with their own team. This federated model avoids a centralized "IFT Docs" department.
</div>

<div class="absolute right-30px bottom-30px">
	<SlideCurrentNo /> / <SlidesTotal />
</div>

---

# Project phases

| **Phase**                                         | **Main steps**                                         |
|:--------------------------------------------------|:-------------------------------------------------------|
| 0. Project documentation (I) and kick-off ⬥       | Project documentation and approval                     |
| 1. GitBook and domain config ⬥                   | GitBook deployment and configuration and domain setup     |
| 2. Monorepo setup ⬥                               | GitHub repository configuration                                   |
| 3. Project documentation (II) ⬥                   | Content guidelines (style guide) and templates                              |
| 4. Pilot migration ⭑                              | Migration, scripting, manual updates, and auditing     |
| 5. Pilot review ⭑                                 | Content clean-up and review                            |

--

##### ⬥ Once only / ⭑ Once per IFT project

<div class="absolute right-30px bottom-30px">
	<SlideCurrentNo /> / <SlidesTotal />
</div>

---

# Project phases (cont.)

| **Phase**                                         | **Main steps**                                         |
|:--------------------------------------------------|:-------------------------------------------------------|
| 6. Feedback and adjust ⭑                          | Gather feedback, update workflows                      |
| 7. Project documentation (III) ⬥                  | Style guide and templates updates                      |
| 8. Linter implementation ⬥                        | Write VALE linter rules and linter implementation      |
| 9. Project documentation (IV) ⬥                   | Training materials                                     |
| 10. Training and mentoring ⭑                      | Training and mentoring the IFT project owner|

--

##### ⬥ Once only / ⭑ Once per IFT project

<div class="absolute right-30px bottom-30px">
	<SlideCurrentNo /> / <SlidesTotal />
</div>

---

# Out of scope

- Adapting existing docs -- Update the existing documentation to follow standards
- Implementing analytics -- Configure GitBook analytics, prioritizing users' privacy

While these tasks are outside the direct scope of this project, we will provide the necessary support to facilitate their implementation.

<div class="absolute right-30px bottom-30px">
	<SlideCurrentNo /> / <SlidesTotal />
</div>

---
zoom: 0.7
---

# Project snapshot

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

🟢 Done 🟡 In progress ⚪ Not started 🔴 Blocked

<div class="absolute right-30px bottom-30px">
	<SlideCurrentNo /> / <SlidesTotal />
</div>

---
zoom: 0.9
---

# Risks and asks

| **Risk**                                                             | **Likelihood** | **Mitigation** |
| :--------------------------------------------------------------- | :--------: | :--------: |
| Project leads declined to participate (R1)                          | 🟡          | TBD        |
| Workload underestimated for a single writer as project lead (R2) | 🔴          | TBD        |
| Hidden technical debt in legacy docs (R3)                        | 🔴          | ✅          |
| Executive sponsor changes / funding cut (R4)                     | ⚪          | TBD        |
| Veto on SaaS hosting or non-Open Source solution (R5)            | 🟡          | ✅          |
| Access to docs broken during migration (R6)                      | 🟢          | ✅          |
| A single GitHub repo / GitBook server becomes a bottleneck (R7)  | 🟢          | ✅          |
| Status and Keycard docs not migrated (R8)                        | 🟡          | TBD        |
