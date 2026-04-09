# Plan Registry — chevp-ai-framework

Compact overview of all active plans in `context/plans/`.
Plans are grouped by chapters (§x.y) — see [plans/chapters/](plans/chapters/).

This repository uses **§-numbering** per [guidelines/paragraph-numbering.md](../guidelines/paragraph-numbering.md).

---

## Chapters

| Chapter | Topic | Plans |
|---------|-------|-------|
| [§1](plans/chapters/§1_framework-evolution.chapter.md) | Framework Evolution — structural changes to chevp-ai-framework itself | §1.1 |

---

## Active Plans

### Context (CTX)

_(none)_

### Exploration (EXP)

| ID | Status | Description |
|----|--------|-------------|
| [§1.1](plans/active/§1.1_thinking-learning-upgrade.exp.md) | active (awaiting `/approve`) | Framework upgrade — vom Execution- zum Thinking & Learning Framework. Adds uncertainty triplet, A/B-Exploration, Learning Loop, evidence-based gates, Challenger role, Kill Criteria, Gatekeeper subagents, Plan Proposal loop. Self-hosting pilot — see [insights](plans/active/§1.1_thinking-learning-upgrade.insights.md). |
| [§1.2](plans/active/§1.2_plugin-and-consumer-rollout.exp.md) | draft | Consumer rollout: update `hooks/`, `commands/`, and consumer repos (`chevp-workflow` etc.) to honour the new evidence block, gatekeepers, and proposal loop introduced in §1.1. |

### Production (PRD)

_(none)_

---

## Pending Plan Proposals

Spawned by Gatekeepers; awaiting human triage via `/promote`, `/defer`, or `/reject`.

| ID | Source Gate | Source Plan | Trigger | Suggested Type |
|----|-------------|-------------|---------|----------------|
| _(none yet — run `/gate-check G2` on §1.1 to populate)_ | | | | |

See [plans/proposals/README.md](plans/proposals/README.md) for the lifecycle.

---

## Maintenance

- Add new plans to the appropriate phase table when created
- Move plans from `active/` to `finished/` and remove from this registry when done
- Pending Proposals table is updated by Gatekeepers and `/promote` / `/reject` commands
- This registry is the entry point that Claude loads first to decide which plans to read for a given task
