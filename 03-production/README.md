# Step 3: Production

> Build, verify, ship — nothing more, nothing less.
> The AI enters Production mode when the user requests implementation of an approved plan. In this mode, AI implements the approved plan. No new plans, no scope changes.

## Goal

Write production-ready code that follows the plan, validate it against the spec and prototype, and deliver it cleanly.

## When

After Exploration is complete (G2 passed). Plan/spec is approved, prototype is confirmed (where applicable).

## Prerequisites (from prior steps)

- **From Context (G1)**: System Spec, Architecture, ADRs, Context Inventory — all verified
- **From Exploration (G2)**: Feature plan/spec approved, prototype confirmed (where applicable), acceptance criteria defined

**Stable Plan Rule**: If the approved plan has not changed since G2, execute directly — do not re-analyze goals, re-evaluate alternatives, or re-justify the approach.

## Inputs

- Approved feature plan/spec from Exploration
- UX prototype as visual reference (where applicable)
- Confirmed acceptance criteria

## Activities

- Produce Production-Plan (PPLAN) referencing the approved G2 plan
- Obtain human approval of Production-Plan before writing code
- Step-by-step implementation according to plan
- Build verification after each step
- Visual validation against prototype (where applicable)
- Spec comparison: all acceptance criteria checked
- Tests executed
- Commit with meaningful message
- Documentation updated

## Outputs

- Production-Plan (approved by human)
- Production code (compiles, follows plan, follows patterns)
- Validation result (all acceptance criteria passed)
- Commit(s) on main
- Plans moved to `finished/` (PPLAN + PLAN)
- Up-to-date documentation

## Roles Active in This Step

| Role | Responsibility |
|------|---------------|
| [SDLC](sdlc.md) | Implementation + validation + delivery rules |
| [AI-Plans](ai-plans.md) | Plan execution tracking, finalization |
| [UX-Tooling](ux-tooling.md) | Visual validation, preview comparison |
| [DevOps](devops.md) | Build verification, commit workflow, CI |
| [Software-Architecture](software-architecture.md) | Pattern enforcement, anti-patterns |
| [Context-Engineering](context-engineering.md) | Post-delivery: update CLAUDE.md, docs |

## Quality Gate G3: Production Complete

- [ ] Production-Plan exists and was approved by human before implementation
- [ ] Code compiles / build is successful
- [ ] Only changes specified in the plan — no scope expansion
- [ ] Existing patterns followed
- [ ] No over-engineering, no extra features
- [ ] All acceptance criteria from spec fulfilled
- [ ] Visual result matches prototype (if applicable)
- [ ] No regressions
- [ ] Tests pass (if test suite exists)
- [ ] Plans moved to `finished/` (PPLAN + PLAN)
- [ ] Documentation is up to date (CLAUDE.md, ADRs if needed)
- [ ] No open TODOs
- [ ] **Human has given final approval**

**Production is complete when G3 is fully passed.** Single-pass check: verify each criterion once. Do not re-evaluate unless the human flags an issue.