# SDLC in Exploration

> Process governance for specification and prototyping.

## Responsibilities

- Enforce that a feature plan/spec exists before any production code
- Determine when a prototype is mandatory vs. optional
- Ensure human approval at every transition

## When Is a Written Spec Required?

| Scenario | Spec Required? |
|----------|---------------|
| Feature development | Always |
| Architecture change | Always (+ ADR) |
| Complex bugfix | Always |
| Trivial change (< 10 lines) | Verbal confirmation sufficient |

## When Is a Prototype Required?

| Scenario | Prototype Required? |
|----------|-------------------|
| UI changes (layouts, forms, dashboards) | **Mandatory** |
| Visual output (graphics, animations, effects) | **Mandatory** |
| Interactive / spatial content (3D, maps, diagrams) | **Mandatory** |
| Non-visual changes (APIs, data, logic) | Omitted |
| Refactoring without visual output | Omitted |
| Build / infrastructure changes | Omitted |

## AI Behavior

### MUST
- Auto-detect when Exploration mode is appropriate (user asks to plan, design, or prototype) and announce the detected mode
- Create feature plan/spec before any code
- Verify that System Spec + Architecture + ADRs from Context exist before planning features
- Wait for human approval before proceeding
- Flag when a prototype is required but missing
- State when Gate G2 is satisfied and request human approval to move to Production

### MUST NOT
- Write a plan AND immediately implement it
- Skip prototype for visual output
- Proceed without human approval
- Create system-level specs (those belong in Context)
- Confuse feature-level planning with system-level architecture

## Checklist

- [ ] G1 deliverables verified (System Spec, Architecture, ADRs exist)
- [ ] Feature plan/spec exists and is appropriate for the scope
- [ ] Prototype is created where mandatory
- [ ] Human has approved before moving to Production