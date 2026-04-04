# Production-Plan Template

> For the Production phase (Step 3). Location: `context/plans/PRD-NNN-<description>.md`
> Mode: Production

```markdown
---
id: PRD-NNN
type: PRD
status: draft            # draft | proposed | approved
proposed-by: ai          # ai | human | pair
decided-by: —            # human (required before implementation begins)
approved-by: —           # human identifier
approved-at: —           # YYYY-MM-DD
implements: EXP-NNN      # the G2-approved EXP plan
---

# PRD-NNN: <Production-Plan Title>

## Reference
- Feature Plan: `EXP-NNN-<description>.md` (approved at G2)
- Prototype: <reference if applicable>

## Implementation Scope
Which steps from the G2 plan will be implemented in this production cycle?

1. Step from G2 plan
2. Step from G2 plan
3. ...

## Affected Files
- `path/to/file.ext` — What will be changed

## Validation Strategy
- [ ] Build verification after each step
- [ ] Test execution: <which tests>
- [ ] Visual comparison: <if applicable>
- [ ] Acceptance criteria check (from G2 plan)

## Risks
- Risk 1 → Mitigation

## Constraints
- No scope expansion beyond the approved G2 plan
- Implementation order as listed above
```

## Naming Convention

- Open: `PRD-NNN-<description>.md` (three digits, sequential)
- Completed: `finished/PRD-FNNN-<description>.md`

## Abbreviation

For trivial changes (< 10 lines), a one-line Production-Plan is sufficient: `Implements EXP-NNN`. Human must still approve before implementation begins.

## Provenance

Frontmatter governed by [architecture-governance](../guidelines/architecture-governance.md). Production code writes are blocked by [hooks/provenance-check.py](../hooks/provenance-check.py) unless this plan is `status: approved` with `approved-by` filled (via `/approve PRD-NNN`).
