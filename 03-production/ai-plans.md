# AI-Plans in Production

> Execute the plan, track progress, finalize.

## Responsibilities

- Track plan execution step by step
- Mark steps as complete during implementation
- Finalize the plan after successful delivery

## Plan Execution

Go through each step in the plan sequentially:

```
- [ ] Step 1 → Implemented? Build OK?
- [ ] Step 2 → Implemented? Build OK?
- [ ] Step 3 → Implemented? Build OK?
```

## Spec Comparison

Go through each acceptance criterion individually:

```
- [ ] Criterion 1 → Fulfilled? Where in the code?
- [ ] Criterion 2 → Fulfilled? Where in the code?
```

## Plan Finalization

After successful delivery:

```bash
mv context/plans/PLAN-NNN-<name>.md context/plans/finished/PLAN-FNNN-<name>.md
```

## AI Behavior

### MUST
- Track which plan steps are complete
- Verify each acceptance criterion explicitly
- Move plan to `finished/` after delivery

### MUST NOT
- Skip plan steps
- Mark criteria as fulfilled without verification
- Leave plans in active state after delivery

## Checklist

- [ ] All plan steps executed in order
- [ ] All acceptance criteria verified
- [ ] Plan moved to `finished/` (if plan-based)
