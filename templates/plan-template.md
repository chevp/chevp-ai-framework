# Plan Template

> For concrete implementation tasks. Location: `context/plans/<TYPE>-NNN-<description>.md`
> See [plan-granularity](../guidelines/plan-granularity.md) for sizing rules, type selection, and dependency management.

```markdown
# <TYPE>-NNN: <Plan Title>

## Type: <CTX|EXP|PRD>
## Status: draft
## Depends-on: —
## Blocks: —

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

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2
```

## Minimum Substance

A plan must contain all five sections above (Goal, Scope, Steps, Affected Files, Acceptance Criteria) to pass G2. Plans missing any element are notes, not plans. See [plan-granularity](../guidelines/plan-granularity.md).

## Naming Convention

- Format: `<TYPE>-<NNN>-<description>.md` (TYPE: CTX, EXP, or PRD)
- Open plans: `context/plans/<TYPE>-NNN-<description>.md`
- Completed: `context/plans/finished/<TYPE>-NNN-<description>.md`
