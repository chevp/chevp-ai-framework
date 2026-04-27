---
name: AskUserQuestion-First
description: Every question to the user is asked via AskUserQuestion with concrete clickable options — not as free-text prose
type: guideline
---

# Guideline: AskUserQuestion-First

**Rule:** Whenever the AI needs a decision, preference, or disambiguation from the human, it MUST use the `AskUserQuestion` tool with 2–4 concrete, mutually exclusive, clickable options. Free-text questions buried in prose are forbidden — including for non-gate matters such as scope clarification, mode disambiguation, library/approach choice, naming, refactor depth, or "should I continue?" checkpoints.

**Why:** The human's job in this framework is to decide, not to re-read explanations. Free-text questions force the human to scan a wall of text, mentally extract the choice, and reply in prose — which slows every loop and silently degrades to rubber-stamping. Clickable options compress the decision surface to its essential degrees of freedom and make trade-offs explicit. This is the same principle the framework already enforces for gates (evidence + verdict, not narrative) — applied to every interaction.

**How to apply:**

- **Default:** any user-facing question goes through `AskUserQuestion`. If the AI catches itself ending a paragraph with `?`, that is a violation — rewrite as an `AskUserQuestion` call.
- **Options must be concrete:** label ≤ 5 words, mutually exclusive, decision-shaped. No "Yes/No" pairs where one side is obviously wrong; no vague "Other / Custom" filler (the tool already provides "Other" automatically).
- **Recommend explicitly:** if the AI has a preferred option, it goes first and is suffixed with `(Recommended)`. The recommendation is the AI's job — leaving the human to guess violates Rule 5 (AI suggests, human decides).
- **Bundle related questions:** up to 4 questions in one call when they belong to the same decision (e.g. *approach* + *scope* + *enforcement*). Do not split related decisions across consecutive turns.
- **Trade-offs in `description`:** each option's `description` field carries the *why* — cost, risk, reversibility — so the human can decide without scrolling back.
- **Use `preview` for visual artefacts:** mockups, code snippets, diagram variants, config samples. Skip preview for plain preference questions.
- **Kept prose is allowed before the call:** one or two sentences of context to set up the decision is fine and often needed. The forbidden pattern is *prose-question instead of tool call*, not *prose-then-tool-call*.

## Scope

Applies to **all** user-facing questions in framework-driven work, including:

| Situation | Use AskUserQuestion |
|-----------|---------------------|
| Mode/intent ambiguous (Context vs. Exploration vs. Production) | ✅ |
| Scope clarification (which file, which feature, how deep) | ✅ |
| Approach choice (library, pattern, refactor depth) | ✅ |
| Gate decisions (G1 / G2 / G3 — alongside the evidence block, not replacing it) | ✅ |
| Plan-proposal triage (`/promote` vs. `/defer` vs. `/reject`) | ✅ |
| Naming / file-placement decisions | ✅ |
| "Should I continue?" / "Anything else before I proceed?" checkpoints | ✅ |

## When NOT to use

- **Reporting results** — finished work, diff summaries, status updates are statements, not questions.
- **Pure information requests from the human to the AI** — the human asks; the AI answers. The tool is for the reverse direction.
- **Internal AI deliberation** — the Challenger role critiques the plan inside the AI; it does not surface as a user question.
- **When there is genuinely no decision** — if only one viable path exists, take it and report. Don't manufacture a fake choice.

## Anti-Patterns

| Anti-Pattern | Why it fails | Better |
|--------------|--------------|--------|
| `"Should I use Postgres or SQLite? Postgres is more robust but heavier, SQLite is simpler but…"` (free-text) | Forces re-reading; ambiguous to answer | `AskUserQuestion` with two options + trade-offs in `description` |
| Single-option AskUserQuestion ("Confirm? → Yes / No") where No is meaningless | Theatre, not decision | Just proceed and report; or ask a real either/or |
| Splitting one decision across three consecutive turns | Adds latency, loses context | One `AskUserQuestion` call with multiple `questions` |
| Ending an `AskUserQuestion` call with a follow-up free-text question in the same response | Re-introduces the prose-question pattern | Bundle into the same call, or wait for the answer |
| "Other"-shaped filler option to look balanced | The tool adds "Other" automatically — manual ones add noise | Drop it; rely on the built-in fallback |

## Relation to other rules

- **Rule 2 (AI enforces, human decides):** clickable options are the mechanical form of "human decides".
- **Rule 5 (Ownership stays with the human):** the AI must still recommend; the human still chooses.
- **Rule 8 (Approval requires evidence):** for gate transitions, `AskUserQuestion` carries the *decision*; the `evidence:` block carries the *justification*. Both are required — neither replaces the other.
