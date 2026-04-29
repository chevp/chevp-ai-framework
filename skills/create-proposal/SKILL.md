---
name: create-proposal
description: Use when an out-of-scope item, Challenger-identified failure mode, or NOT-in-Scope row warrants its own future plan (Rule 12). Trigger phrases: "create proposal", "PROP for this", "open a proposal", "log this for later", "this is out of scope but worth tracking". Produces a `PROP-NNN` file per the plan-proposal template.
---

# Create Plan Proposal (PROP-NNN)

A Plan Proposal is the cheapest possible structured form a concern can take. It is **not** a plan — it is a backlog entry that the AI writes and the human triages via `/promote`, `/defer`, or `/reject`. Without proposals, every out-of-scope item disappears the moment a plan is approved (Rule 12).

## When to trigger

- A Gatekeeper subagent (G1/G2/G3) flagged a candidate while reviewing a plan
- A Challenger output identified a failure mode worth its own future plan
- A `NOT in Scope` row in a current plan describes work the team will need eventually
- User explicitly says: "open a proposal for X", "log PROP for this", "track this for later"

## Prerequisite

A *source plan* exists (CTX / EXP / PRD or a §-numbered chapter). Proposals must reference what produced them — generic proposals with no source are an anti-pattern.

## Steps

1. **Read the template**: [templates/plan-proposal-template.md](../../templates/plan-proposal-template.md).
2. **Identify the source** — which plan, Challenger output, or NOT-in-Scope row triggered this proposal? Capture the id or §-number for the `source-plan:` field.
3. **Determine the proposals folder** from the project's CLAUDE.md — typical: `context/plans/proposals/`.
4. **Assign the next PROP number** by scanning existing proposals across `proposals/`, `proposals/promoted/`, and `proposals/rejected/`. Never reuse an id, even from rejected proposals — the audit trail must hold.
5. **Draft** the proposal:
   - **Trigger** — quote the source NOT-in-Scope row, Challenger failure mode, or Gatekeeper finding
   - **Suggested Goal** — one sentence; the seed for the eventual plan's `## Goal`
   - **Why now / why later** — escalation vs. backlog, plus the condition under which "later" becomes "now"
   - **Suggested Kill Criterion** — when does this proposal become obsolete? *(mandatory — proposals without exit ramps are anti-pattern)*
   - **Estimated effort** — Tiny / Small / Medium / Large (gut check, not a commitment)
   - **Notes** — context the human will need when triaging
6. **Set frontmatter**:
   - `proposed-by: ai` (always — humans write plans, not proposals)
   - `source-gate: G1 | G2 | G3` if a Gatekeeper raised it; omit if human-requested
   - `suggested-type: ctx | exp | prd`
   - `status: pending-human-review`
   - Never write `decided-by:` — that is human-only.
7. **Confirm** path, id, and content with the user before writing.

## Rules

- Proposals are AI-proposed but **human-decided**. Never `/promote` a proposal autonomously — that is a human action.
- Cap of **5 proposals per Gatekeeper gate-check**. If more candidates exist, list the top 5 and roll the rest into a single Sammel-Notiz paragraph in the verdict report.
- Generic proposals ("we should clean up code") are anti-pattern — too vague to triage. Prefer a sharper proposal or none at all.
- Rejected proposals may be re-opened only by an explicit human action; the AI does not resurrect them.
- After 90 days `pending-human-review`, the G1 review process auto-defers a proposal — note this in the proposal's `notes` if it is borderline urgent.

## Output

A `PROP-NNN_<slug>.md` file in `context/plans/proposals/`, status `pending-human-review`. The Gatekeeper / governance log records its creation; the human decides next via `/promote`, `/defer`, or `/reject`.
