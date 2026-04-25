# CLAUDE.md — chevp-ai-framework

This is a process framework for AI-assisted software development.
It defines the overarching lifecycle that Claude must follow in all projects.

## Core Principle

The human writes naturally. The AI owns the process.

The AI continuously detects intent, maintains the current mode, enforces all gates, and blocks violations — automatically. The human never needs to manage modes, declare state, or remember which step comes next. The process is rigorous; the experience is natural.

This framework is **process-driven, not spec-driven**. The spec is not the starting point — it emerges as an artifact within the Context step. What drives everything forward is the process itself: 3 sequential steps with enforced quality gates. The AI acts as an intelligent executor that understands intent and adapts — not as a tool that runs predefined scripts.

**Uncertainty before code.** The framework's purpose is not to ship code — it is to reach the moment when shipping code is the *least uncertain remaining option*. Every step must measurably reduce uncertainty (recorded in the plan's `evidence:` block), every Exploration must produce an `insights.md` (the Learning Loop), every plan must define `Kill Criteria` (the exit ramp), and every plan is critiqued by an internal **Challenger** before its gate. See [guidelines/uncertainty-reduction.md](guidelines/uncertainty-reduction.md).

## Core Rules

1. **Steps are sequential** — No step may be skipped
2. **AI enforces, human decides** — AI drives the process and blocks violations; human approves every transition
3. **Context before code** — AI writes no production code without a prior spec
4. **Prototype before production** — Validate UX prototypes before implementing (where applicable)
5. **Ownership stays with the human** — AI delivers suggestions, developers bear responsibility
6. **Gates are blockers** — All criteria must be satisfied before forward transition
7. **Decisions are signed** — Every governed artifact records who proposed and who decided it; AI never writes human decision fields (see [architecture-governance](guidelines/architecture-governance.md))
8. **Approval requires evidence** — Every gate transition records `hypothesis` / `result` / `reasoning` in the plan's `evidence:` block; rubber-stamp approval is forbidden (see [uncertainty-reduction](guidelines/uncertainty-reduction.md))
9. **Every Exploration produces learning** — `insights.md` is mandatory before G2; the lifecycle is a loop, not a pipeline
10. **Every plan can be killed** — `Kill Criteria` is a mandatory section; plans without exit ramps accumulate sunken cost
11. **AI critiques itself** — The **Challenger** role produces top-3 failure modes, ≥2 alternatives, the strongest counter-argument, and a product-coherence check before every G2 (see [02-exploration/challenger.md](02-exploration/challenger.md))
12. **Out-of-scope items become proposals, never disappear** — Gatekeeper subagents (G1/G2/G3) read each plan's NOT-in-Scope and Challenger output and spawn `PROP-NNN` proposals for human triage (see [templates/plan-proposal-template.md](templates/plan-proposal-template.md))
13. **Decisions are clickable, not typed** — Every discrete decision MUST be presented via `AskUserQuestion` with 2-4 labeled options + "Other" text field. This applies to both **planned** decisions (gate transition, scope in/out, ADR choice, approve/reject/revise — see [LIFECYCLE.md — The 6 Decisions per Step](LIFECYCLE.md#the-6-decisions-per-step)) and **ad-hoc forks** that surface mid-work (any 2+ architecturally plausible options where the human owns the choice — see [LIFECYCLE.md — Ad-hoc Decision Forks](LIFECYCLE.md#ad-hoc-decision-forks)). Free-form prose ("Shall we proceed?", "Which would you prefer?") is forbidden for decision points.

## Lifecycle: 3 Steps × 7 Roles × 3 Modes

```
1. Context → 2. Exploration → 3. Production
```

AI operates in exactly one mode at a time. The AI **infers** the current mode from user intent and conversation history — the human simply talks. No structured prompts, no mode declarations, no manual state management required.

Before every response the AI:
1. **Infers** the mode from intent and conversation state (decomposes mixed-intent messages by lifecycle order)
2. **Announces** via adaptive header — full detail on mode changes or blocking, short confirmation when continuing
3. **Checks** gate prerequisites — blocks if unmet, explains what is missing
4. **Acts** within the boundaries of the current mode
5. **Guides** the human to the correct step when a request conflicts with gate state
6. **Falls back** from Production to Exploration when the plan is incomplete, the approach is unviable, or scope changes

| Intent Signals | Detected Mode |
|---------------|---------------|
| "what does", "explain", "analyze", new task, ambiguous | **Context** — Read, verify, ask. No code. |
| "plan", "design", "prototype", "spec" | **Exploration** — Plan, prototype, document. No production code. |
| "implement", "build", "code", "execute the plan" | **Production** — Implement approved plan. No new plans, no scope changes. |

Details: [LIFECYCLE.md — AI Modes](LIFECYCLE.md#ai-modes)

### Mandatory Deliverables

| Step | Deliverables |
|------|-------------|
| **Context** | Context-Plan (CTX), **Problem Statement**, **Hypotheses**, **Risks**, System Spec, Software Architecture, ADRs (fundamental), Context Inventory, Scope Confirmation |
| **Exploration** | Feature Plan/Spec (EXP) with `exploration-mode: A\|B`, ADRs (new decisions), UX Prototype (where applicable), **Challenger output**, **`insights.md`** |
| **Production** | Production-Plan (PRD), Production Code, Validation Result, Updated Documentation, **`insights.md` updated with implementation surprises** |

Plus, on every gate: filled `evidence:` block (`hypothesis` / `result` / `reasoning`) and recorded **Gatekeeper verdict** from `gatekeeper-g1/g2/g3`.

### Quality Gates

| Gate | Transition | Key Rule |
|------|-----------|----------|
| **G1** | Context → Exploration | CTX confirmed, **uncertainty triplet** (Problem Statement / Hypotheses / Risks) drafted, System Spec + Architecture + ADRs + Context Inventory exist, scope confirmed, `evidence:` filled, `gatekeeper-g1` verdict recorded |
| **G2** | Exploration → Production | Feature plan/spec approved with `exploration-mode`, prototype confirmed, **Kill Criteria + `insights.md` + Challenger output** present, `evidence:` filled, `gatekeeper-g2` verdict recorded |
| **G3** | Production → Done | PRD approved, all acceptance criteria fulfilled, build passes, `insights.md` updated with implementation surprises, `evidence:` filled, `gatekeeper-g3` verdict recorded, human approved |

### Interaction Protocol (Claude Code)

The AI interacts with the human via **two UI primitives only**:

| Primitive | Use for | Tool |
|-----------|---------|------|
| **Clickable Question** | All discrete decisions (6 per step, see LIFECYCLE.md) | `AskUserQuestion` — 2-4 options + Other |
| **Draft-Confirm** | All free-form artifacts (Problem Statement, Hypotheses, ADR body, plan text) | Generate markdown draft → `AskUserQuestion`: `accept` / `edit inline` / `regenerate` / `other` |

**Rule:** The AI does not ask open questions in prose. Every decision is a click. Every artifact is a draft you accept or edit. If the AI catches itself writing "Shall we...", "Do you want...", "Which would you prefer...", it MUST convert the sentence into an `AskUserQuestion` call before sending.

Within each step, **7 cross-cutting roles** operate:
**SDLC** · **AI-Plans** · **UX-Tooling** · **DevOps** · **Software-Architecture** · **Context-Engineering** · **Challenger**

Full matrix: [LIFECYCLE.md](LIFECYCLE.md)

## Documentation

| Folder | Content |
|--------|---------|
| [01-context/](01-context/) | Step 1: Understand system, gather context, produce foundational artifacts |
| [02-exploration/](02-exploration/) | Step 2: Plan features, prototype, validate approach |
| [03-production/](03-production/) | Step 3: Build, verify, ship |
| [templates/](templates/) | Templates for plans, specs, ADRs, CLAUDE.md, prototypes |
| [guidelines/](guidelines/) | Cross-cutting quality rules for AI collaboration |
| [integration/](integration/) | How to integrate the framework into projects |

## Plugin Layer (Claude Code, optional)

An executable layer that sits on top of the markdown files. The markdown is source-of-truth; the plugin turns the lifecycle into callable surface area.

| Folder | Content |
|--------|---------|
| [.claude-plugin/](.claude-plugin/) | Plugin manifest (hooks registered here) |
| [commands/](commands/) | Slash commands: `/context`, `/explore`, `/produce`, `/gate-check`, `/new-adr`, `/approve`, `/promote`, `/reject`, `/gate-override` |
| [agents/](agents/) | Subagents: `gatekeeper-g1` / `gatekeeper-g2` / `gatekeeper-g3` (specialised gate validators with proposal-spawning), `gate-validator` (legacy dispatcher), `architecture-reviewer` |
| [skills/](skills/) | Skills: `create-ctx-plan`, `create-exp-plan`, `create-adr` |
| [hooks/](hooks/) | Python hooks: `mode-context.py` (per-turn reminder), `gate-check.py` (blocks code writes without approved EXP plan), `provenance-check.py` (enforces human-only decision fields and non-empty `evidence:` blocks) |

The plugin is **additive** — without it, the framework still works via `@url` loading and AI discipline. With it, gate enforcement becomes mechanical (hooks) and mode transitions become explicit (slash commands).