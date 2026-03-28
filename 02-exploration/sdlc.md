# SDLC in Exploration

> Process governance for specification and prototyping.

## Responsibilities

- Enforce that a plan/spec exists before any production code
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
| UI changes (layouts, forms, dashboards) | Mandatory |
| Shaders / visual effects | Mandatory |
| 3D scenes and levels | Mandatory |
| Backend APIs, database migrations | Omitted |
| Refactoring without visual output | Omitted |
| Build system changes | Omitted |

## AI Behavior

### MUST
- Create plan/spec before any code
- Wait for human approval before proceeding
- Flag when a prototype is required but missing

### MUST NOT
- Write a plan AND immediately implement it
- Skip prototype for visual output
- Proceed without human approval

## Checklist

- [ ] Plan/spec exists and is appropriate for the scope
- [ ] Prototype is created where mandatory
- [ ] Human has approved before moving to Production
