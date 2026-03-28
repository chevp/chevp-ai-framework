# AI-Assisted Development Lifecycle

## The 3-Step Model

<p align="center">
  <img src="images/chevp-ai-framework.png" alt="chevp-ai-framework" width="680" />
</p>

Each step produces defined artifacts. No step is skipped. The human approves every transition.

---

## Steps × Roles Matrix

|                          | [Context](01-context/)           | [Exploration](02-exploration/)         | [Production](03-production/)             |
|--------------------------|----------------------------------|----------------------------------------|------------------------------------------|
| **SDLC**                 | [sdlc](01-context/sdlc.md)       | [sdlc](02-exploration/sdlc.md)         | [sdlc](03-production/sdlc.md)            |
| **AI-Plans**             | [ai-plans](01-context/ai-plans.md) | [ai-plans](02-exploration/ai-plans.md) | [ai-plans](03-production/ai-plans.md)    |
| **UX-Tooling**           | —                                | [ux-tooling](02-exploration/ux-tooling.md) | [ux-tooling](03-production/ux-tooling.md) |
| **DevOps**               | —                                | —                                      | [devops](03-production/devops.md)        |
| **Software-Architecture**| [arch](01-context/software-architecture.md) | [arch](02-exploration/software-architecture.md) | [arch](03-production/software-architecture.md) |
| **Context-Engineering**  | [ctx](01-context/context-engineering.md) | [ctx](02-exploration/context-engineering.md) | [ctx](03-production/context-engineering.md) |

---

## Role Definitions

| Role | Scope |
|------|-------|
| **SDLC** | Process governance, step transitions, quality gates, iteration rules |
| **AI-Plans** | Plan/spec artifacts, acceptance criteria, scope management |
| **UX-Tooling** | Prototypes, screenshot feedback loops, visual validation |
| **DevOps** | Build verification, commit workflow, CI/CD, delivery pipeline |
| **Software-Architecture** | Architecture analysis, ADRs, pattern enforcement, design decisions |
| **Context-Engineering** | CLAUDE.md, context hierarchy, what AI must read, context freshness |

---

## Quality Gates

| Transition | Gate | Key Criteria |
|------------|------|--------------|
| Context → Exploration | **G1** | Problem understood, affected modules identified, scope confirmed by human |
| Exploration → Production | **G2** | Plan/spec approved, prototype visually confirmed (where applicable) |
| Production → Done | **G3** | All acceptance criteria fulfilled, no regressions, human has approved |

Details in each step's [README.md](01-context/README.md).

---

## When Steps May Be Abbreviated

| Scenario | Allowed |
|----------|---------|
| Small bugfix (< 10 lines) | Exploration can be verbal (no written spec), UX-Tooling omitted |
| Purely technical refactoring | UX-Tooling omitted in Exploration and Production |
| Visual feature (UI, shader) | No step is skippable |
| Architecture decision | UX-Tooling omitted, but ADR is mandatory |
| Exploration / spike | Only Context + Exploration, no Production code |

---

## Iteration

The lifecycle is not strictly linear. Backward jumps are allowed:

- **Production → Exploration**: Plan needs adjustment
- **Production → Context**: New insights change the scope
- **Exploration → Context**: Discovery reveals misunderstood requirements

But: **Forward only with a passed quality gate.** No jump from Context to Production.
