# AI-Assisted Development Lifecycle

> **Scope: The 3-step lifecycle applies to EVERY individual change — not to the product as a whole. Each task (feature, bugfix, refactoring) starts fresh at Context and progresses through Exploration to Production. The lifecycle is independent of the project's SDLC phase.**

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
| **UX-Tooling** | Prototypes, preview feedback loops, visual/physical validation |
| **DevOps** | Build verification, commit workflow, CI/CD, delivery pipeline |
| **Software-Architecture** | Architecture analysis, ADRs, pattern enforcement, design decisions |
| **Context-Engineering** | CLAUDE.md, context hierarchy, what AI must read, context freshness |

---

## AI Modes

AI operates in exactly one mode at a time. The mode determines what AI may and may not do. Each mode is signaled by a **prompt prefix** and enforced through a **prompt header**.

| Mode | Prompt Prefix | Purpose | Allowed | Not Allowed |
|------|---------------|---------|---------|-------------|
| **Context** | `chp-context:` | Understand system & problem | Read/verify artifacts, ask questions, create Context-Plan, produce System Spec | Change code, create feature plans, alter scope |
| **Exploration** | `chp-exploration:` | Plan features & prototype | Create Feature Plan/Spec, write ADRs, iterate prototypes, document risks | Write production code, expand scope unilaterally |
| **Production** | `chp-production:` | Implement & validate | Execute approved plan, run tests, verify build, create commits | Create new plans, expand scope, make unplanned changes |

### Prompt Header (Meta-Strategy)

Every prompt begins with the framework header. This reminds both human and AI of the current mode and its constraints:

```
# CHEVP-AI-FRAMEWORK
# Mode Reminder:
# 1. Context (G1)     → Read, verify, ask questions, create Context-Plan
# 2. Exploration (G2)  → Plans, specs, prototypes, document risks
# 3. Production (G3)   → Implement approved plan step-by-step, validate

current_mode: <context|exploration|production>
human_approved: <true|false>
approved_plan: <PLAN-NNN.md or null>
prototype_confirmed: <true|false>
context_verified: <true|false>
```

### Prompt Structure for Actions

After the header, each prompt follows this structure:

```
chp-<current_mode>:
- Goal: <Describe goal within this mode>
- Inputs: <Which artifacts/plans/prototypes are needed>
- Output: <What AI should deliver>
- Forbidden in this mode: <List of prohibited actions>
```

### AI Status-Check (before every response)

AI outputs a brief status check before acting:

```
Status: current_mode=exploration, human_approved=true, prototype_confirmed=false
Allowed: Create Plan/Spec, iterate prototype
Forbidden: Write production code, commit changes
```

This ensures the human sees whether the prompt is mode-compliant before AI proceeds.

### Mode Transitions

```
Context ──[G1 passed + Human confirms]──→ Exploration
Exploration ──[G2 passed + Human approves]──→ Production
Production ──[G3 passed + Human approves]──→ Done
```

Backward jumps allowed: Production → Exploration (plan wrong), Production → Context (fundamental problem), Exploration → Context (requirements misunderstood).

**Rule:** Forward only with passed gate + human confirmation. Backward at any time when needed.

### Session State (in project CLAUDE.md)

```markdown
## Current Session State
- **Mode**: chp-context | chp-exploration | chp-production
- **Active Plan**: PLAN-NNN (or none)
- **Gate Status**: G1 ○/✓ | G2 ○/✓ | G3 ○/✓
- **human_approved**: true/false
- **prototype_confirmed**: true/false
- **context_verified**: true/false
```

---

## Mandatory Deliverables per Step

| Deliverable | Context | Exploration | Production |
|-------------|---------|-------------|------------|
| Context-Plan (CPLAN) | **Mandatory** | — | — |
| System Spec | **Mandatory** | — | — |
| Software Architecture | **Mandatory** | — | — |
| ADRs (fundamental) | **Mandatory** | — | — |
| Context Inventory | **Mandatory** | — | — |
| Scope Confirmation | **Mandatory** | — | — |
| Feature Plan/Spec | — | **Mandatory** | — |
| ADRs (new decisions) | — | As needed | — |
| UX Prototype | — | **Mandatory** (where applicable) | — |
| Production-Plan (PPLAN) | — | — | **Mandatory** |
| Production Code | — | — | **Mandatory** |
| Validation Result | — | — | **Mandatory** |

---

## Quality Gates

| Transition | Gate | Key Criteria |
|------------|------|--------------|
| Context → Exploration | **G1** | Context-Plan confirmed, System Spec exists, Architecture documented, fundamental ADRs written, existing artifacts catalogued, scope confirmed by human, mode transition approved |
| Exploration → Production | **G2** | Feature plan/spec approved, prototype visually confirmed (where applicable), acceptance criteria defined, human approved |
| Production → Done | **G3** | Production-Plan approved before implementation, all acceptance criteria fulfilled, build passes, no regressions, documentation updated, human approved |

**Gates are blockers.** No forward movement until every criterion is satisfied. The human must explicitly approve each gate transition.

Details in each step's [README.md](01-context/README.md).

---

## When Steps May Be Abbreviated

| Scenario | Allowed |
|----------|---------|
| Small bugfix (< 10 lines) | CPLAN and PLAN can be verbal, PPLAN one-liner ("Implements PLAN-NNN"), UX-Tooling omitted. Context deliverables must still be **read and verified**. |
| Purely technical refactoring | UX-Tooling omitted in Exploration and Production |
| Visual feature (UI, shader) | No step is skippable, all plans must be written |
| Architecture decision | UX-Tooling omitted, but ADR is mandatory |
| Exploration / spike | Only Context + Exploration, no Production code |

Even when abbreviated: **no step is skipped entirely**, and **human approval is always required**.

---

## Iteration

The lifecycle is not strictly linear. Backward jumps are allowed:

- **Production → Exploration**: Plan needs adjustment
- **Production → Context**: New insights change the scope
- **Exploration → Context**: Discovery reveals misunderstood requirements

But: **Forward only with a passed quality gate.** No jump from Context to Production.