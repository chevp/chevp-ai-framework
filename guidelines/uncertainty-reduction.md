---
name: Uncertainty Reduction
description: Every step in the lifecycle must measurably reduce uncertainty before the team is allowed to advance
type: guideline
---

# Guideline: Uncertainty Reduction

**Rule:** Every transition between lifecycle steps must reduce uncertainty by a *named, recorded amount*. The framework's purpose is not to ship code — it is to reach the moment when shipping code is the *least uncertain remaining option*. Plans that do not reduce uncertainty are blocked at their gate.

**Why:** Without this rule, the lifecycle decays into a build pipeline that ships features regardless of whether the team actually understands the problem. The Context phase becomes a checklist, Exploration becomes prototype-theatre, and Production becomes the only step where reality intrudes — too late. By contrast, when each step is required to *retire a hypothesis*, *kill an assumption*, or *measure a risk*, the cost of being wrong is paid early when it is cheap.

**How to apply:**
1. At every step, name the uncertainty you intend to reduce *before* you start work
2. At every gate, record what was actually reduced in the plan's `evidence:` block
3. The Gatekeeper subagents block transitions where the recorded reduction is empty, generic, or only restates the plan's Goal
4. Backward jumps are not failures — they are the system working as intended when uncertainty *increases*

## What "uncertainty" means here

| Type | Where it lives | How it gets reduced |
|------|---------------|---------------------|
| **About the problem** | [problem-statement](../templates/problem-statement-template.md) | Reading, interviews, observing existing users |
| **About the approach** | [hypotheses](../templates/hypotheses-template.md) | Prototypes, benchmarks, side-by-side comparisons |
| **About what could go wrong** | [risks](../templates/risks-template.md) | Cheap failure-mode tests, counter-evidence search |
| **About the implementation** | EXP plan + Production-Plan | Acceptance criteria, validation runs |

The lifecycle starts with the maximum amount of uncertainty across all four types and tries to reach the gate where the *cheapest remaining way to learn more* is to actually ship and measure.

## Per-step contract

| Step | Must reduce | Recorded in |
|------|------------|-------------|
| **Context** | Uncertainty about *what* the problem is and *who* has it | Problem Statement, Hypotheses, Risks, evidence block in CTX plan |
| **Exploration-A** | Uncertainty about *whether the problem framing is right* | Updated Hypotheses (some marked `confirmed` / `killed`), `insights.md` |
| **Exploration-B** | Uncertainty about *which solution is best* | Side-by-side prototype comparison, ADR, `insights.md`, Challenger output |
| **Production** | Uncertainty about *whether the chosen solution actually ships and behaves* | Validation results, updated `insights.md`, regression checks |

A step that "completes" without reducing its assigned uncertainty is incomplete. The Gatekeeper subagent reads the `evidence:` block and the linked artifacts and refuses to issue `pass` if the reduction is unrecorded or boilerplate.

## Evidence Block — the operational form of this rule

The frontmatter `evidence:` block is the recording mechanism:

```yaml
evidence:
  hypothesis: "We believed users would prefer X over Y because Z"
  result: "Side-by-side prototype with 5 users — 4/5 preferred Y, citing Z'"
  reasoning: "Hypothesis refuted; switching to Y. Insights file logged. Proceeding to Production with Y."
```

The block is *not* a summary. It is an *uncertainty ledger entry*. Three things must be true:

1. **`hypothesis`** names a belief the team *could have been wrong about*
2. **`result`** is something *observable*, not an opinion
3. **`reasoning`** is the bridge from result to action — and the action is *one of: proceed, fall back, kill*

A block where `hypothesis` is "we want to add feature X" fails because *wanting to add a feature* is not a hypothesis. A block where `result` is "the team agreed" fails because *agreement* is not an observation.

## Kill Criteria — uncertainty's exit door

The plan-template `Kill Criteria` section is the explicit complement to this rule. Kill criteria answer: *what evidence would tell us this plan should not advance?* Without kill criteria, uncertainty has no escape valve and plans accumulate like sunken cost.

See [plan-granularity](plan-granularity.md) for the rule that every plan must define kill criteria.

## Anti-patterns

| Anti-pattern | Why it breaks the rule |
|--------------|------------------------|
| Treating Context as documentation | Documentation does not reduce uncertainty unless the act of writing it forces the team to confront what they did not know |
| Skipping Exploration-A and going straight to building | The team has *assumed* the problem framing instead of testing it |
| Approving G2 with empty `evidence:` block | Approval is no longer attached to evidence — rubber-stamp returns |
| Plans without kill criteria | No exit ramp — the team works past the point where evidence has refuted them |
| Insights files written *after* G2 approval | Story retro-fitted to the decision; no actual learning occurred |
| One hypothesis only in `hypotheses.md` | Pretending to explore but already decided |
| Risks marked all "low" | Either the team is in denial or has not actually thought about risks |
| Generic Challenger output ("schedule slip") | The Challenger has not engaged with the specific proposal — failure of the role |

## Relation to other guidelines

| Guideline | Relation |
|-----------|----------|
| [architecture-governance](architecture-governance.md) | Provenance answers *who*; this guideline answers *on what basis* |
| [plan-granularity](plan-granularity.md) | Defines plan structure; this guideline defines what must change between plans |
| [ai-collaboration](ai-collaboration.md) | Defines the Challenger and Learning Loop as the operational mechanisms of uncertainty reduction |
