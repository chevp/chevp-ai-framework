# SDLC in Production

> The plan is the plan, nothing more and nothing less.

## Responsibilities

- Govern the implementation-validation-delivery cycle
- Enforce step-by-step execution
- Manage backward jumps when corrections are needed

## Prerequisites

Before starting Production, verify:
- G1 deliverables exist (System Spec, Architecture, ADRs)
- G2 deliverables exist (Feature plan/spec approved, prototype confirmed where applicable)

If anything is missing: **stop and go back** to the appropriate step.

## Rules

1. **One step at a time** — Not everything at once
2. **Build after each step** — Does it still compile?
3. **Minimal changes** — Only what the plan specifies
4. **No scope expansion** — The plan is the plan
5. **Validate before delivery** — Every acceptance criterion checked

## Backward Jumps

- **Small correction**: Fix in Production, validate again
- **Plan is wrong**: Back to Exploration, adjust plan
- **Fundamental problem**: Back to Context, re-evaluate

## Validation Methods

| Method | When |
|--------|------|
| Build verification | Always |
| Preview comparison | For visual or physical output |
| Spec comparison | Always (check all acceptance criteria) |
| Tests | When test suite exists |
| Manual review | For complex logic |

## AI Behavior

### MUST
- Verify G1 and G2 deliverables exist before starting
- Proceed step by step according to plan
- Verify build success after each step
- Check each acceptance criterion individually
- Stop and ask the human when blocked

### MUST NOT
- Start Production without approved plan/spec from Exploration
- Implement out of order
- Skip validation
- Deliver without human approval
- Batch multiple unrelated changes

## Checklist

- [ ] G1 and G2 deliverables verified
- [ ] Implementation follows the plan step by step
- [ ] Build verified after each step
- [ ] All acceptance criteria checked
- [ ] Human has approved the result
