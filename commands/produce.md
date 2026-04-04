---
description: Enter Production mode — implement the approved plan. No new plans, no scope changes.
---

Switch to **Production** mode per [chevp-ai-framework LIFECYCLE](../LIFECYCLE.md#ai-modes).

**Prerequisite**: G2 must be passed (Feature Plan/Spec approved, prototype confirmed where applicable, acceptance criteria defined, human approved).

Before switching:
1. Verify G2 by invoking the `gate-validator` subagent with `gate=G2`.
2. If G2 is NOT passed, block the transition, list missing prerequisites, redirect to `/explore`.
3. If G2 IS passed, create or load the Production-Plan (PRD) using [templates/production-plan-template.md](../templates/production-plan-template.md).

Allowed in this mode:
- Execute the approved plan exactly
- Run tests, verify builds, create commits
- Update documentation as specified in the plan

**NOT allowed**: new plans, scope expansion, unplanned changes.

**Fallback rule**: If during implementation the plan turns out to be incomplete, the approach unviable, or the scope changes — STOP, state the trigger, and propose a fallback to Exploration.

Announce the mode with the Adaptive Mode-Awareness Header and list what is needed to pass **G3**.

Task from user (optional): $ARGUMENTS
