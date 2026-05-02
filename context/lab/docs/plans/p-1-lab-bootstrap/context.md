---
id: p-1-context
title: Context
sidebar_position: 1
plan_id: P-1
plan_slug: lab-bootstrap
phase: ctx
status: active
created: 2026-05-02
---

# P-1 — Context: Lab Bootstrap

## Problem Statement

The chevp-ai-framework documentation is split between:

- 30+ hand-written static HTML pages in `docs/` (rendered by GitHub Pages)
- markdown plans in `context/plans/` using a `§`-numbering scheme

Both have known friction:

- The HTML pages are written manually — adding a new doc requires writing tailwind, copying the header, and remembering all the cross-links.
- The `§`-scheme breaks URLs (`%C2%A7` encoding), changes ID when a plan moves between phases, and gives no structural cue about the topic of a plan.
- There is no sidebar, search, or way to discover related plans.

## Hypotheses

| H | Statement | How to falsify |
|---|-----------|----------------|
| H1 | A flat global ID (`P-1`, `P-2`, … and `D-1`, `D-2`, …) is easier to grep, share, and remember than `§1.1.2` or category-prefixed IDs. | Author 5 plans, ask a reader to find them — measure time-to-find against the legacy. |
| H2 | One folder per plan with phase files inside (`context.md`, `exploration.md`, `production.md`) makes phase progression visible without renaming files. | Promote a plan through 3 phases; check that no link breaks. |
| H3 | A Docusaurus subsite at `/flow/` can coexist with the existing static HTML pages without conflict. | Build, push, verify both URLs work. |
| H4 | Frontmatter `status` plus a filtered MDX index page beats hard-coded `active/` and `finished/` folders. | Move 2 plans through statuses without renaming files; verify the index updates and no link breaks. |
| H5 | The `lab-curator` agent reduces authoring friction enough that writing in the Lab is faster than markdown-only flow. | Time-box a plan creation; compare to legacy authoring. |

## Risks

| R | Risk | Mitigation |
|---|------|------------|
| R1 | Build output bloats the repo — Docusaurus generates many small files. | Measure repo size delta after first build; abort if &gt; 50 MB. |
| R2 | Two parallel doc systems confuse readers and authors. | Lab is clearly marked **EXPERIMENT**; legacy is canonical until experiment passes. |
| R3 | Frontmatter `status` filter is harder to discover than a folder named `active/`. | Add a clearly linked `/plans/` index that defaults to active and lets the reader switch. |
| R4 | The agent's hard boundary (only `context/lab/` and `docs/flow/`) is bypassed. | Document the boundary in `agents/lab-curator.md`; add a simple validation step in `validate` operation. |

## Scope

**In scope:**

- Set up `context/lab/` with Docusaurus 3.x.
- Build into `docs/flow/`.
- Define and document the new flat ID scheme (`P-<N>`, `D-<N>`).
- Define folder-per-plan layout with four phase files.
- Define frontmatter schemas including `status` as a filterable property.
- Author this plan as the first dogfooding instance.
- Create the `lab-curator` agent.
- Provide a `/plans/` index that filters by `status`.

**NOT in scope:**

- Migrating any existing `context/plans/§*` plan into the Lab.
- Changing the existing static HTML pages in `docs/`.
- Defining a CI pipeline to auto-build (manual `npm run build` is enough for the experiment).
- Reaching feature parity with the existing HTML site.
- Categorising plans by topic (e.g. framework / tooling / docs). The flat global counter is the entire scheme.
