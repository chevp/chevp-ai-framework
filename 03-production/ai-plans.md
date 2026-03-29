# AI-Plans in Production

> Commit to scope, execute the plan, track progress, finalize.
> The AI enters Production mode automatically for this role. AI implements the approved plan. No new plans, no scope changes.

## Responsibilities

- Produce the **Production-Plan** and obtain human approval before writing any code
- Track plan execution step by step
- Mark steps as complete during implementation
- Finalize the plan after successful delivery

## Production-Plan (Mandatory Deliverable)

The Production-Plan is an execution commitment that must be created and approved by the human **before any code is written**. It answers:
- Which G2 plan is being implemented? (reference by ID)
- Which steps will be executed in this production cycle?
- Which files are affected?
- How will the result be validated?

For trivial changes (< 10 lines), a one-liner is sufficient: "Implements PLAN-NNN".

Template: [production-plan-template](../templates/production-plan-template.md)

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
mv context/plans/PPLAN-NNN-<name>.md context/plans/finished/PPLAN-FNNN-<name>.md
mv context/plans/PLAN-NNN-<name>.md context/plans/finished/PLAN-FNNN-<name>.md
```

## AI Behavior

### MUST
- Produce a Production-Plan and obtain human approval before writing any code
- Track which plan steps are complete
- Verify each acceptance criterion explicitly
- Move plans (PPLAN + PLAN) to `finished/` after delivery

### MUST NOT
- Start implementing without an approved Production-Plan
- Create new feature plans or specs (wrong mode — that belongs to Exploration)
- Expand scope beyond the approved G2 plan
- Skip plan steps
- Mark criteria as fulfilled without verification
- Leave plans in active state after delivery

## Checklist

- [ ] Production-Plan exists and is approved by human
- [ ] All plan steps executed in order
- [ ] All acceptance criteria verified
- [ ] Plans moved to `finished/` (PPLAN + PLAN)
