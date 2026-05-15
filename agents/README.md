# agents/

> Many small reviewers. One orchestrator. Friction lives in the AI, not in the human.

This folder defines the **agentic workflow** of `chevp-ai-framework`: the way the framework spreads review responsibility across many specialised sub-agents instead of asking one large LLM session — or one human — to do everything.

A standalone HTML version of this overview is published at <https://chevp.github.io/chevp-ai-framework/agents.html>.

## What is an agentic workflow?

A **single LLM session** that proposes, plans, prototypes, codes, reviews, audits and ships is doing too much at once. The same context window holds the proposal *and* the rebuttal — so the rebuttal is never very strong, and review collapses into rationalisation.

An **agentic workflow** splits that single session into:

- One **orchestrator** — the main AI the human talks to. Drives the conversation, owns the lifecycle, writes code (with human approval).
- Many **specialised agents** — sub-sessions with their own prompt, tools and read-only/read-write boundaries. Each one reviews a narrow slice with fresh eyes and returns a structured verdict. They do not see the orchestrator's history; only what is passed in.

The orchestrator integrates the verdicts and reports back to the human. **Specialised agents are read-only by default.** Only the orchestrator (with human approval) writes code or signs decisions.

## Why many small agents?

| Failure mode of a single big AI | What a narrow agent fixes |
|---|---|
| **Confirmation bias** — a model that just wrote the plan is the worst reviewer of that plan | Challenger lives in a separate sub-session and does not auto-defer |
| **Diluted attention** — long context with code, plans and ADRs cannot be deeply checked end-to-end | A narrow agent reads only what it needs — ten lines, with intent |
| **Unauditable verdicts** — free-form chat output cannot be diffed or replayed | Every agent emits a structured report (`pass` / `block` + findings) committable to the repo |

## The pattern

```
            Human
              │
              ▼
       Orchestrator AI         ← you talk to this one
              │
   ┌──────────┼──────────┬──────────┬──────────┬──────────┐
   ▼          ▼          ▼          ▼          ▼          ▼
Challenger  G1   G2   G3   arch-     gov-      ... your own ...
(sceptic)   gatekeepers    reviewer  auditor   security · perf · a11y · deps · …
```

## Roster — agents shipped with the framework

The framework ships **one cross-cutting role** (Challenger) and **six concrete agents**. The set is opinionated, not closed — see *Adding your own* below.

### Challenger — cross-cutting role

| Field | Value |
|---|---|
| Active in | Exploration (mandatory), Production (on scope-change), Context (optional, when risks are thin) |
| Trigger | EXP plan transitions `draft → proposed`; mid-Production scope-change request |
| Output | Four sections inside the EXP plan: top-3 failure modes, ≥2 alternatives, strongest counter-argument, product-coherence check |
| Auto-fail | Generic findings (*"schedule slip"*, *"scope creep"*, *"use a different library"*) — regenerate |
| Source | [`02-exploration/challenger.md`](../02-exploration/challenger.md) |

The internal sceptic. Before any G2 transition, the AI must engage with its own plan as the sharpest reviewer the team has. The Challenger does not *block* — verdicts belong to the Gatekeepers — but it makes the cost of being wrong visible **before** the gate is crossed.

### Gatekeepers — gate verdicts

Three specialised, read-only agents. Each one validates exactly one transition.

| Agent | Transition | Tools | Source |
|---|---|---|---|
| `gatekeeper-g1` | Context → Exploration | Read · Glob · Grep | [gatekeeper-g1.md](gatekeeper-g1.md) |
| `gatekeeper-g2` | Exploration → Production | Read · Glob · Grep | [gatekeeper-g2.md](gatekeeper-g2.md) |
| `gatekeeper-g3` | Production → Done | Read · Glob · Grep · Bash *(build only)* | [gatekeeper-g3.md](gatekeeper-g3.md) |

Common contract:

- Verdicts: `pass` / `conditional-pass` / `block`
- Out-of-scope items become `PROP-NNN` Plan Proposals (max 5 per gate-check; excess rolled into one *Sammel-Notiz* paragraph)
- Generic, boilerplate findings are forbidden — every finding must point to a concrete file and line
- Empty or generic `evidence:` blocks (`hypothesis` / `result` / `reasoning`) are an automatic `block`

