# Step 2: Exploration

> Think first, see first — then build.

Exploration runs in **two sub-modes**, in this order:

| Sub-mode | Goal | Fidelity | Output |
|----------|------|----------|--------|
| **Exploration-A — Problem Exploration** | *Understand* the problem in motion | Low (sketches, throwaway scripts, paper, single-screen demos) | A confirmed framing of the problem — and a *retired* hypothesis or two |
| **Exploration-B — Solution Exploration** | *Decide* between concrete solutions | High enough to compare (≥2 candidates side-by-side) | A chosen approach with documented trade-offs |

A plan declares which sub-mode it is in via the frontmatter field `exploration-mode: A | B`. Skipping A and going straight to B is allowed only when the [hypotheses](../templates/hypotheses-template.md) artifact already records the problem framing as `confirmed`.

## Goal

Plan concrete features, prototype them where applicable, and validate the approach before writing production code. System-level architecture is already established in Context — this step focuses on **feature-level** planning.

## When

After Context is complete (G1 passed). Always for features, architecture changes, and complex bugfixes. Can be verbal for trivial changes (< 10 lines).

## Inputs

- Confirmed scope from Context (G1)
- System Spec, Architecture document, ADRs from Context
- Existing code and conventions (from Context Inventory)
- Design references (if available)

## Mandatory Deliverables

| # | Deliverable | When Required | Sub-mode |
|---|-------------|---------------|----------|
| 1 | **Feature Plan/Spec** | Always (written for features/complex changes, verbal for trivial) | A and B |
| 2 | **ADR** | Only for new decisions arising during exploration | usually B |
| 3 | **UX Prototype (low-fidelity)** | Whenever the problem framing is uncertain | A |
| 4 | **UX Prototype (comparable)** | Mandatory for visual/physical output, ≥2 candidates side-by-side | B |
| 5 | **Challenger Output** | Always before G2 — see [challenger.md](challenger.md) | B |
| 6 | **`insights.md`** | Always at the end of Exploration — records what was learned | A and B |

## Activities

- Create feature plan or spec (depending on scope)
- Define steps, affected files, risks, acceptance criteria
- Create ADR if a new architectural decision is involved
- Create prototype for visual/UX work
- Iterate on prototype with human feedback
- Obtain **explicit human approval** before proceeding

## Outputs

- **Plan/Spec**: Written and approved (EXP-NNN-*.md or verbal confirmation)
- **ADR**: If a new architecture decision was made (not fundamental — those belong in Context)
- **Prototype**: Visual reference file(s) + human confirmation (where applicable)

## Roles Active in This Step

| Role | Responsibility |
|------|---------------|
| [SDLC](sdlc.md) | Spec + prototype governance, when to require what |
| [AI-Plans](ai-plans.md) | Feature plan/spec creation, acceptance criteria |
| [UX-Tooling](ux-tooling.md) | Prototype creation, preview feedback loop |
| [Software-Architecture](software-architecture.md) | ADR for new decisions, design alternatives |
| [Context-Engineering](context-engineering.md) | Storing specs/plans in context/ |

## Artifact Boundary

| Artifact | Context (Step 1) | Exploration (Step 2) |
|----------|-----------------|---------------------|
| System Spec (whole system) | Mandatory | — |
| Software Architecture | Mandatory | — |
| ADRs (fundamental decisions) | Mandatory | — |
| Feature Plan/Spec | — | **Mandatory** |
| ADRs (new decisions during exploration) | — | As needed |
| UX Prototype | — | **Mandatory** (where applicable) |

## Quality Gate G2: Exploration Complete

- [ ] Feature plan/spec exists with `exploration-mode: A | B` declared
- [ ] Steps are concrete enough for direct implementation
- [ ] Scope and non-scope are clearly defined
- [ ] **Kill Criteria** are defined (when do we abandon?)
- [ ] Risks and alternatives are documented
- [ ] Acceptance criteria are defined
- [ ] Prototype exists and is visually confirmed (where applicable)
- [ ] Insights from prototype have been fed back into spec (if needed)
- [ ] **`insights.md`** exists and is non-empty — at least one hypothesis confirmed/killed
- [ ] **Challenger output** present: Top-3 failure modes, ≥2 alternatives, strongest counter-argument
- [ ] **Evidence block** filled in plan frontmatter (`hypothesis` / `result` / `reasoning`)
- [ ] **Gatekeeper-G2 verdict** recorded (`pass` or `conditional-pass` with proposals filed)
- [ ] **Human has approved the plan/spec** (evidence-based, not rubber-stamp)

**BLOCKER: Do NOT proceed to [Production](../03-production/) until every checkbox is satisfied.**