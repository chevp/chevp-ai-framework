---
name: create-prd-plan
description: Use when an approved EXP plan is ready to be implemented and a Production-Plan (PRD) is needed, or when the user says "PRD plan", "production plan", "produce", "implement EXP-NNN", "draft PRD". Produces a PRD per the chevp-ai-framework template.
---

# Create Production-Plan (PRD)

Step 3 artifact: captures HOW the approved EXP plan will be implemented — execution scope, affected files, validation strategy, and kill criteria.

## Prerequisite

G2 must be passed for the EXP plan being implemented. Before creating, verify via the `gate-validator` subagent (`gate=G2`) or `gatekeeper-g2`. If G2 is not passed, block and redirect to `/explore`.

## Steps

1. **Read the template**: [templates/production-plan-template.md](../../templates/production-plan-template.md).
2. **Read the Production step guide**: [03-production/README.md](../../03-production/README.md) and [03-production/ai-plans.md](../../03-production/ai-plans.md).
3. **Identify the EXP plan being implemented** (must be `status: approved`). Capture its id for the `implements:` field.
4. **Determine the project's plan location** from the project's CLAUDE.md (typical: `context/plans/`).
5. **Assign the next PRD number** by scanning existing plans (`PRD-NNN`, three digits).
6. **Draft** the plan with:
   - Reference to EXP plan and (if any) prototype
   - **Implementation Scope** — the steps from the EXP plan to be executed in this cycle
   - **Affected Files** — concrete paths and what changes
   - **Validation Strategy** — build, tests, acceptance criteria from EXP
   - **Risks → Mitigations**
   - **Constraints** — no scope expansion, implementation order
   - **Kill Criteria** — when to abort and fall back to Exploration (mandatory; see `guidelines/uncertainty-reduction.md`)
   - `evidence:` block — pre-fill `hypothesis` from the EXP plan; leave `result` and `reasoning` empty (filled at G3)
7. **Confirm** path, number, and content with the user before writing.

## Rules

- Status starts as `Draft`; becomes `Approved` only after `/approve PRD-NNN` is run by the human (provenance hook enforces this).
- For trivial changes (< 10 lines), a one-line PRD `Implements EXP-NNN` is allowed; the human still must approve.
- Never start implementation before the human approves the PRD — production-code writes are blocked by [hooks/provenance-check.py](../../hooks/provenance-check.py) until the PRD is approved.
- Never write the `decided-by:` or `approved-by:` fields yourself — those are human-only (see [guidelines/architecture-governance.md](../../guidelines/architecture-governance.md)).

## Output

A PRD plan file at the project's conventional path. Status `Draft` until the human runs `/approve PRD-NNN`. After approval, the AI may begin Step 3 implementation.
