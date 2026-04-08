# Plan Registry Template

> Compact overview of all active plans. Location: `context/PLAN_REGISTRY.md`
> Claude loads this file first and opens only the plans relevant to the current task.
> See [paragraph-numbering](../guidelines/paragraph-numbering.md) for the §-numbering convention.

```markdown
# Plan Registry

Compact overview of all active plans in `context/plans/`.
Plans are grouped by chapters (§x.y) — see [plans/chapters/](plans/chapters/README.md).

---

## Active Plans

### Context (CTX)

| ID | Status | Description |
|----|--------|-------------|
| §x.y.z | active | Short description |

### Exploration (EXP)

| ID | Status | Description |
|----|--------|-------------|
| §x.y.z | active | Short description |

### Production (PRD)

| ID | Status | Description |
|----|--------|-------------|
| §x.y.z | active | Short description |

---

## Chapter Overview

| Chapter | Topic | Plans |
|---------|-------|-------|
| §1.1 | <Topic> | §1.1.1, §1.1.2 |
| §1.2 | <Topic> | §1.2.1, §1.2.2, §1.2.3 |

---

## In Progress

(Plans currently in status `in-progress` — status is maintained in the plan file itself.)
```

## Conventions

- The registry is a **flat overview**, not a detailed description — one line per plan
- Group plans by lifecycle phase (CTX / EXP / PRD) for quick scanning
- The Chapter Overview maps chapters to their constituent plans
- Keep the registry in sync when plans are created, finished, or deprecated
- AI reads this file as entry point — it should be sufficient to identify which plans to load for a given task

## Maintenance

- When creating a new plan: add it to the appropriate phase table and chapter overview
- When finishing a plan: remove it from Active Plans (it remains in `plans/INDEX.md` with status tag)
- When deprecating: remove from registry, mark in `plans/INDEX.md` as deprecated
- Optional: use a rebuild script (`context/plans/_rebuild_index.py`) to regenerate from filenames
