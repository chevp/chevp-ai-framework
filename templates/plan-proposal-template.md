# Plan Proposal Template

> Lightweight artifact produced by Gatekeeper subagents (G1/G2/G3) when an out-of-scope item or challenger-identified failure mode warrants its own future plan. Location: `context/plans/proposals/PROP-NNN_<slug>.md`.
>
> A Plan Proposal is **not** a plan. It is a structured backlog entry that the Gatekeeper writes and the human triages via `/promote`, `/defer`, or `/reject`.

```markdown
---
id: PROP-NNN
type: proposal
proposed-by: ai          # always ai — humans write plans, not proposals
source-gate: G1 | G2 | G3
source-plan: <CTX/EXP/PRD-id or §-number>
suggested-type: ctx | exp | prd
suggested-chapter: §<x> or §<x.y>   # if §-numbering is used
status: pending-human-review        # pending-human-review | promoted | deferred | rejected
date: YYYY-MM-DD
---

# PROP-NNN: <Short title>

## Trigger
What out-of-scope item, risk, or challenger-identified failure mode produced this proposal? Quote the source plan if possible.

## Suggested Goal
What should a future plan accomplish? One sentence — this is the seed for `## Goal` of the eventual plan.

## Why now / why later
Should this be escalated immediately, or does it belong in the backlog? If "later", under what condition does it become "now"?

## Suggested Kill Criterion
When does this proposal become obsolete? (e.g., "if §1.1 ships and the issue does not actually surface", "if the dependency we worried about gets retired")

## Estimated effort
Tiny / Small / Medium / Large — best-effort gut check, not a commitment.

## Notes
Any additional context the human will need when triaging this proposal.
```

## Lifecycle of a Proposal

```
pending-human-review
    ├──→ /promote PROP-NNN  →  promoted    (becomes a real CTX/EXP/PRD plan; AI generates the stub)
    ├──→ /defer PROP-NNN    →  deferred    (stays in proposals/, gets reviewed before next G1)
    └──→ /reject PROP-NNN <reason>  →  rejected (moved to proposals/rejected/ with reason recorded)
```

A proposal may be re-opened from `rejected` only by an explicit human action — the AI may not resurrect rejected proposals on its own.

## Folder Layout

```
context/plans/proposals/
├── PROP-001_some-followup.md       ← pending or deferred
├── PROP-002_another.md
├── promoted/
│   └── PROP-003_now-§1.2.md        ← archive of promoted proposals (stub remains for traceability)
└── rejected/
    └── PROP-004_not-needed.md      ← archive with rejection reason in frontmatter
```

## Why proposals exist

Without this artifact, every out-of-scope item in a plan is *lost the moment the plan is approved*. Teams either widen plans to capture every concern (bloat) or silently drop concerns (drift). A Plan Proposal is the cheapest possible structured form a concern can take — small enough that the Gatekeeper writes it for free, structured enough that the human can triage in a few seconds.

The 5-cap-per-gate-check (defined in the gatekeeper agents) prevents proposal-spam: when the gatekeeper finds more than 5 candidates, it lists the top 5 and rolls the rest into a single Sammel-Notiz paragraph in the verdict report.

The 90-day auto-defer rule (enforced at G1 review time) prevents the proposal backlog from growing without bound: any proposal still `pending-human-review` after 90 days is automatically moved to `deferred`.

## How proposals relate to other artifacts

| Artifact | Relation |
|----------|----------|
| Source plan | The plan whose `NOT in Scope` (or Challenger output) produced this proposal — referenced via `source-plan` |
| `governance-log.md` | Promotion / rejection events are appended (not pending or deferred) |
| `PLAN_REGISTRY.md` | Active proposals appear in a separate "Pending Proposals" section |
| Real plans (after promotion) | Promoted proposals become regular CTX/EXP/PRD plans and stop being proposals |

## Anti-patterns

| Anti-pattern | Why it breaks the artifact |
|--------------|---------------------------|
| Gatekeeper spawns >5 proposals per check | Spam — break the rule, lose signal |
| AI promotes a proposal on its own | Promotion is a human decision — proposals are AI-proposed but human-decided |
| Reusing a proposal id after rejection | Audit trail breaks |
| Proposal without `suggested-kill-criterion` | Backlog item without an exit ramp; will haunt the team forever |
| Generic proposals ("we should clean up code") | Should not have been raised — too vague to triage |