What each gatekeeper specifically checks:

- **G1** — CTX-Plan, the *uncertainty triplet* (problem-statement / hypotheses / risks), System Spec, Software Architecture, fundamental ADRs, Context Inventory, scope confirmation, non-generic `evidence:` block.
- **G2** — EXP plan with `exploration-mode: A|B`, ≥3 implementation-ready steps, explicit Scope and NOT-in-Scope, **Kill Criteria**, ≥2 verifiable Acceptance Criteria, ≥2 Risks with mitigations, UX prototype, non-empty `insights.md`, **Challenger output that engages with this plan**, non-generic `evidence:` block.
- **G3** — every PRD acceptance criterion satisfied with evidence, build passes, docs updated, `insights.md` updated with implementation surprises (not just copied from G2), human-approval line in `governance-log.log`, **no code outside the approved PRD scope** (surprise refactors are an automatic block).

### architecture-reviewer — per-change review

| Field | Value |
|---|---|
| Tools | Read · Glob · Grep |
| Triggers | New pattern proposed, layer boundary crossed, ADR drafted |
| Output | `REVIEW · VERDICT · FINDINGS` with severity per finding (`info` / `warn` / `block`) |
| Source | [architecture-reviewer.md](architecture-reviewer.md) |

Reviews **individual changes** — a plan, a code diff, a new ADR — against the project's documented architecture invariants and accepted ADRs. Flags forbidden layer crossings, wrong dependency directions, and patterns that conflict with prior decisions. Does not invent invariants — if nothing is documented, it says so and proposes writing an ADR.

### governance-auditor — repo-wide drift detection

| Field | Value |
|---|---|
| Tools | Read · Glob · Grep |
| Triggers | `/governance-audit`; per release; after any ADR is accepted, superseded or deprecated |
| Output | Findings with severity `BLOCK` / `CONCERN` / `INFO` |
| Source | [governance-auditor.md](governance-auditor.md) |

Audits the **whole repository** for content-level drift against accepted ADRs and architecture invariants. Three mandatory checks:

1. **ADR-drift** — does code currently violate constraints declared by accepted ADRs?
2. **Undocumented patterns** — recurring code structures (≥3 occurrences) that have no binding ADR.
3. **Obsolete ADRs** — accepted ADRs whose subject has been removed from the codebase.

Where the architecture-reviewer is per-change at gate time, the auditor is repo-wide on demand.

### gate-validator — superseded

Backward-compatibility dispatcher. Older `/gate-check` invocations route through it; it forwards to the matching `gatekeeper-g1/g2/g3` and returns its output unchanged. New code should call the specialised gatekeepers directly. Source: [gate-validator.md](gate-validator.md).

## Where each agent activates

```
       Context  ─G1─▶  Exploration  ─G2─▶  Production  ─G3─▶  Done
                                                                 ▲
Challenger:               ✓ mandatory      ✓ on scope-change      │
gatekeeper-g1:    ✓ verdict                                       │
gatekeeper-g2:                       ✓ verdict                    │
gatekeeper-g3:                                              ✓ verdict
arch-reviewer:    on ADR     on plan                  on diff
gov-auditor:                                                ✓ periodic, repo-wide
```

The Gatekeepers gate **transitions**. The Challenger gates **thinking**. The architecture-reviewer gates **changes**. The governance-auditor gates **drift**.

## The output contract

Every agent returns a **structured verdict**, never free-form prose. Example G2 output:

```
GATEKEEPER: G2
PLAN: EXP-014-auth-refactor
VERDICT: conditional-pass

FINDINGS:
  - satisfied  exploration-mode declared:    context/plans/EXP-014.md:3
  - satisfied  Kill Criteria present:        §"Kill Criteria" non-empty
  - missing    Challenger product-coherence: no engagement with §Vision Alignment

EVIDENCE-BLOCK CHECK:
  - hypothesis: "session-token storage rewrite reduces compliance surface"
  - result:     "prototype confirmed on 2026-04-22"
  - reasoning:  "ship behind feature flag, dual-read 7d"

CHALLENGER CHECK:
  - failure-modes:     3, concrete
  - alternatives:      2, engaged
  - counter-argument:  engaged
  - product-coherence: rubber-stamp

SPAWNED PLAN PROPOSALS (max 5):
  - PROP-027: long-running session migration plan (suggested-type: prd)

NEXT ACTION: regenerate Challenger §4 (product-coherence) before requesting /approve EXP-014
```

