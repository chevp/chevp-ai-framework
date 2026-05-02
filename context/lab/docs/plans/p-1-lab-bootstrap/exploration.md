---
id: p-1-exploration
title: Exploration
sidebar_position: 2
plan_id: P-1
plan_slug: lab-bootstrap
phase: exp
status: active
created: 2026-05-02
---

# P-1 — Exploration: Lab Bootstrap

## Approach (settled)

After iterating through several naming-scheme proposals, the chosen design is:

- **Folder**: `context/lab/` — Docusaurus source, sibling of `context/plans/`.
- **Build output**: `../../docs/flow/` — written into the gh-pages root, served at `/chevp-ai-framework/flow/`.
- **ID scheme**: flat global counters — `P-<N>` for plans, `D-<N>` for decisions/ADRs. No categories, no zero-padding. Numbers are unique and never reused.
- **Plan layout**: one folder per plan, four phase files inside (`context.md`, `exploration.md`, `insights.md`, `production.md`).
- **No status folders**: the folder structure under `plans/` is flat. Status (`active` / `finished` / `archived` / `deprecated`) is a frontmatter property that can change without renaming the folder or breaking any link.
- **Frontmatter**: stable `plan_id` and `plan_slug` across all phase files; `phase` and `sidebar_position` differ; `status` is the filterable property.

## Alternatives considered

| Option | Why rejected |
|--------|--------------|
| Keep `§`-numbering, only drop the `§` symbol | Phase still encoded in filename; ID changes per phase; URLs still ugly. |
| Category prefix (`FW-01`, `TOOL-01`, …) | Adds a taxonomy that must be governed; categorisation is a property of the plan, not its identity. Flat global ID is enough; topics can be tags later if needed. |
| One file per plan with phase as `## sections` | Long files, bad git diffs, unclear `phase` field semantics. |
| `active/` and `finished/` subfolders | Status changes are routine; renaming a folder breaks every URL and every cross-reference. Status belongs in mutable frontmatter, not in the immutable path. |
| Auto-sync from `context/plans/` into `context/lab/docs/plans/` | Mixes migration with experiment; doubles the failure surface. |

## Why frontmatter `status` instead of a folder

A folder name is part of the URL. Renaming a folder breaks:

- every internal link that pointed to a file inside it
- every external link someone bookmarked or pasted in a commit message
- the file's git history (technically preserved by git, but visibly noisy in tooling)

A frontmatter field is metadata. Editing it is a one-line diff with zero side effects. Docusaurus can read it at build time and render filtered lists. The reader sees the same logical grouping (active vs. finished) without paying the cost of structural rename.

The `/plans/` index page is responsible for the visual grouping. It is the *one* place that knows about the `status` enum.

## Filtering in Docusaurus

Two implementation paths considered:

1. **MDX page + small React component**. Reads all docs via `usePluginData('docusaurus-plugin-content-docs')`, filters by `frontMatter.status`, renders one table per status group. Lives at `context/lab/docs/plans/index.mdx` + `context/lab/src/components/PlanList.tsx`. Chosen — minimal infra, full control.
2. **Docusaurus tags**. Use `tags: [active]` in frontmatter; tag pages are auto-generated. Rejected: tags are designed for multi-tag overlap (a doc can have many), but `status` is mutually exclusive (a plan has exactly one). Forcing tags would muddy the semantics.

For P-1 the `index.mdx` ships as a documented stub; the React component is a trivial implementation that gets refined as more plans accumulate.

## Challenger output

**Top-3 failure modes:**

1. The Lab is more work than benefit. Authors keep writing markdown in `context/plans/` and the Lab rots after two plans.
2. The `status` filter feels less concrete than an `active/` folder; readers cannot tell "what is active right now" at a glance from the file tree alone.
3. The agent boundary erodes — someone copies legacy plans into the Lab without migration discipline. The "fresh start" promise breaks.

**Counter-argument the Challenger gave:**

> "You're solving an authoring problem with a publishing tool. Docusaurus is heavy infra for what is essentially a flat naming convention plus a status field. You could get 80% of the win with `context/plans/p-1-foo.md` and a generated `INDEX.md` that reads frontmatter."

**Response:** Accepted as a real risk — captured in H4 / H5 and the Kill Criteria. The Lab passes only if it measurably beats markdown-only authoring AND the filtered index gives readers a better experience than `ls`. If H4/H5 fail, we keep the new ID scheme and discard Docusaurus.

## Kill Criteria

The Lab is killed and `context/lab/` + `docs/flow/` are deleted if any of these hold after **4 weeks** of trial use:

- Authoring a plan in the Lab takes longer than the markdown-only flow in `context/plans/`.
- Build output bloats the repo by &gt; 50 MB.
- Search/navigation in the Lab is not measurably better than `grep` over `context/plans/`.
- The `status` frontmatter filter proves harder to use than just naming subfolders `active/` / `finished/` after all.

If killed, the new ID scheme proposal can survive separately as a `D-<N>` decision document.

## Acceptance criteria for G2 → Production

- `context/lab/` builds without errors via `npm run build`.
- `docs/flow/index.html` exists and renders.
- Both URLs work simultaneously: `/chevp-ai-framework/` (existing) and `/chevp-ai-framework/flow/` (new).
- This very plan (P-1) is fully authored in the new schema and visible in the Lab sidebar.
- The `/plans/` index page renders a list of active plans driven by frontmatter `status`.
- The `lab-curator` agent is documented in `agents/lab-curator.md` with hard boundary rules and updated for the flat P-/D- scheme.
