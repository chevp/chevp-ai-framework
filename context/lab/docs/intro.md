---
id: intro
title: Welcome to the Lab
sidebar_position: 1
slug: /
---

# chevp-ai-framework — Lab

The **Lab** is an experimental Docusaurus subsite for the chevp-ai-framework. It runs alongside the existing static HTML pages at <https://chevp.github.io/chevp-ai-framework/> and lives at the `/flow/` subpath.

This is **not** a replacement for the canonical documentation yet. It is an experiment to find out whether a generated, navigable site beats the current hand-written HTML pages and the markdown-only `context/plans/` flow.

## Why a Lab?

Three problems in the legacy setup motivated the experiment:

1. **`§`-numbering breaks URLs.** Special characters get encoded into `%C2%A7` and are awkward to type, share, or grep.
2. **Plan IDs change between phases.** A plan filed under `EXP-001` becomes hard to trace once it advances to production.
3. **Nothing structures the navigation.** A folder of markdown files works for one author but not for readers who want to discover related plans.

The Lab fixes all three by combining:

- a flat, categorised ID scheme — `FW-01`, `TOOL-01`, `INT-03`, …
- one folder per plan with phase files inside (`context.md`, `exploration.md`, `insights.md`, `production.md`)
- Docusaurus for sidebar, search, and stable URLs

## Where to start

- **[Plans](/plans/)** — current and historical work items in the new ID scheme.
- **[Decisions](/decisions/)** — ADRs scoped to the Lab itself.
- **[Pilot plan: FW-01 Lab Bootstrap](/plans/active/fw-01-lab-bootstrap/context/)** — the meta-plan that sets up this very site.

## How this is built

- Source: `context/lab/` in the [repository](https://github.com/chevp/chevp-ai-framework/tree/main/context/lab).
- Build target: `docs/flow/` (committed, served by GitHub Pages).
- Authoring agent: [`lab-curator`](https://github.com/chevp/chevp-ai-framework/blob/main/agents/lab-curator.md).

## Hard boundary

The Lab does **not** touch the legacy `context/plans/`, `context/adr/`, or any of the static HTML pages in `docs/`. Both worlds coexist until the experiment is validated or killed.

If the experiment succeeds, a follow-up plan will migrate the legacy `context/plans/` into the Lab schema and retire the §-numbering. If it fails, the Lab is deleted and the legacy world remains canonical.

The kill criteria are listed in the [pilot plan](/plans/active/fw-01-lab-bootstrap/context/).
