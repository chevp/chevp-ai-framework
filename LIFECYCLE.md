# AI-Assisted Development Lifecycle

> **Scope: The 3-step lifecycle applies to EVERY individual change — not to the product as a whole. Each task (feature, bugfix, refactoring) starts fresh at Context and progresses through Exploration to Production. The lifecycle is independent of the project's SDLC phase.**

## The 3-Step Model

<p align="center">
  <img src="images/chevp-ai-framework.png" alt="chevp-ai-framework" width="680" />
</p>

Each step produces defined artifacts. No step is skipped. The AI enforces the process; the human approves every transition.

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
| **Challenger**           | (optional, when risks are thin)  | [challenger](02-exploration/challenger.md) **mandatory before G2** | (only on scope-change requests) |

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
| **Challenger** | Internal sceptic — produces top-3 failure modes, ≥2 alternatives, strongest counter-argument before G2 |

---

## AI Modes

The AI owns the process. The human writes naturally; the AI infers the mode, enforces gates, and blocks violations — automatically. No structured prompts, mode declarations, or manual state management required.

AI operates in exactly one mode at a time. The mode determines what AI may and may not do.

| Mode | Intent Signals | Allowed | Not Allowed |
|------|---------------|---------|-------------|
| **Context** | "what does", "explain", "analyze", "understand", new task, ambiguous start | Read/verify artifacts, ask questions, create Context-Plan, produce System Spec | Change code, create feature plans, alter scope |
| **Exploration** | "plan", "design", "prototype", "spec", "how should we" | Create Feature Plan/Spec, write ADRs, iterate prototypes, document risks | Write production code, expand scope unilaterally |
| **Production** | "implement", "build", "code", "execute the plan", "fix" (with approved plan) | Execute approved plan, run tests, verify build, create commits | Create new plans, expand scope, make unplanned changes |

### AI Mode-Detection Protocol

Before every response, the AI determines the current mode through this priority order:

1. **Conversation state** — If a mode is already active and no transition has occurred, stay in that mode
2. **Intent classification** — Classify user intent from natural language using the signal words above
3. **Default to Context** — When intent is ambiguous and no mode is active, start in Context (the safest mode)
4. **Block when conflicting** — If the user's intent requires a later mode but the gate is not passed, the AI blocks the request, explains what prerequisites are missing, and guides the user back to the correct step

The AI **MUST NOT** silently switch modes. Any mode change must be explicitly announced with reasoning. Forward transitions require human approval.

### Mixed-Intent Resolution

When a single message contains signals for multiple modes (e.g., "explain how auth works and then implement the fix"), the AI:

1. **Decomposes** the request into its distinct intents
2. **Sequences** them by lifecycle order — earlier modes first
3. **Executes** the earliest mode's portion and stops at the gate boundary
4. **States** what remains: "I've addressed the Context part. The implementation requires G1 + G2 to be passed first — here's where we stand."

The AI never cherry-picks the later intent and skips the earlier one.

### Adaptive Mode-Awareness Header

The AI outputs a header before every response. The header's detail level adapts to what is useful — not every response needs full gate status.

| Situation | Header Level | Example |
|-----------|-------------|---------|
| Mode change, gate transition, or blocking | **Full** — mode + reasoning, gate progress, next action | `[Context] You're asking about the codebase. G1 not yet passed (missing: System Spec). Let me start there.` |
| Continuing work in the same mode | **Short** — mode confirmation only | `[Production] Continuing implementation.` |
| Blocking a request | **Full + redirect** — why it's blocked, what's missing, how to proceed | `[Blocked → Exploration] No approved plan exists. Let me help you write one.` |

The header is the AI's responsibility — the human never needs to provide or manage it.

### AI Gatekeeper Behavior

The AI acts as an autonomous process enforcer. Before every response, the AI:

1. **Infers** the mode from user intent and conversation history
2. **Checks** whether the current gate prerequisites are met
3. **Blocks** if the user's request belongs to a later mode and the gate is not passed — the AI states the specific missing prerequisites and redirects to the current step
4. **Proposes** forward transitions when all gate criteria are satisfied: "All Context deliverables are ready. G1 is satisfied. Shall we move to Exploration?"
5. **Detects** backward jumps when the conversation shifts (e.g., "actually, the requirements are wrong") and proposes the jump
6. **Guides** — when blocking, the AI does not just say "no" but actively helps the user complete the missing prerequisites

**Examples of blocking:**

- User asks "implement feature X" but no plan exists → AI blocks: "We need a feature plan first. Let me help you create one — what problem does feature X solve?"
- User asks "write the code" but G1 is not passed → AI blocks: "We haven't confirmed the context yet. Here's what's still missing: [lists items]. Let me help with those first."

