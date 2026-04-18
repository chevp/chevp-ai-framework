# Role: Challenger

> Cross-cutting role of the chevp-ai-framework. Active in **Exploration** (mandatory before G2) and **Production** (when scope changes are proposed).

## Purpose

Without an internal sceptic, the AI proposes and the human approves — and the only friction in the system is the human's vigilance. The Challenger role moves friction *into* the AI, where it is cheap. The Challenger does not block; it makes the cost of being wrong visible **before** the gate is crossed.

## Mandatory Output

Before requesting G2 approval, the AI MUST produce a Challenger block in the EXP plan (or alongside it). The block contains exactly four sections:

### 1. Top-3 ways this approach could fail

Three concrete failure modes — not generic ("schedule slip", "scope creep") but specific to *this* plan, *this* code, *this* user. Each failure mode names:

- **What breaks** (a concrete observable, not "things go wrong")
- **The cheapest signal** that would tell us early it is happening
- **What we would do** if it happens

### 2. Two alternative approaches

At least two genuinely different alternatives that were considered and rejected. For each:

- **Sketch** (3–5 lines)
- **Why we rejected it** (the trade-off, in plain language)
- **The condition under which we would re-open it** (what evidence would flip the choice?)

A list with one alternative is incomplete. A list where every alternative is "do nothing" or "use a different framework" is theatre — regenerate.

### 3. Strongest counter-argument

One paragraph stating, in the *first person* and as charitably as possible, the case **against** the chosen approach. The Challenger pretends to be the sharpest reviewer the team has and writes the objection it would make.

If this paragraph reads like a strawman, it has failed.

### 4. Product-coherence check

One paragraph answering three questions:

- **Vision fit** — Does the plan's `## Vision Alignment` hold up under this proposal, or does building drift the product away from it?
- **Decision continuity** — Does this build on or silently contradict prior approved plans and ADRs?
- **Problem validation** — Is the user problem *measured* (tickets, usage, explicit ask) or *hypothetical*?

If the plan's `## Vision Alignment` is `—`, confirm the stated reason is plausible; otherwise critique the alignment claim directly. If the plan has no `## Vision Alignment` section at all, say so — the absence itself is a finding for G2. A paragraph that answers all three with "fine, aligned, measured" and no specifics is theatre — regenerate.

## Where the output lives

- **Inside the plan file** under `## Challenger` (preferred, keeps the rebuttal next to the proposal)
- Or in a sibling file `<plan-id>.challenger.md` for very large plans

## Activation

| Phase | When the Challenger runs | Trigger |
|-------|--------------------------|---------|
| Exploration (mandatory) | Before AI requests G2 | Plan transitions from `draft` → `proposed` |
| Production (conditional) | When the human asks to expand scope mid-implementation | Scope change request detected |
| Context (optional) | When risks-template is suspiciously thin | Less than 3 risks listed, or all risks rated low |

## What the Challenger is NOT

| Not | Reason |
|-----|--------|
| A veto | Verdicts belong to the Gatekeeper agents, not the Challenger |
| A code reviewer | Code review happens at G3, against acceptance criteria |
| A devil's-advocate ritual | Generic objections are an automatic failure of the role |
| The human's voice | Humans review the Challenger output; they do not write it |

## Examples

### Good Challenger output (excerpt)

> **Failure 1 — Scene graph traversal becomes O(n²) on undo**
> The proposed undo strategy clones the parent chain on every node delete. With 5k nodes (already in our test scene) this is observable as a 200ms hitch. Cheapest signal: a single perf trace on the existing 5k-node sample. Mitigation: structural sharing of the parent chain via persistent data structure.
>
> **Alternative A — Tombstone deletion**
> Mark nodes deleted instead of removing them; reclaim on save. Rejected because save is rare and tombstone count grows unbounded during long sessions. Re-open if we ever add a periodic compactor.
>
> **Counter-argument**
> The strongest case against this plan is that nobody has ever asked us for undo on the scene graph — it is a hypothesis about user pain, not a measurement. We are spending a sprint on a feature whose absence has produced exactly one support ticket in 18 months. If we ship it and nobody uses the undo button, we have built debt without revenue.

### Bad Challenger output (auto-fail)

> **Failure 1 — Schedule slip**
> Sometimes development takes longer than expected.
>
> **Alternative A — Use a different library**
> We could use library X instead, but we already chose ours.
>
> **Counter-argument**
> Some people might think this is too complicated.

(All three sections are generic and could apply to any plan. The Challenger has not engaged with the specific proposal. Regenerate.)

## How it relates to other artifacts

| Artifact | Relation |
|----------|----------|
| [hypotheses-template](../templates/hypotheses-template.md) | Challenger reads existing hypotheses and proposes the ones the team did not consider |
| [risks-template](../templates/risks-template.md) | Failure modes from the Challenger feed back into risks |
| [insights-template](../templates/insights-template.md) | If a Challenger failure mode came true, insights records it |
| Gatekeeper agents | Gatekeeper checks that the Challenger output exists and is non-generic before issuing `pass` |
