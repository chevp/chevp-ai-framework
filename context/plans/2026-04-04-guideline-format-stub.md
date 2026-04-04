---
name: Reference stub — Guideline format harmonization
description: This repo adopts the memory-style guideline format defined by chevp-workflow
type: reference-stub
owner-plan: misc/chevp-workflow/context/plans/2026-04-04-guideline-format-harmonization.md
status: approved
date: 2026-04-04
---

# Reference — Guideline Format Harmonization

This repo (`misc/chevp-ai-framework`) participates in a workspace plan whose primary owner is:

**`misc/chevp-workflow`** → `../../../chevp-workflow/context/plans/2026-04-04-guideline-format-harmonization.md`

## What changes in this repo

- `guidelines/ai-collaboration.md` — add frontmatter + Rule/Why/How-to-apply header
- `guidelines/context-management.md` — add frontmatter + Rule/Why/How-to-apply header
- `guidelines/plan-granularity.md` — add frontmatter + Rule/Why/How-to-apply header
- `guidelines/README.md` — new file, references canonical format

## What NOT to do

- Do not change the content of existing guidelines, only the structure at the top.
- Do not redefine the format here — reference the canonical definition in chevp-workflow.
- Do not expand scope to other folders (`templates/`, `integration/`, lifecycle folders).

## Commit back-reference

All commits in this repo related to this workspace plan carry:

```
Refs workspace-plan: misc/chevp-workflow#2026-04-04-guideline-format-harmonization
Refs upstream: misc/chevp-workflow@<sha-of-owner-commit>
```

## Sequence

This repo is **#2** in the workspace plan's commit sequence.
Commit only after `misc/chevp-workflow` has committed its note in `guidelines/README.md`.
