---
description: Enter Context mode — read, verify, ask. No code changes allowed.
---

Switch to **Context** mode per [chevp-ai-framework LIFECYCLE](../LIFECYCLE.md#ai-modes).

Allowed in this mode:
- Read and verify artifacts
- Ask clarifying questions
- Create or update the Context-Plan (CTX)
- Produce System Spec, Software Architecture, fundamental ADRs, Context Inventory
- Confirm scope with the human

**NOT allowed**: code changes, feature plans, scope changes.

Before proceeding:
1. Check whether a CTX plan already exists for the current task. If yes, read it.
2. Read [01-context/README.md](../01-context/README.md) for the Context step deliverables.
3. If the user's request has a concrete task in mind, output a short Context-Plan draft using [templates/context-plan-template.md](../templates/context-plan-template.md).
4. Announce the mode with the Adaptive Mode-Awareness Header and list what is needed to pass **G1**.

Task from user (optional): $ARGUMENTS
