# Kanban Integration

> How the chevp-ai-framework embeds into a flow-based Kanban system.

## Principle

Kanban manages the *flow* of work. The framework defines *how* each work item is executed. The 3-step lifecycle maps directly to Kanban columns — each step is a stage in the flow.

```
Kanban Board (flow management)
  └── chevp-ai-framework (task execution within each stage)
```

## Board Layout

The framework's 3 steps become Kanban columns:

```
┌──────────┐   ┌───────────┐   ┌──────────────┐   ┌──────────┐   ┌──────┐
│ Backlog  │ → │  Context  │ → │ Exploration  │ → │Production│ → │ Done │
│          │   │   (CTX)   │   │    (EXP)     │   │  (PRD)   │   │      │
└──────────┘   └───────────┘   └──────────────┘   └──────────┘   └──────┘
                    G1 ──→          G2 ──→             G3 ──→
```

Gate transitions are the pull signals: a task moves to the next column only when the gate is passed and the human approves.

## WIP Limits per Step

Kanban's core mechanism — limiting work in progress — applies per step:

| Column | Recommended WIP Limit | Rationale |
|--------|----------------------|-----------|
| Context | 2-3 | Context is mostly reading/analysis — lightweight, can run in parallel |
| Exploration | 1-2 | Planning requires focus — too many parallel plans creates confusion |
| Production | 1 | Implementation demands deep focus — context switching between active implementations is costly |

These are starting points. Teams adjust based on experience and capacity.

**Critical rule**: WIP limits do not override gate enforcement. If Production has a WIP limit of 1 and that slot is occupied, new tasks wait in Exploration — they do not skip EXP to "keep moving."

## Pull Principle

Tasks are pulled, not pushed:

1. Developer finishes a PRD task (G3 passed) → slot opens in Production
2. Developer pulls the highest-priority EXP task that has passed G2
3. EXP slot opens → Developer pulls the highest-priority CTX task that has passed G1
4. CTX slot opens → Developer pulls from Backlog

The AI does not manage the pull — the developer (or team) decides what to pull next. The AI executes the lifecycle for whichever task is pulled.

## Flow Metrics

| Kanban Metric | Framework Mapping |
|--------------|-------------------|
| Lead Time | Backlog entry → G3 passed |
| Cycle Time | CTX start → G3 passed |
| Throughput | Number of G3-passed tasks per time period |
| Blocked Items | Tasks where a gate cannot be passed (missing artifact, waiting for human approval) |
| Step Duration | Time spent in each column (CTX, EXP, PRD) — identifies bottlenecks |

## Expedite Lane

For urgent items (production incidents, critical bugs):

| Severity | Lifecycle |
|----------|-----------|
| Critical (production down) | Abbreviated lifecycle — verbal CTX + EXP, minimal PRD. Gates still apply but artifacts are minimal |
| Urgent (important bug) | Normal lifecycle, but enters at top of Backlog and has priority for WIP slots |
| Normal | Standard flow |

The framework's abbreviation rules already support this: "Small bugfix (< 10 lines): CTX and EXP can be verbal."

## Classes of Service

Kanban often categorizes work by class of service. Each class maps to a lifecycle variant:

| Class of Service | Lifecycle Variant |
|-----------------|-------------------|
| Standard | Full lifecycle |
| Fixed Date | Full lifecycle — deadline is a constraint captured in CTX |
| Expedite | Abbreviated lifecycle (see above) |
| Intangible (tech debt) | Full lifecycle — tech debt is a first-class task |

## Continuous Flow vs. Sprints

Unlike Scrum, Kanban has no timeboxes. This removes the sprint-boundary tension entirely:

- Tasks take as long as they need
- Gates are passed when ready, not forced by a deadline
- Throughput is measured continuously, not per iteration
- No "unfinished at sprint end" problem

This makes Kanban the most natural fit for the framework's gate-driven approach.

## Anti-Patterns

| Mistake | Why It Fails |
|---------|-------------|
| Ignoring WIP limits because "AI is fast" | AI speed does not reduce context-switching cost for the human reviewer |
| Pushing tasks forward without gate approval | Violates both Kanban's pull principle and the framework's gate enforcement |
| Skipping CTX for "small" items | Even in Kanban, every task starts at Context — abbreviation is allowed, skipping is not |
| No WIP limit on Production | Leads to multiple half-implemented features — the worst outcome for flow |
