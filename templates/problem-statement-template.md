# Problem Statement Template

> Context phase artifact (Step 1). Location: `context/problem-statement.md` or per-task `context/<task>/problem-statement.md`.
> Mode: Context

```markdown
---
name: <Short title>
type: problem-statement
status: draft            # draft | confirmed
proposed-by: ai          # ai | human | pair
decided-by: —            # human (required at G1)
date: YYYY-MM-DD
---

# Problem Statement — <Title>

## Who has the problem?
Which user, role, team, or system experiences the pain? Be specific — "users" is not an answer, "first-time editors who never opened the 3D viewport" is.

## What does not work today?
Describe the current state in observable terms. No solution language, no "we should". What does the user see, do, or fail to do?

## Why does it matter?
What is the cost of leaving it broken? Time wasted, decisions misled, money lost, users churned, risk accumulated? Quantify if possible.

## Why now?
What changed (deadline, regulation, customer pressure, new platform, scaling event) that makes this the right moment to solve it? If nothing changed, the problem may be a chronic itch — re-evaluate priority.

## Out-of-scope problems (intentionally)
List adjacent problems that look related but are explicitly NOT addressed here. Each one is a candidate for a separate plan or proposal.
```

## Minimum Substance

A problem statement is complete when **all five questions** above are answered in concrete terms — no abstract platitudes. If any answer is "we don't know yet", that uncertainty belongs in [hypotheses](hypotheses-template.md) or [risks](risks-template.md), not here.

## How it relates to other Context artifacts

| Artifact | Relation |
|----------|----------|
| [hypotheses-template](hypotheses-template.md) | What you *think* the problem causes / how it might be solved |
| [risks-template](risks-template.md) | Where you might be wrong about the problem itself |
| Context-Plan (CTX) | References this file as foundational input |
| System Spec | Is shaped by what this problem says is broken |

## Anti-patterns

| Anti-pattern | Why it breaks the artifact |
|--------------|---------------------------|
| Solution language ("we need to add a button") | Pre-decides Exploration; problem is no longer the subject |
| "Users want X" without naming the user | Untestable; produces features no one uses |
| Listing every adjacent issue | Scope-bloat; split into multiple problem statements |
| Skipping "Why now?" | Leads to features that ship into a vacuum |
