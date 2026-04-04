---
name: create-exp-plan
description: Use when a feature needs to be planned/designed in the Exploration step, or when the user says "EXP plan", "feature plan", "exploration plan", "design the feature". Produces an EXP plan/spec per chevp-ai-framework templates.
---

# Create Exploration-Plan (EXP)

Step 2 artifact: captures HOW the feature will be built, the chosen approach, risks, and acceptance criteria.

## Prerequisite

G1 must be passed. Before creating, verify via the `gate-validator` subagent (`gate=G1`). If G1 is not passed, block and redirect to `/context`.

## Steps

1. **Read templates**: [templates/plan-template.md](../../templates/plan-template.md) and [templates/spec-template.md](../../templates/spec-template.md).
2. **Read the Exploration step guide**: [02-exploration/README.md](../../02-exploration/README.md) and [02-exploration/ai-plans.md](../../02-exploration/ai-plans.md).
3. **Check** `guidelines/plan-granularity.md` (project-level override takes precedence) for size limits and plan type.
4. **Assign** the next EXP number by scanning existing plans.
5. **Draft** the plan with:
   - Problem statement and motivation (derived from CTX)
   - Chosen approach and considered alternatives
   - Scope (in / out)
   - Acceptance criteria (testable)
   - Risks and open questions
   - Required ADRs (new or referenced)
   - UX prototype requirement (Yes / No + reason)
6. **Confirm** path, number, and content with user before writing.

## Output

An EXP plan file. Status is `Draft` until human approves (required for G2).