### Mode Transitions

```
Context ──[G1 passed + Human confirms]──→ Exploration
Exploration ──[G2 passed + Human approves]──→ Production
Production ──[G3 passed + Human approves]──→ Done
```

**Forward transitions**: AI verifies all gate criteria, lists them, proposes the transition, and waits for human approval.

**Backward jumps**: AI detects when the conversation shifts backward (plan is wrong, requirements misunderstood, fundamental problem discovered) and proposes the jump. Human confirms.

**Production → Exploration fallback**: During Production, the AI **must** propose a fallback to Exploration when any of these triggers occur:
- Implementation reveals the plan is incomplete or ambiguous (an unaddressed edge case, a missing step)
- A technical constraint makes the approved approach unviable
- The human requests a change that exceeds the plan's scope

The AI stops implementing, states the specific trigger, and proposes: "This needs a plan update. Shall we fall back to Exploration?" The AI does not silently patch the plan or improvise beyond the approved scope.

**Rule:** Forward only with passed gate + human confirmation. Backward at any time when needed.

### State Tracking

The AI tracks all session state internally — the human never manages state:
- Current mode (Context / Exploration / Production)
- Active plan reference (if any)
- Gate status (G1, G2, G3 — passed or pending with specific missing items)
- Whether the human has approved the current gate

No manual session state block, prompt headers, or mode declarations are required from the human. The AI announces state changes through its mode-awareness header and is solely responsible for maintaining process continuity.

---

## Interaction Protocol

The AI interacts with the human via **two UI primitives only**. Free-form prose for decision points is forbidden — every choice is a click, every artifact is a draft you accept or edit.

| Primitive | Use for | Tool |
|-----------|---------|------|
| **Clickable Question** | All discrete decisions (the 6 per step listed below) | `AskUserQuestion` — 2-4 labeled options + automatic "Other" text field |
| **Draft-Confirm** | All free-form artifacts (Problem Statement, Hypotheses, ADR body, plan text, scope edits) | Generate markdown draft → `AskUserQuestion` with options: `accept` / `edit inline` / `regenerate` / `other` |

**Self-check rule:** If the AI catches itself writing "Shall we…", "Do you want…", "Which would you prefer…", or any other open question that has a finite answer set, it MUST convert the sentence into an `AskUserQuestion` call before sending the response.

### Ad-hoc Decision Forks

The 6 Decisions per Step (below) are the **planned** decision points. But forks also surface mid-work — when the AI hits a place where two or more architecturally plausible options exist and the human (not the AI) should make the call. These ad-hoc forks follow the same Clickable-Question primitive.

