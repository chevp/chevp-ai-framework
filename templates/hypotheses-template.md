# Hypotheses Template

> Context phase artifact (Step 1). Location: `context/hypotheses.md` or per-task `context/<task>/hypotheses.md`.
> Mode: Context

```markdown
---
name: <Short title>
type: hypotheses
status: draft            # draft | confirmed
proposed-by: ai          # ai | human | pair
decided-by: —            # human (required at G1)
date: YYYY-MM-DD
---

# Hypotheses — <Title>

## Assumptions about the problem
What must be true for the problem statement to hold? Each assumption is testable in principle, even if you cannot test it now.

| # | Assumption | Confidence | How could we test it? |
|---|-----------|------------|----------------------|
| 1 | ... | high / med / low | observation, interview, prototype, log query, ... |

## Hypothesised solutions
What approaches *might* solve the problem? List multiple — at least two — so the team has something to compare.

| # | Hypothesis | Cheapest test | Kill criterion |
|---|-----------|--------------|----------------|
| 1 | "If we do X, then Y happens, because Z" | A 1-hour prototype, a query, ... | What evidence would make us drop this? |

Each hypothesis follows the form **"If we do X, then Y, because Z"** — without the *because*, it is a guess, not a hypothesis.

## What we deliberately do NOT yet assume
Things the team has been tempted to assume but explicitly refuses to commit to until evidence arrives. Listing them prevents silent drift.
```

## Minimum Substance

- At least **2 hypothesised solutions** (single-option hypotheses are predetermined conclusions, not exploration)
- Every assumption rated `high / med / low` confidence
- Every hypothesis has a **cheapest test** and a **kill criterion** — without these, the hypothesis cannot be retired and Exploration becomes infinite

## How it relates to other Context artifacts

| Artifact | Relation |
|----------|----------|
| [problem-statement-template](problem-statement-template.md) | The problem this hypothesis attempts to solve |
| [risks-template](risks-template.md) | What goes wrong if the hypothesis is false |
| `insights.md` (post-Exploration) | Records which hypothesis was confirmed / killed |

## Anti-patterns

| Anti-pattern | Why it breaks the artifact |
|--------------|---------------------------|
| One hypothesis only | Pretends to explore but already decided |
| Hypotheses without `because` | Indistinguishable from gut feel; cannot be falsified |
| No kill criterion | Pet ideas survive forever; Exploration never converges |
| Listing every brainstormed idea | Noise; prefer 2–4 well-formed hypotheses |
