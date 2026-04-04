---
description: Validate a quality gate (G1, G2, or G3) against required deliverables.
argument-hint: G1|G2|G3
---

Run a gate validation for gate $ARGUMENTS (G1, G2, or G3).

Delegate this entirely to the `gate-validator` subagent. Pass the gate name and return the result:
- **PASSED** — list the satisfied criteria, propose the forward transition, wait for human approval.
- **FAILED** — list the specific missing prerequisites and what action is needed next.

Do not create or modify any artifacts during the check. This is a read-only validation.

See [LIFECYCLE.md — Quality Gates](../LIFECYCLE.md#quality-gates) for gate criteria.
