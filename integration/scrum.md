# Scrum Integration

> How the chevp-ai-framework embeds into Scrum sprints.

## Principle

Scrum organizes *which* work happens *when*. The framework defines *how* each task is executed. They operate at different levels and do not conflict.

```
Scrum (Sprint organization)
  └── chevp-ai-framework (Task execution)
```

## Mapping

| Scrum Concept | Framework Equivalent |
|---------------|---------------------|
| Product Backlog Item | Input for Context step |
| Sprint Backlog Item | One lifecycle instance (CTX → EXP → PRD) |
| Definition of Done | G3 checklist + project-specific `review-criteria.md` |
| Sprint Goal | Guides which tasks enter Context, not how they are executed |
| Refinement | Produces better inputs for Context — reduces CTX-Session duration |
| Sprint Review | Aggregated G3 results — already validated by the framework |
| Retrospective | May produce feedback for `context/guidelines/` extensions |

## Task Flow Within a Sprint

```
Sprint Planning
  ↓
  Select Backlog Items
  ↓
  For each item:
    [CTX] → G1 → [EXP] → G2 → [PRD] → G3 → Done
  ↓
Sprint Review (all G3-passed items)
```

Each item runs its own lifecycle independently. Multiple items can be in different steps simultaneously.

## Handling Sprint Boundaries

| Situation | Rule |
|-----------|------|
| Task reaches G3 within sprint | Done — include in Sprint Review |
| Task at EXP/PRD when sprint ends | Goes back to backlog as unfinished — do not skip gates to "finish" it |
| Task at CTX when sprint ends | Context artifacts persist in `context/` — next sprint resumes where it stopped |

**Critical rule**: Sprint timebox does not override gate enforcement. A task that has not passed G3 is not done — regardless of sprint boundaries.

## Roles

| Scrum Role | Interaction with Framework |
|------------|---------------------------|
| **Product Owner** | Provides task input, confirms scope in CTX, approves G1 (scope confirmation) |
| **Developer** | Drives the lifecycle with AI through all steps |
| **Scrum Master** | Does not interact with the framework directly — ensures the team has time/space to follow the process |

## Refinement as Context Preparation

Well-refined Backlog Items reduce the duration of the Context step:

| Refinement Quality | CTX Duration |
|-------------------|--------------|
| Vague ("improve performance") | Full CTX — AI must discover scope, dependencies, constraints |
| Refined (acceptance criteria, affected area identified) | Abbreviated CTX — AI verifies existing context, confirms scope quickly |
| Pre-analyzed (spike completed, ADR exists) | Minimal CTX — AI reads and confirms existing artifacts |

## Sprint Metrics and the Framework

| Metric | How the Framework Helps |
|--------|------------------------|
| Velocity | Each completed lifecycle (G3 passed) = 1 done item. Predictable because gates prevent half-done work |
| Cycle Time | Measurable per step: CTX duration + EXP duration + PRD duration |
| Quality | G3 enforces validation before delivery — fewer bugs escape the sprint |

## Anti-Patterns

| Mistake | Why It Fails |
|---------|-------------|
| Skipping CTX because "we refined it already" | Refinement is not Context — AI must still verify artifacts and confirm scope |
| Forcing G3 at sprint end | Produces unvalidated code — defeats the purpose of both Scrum and the framework |
| One lifecycle per epic | Lifecycle is per-task, not per-epic. An epic decomposes into multiple tasks, each with its own lifecycle |
| PO skips gate approvals | Gates require human approval — PO or Dev must explicitly confirm |
