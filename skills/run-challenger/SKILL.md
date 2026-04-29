---
name: run-challenger
description: Use before requesting G2 approval for an EXP plan, or when scope changes are proposed mid-Production (Rule 11 / Challenger role). Trigger phrases: "run challenger", "challenge this plan", "stress-test the approach", "draft the challenger block", "what could go wrong with this plan". Produces the four mandatory Challenger sections per [02-exploration/challenger.md].
---

# Run Challenger

The Challenger is the AI's internal sceptic. It moves friction *into* the AI — where it is cheap — instead of relying on the human's vigilance at the gate. The Challenger does not block; it makes the cost of being wrong visible *before* G2 is crossed.

## When to trigger

- **Mandatory** — Before AI requests G2 approval; plan is transitioning `draft` → `proposed` and has no `## Challenger` section yet
- **Conditional** — During Production when the human proposes a scope expansion
- **Optional** — During Context when `risks.md` is suspiciously thin (< 3 risks or all rated low)

## Prerequisite

The target EXP plan exists and has, at minimum, a stated approach, alternatives, and a `## Vision Alignment` section (or an explicit `—` with a reason). If those are missing, redirect to `create-exp-plan` first.

## Steps

1. **Read the role spec**: [02-exploration/challenger.md](../../02-exploration/challenger.md). The four mandatory sections and the *auto-fail* anti-patterns are defined there.
2. **Read source material**: the target EXP plan, its `hypotheses.md`, `risks.md`, related ADRs, and any prior approved plans this proposal builds on (for *decision continuity*).
3. **Draft the four sections** — each must be specific to *this* plan, not generic:
   - **Top-3 failure modes** — for each: what breaks (a concrete observable, not "things go wrong"), the cheapest signal that would tell us early, what we would do
   - **Two alternative approaches** — sketch (3–5 lines), why rejected, the condition under which we would re-open
   - **Strongest counter-argument** — first-person, charitable, the sharpest reviewer's objection
   - **Product-coherence check** — vision fit, decision continuity, problem validation (measured vs. hypothetical)
4. **Self-check against the auto-fail patterns** before showing the user:
   - Generic failure modes ("schedule slip", "scope creep") → regenerate
   - Alternatives that are "do nothing" or "use a different framework" → regenerate
   - Strawman counter-argument → regenerate
   - "Fine, aligned, measured" coherence paragraph with no specifics → regenerate
   - Plan has no `## Vision Alignment` section → record this as a finding for G2; do not paper over it
5. **Place the output** in the plan file under `## Challenger`, or for very large plans in a sibling file `<plan-id>.challenger.md`.
6. **Confirm** the draft with the user before writing.

## Rules

- The Challenger does **not** issue verdicts — that is the Gatekeeper agents' job. The Challenger surfaces the cost of being wrong; the human decides.
- Code review is **not** the Challenger's job — that happens at G3 against acceptance criteria.
- The Challenger is **not** the human's voice — humans review Challenger output, they do not write it.
- If a prior Challenger failure mode came true during Production, append it to `insights.md` (`write-insights` skill) — the loop closes.

## Output

A `## Challenger` block (in the plan, or a sibling file for very large plans) containing all four sections, each non-generic and concretely tied to the plan. The Gatekeeper checks both existence and substance before issuing G2 `pass`.
