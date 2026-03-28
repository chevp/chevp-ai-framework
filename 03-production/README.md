# Step 3: Production

> Build, verify, ship — nothing more, nothing less.

## Goal

Write production-ready code that follows the plan, validate it against the spec and prototype, and deliver it cleanly.

## When

After Exploration is complete (G2 passed). Plan/spec is approved, prototype is confirmed (where applicable).

## Inputs

- Approved plan/spec from Exploration
- UX prototype as visual reference (where applicable)
- Confirmed acceptance criteria

## Activities

- Step-by-step implementation according to plan
- Build verification after each step
- Visual validation against prototype (where applicable)
- Spec comparison: all acceptance criteria checked
- Tests executed
- Commit with meaningful message
- Documentation updated

## Outputs

- Production code (compiles, follows plan, follows patterns)
- Validation result (all acceptance criteria passed)
- Commit(s) on main
- Plan moved to `finished/` (if plan-based)
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

- [ ] Code compiles / build is successful
- [ ] Only changes specified in the plan
- [ ] Existing patterns followed
- [ ] No over-engineering, no extra features
- [ ] All acceptance criteria from spec fulfilled
- [ ] Visual result matches prototype (if applicable)
- [ ] No regressions
- [ ] Tests pass (if test suite exists)
- [ ] Human has given final approval
- [ ] Commit is on main
- [ ] Plan status updated
- [ ] Documentation is up to date
- [ ] No open TODOs

**Production is complete when G3 is fully passed.**
