# Production-Plan Template

> For the Production phase (Step 3). Location: `context/plans/PPLAN-NNN-<description>.md`
> Mode: `chp-production:`

```markdown
# PPLAN-NNN: <Production-Plan Title>

## Reference
- Feature Plan: `PLAN-NNN-<description>.md` (approved at G2)
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

- Open: `PPLAN-NNN-<description>.md` (three digits, sequential)
- Completed: `finished/PPLAN-FNNN-<description>.md`

## Abbreviation

For trivial changes (< 10 lines), a one-line Production-Plan is sufficient: `Implements PLAN-NNN`. Human must still approve before implementation begins.
