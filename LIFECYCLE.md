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

AI operates in exactly one mode at a time. The mode determines what AI may and may not do. The AI **auto-detects** the current mode from user intent and conversation state. Optional prompt prefixes (`chp-context:`, `chp-exploration:`, `chp-production:`) can be used as shortcuts to override auto-detection.

| Mode | Intent Signals | Optional Prefix | Allowed | Not Allowed |
|------|---------------|-----------------|---------|-------------|
| **Context** | "what does", "explain", "analyze", "understand", new task, ambiguous start | `chp-context:` | Read/verify artifacts, ask questions, create Context-Plan, produce System Spec | Change code, create feature plans, alter scope |
| **Exploration** | "plan", "design", "prototype", "spec", "how should we" | `chp-exploration:` | Create Feature Plan/Spec, write ADRs, iterate prototypes, document risks | Write production code, expand scope unilaterally |
| **Production** | "implement", "build", "code", "execute the plan", "fix" (with approved plan) | `chp-production:` | Execute approved plan, run tests, verify build, create commits | Create new plans, expand scope, make unplanned changes |

### AI Mode-Detection Protocol

The AI determines the current mode through this priority order:

1. **Explicit prefix** — If the user writes `chp-context:`, `chp-exploration:`, or `chp-production:`, use that mode (but still validate against gate state)
2. **Conversation state** — If a mode is already active and no transition has occurred, stay in that mode
3. **Intent classification** — Classify user intent from natural language using the signal words above
4. **Default to Context** — When intent is ambiguous and no mode is active, start in Context (the safest mode)
5. **Ask when conflicting** — If the user's intent conflicts with the current gate state (e.g., asks for code but G2 is not passed), explain the conflict and redirect

The AI **MUST NOT** silently switch modes. Any mode change must be announced and, for forward transitions, approved by the human.

### AI Mode-Awareness Header (before every response)

AI outputs a brief natural-language header before acting:

```
[Context] Understanding the system — you're asking about how the codebase works.
Gate: G1 not yet passed (missing: System Spec, Scope Confirmation)
Next: Complete remaining Context deliverables before moving to Exploration.
```

The header states:
- The detected mode and the reasoning behind it
- Gate progress — what is satisfied, what is still missing
- What the AI will do next (or why it is blocking)

### AI Gatekeeper Behavior

The AI acts as an autonomous gatekeeper. Before every response, the AI:

1. **Detects** the mode from user intent (see Mode-Detection Protocol above)
2. **Checks** whether the current gate prerequisites are met
3. **Blocks** if the user's request belongs to a later mode and the gate is not passed — the AI explains what is missing and redirects to the current step
4. **Proposes** forward transitions when all gate criteria are satisfied: "All Context deliverables are ready. G1 is satisfied. Shall we move to Exploration?"
5. **Detects** backward jumps when the conversation shifts (e.g., "actually, the requirements are wrong") and proposes the jump

**Examples of blocking:**

- User asks "implement feature X" but no plan exists → AI blocks: "We need a feature plan first. Let me help you create one in Exploration mode."
- User asks "write the code" but G1 is not passed → AI blocks: "We haven't confirmed the context yet. Let's finish Context first: [lists missing items]."

### Mode Transitions

```
Context ──[G1 passed + Human confirms]──→ Exploration
Exploration ──[G2 passed + Human approves]──→ Production
Production ──[G3 passed + Human approves]──→ Done
```

**Forward transitions**: AI verifies all gate criteria, lists them, proposes the transition, and waits for human approval.

**Backward jumps**: AI detects when the conversation shifts backward (plan is wrong, requirements misunderstood, fundamental problem discovered) and proposes the jump. Human confirms.

**Rule:** Forward only with passed gate + human confirmation. Backward at any time when needed.

### State Tracking

The AI tracks session state internally:
- Current mode (Context / Exploration / Production)
- Active plan reference (if any)
- Gate status (G1, G2, G3 — passed or pending with specific missing items)
- Whether the human has approved the current gate

No manual session state block is required in the project CLAUDE.md. The AI announces state changes through its mode-awareness header.

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