---
name: Paragraph Numbering
description: Hierarchical §-numbering for plans — stable, tree-structured IDs organized by chapters
type: guideline
---

# Guideline: Paragraph Numbering (§-System)

**Rule:** Every plan receives a stable, hierarchical **§-number** (`§1.2.3`) that reflects its position in a chapter tree. Plans are organized by thematic chapters, not by creation order. §-numbers are never reused and follow strict tree rules.

**Why:** Sequential IDs like `EXP-042` give no structural context — you cannot tell at a glance which area of the project a plan belongs to. A hierarchical §-number groups related plans by domain, makes cross-references meaningful, and scales to large projects with hundreds of plans.

**How to apply:** Define project-specific chapters in `context/plans/chapters/`. Assign each new plan the next free §-number within its chapter. Use the §-number as the plan's primary identifier in registries, cross-references, commits, and code annotations.

---

## Concept

Like sections in a legal code, each plan gets a **stable, hierarchical number** under which it is uniquely identifiable. The §-number serves as a documentation anchor — **not** as a runtime identifier.

```
§1      Top-level chapter (thematic area)
§1.2    Sub-chapter (topic within the area)
§1.2.3  Concrete plan (actionable work item)
```

---

## Hierarchy Rules

| Rule | Detail |
|------|--------|
| **Tree-structured** | New children are appended at the end. IDs do not need to be sequential (gaps are allowed), but must never be reused. No letter suffixes (e.g., `§6.3.1a`) — use the next free number instead |
| **Maximum 4 levels** | `§1.2.3.4` is the deepest allowed; if deeper is needed, split into a parallel chapter |
| **No leading zeros** | `§1.2.3`, not `§01.02.03` |
| **Numbers are never reused** | Deleted or deprecated plans retain their number as `DEPRECATED_*` so old references do not break |
| **Numbers may be reorganized** | §-numbers are documentation anchors, not runtime IDs — they may change during restructuring (unlike slugs) |

---

## Chapters

Chapters are the organizational backbone of the §-tree. They are **not** work plans themselves — they are orientation maps for the plans beneath them.

### Chapter Definition

Each chapter is a file in `context/plans/chapters/` with this structure:

- **Frontmatter**: `id`, `name`, `description`, `type: chapter`, `status`
- **Goal**: What this chapter area aims to achieve
- **Scope**: List of topics / sub-plans covered
- **Guiding Questions**: Key questions that plans in this chapter should answer

See [chapter-template](../templates/chapter-template.md) for the full template.

### Chapter Levels

| Level | Example | Meaning |
|-------|---------|---------|
| Top-level | `§1` | Major thematic area (e.g., Infrastructure, UI, Data) |
| Sub-chapter | `§1.2` | Topic within the area (e.g., Deployment, Auth) |
| Plan | `§1.2.3` | Concrete, actionable plan |
| Sub-plan | `§1.2.3.4` | Fine-grained task within a plan (use sparingly) |

Projects define their own top-level chapters based on their domain. There is no fixed chapter numbering — the structure must reflect the project's actual architecture.

---

## File Naming

### Plans

```
§<number>_<slug-with-hyphens>.<type>.md
```

- **Type suffix**: `.ctx.md` (Context) / `.exp.md` (Exploration) / `.prd.md` (Production) / `.task.md`
- **Example**: `§1.2.3_static-asset-server.exp.md`

### Chapters

```
§<number>_<slug-with-hyphens>.chapter.md
```

- **Example**: `§1.2_assets-deployment-and-serving.chapter.md`

### Common Rules

- Number is dot-separated, no leading zeros
- Underscore `_` separates number from slug
- Slug uses hyphens (`static-asset-server`)
- Maximum 4 hierarchy levels

---

## Frontmatter

Plans using §-numbering use this frontmatter schema:

```yaml
---
paragraph: §1.2.3
slug: static-asset-server
type: exp                # ctx | exp | prd | task
status: active           # active | finished | archived | deprecated
proposed-by: ai          # ai | human | pair
decided-by: —            # human (required when status advances past proposed)
approved-by: —           # human identifier
approved-at: —           # YYYY-MM-DD
---
```

The `paragraph` field replaces the sequential `id` field (e.g., `EXP-042`) from the flat numbering scheme. Both schemes are valid — projects choose one and use it consistently.

---

## Status Workflow

Plans move through status folders while retaining their §-number:

```
context/plans/
├── active/       ← currently being worked on
├── finished/     ← done, retained for reference
├── archived/     ← no longer relevant, but historically valuable
└── deprecated/   ← idea rejected, or replaced by another §
```

| Status | Folder | Meaning |
|--------|--------|---------|
| `active` | `active/` | Plan is in progress or queued |
| `finished` | `finished/` | Work is done, plan kept as reference |
| `archived` | `archived/` | No longer relevant, historical value only |
| `deprecated` | `deprecated/` | Rejected or superseded by another plan |

---

## Plan Registry

Each project maintains a `context/PLAN_REGISTRY.md` as a compact overview of all active plans. Claude loads this file first and opens only the plans relevant to the current task.

The registry groups plans by chapter (`§x.y`) and lists them by lifecycle phase (CTX / EXP / PRD).

See [plan-registry-template](../templates/plan-registry-template.md) for the full template.

---

## Cross-Referencing

### In Plans, ADRs, and Specs

Reference plans by §-number and title:

> "This change is part of §1.2.3 (Static Asset Server)."

### In Commits

Use the §-number in commit subjects for traceability:

```
feat(assets): add cache headers for §1.2.3_static-asset-server
```

### In Code Annotations

Use `@capability` or `@see` tags with the §-number:

```cpp
/**
 * @see §1.2.3 static-asset-server
 */
```

---

## Coexistence with Flat Numbering

The §-system and the flat `<TYPE>-NNN` system (see [plan-granularity](plan-granularity.md)) are both valid. Projects choose one scheme:

| Scheme | Best For | ID Example |
|--------|----------|------------|
| **Flat** (`TYPE-NNN`) | Small projects, few plans, simple structure | `EXP-042` |
| **§-numbering** | Large projects, many plans, thematic organization needed | `§1.2.3` |

A project must not mix schemes. The plan type (CTX/EXP/PRD) is always expressed — in flat numbering as a prefix, in §-numbering as the file suffix and frontmatter `type` field.

---

## Assigning New Numbers

1. Identify the chapter the plan belongs to (or create a new chapter if needed)
2. Find the highest existing number in that chapter
3. Use any unused number higher than existing ones — gaps are allowed (e.g., `§1.2.5` → `§1.2.7` is fine)
4. Never use letter suffixes (`§1.2.5a`) — always use a new numeric ID
5. Register the new plan in `PLAN_REGISTRY.md` and `plans/INDEX.md`

---

## Summary

| Rule | Purpose |
|------|---------|
| Hierarchical §-numbers | Groups plans by domain, not creation order |
| Chapter structure | Provides orientation and thematic organization |
| Stable numbers (never reused) | Old references remain valid |
| Status folders | Track plan lifecycle without renumbering |
| Plan Registry | Quick-access overview for AI and humans |
| File naming with § prefix | Plan identity visible in directory listings |
