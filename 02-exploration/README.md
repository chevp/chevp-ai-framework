# Step 2: Exploration

> Think first, see first — then build.

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

| # | Deliverable | When Required |
|---|-------------|---------------|
| 1 | **Feature Plan/Spec** | Always (written for features/complex changes, verbal for trivial) |
| 2 | **ADR** | Only for new decisions arising during exploration |
| 3 | **UX Prototype** | Mandatory for visual/physical output |

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

- [ ] Feature plan/spec exists (as file or confirmed in chat)
- [ ] Steps are concrete enough for direct implementation
- [ ] Scope and non-scope are clearly defined
- [ ] Risks and alternatives are documented
- [ ] Acceptance criteria are defined
- [ ] Prototype exists and is visually confirmed (where applicable)
- [ ] Insights from prototype have been fed back into spec (if needed)
- [ ] **Human has approved the plan/spec**

**BLOCKER: Do NOT proceed to [Production](../03-production/) until every checkbox is satisfied.**