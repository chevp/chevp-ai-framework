# Risks Template

> Context phase artifact (Step 1). Location: `context/risks.md` or per-task `context/<task>/risks.md`.
> Mode: Context

```markdown
---
name: <Short title>
type: risks
status: draft            # draft | confirmed
proposed-by: ai          # ai | human | pair
decided-by: —            # human (required at G1)
date: YYYY-MM-DD
---

# Risks — <Title>

## Where could we be wrong?
List concrete things that could turn out to be untrue about the problem, the user, the constraints, the technology, or the team's capability. Each risk is paired with what we would do about it.

| # | Risk | Likelihood | Cost if it bites | Mitigation / early signal |
|---|------|-----------|------------------|---------------------------|
| 1 | "The user does not actually need X" | high | abandon work, lose 2 weeks | interview before building |
| 2 | "Library Y does not scale to N items" | med | rewrite the data layer | benchmark in week 1 |

## Top-3 expensive failure modes
The three risks with the highest **cost × likelihood** product. These dictate where Exploration should put its first prototype.

1. ...
2. ...
3. ...

## Counter-evidence we are ignoring
Has anyone (a teammate, prior project, customer feedback) already suggested this approach is wrong? List the dissent explicitly so it cannot be silently dismissed.

## Risks we accept knowingly
Risks we have evaluated and chosen to live with — with the reason. This protects future-you from re-litigating settled trade-offs.
```

## Minimum Substance

- At least **3 risks**, each with likelihood, cost, and mitigation
- Top-3 expensive failure modes called out separately — these drive Exploration priorities
- Either a "counter-evidence" section *or* an explicit "no dissent encountered" line — silence is suspicious

## How it relates to other Context artifacts

| Artifact | Relation |
|----------|----------|
| [problem-statement-template](problem-statement-template.md) | The problem whose framing might be wrong |
| [hypotheses-template](hypotheses-template.md) | Risks are the failure modes of the hypotheses |
| Plan `Risks` table | Risks here are wider (about the *direction*); plan-level risks are about the *execution* |
| Challenger output ([02-exploration/challenger.md](../02-exploration/challenger.md)) | Challenger reads this file and proposes additions before G2 |

## Anti-patterns

| Anti-pattern | Why it breaks the artifact |
|--------------|---------------------------|
| Generic risks ("schedule slip", "scope creep") | Apply to every project; carry no information |
| No likelihood / cost rating | Cannot be triaged; everything looks equally urgent |
| No mitigation column | Risks become anxiety, not action |
| Skipping counter-evidence | Confirmation bias gets baked into the plan |
