# SAFe Integration

> How the chevp-ai-framework embeds into the Scaled Agile Framework at team level.

## Principle

SAFe organizes work across teams and programs. The framework defines how each task is executed within a team. The framework operates at the **Team Level** of SAFe — it does not replace ART coordination, portfolio management, or PI-level ceremonies.

```
SAFe Portfolio / Program (organization)
  └── SAFe Team Level (coordination)
       └── chevp-ai-framework (task execution)
```

## Mapping

| SAFe Concept | Framework Equivalent |
|-------------|---------------------|
| Feature / Story | Input for Context step |
| Enabler Story (Spike) | Lifecycle that stops after Exploration — no PRD step |
| Architectural Runway | ADRs + Architecture document from Context step |
| Team PI Objectives | Guide which tasks enter Context during the PI |
| Iteration (Sprint) | Same as Scrum integration — see [scrum.md](scrum.md) |
| System Demo | Aggregated G3 results across team's completed tasks |
| Inspect & Adapt | May produce feedback for `context/guidelines/` extensions |

## Task Flow Within a PI

```
PI Planning
  ↓
  Features decomposed into Stories
  ↓
  Stories assigned to Iterations
  ↓
  For each Story per Iteration:
    [CTX] → G1 → [EXP] → G2 → [PRD] → G3 → Done
  ↓
System Demo (all G3-passed stories across iterations)
```

## Enabler Stories and Spikes

SAFe distinguishes Enablers from Features. The framework supports this natively:

| Story Type | Lifecycle |
|-----------|-----------|
| Feature Story | Full lifecycle: CTX → EXP → PRD |
| Enabler (Spike / Research) | Partial lifecycle: CTX → EXP only. No production code. |
| Enabler (Infrastructure) | Full lifecycle — the "production code" is infrastructure |

For spikes: the Exploration artifacts (plan, ADR, prototype) become the deliverable. G2 marks completion — G3 is not required.

## Architectural Runway

SAFe requires teams to maintain an Architectural Runway — decisions and infrastructure that enable future features without excessive redesign.

The framework's Context step produces the same artifacts:

| Runway Element | Framework Artifact |
|---------------|-------------------|
| Architectural decisions | ADRs (`context/adr/`) |
| System design | Architecture document (`context/architecture/`) |
| Constraints and trade-offs | Documented in ADR Consequences section |
| Technical debt visibility | Captured during Context as constraints |

**Rule**: When a Feature Story requires architectural work that does not exist in the runway, the Context step will surface this. The AI blocks forward progress until the Architecture document and ADRs are produced — this is the framework enforcing runway maintenance.

## Cross-Team Dependencies

The framework operates within one repository / one team. Cross-team dependencies in SAFe are handled outside the framework:

| Dependency Type | How to Handle |
|----------------|---------------|
| Another team must deliver an API first | Capture as constraint in Context step — scope confirmation must acknowledge the dependency |
| Shared module owned by another team | `context/constraints/` blocks changes until coordination is complete |
| Cross-ART dependency | Outside framework scope — handled at ART level |

## Multi-Agent for Parallel Stories

Within one team, multiple AI agents can work on separate stories in parallel during a PI iteration. See [LIFECYCLE.md § Multi-Agent Execution](../LIFECYCLE.md#multi-agent-execution) for setup and rules.

## IP Iteration (Innovation and Planning)

SAFe's IP Iteration maps naturally to the framework:

| IP Activity | Framework Usage |
|------------|----------------|
| Innovation | Multiple CTX → EXP cycles (spikes, prototypes) |
| Planning | CTX sessions for upcoming PI's features |
| Hackathon | Abbreviated lifecycle — verbal CTX, rapid EXP, experimental PRD |
| Technical debt | Full lifecycle targeting debt items |

## Anti-Patterns

| Mistake | Why It Fails |
|---------|-------------|
| Using the framework for PI Planning | Framework is task-level, not program-level. PI Planning organizes tasks — the framework executes them |
| Skipping CTX because "the Feature was defined at PI Planning" | PI-level Feature definition is not task-level Context. Each story needs its own CTX |
| Treating ADRs as ART-level artifacts | Framework ADRs are per-repository. ART-level architectural decisions live in ART-level documentation |
| Forcing all stories to G3 at iteration boundary | Same as Scrum — gate enforcement overrides timebox |
