# Plan Template

> For concrete implementation tasks.
> See [plan-granularity](../guidelines/plan-granularity.md) for sizing rules, type selection, and dependency management.
> See [paragraph-numbering](../guidelines/paragraph-numbering.md) for §-numbering as an alternative to flat IDs.

## Flat Numbering (TYPE-NNN)

Location: `context/plans/<TYPE>-NNN-<description>.md`

```markdown
---
id: <TYPE>-NNN
type: <CTX|EXP|PRD>
status: draft            # draft | proposed | approved | superseded
proposed-by: ai          # ai | human | pair
decided-by: —            # human (required when status advances past proposed)
approved-by: —           # human identifier
approved-at: —           # YYYY-MM-DD
depends-on: —
blocks: —
exploration-mode: —      # A | B (only for EXP plans; A = problem, B = solution)
evidence:
  hypothesis: —          # what we believed before this gate
  result: —              # what we observed
  reasoning: —           # why that justifies the transition
---

# <TYPE>-NNN: <Plan Title>

## Goal
What should be achieved? (2–3 sentences, concrete and measurable)

## Context
Why is this needed? What existing systems are affected?

## Scope

### IN Scope
- What is included

### NOT in Scope
- What is explicitly excluded
- Cross-reference to other plans where boundaries overlap: "See EXP-063 for ..."

### REMOVED / Obsoleted
- What this change makes obsolete and therefore **deletes** (files, modules, fields, flags, dependencies)
- If nothing is removed, state "—" explicitly. Empty is not allowed.
- For each entry: *why* it is safe to remove (no remaining callers, replaced by X, unused since Y)

## Steps
1. Step 1
2. Step 2
3. ...

## Affected Files
- `path/to/file.ext` — What will be changed

## Risks
| Risk | Mitigation |
|------|------------|
| ... | ... |

## Kill Criteria
- When is this idea dead?
- What evidence (cost overrun, refuted hypothesis, blocking dependency) makes us NOT proceed to Production?
- A plan without kill criteria is a note, not a plan.

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2
```

## Minimum Substance

A plan must contain all six sections above (Goal, Scope, Steps, Affected Files, **Kill Criteria**, Acceptance Criteria) **and** a non-empty `evidence:` block before requesting its gate. The Scope section must have all three subsections filled — `REMOVED / Obsoleted` may be `—` only when the change is purely additive. Plans missing any element are notes, not plans. See [plan-granularity](../guidelines/plan-granularity.md) and [uncertainty-reduction](../guidelines/uncertainty-reduction.md).

## Provenance

The frontmatter provenance block (`proposed-by`, `decided-by`, `approved-by`, `approved-at`) is governed by [architecture-governance](../guidelines/architecture-governance.md). AI may only set `proposed-by`. A human sets the decision fields via `/approve <plan-id>`. A plan must be `status: approved` with `approved-by` filled before its gate is considered passed.

## Naming Convention

### Flat Numbering

- Format: `<TYPE>-<NNN>-<description>.md` (TYPE: CTX, EXP, or PRD)
- Open plans: `context/plans/<TYPE>-NNN-<description>.md`
- Completed: `context/plans/finished/<TYPE>-NNN-<description>.md`

---

## §-Numbering (Paragraph System)

Location: `context/plans/active/§<number>_<slug>.<type>.md`

For projects with many plans that benefit from thematic organization, use hierarchical §-numbering instead of flat IDs. See [paragraph-numbering](../guidelines/paragraph-numbering.md) for the full convention.

```markdown
---
paragraph: §<number>
slug: <slug-with-hyphens>
type: <ctx|exp|prd|task>
status: active           # active | finished | archived | deprecated
proposed-by: ai          # ai | human | pair
decided-by: —            # human (required when status advances past proposed)
approved-by: —           # human identifier
approved-at: —           # YYYY-MM-DD
exploration-mode: —      # A | B (only for exp plans; A = problem, B = solution)
evidence:
  hypothesis: —
  result: —
  reasoning: —
---

# §<number> <Plan Title>

## Goal
What should be achieved? (2–3 sentences, concrete and measurable)

## Context
Why is this needed? What existing systems are affected?

## Scope

### IN Scope
- What is included

### NOT in Scope
- What is explicitly excluded

### REMOVED / Obsoleted
- What this change makes obsolete and therefore **deletes** (files, modules, fields, flags, dependencies)
- If nothing is removed, state "—" explicitly. Empty is not allowed.
- For each entry: *why* it is safe to remove (no remaining callers, replaced by X, unused since Y)

## Steps
1. Step 1
2. Step 2
3. ...

## Affected Files
- `path/to/file.ext` — What will be changed

## Risks
| Risk | Mitigation |
|------|------------|
| ... | ... |

## Kill Criteria
- When is this idea dead?
- What evidence makes us NOT proceed?

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2
```

### §-Numbering Naming Convention

- Format: `§<number>_<slug-with-hyphens>.<type>.md`
- Active plans: `context/plans/active/`
- Finished: `context/plans/finished/`
- Archived: `context/plans/archived/`
- Deprecated: `context/plans/deprecated/`

Projects choose one scheme (flat or §) and use it consistently. See [paragraph-numbering](../guidelines/paragraph-numbering.md).
