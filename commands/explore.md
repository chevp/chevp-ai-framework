---
description: Enter Exploration mode — plan, design, prototype. No production code.
---

Switch to **Exploration** mode per [chevp-ai-framework LIFECYCLE](../LIFECYCLE.md#ai-modes).

**Prerequisite**: G1 must be passed (Context-Plan confirmed, System Spec + Architecture + ADRs + Context Inventory exist, scope confirmed).

Before switching:
1. Verify G1 by invoking the `gate-validator` subagent with `gate=G1`.
2. If G1 is NOT passed, block the transition, list the missing prerequisites, and redirect the user to `/context`.
3. If G1 IS passed, enter Exploration mode.

Allowed in this mode:
- Create Feature Plan / Spec (EXP) using [templates/plan-template.md](../templates/plan-template.md) and [templates/spec-template.md](../templates/spec-template.md)
- Write ADRs for new decisions using [templates/adr-template.md](../templates/adr-template.md)
- Iterate UX prototypes using [templates/ux-prototype-template.md](../templates/ux-prototype-template.md)
- Document risks, alternatives, acceptance criteria

**NOT allowed**: production code, unilateral scope expansion.

Announce the mode with the Adaptive Mode-Awareness Header and list what is needed to pass **G2**.

Task from user (optional): $ARGUMENTS
