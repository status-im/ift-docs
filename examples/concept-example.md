---
title: About the codespace lifecycle
topic: Codespaces
author: jorge-campo
version: 1
url: docs/codespaces/about-codespace-lifecycle
---

<!-- This document is an example for the concept template. It is not a real document and should be used for illustration purposes only. -->

# About the codespace lifecycle

#### Explore how GitHub Codespaces provides instant, cloud-based development environments for any project.

> 📒 **Note**  
> GitHub Codespaces is available on GitHub Free, Pro, Team, and Enterprise Cloud plans.

A [codespace](./about-codespaces.md) is a cloud-hosted development environment that lives on GitHub’s infrastructure. The [codespace lifecycle](#lifecycle-events) determines what happens to your source code, container state, and [billing](#billing). By understanding each event you can keep changes safe, avoid surprise costs, and choose the right retention strategy for every project.

You can create a short-lived workspace for quick tasks and delete it the same day to avoid storage costs, or keep a workspace running for longer to retain caches and build outputs. How long you keep a codespace running depends on your workflow.

Codespaces offer a flexible environment for different scenarios. Here are some common use cases:

- A ready-to-code environment for exploring or contributing to open-source projects.
- Safe sandboxing for experimental features, review of pull requests, or debugging rare bugs on a specific commit.
- Onboarding new developers to a standardized workspace without lengthy setup instructions.

GitHub Codespaces and [GitHub.dev](./about-github-dev.md) both let you work with your code directly from your browser, but they address different development needs. Use the table below to see how these solutions compare.

| Feature                | GitHub Codespaces                       | GitHub.dev                 |
|------------------------|-----------------------------------------|----------------------------|
| Environment            | Full container-based dev environment    | Lightweight code editor    |
| Customization          | Highly customizable via dev containers  | Minimal (settings sync)    |
| IDE integration        | VS Code, JetBrains, JupyterLab, browser | Browser-based only         |
| Running code           | Yes                                     | No (edit only)             |
| Collaboration support  | Yes, identical environments for teams   | No                         |


## The basics

-  A stopped codespace keeps its file system and container image until deleted.
* Only the running state accrues compute charges; stopped instances incur storage fees.
* GitHub auto-deletes a codespace after its retention period unless you delete it sooner.

## Lifecycle events

Every codespace moves through predictable events, from running, stopping, and rebuilding to eventual deletion. This diagram illustrates the full lifecycle:

```mermaid
flowchart LR
  create[Created] --> run[Running]
  run -->|Idle timeout| stop[Stopped]
  stop --> restart[Restarted]
  restart --> rebuild[Rebuilt]
  rebuild --> delete[Deleted]
```

Check this table to understand who or what triggers each event and how it affects your environment:

| Event            | Trigger                                                        | Result                                                                                    |
| ---------------- | -------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **Created**      | You start a new codespace from GitHub.com or the CLI.          | GitHub clones the repository and builds the dev container defined by `devcontainer.json`. |
| **Running**      | Codespace is active immediately after creation or restart.     | VM is online; edits, terminals, and ports run in real time. Compute charges accrue.       |
| **Stopped**      | You stop the codespace or it reaches the idle timeout.         | Compute halts but disk persists. Only storage charges continue.                           |
| **Idle timeout** | No active connection for the configured period (15 min–4 hrs). | Transitions the codespace to **Stopped** automatically.                                   |
| **Rebuilt**      | You rebuild to apply container or image updates.               | Container image is recreated while workspace files stay intact.                           |
| **Deleted**      | You delete the codespace or the retention period expires.      | Storage is removed. Unpushed commits are lost and all charges stop.                       |

## Persistence and state

Codespaces store data in two separate volumes. Understanding what each volume holds helps you decide when to commit, rebuild, or delete.

### Workspace volume

This repository-specific volume contains your project files, build artifacts, and caches. Stopping or rebuilding leaves the volume intact, so unsaved edits persist between sessions.

#### When the workspace volume persists

The volume remains available when you stop, restart, or rebuild a codespace, so unpushed edits and cached layers stay intact for the next session.

#### When the workspace volume is removed

GitHub detaches and deletes the volume only when you delete the codespace or its retention period expires, permanently discarding any data that has not been pushed.

### User settings volume

GitHub mounts a personal volume with your editor settings, extensions, and dotfiles into every codespace. Because it is independent of any single workspace, your customized tools reappear automatically, even after you recreate codespaces across multiple repositories.


## Billing implications

Compute is billed per active minute based on the instance size. Storage is billed per GB per month for every stopped or running codespace. Frequent rebuilds do not affect cost; they reuse cached layers. Deleting a codespace immediately stops all charges.

---
*Examples adapted from GitHub Docs (CC BY 4.0). See [Attributions](/ATTRIBUTIONS.md) for details.*
