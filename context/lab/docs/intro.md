---
id: intro
title: Welcome to the Lab
sidebar_position: 1
slug: /
---

# chevp-ai-framework — Lab

The **Lab** is the **canonical source-of-truth for plans and decisions** in the chevp-ai-framework. It is a Docusaurus site sourced from `context/lab/`, intended to be served at the `/flow/` subpath of `chevp.github.io/chevp-ai-framework` once the GitHub Pages deployment is wired up. Until then, the Lab is read locally via `npm run start` in `context/lab/` (and as plain markdown in the repo).

Plans and decisions are authored here, in a flat global ID scheme (`P-<N>`, `D-<N>`), with one folder per plan and `status` as mutable frontmatter. The legacy `context/plans/` folder with `§`-numbering has been migrated and removed.

## Why the Lab

Three problems in the legacy `context/plans/` setup motivated the move:

1. **`§`-numbering breaks URLs.** Special characters get encoded into `%C2%A7` and are awkward to type, share, or grep.
2. **Plan IDs change between phases.** A plan filed under `EXP-001` becomes hard to trace once it advances to production.
3. **Status encoded as a folder name.** Renaming `active/` → `finished/` breaks every URL and every cross-reference.

The Lab fixes all three by combining:

- a flat global ID scheme — `P-1`, `P-2`, `P-32`, … and `D-1`, `D-2`, …
- one folder per plan with phase files inside (`context.md`, `exploration.md`, `insights.md`, `production.md`)
- `status` as **frontmatter only** — never a folder name; filtered live via the `/plans/` index
- Docusaurus for sidebar, search, and stable URLs

## Where to start

- **[Plans](/plans/)** — current and historical work items, filtered by `status` from frontmatter.
- **Decisions** — `D-<N>` ADRs (under `decisions/`).
- **[Pilot plan: P-1 Lab Bootstrap](/plans/p-1-lab-bootstrap/context/)** — the meta-plan that established this site and ID scheme.

## ID scheme at a glance

| Prefix | Used for | Examples |
|--------|----------|----------|
| `P-<N>` | Plans | `P-1`, `P-32` |
| `D-<N>` | Decisions / ADRs | `D-1`, `D-123` |
| `PROP-<NNN>` | Proposals (lightweight backlog entries spawned by Gatekeepers) | `PROP-001` |

Plans and decisions use no categories, no padding, no reuse. Status (`active` / `finished` / `archived` / `deprecated`) is mutable frontmatter — never part of the path. Proposals live under `plans/proposals/` and follow their own promote/defer/reject lifecycle (see [proposals](/plans/proposals/PROP-001_multi-provider-llm)).

## How this is built

- Source: `context/lab/` in the [repository](https://github.com/chevp/chevp-ai-framework/tree/main/context/lab).
- Build target: `docs/flow/` (committed, served by GitHub Pages).
- Authoring agent: [`lab-curator`](https://github.com/chevp/chevp-ai-framework/blob/main/agents/lab-curator.md).
