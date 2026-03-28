# Step 2: Exploration

> Think first, see first — then build.

## Goal

Plan the solution, prototype it where applicable, and validate the approach before writing production code.

## When

After Context is complete (G1 passed). Always for features, architecture changes, and complex bugfixes. Can be verbal for trivial changes (< 10 lines).

## Inputs

- Confirmed scope from Context (G1)
- Existing architecture docs, ADRs
- Design references (if available)

## Activities

- Create plan or spec (depending on scope)
- Define steps, affected files, risks, acceptance criteria
- Create ADR if architectural decision is involved
- Create prototype for visual/UX work
- Iterate on prototype with human feedback
- Obtain human approval before proceeding

## Outputs

- **Plan/Spec**: Written and approved (PLAN-NNN-*.md or verbal confirmation)
- **ADR**: If architecture decision was made
- **Prototype**: Visual reference file(s) + human confirmation (where applicable)

## Roles Active in This Step

| Role | Responsibility |
|------|---------------|
| [SDLC](sdlc.md) | Spec + prototype governance, when to require what |
| [AI-Plans](ai-plans.md) | Plan/spec creation, scope definition, acceptance criteria |
| [UX-Tooling](ux-tooling.md) | Prototype creation, preview feedback loop |
| [Software-Architecture](software-architecture.md) | ADR creation, design alternatives, trade-offs |
| [Context-Engineering](context-engineering.md) | Storing specs/plans in context/ |

## Quality Gate G2: Exploration Complete

- [ ] Plan/spec exists (as file or confirmed in chat)
- [ ] Steps are concrete enough for direct implementation
- [ ] Scope and non-scope are clearly defined
- [ ] Risks and alternatives are documented
- [ ] Human has approved the plan/spec
- [ ] Prototype exists and is visually confirmed (where applicable)
- [ ] Insights from prototype have been fed back into spec (if needed)

**Only proceed to [Production](../03-production/) after G2 is passed.**
