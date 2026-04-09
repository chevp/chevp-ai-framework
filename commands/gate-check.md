---
description: Validate a quality gate (G1, G2, or G3) against required deliverables.
argument-hint: G1|G2|G3
---

Run a gate validation for gate $ARGUMENTS (G1, G2, or G3).

Delegate this entirely to the matching specialised gatekeeper subagent:

| Argument | Subagent |
|----------|----------|
| `G1` | [gatekeeper-g1](../agents/gatekeeper-g1.md) — Context → Exploration |
| `G2` | [gatekeeper-g2](../agents/gatekeeper-g2.md) — Exploration → Production |
| `G3` | [gatekeeper-g3](../agents/gatekeeper-g3.md) — Production → Done |

Each gatekeeper returns a structured verdict:

- **`pass`** — list satisfied criteria, propose the forward transition, wait for human approval
- **`conditional-pass`** — criteria met, but Spawned Plan Proposals exist for out-of-scope items; human runs `/promote`, `/defer`, or `/reject` on each
- **`block`** — list specific missing prerequisites and the next action

Do not create or modify any artifacts during the check. This is a read-only validation.

See [LIFECYCLE.md — Quality Gates](../LIFECYCLE.md#quality-gates) for gate criteria and [guidelines/uncertainty-reduction.md](../guidelines/uncertainty-reduction.md) for the evidence-block requirement.