**Trigger.** Surface a fork structurally — not as prose — whenever **all three** hold:
1. Two or more options are architecturally plausible (not just a clear best + obvious losers).
2. The choice is owned by the human (taste, scope, product fit, irreversible commitment) — not a pure implementation detail the AI can decide silently.
3. The decision affects subsequent work (changes the plan, the artifact, or the next gate's evidence).

**Format.** 2–4 mutually-exclusive options. Each option carries a one-sentence trade-off. One option is marked as the AI's **recommended default** with a one-line reason. Always include the automatic "Other" text field.

**Tooling.** Use `AskUserQuestion` (Claude Code) or the equivalent structured picker in the host environment. Plain prose with a numbered list is only an acceptable fallback when no structured tool is available.

**Negative rule — propose-and-confirm, not open-ended ask.** When the AI has a clear preference from context (only one option is actually viable, or the others would violate an ADR / gate / Kill Criterion), do **not** fabricate a multi-option fork. Instead present a single proposal with two options: `accept` and `discuss alternatives`. Manufacturing fake choices to look collaborative is forbidden — it wastes the human's attention budget that the framework is trying to protect.

**Boundary with the planned 6.** Ad-hoc forks supplement, never replace, the 6 per-step decisions. If an ad-hoc fork turns out to be one of the 6 in disguise (e.g. a scope question), record it in the appropriate slot rather than treating it as bonus interaction.

### The 6 Decisions per Step

Each step has exactly **6 discrete decisions** that the human owns. The AI never decides these silently — each is presented as a Clickable Question.

**Context (toward G1)**
1. Confirm the **Problem Statement** (accept / edit / regenerate)
2. Confirm the **Hypotheses** (accept / edit / regenerate)
3. Confirm the **Risks** (accept / edit / regenerate)
4. Approve the **System Spec & Architecture** snapshot (accept / edit / regenerate)
5. Confirm **scope** — what is in / out / uncertain
6. **Pass G1** → Exploration (approve / reject / revise)

**Exploration (toward G2)**
1. Choose **`exploration-mode`** — A (plan-first) or B (prototype-first)
2. Approve the **Feature Plan/Spec** (accept / edit / regenerate)
3. Pick among **Challenger alternatives** (≥2 options + counter-argument)
4. Confirm the **prototype validation** result (works / partial / fails → kill)
5. Confirm **Kill Criteria** and **`insights.md`** are recorded
6. **Pass G2** → Production (approve / reject / revise)

**Production (toward G3)**
1. Approve **start of PRD execution** against the approved plan
2. Approve any **scope change** or **fallback to Exploration** when triggered
3. Approve **commits / PR** at boundary points (not every file)
4. Confirm **acceptance criteria** fulfilled (each criterion: pass / fail)
5. Confirm **`insights.md`** updated with implementation surprises
6. **Pass G3** → Done (approve / reject / revise)

Out-of-scope items raised at any decision point become `PROP-NNN` proposals (Rule #12) — they never disappear into prose.

---

## Mandatory Deliverables per Step

| Deliverable | Context | Exploration | Production |
|-------------|---------|-------------|------------|
| Context-Plan (CTX) | **Mandatory** | — | — |
| System Spec | **Mandatory** | — | — |
| Software Architecture | **Mandatory** | — | — |
| ADRs (fundamental) | **Mandatory** | — | — |
| Context Inventory | **Mandatory** | — | — |
| Scope Confirmation | **Mandatory** | — | — |
| Feature Plan/Spec | — | **Mandatory** | — |
| ADRs (new decisions) | — | As needed | — |
| UX Prototype | — | **Mandatory** (where applicable) | — |
| Production-Plan (PRD) | — | — | **Mandatory** |
| Production Code | — | — | **Mandatory** |
| Validation Result | — | — | **Mandatory** |

---

## Quality Gates

| Transition | Gate | Key Criteria |
|------------|------|--------------|
| Context → Exploration | **G1** | Context-Plan confirmed, **uncertainty triplet** (Problem Statement, Hypotheses, Risks) drafted, System Spec exists, Architecture documented, fundamental ADRs written, existing artifacts catalogued, scope confirmed by human, mode transition approved, **evidence block filled**, **Gatekeeper-G1 verdict recorded**. **If cross-platform:** platform targets declared, PAL boundary identified, asset format strategy documented |
| Exploration → Production | **G2** | Feature plan/spec approved with `exploration-mode: A\|B`, prototype visually confirmed (where applicable), acceptance criteria defined, **Kill Criteria defined**, **`insights.md` exists**, **Challenger output present**, **evidence block filled**, **Gatekeeper-G2 verdict recorded**, human approved. **If cross-platform:** plan covers all declared targets, no single-platform design |
| Production → Done | **G3** | Production-Plan approved before implementation, all acceptance criteria fulfilled, build passes, no regressions, documentation updated, **`insights.md` updated with implementation surprises**, **Gatekeeper-G3 verdict recorded**, human approved. **If cross-platform:** build passes on all declared targets, no platform-specific code outside PAL, asset pipeline outputs all required formats |

**Gates are blockers.** No forward movement until every criterion is satisfied. The human must explicitly approve each gate transition.

### Evidence-Based Gates

Approval is no longer a single rubber-stamp. Every gate transition records three explicit fields in the plan's frontmatter `evidence:` block:

```yaml
evidence:
  hypothesis: "We believed X would work because Y"
  result: "Prototype confirmed/refuted X via Z"
  reasoning: "Therefore we are/are not proceeding to the next step"
```

A blank or boilerplate evidence block is a gate failure — see [guidelines/uncertainty-reduction.md](guidelines/uncertainty-reduction.md). The gatekeeper subagents (`gatekeeper-g1/g2/g3`) refuse to issue a `pass` verdict if the evidence block is empty or generic.

Details in each step's [README.md](01-context/README.md).

---

## When Steps May Be Abbreviated

| Scenario | Allowed |
|----------|---------|
| Small bugfix (< 10 lines) | CTX and EXP can be verbal, PRD one-liner ("Implements EXP-NNN"), UX-Tooling omitted. Context deliverables must still be **read and verified**. |
| Purely technical refactoring | UX-Tooling omitted in Exploration and Production |
| Visual feature (UI, shader) | No step is skippable, all plans must be written |
| Architecture decision | UX-Tooling omitted, but ADR is mandatory |
| Exploration / spike | Only Context + Exploration, no Production code |

Even when abbreviated: **no step is skipped entirely**, and **human approval is always required**.

**Abbreviation Justification Rule**: When the AI abbreviates a step, it **must** state which abbreviation condition applies and why (e.g., "< 10 lines, trivial bugfix — verbal CTX sufficient"). Silent abbreviation is not allowed.

---

## Iteration

The lifecycle is not strictly linear. Backward jumps are allowed:

- **Production → Exploration**: Plan needs adjustment
- **Production → Context**: New insights change the scope
- **Exploration → Context**: Discovery reveals misunderstood requirements

But: **Forward only with a passed quality gate.** No jump from Context to Production.

---

## Multi-Agent Execution

Multiple AI agents can work in parallel, each following the lifecycle independently for its own task.

### Isolation Rule

**One agent = one branch = one working directory.**

If two agents share the same working directory, they **must** operate on the same branch. Conversely, if agents need separate branches, they **must** work in separate directories (e.g., git worktrees).

| Setup | Branch | Safe? |
|-------|--------|-------|
| Separate directories (worktrees) | Separate branches | Yes — full parallel lifecycle |
| Same directory | Same branch | Context/Exploration parallel, Production sequential |
| Same directory | Different branches | **Forbidden** — undefined state |

### Lifecycle Scope per Agent

Each agent runs its own lifecycle instance for its assigned task. Gates are per-agent, per-task — one agent passing G1 does not affect another agent's gate status.

```
Agent A (feature/auth):       [Context] → G1 → [Exploration] → G2 → [Production] → G3 → PR
Agent B (feature/dashboard):  [Context] → G1 → [Exploration] → G2 → [Production] → G3 → PR
Agent C (feature/csv-import): [Context] → G1 → [Exploration] → G2 → [Production] → G3 → PR
```

The human assigns tasks with clear scope boundaries before agents start. Each agent receives:
1. The project's CLAUDE.md (loads the framework automatically)
2. A task description in natural language
3. Explicit scope boundaries (what is in scope, what is not)

### Parallelism by Step

| Step | Parallel-safe? | Reason |
|------|---------------|--------|
| **Context** | Yes | Read-only — agents read code and produce plans |
| **Exploration** | Yes | Agents write branch-local artifacts (plans, specs, ADRs) |
| **Production** | Only with separate branches | Agents write production code — concurrent writes to the same branch cause conflicts |

### Shared vs. Branch-Local Artifacts

| Artifact | Scope | Rule |
|----------|-------|------|
| CLAUDE.md | Shared (main) | Never modified in parallel — update only after merge |
| System Spec, Software Architecture | Shared (main) | Read during Context, modified only via PR |
| Plans (CTX/EXP/PRD) | Branch-local | Each agent creates plans on its own branch |
| Feature Specs | Branch-local | Scoped to the agent's task |
| ADRs | Branch-local, reconciled at merge | Conflicting ADRs require human resolution |

### Merge Point

After G3 is passed, each agent's branch is merged via pull request. The human is responsible for:
- Resolving merge conflicts (especially in shared artifacts)
- Reconciling contradictory ADRs from parallel agents
- Ensuring CLAUDE.md is updated consistently after merge
- Verifying that combined changes do not introduce regressions

---

## Project-Specific Extension Points

This framework defines the core process. The following aspects are **intentionally not part of the core** and must be defined per project in `context/guidelines/`:

| Extension Point | File | Purpose |
|----------------|------|---------|
| Architecture Invariants | `context/guidelines/architecture-invariants.md` | Layer rules, forbidden patterns, dependency direction |
| Plan Granularity | `guidelines/plan-granularity.md` | Plan types, size limits, dependencies, duplicate prevention |
| Review Criteria | `context/guidelines/review-criteria.md` | What the human reviewer checks at each gate |
| Testing Strategy | `context/guidelines/testing-strategy.md` | When tests are required, what kind, coverage expectations |
| Dependency Management | `context/guidelines/dependency-management.md` | Update policy, security patches, breaking change handling |
| Rollback / Hotfix Process | `context/guidelines/rollback-process.md` | How to revert, hotfix paths, incident handling |
| Risk Classification | `context/guidelines/risk-classification.md` | Severity levels, how risk affects process depth |
| Platform Targets | `context/guidelines/platform-targets.md` | Declared target platforms, PAL structure, asset format strategy, build matrix |

**Rule**: If an extension point file exists, the AI **must** read and enforce it. If it does not exist, the core process applies without the extension.

### Platform Targets Extension

When `context/guidelines/platform-targets.md` exists, the project is cross-platform. The AI **must** enforce the [cross-platform guideline](guidelines/cross-platform.md) at every lifecycle step. The file declares:

```yaml
targets:
  - desktop-win
  - desktop-linux
  - android-arm64

renderer: vulkan
min_api:
  android: 26        # Android 8.0+
  vulkan: "1.1"

size_budget:
  apk: 150MB
  asset_pack: 512MB

pal_root: src/pal/   # where platform abstractions live
```

If this file does not exist, the cross-platform guideline does not apply — the project is single-platform.