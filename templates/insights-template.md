# Insights Template

> Exploration phase artifact (Step 2). Location: `context/plans/<plan-id>/insights.md` or alongside the EXP plan file.
> Mode: Exploration. Mandatory before G2.

```markdown
---
name: <Plan title> — Insights
type: insights
plan: <§-number or EXP-NNN>
status: draft            # draft | confirmed
proposed-by: ai          # ai | human | pair
decided-by: —            # human (required at G2)
date: YYYY-MM-DD
---

# Insights — <Plan Title>

## Hypotheses tested

| # | Hypothesis (from [hypotheses.md]) | Method | Result | Verdict |
|---|----------------------------------|--------|--------|---------|
| 1 | "If we do X, then Y, because Z"  | prototype / measurement / interview | what actually happened | confirmed / refuted / inconclusive |

## What surprised us
Things we did not expect — both positive and negative. Surprises are the most valuable data; document them even if they did not change the outcome.

## What we now believe
Replace the original hypotheses (or update [hypotheses.md] to mark them `confirmed` / `killed`). State the new working belief in one or two sentences.

## What we still do not know
Open questions that survived this Exploration. These either become new hypotheses for the next Exploration cycle or accepted unknowns rolling into Production.

## Consequence for the plan
- [ ] Plan unchanged — proceed to Production
- [ ] Plan adjusted — see version note in plan frontmatter
- [ ] Plan killed — see [Kill Criteria] section in the plan
- [ ] Falling back to Context — fundamental assumption broken
```

## Minimum Substance

- At least **one row** in *Hypotheses tested* with a non-empty `Result` and `Verdict`
- At least **one bullet** in *What we now believe*
- The *Consequence for the plan* checkbox is set (one of the four options)

An insights file with all four boxes still unchecked is incomplete — Exploration is not yet finished.

## Why this artifact exists

Without an explicit insights file, the framework's process becomes a one-way pipeline: Context → Exploration → Production. The lifecycle ships *output* but produces no *learning*. The insights file converts the linear pipeline into a loop:

```
Context → Exploration → insights.md → (Context again, or Production)
```

The lessons captured here feed back into [hypotheses.md] for the next iteration, or into [risks.md] as newly discovered failure modes.

## How it relates to other artifacts

| Artifact | Relation |
|----------|----------|
| [hypotheses-template](hypotheses-template.md) | Insights *update* hypotheses — confirm or kill |
| [risks-template](risks-template.md) | New surprises become new risks |
| Plan frontmatter `evidence:` block | The condensed claim/result/reasoning that the gatekeeper checks |
| Challenger output | If the challenger raised a failure mode that came true, record it here |

## Anti-patterns

| Anti-pattern | Why it breaks the artifact |
|--------------|---------------------------|
| Marking every hypothesis "confirmed" | Confirmation theater; surprises were ignored |
| Empty *What surprised us* section | Either nothing was learned or surprises were swept under |
| Insights written *after* G2 approval | Retro-fitting a story to a decision already made |
| Copy-paste from the plan's Goal | Plagiarising intent; insights must reflect outcome |
