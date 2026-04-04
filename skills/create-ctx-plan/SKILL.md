---
name: create-ctx-plan
description: Use when the user starts a new task and a Context-Plan (CTX) is needed, or when they say "context plan", "CTX", "start context step", or a new request arrives with no active plan. Produces a CTX plan per the chevp-ai-framework template.
---

# Create Context-Plan (CTX)

A Context-Plan kicks off Step 1 of the lifecycle. It captures WHAT must be understood before any exploration or coding happens.

## When to trigger

- New, unfamiliar task with no active plan
- User explicitly asks for a CTX / Context-Plan
- Before any `/explore` or `/produce` is allowed (G1 requires this artifact)

## Steps

1. **Read the template**: [templates/context-plan-template.md](../../templates/context-plan-template.md).
2. **Read the Context step guide**: [01-context/README.md](../../01-context/README.md) and [01-context/ai-plans.md](../../01-context/ai-plans.md).
3. **Determine the project's plan location** from the project's CLAUDE.md. Typical paths: `context/plans/`, `01-context/ctx-plans/`, or project-specific.
4. **Assign the next CTX number** (e.g. `CTX-003`) by scanning existing plans.
5. **Draft** the plan with:
   - Task goal and motivation
   - Scope boundaries (in / out of scope)
   - What must be read (files, specs, existing ADRs)
   - Questions that must be answered before G1 can pass
   - Expected deliverables for this CTX
6. **Confirm** path and draft content with the user before writing.

## Output

A CTX plan file at the project's conventional path, following the template exactly. The plan is `Draft` until the human confirms.