Verdicts can be committed, replayed, and diffed across runs — that property is what turns review into **governance**.

## Adding your own agents

Anything that fits *"a narrow read-only review with a structured verdict"* can become an agent. Likely candidates for any non-trivial codebase:

| Agent | Reviews |
|---|---|
| `security-reviewer` | OWASP top-10, secret leaks, auth invariants |
| `perf-auditor` | O(n²) hot paths, missing indexes, N+1 queries |
| `accessibility-checker` | ARIA, contrast, keyboard nav, screen-reader paths in UI diffs |
| `doc-checker` | Public APIs touched by a PR are reflected in docs/CLAUDE.md |
| `dependency-watcher` | New deps, license conflicts, unmaintained packages |
| `test-coverage-reviewer` | Acceptance criteria from the PRD have at least one mapped test |
| `i18n-reviewer` | Hardcoded user-facing strings |
| `schema-migrator` | Migrations are reversible and safe on long-running tables |

A new agent is just a markdown file in this folder with frontmatter (`name`, `description`, `tools`) and an output contract.

## Design rules for new agents

1. **One agent = one job.** An agent that reviews "everything" returns nothing useful. Narrow scope makes verdicts strong.
2. **Read-only by default.** Verdicts are advisory. Only the orchestrator (with human approval) writes code or decisions. Bash is reserved for verification (running the build/tests) — never for modification.
3. **Structured output, not prose.** Verdicts must be diffable. *"Looks good"* / *"no issues"* without scope description is forbidden — every finding cites a path or a line.
4. **Generic findings auto-fail.** *"Schedule slip"*, *"scope creep"*, *"could be improved"* — if it could apply to any plan, it has not engaged with this one. Regenerate.
5. **Out-of-scope → proposal, never silence.** An agent that finds a tangent files a `PROP-NNN`; it does not expand its own scope (Rule 12).
6. **Cap output to 5 proposals.** Prevents proposal-spam. Excess goes into a single *Sammel-Notiz* paragraph.
7. **Don't invent invariants.** If nothing is documented, say so and propose writing an ADR — do not synthesise rules from your own taste.

## Relation to the rest of the framework

| Component | Relation to agents |
|---|---|
| [LIFECYCLE.md](../LIFECYCLE.md) | Defines the 3 steps and 3 gates the agents validate |
| [02-exploration/challenger.md](../02-exploration/challenger.md) | Specifies the Challenger role's mandatory output |
| [hooks/provenance-check.py](../hooks/provenance-check.py) | Mechanical, write-time guard. Agents are semantic, read-time |
| [guidelines/architecture-governance.md](../guidelines/architecture-governance.md) | Defines what *signed decisions* mean — the agents enforce the implications |
| [guidelines/uncertainty-reduction.md](../guidelines/uncertainty-reduction.md) | The reason gates require evidence and Kill Criteria |
| [commands/](../commands/) | `/gate-check`, `/governance-audit` etc. invoke these agents |

## Core rules referenced by this workflow

The agentic workflow is a direct consequence of [CLAUDE.md](../CLAUDE.md) Core Rules:

- **Rule 6** — Gates are blockers → Gatekeepers
- **Rule 8** — Approval requires evidence → mandatory `evidence:` block, checked by every gatekeeper
- **Rule 9** — Every Exploration produces learning → `insights.md` checked at G2 / G3
- **Rule 10** — Every plan can be killed → Kill Criteria checked at G2
- **Rule 11** — AI critiques itself → Challenger before G2
- **Rule 12** — Out-of-scope items become proposals, never disappear → all gatekeepers spawn `PROP-NNN`
