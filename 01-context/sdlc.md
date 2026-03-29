# SDLC in Context

> Process governance for the Context step.

## Responsibilities

- Ensure that every individual change starts with understanding, never with code — the lifecycle is per-task, not per-project
- Enforce the rule: no phase is skipped, Context is always the first step
- Enforce mandatory deliverables before gate transition
- Ensure the human confirms scope before moving forward

## AI Behavior

### MUST
- Auto-detect when Context mode is appropriate (new tasks, questions about the system, ambiguous requests) and announce the detected mode
- Begin every task by reading existing code and documentation
- Produce or verify all mandatory deliverables (System Spec, Architecture, ADRs, Context Inventory)
- Clearly state understanding: "I understand you want X. This affects Y and Z."
- Ask open questions instead of making assumptions
- Wait for **explicit** human scope confirmation before proceeding
- State when Gate G1 is satisfied and request human approval to move to Exploration

### MUST NOT
- Skip Context and jump to Exploration or Production
- Move to Exploration without all G1 checkboxes satisfied
- Expand scope on its own ("I also improved X while I was at it")
- Assume requirements without checking
- Treat scope confirmation as implicit — it must be explicit

## Gate G1 Enforcement

Before requesting gate transition, verify:

1. System Spec exists
2. Architecture is documented
3. Fundamental ADRs are written
4. Existing artifacts are catalogued
5. Scope is confirmed by human

If any item is missing: **stop and produce it** before proceeding.

## Checklist

- [ ] Context mode has been detected and announced by the AI
- [ ] All mandatory deliverables exist or are verified
- [ ] Problem is formulated, not just the task
- [ ] Human has explicitly confirmed scope
- [ ] Quality Gate G1 is passed before proceeding