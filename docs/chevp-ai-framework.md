# chevp-ai-framework — AI Reference

> Condensed, machine-readable reference of the chevp-ai-framework.
> Source: https://github.com/chevp/chevp-ai-framework

## Core Rules

1. Steps are sequential — no step may be skipped
2. Human decides — explicit approval at every gate transition
3. Context before code — no production code without a prior spec
4. Prototype before production — validate UX prototypes before implementing (where applicable)
5. Ownership stays with the human — AI suggests, developers bear responsibility

## Lifecycle: 3 Steps

```
Context (G1) → Exploration (G2) → Production (G3)
```

### Step 1: Context — Understand the problem

- Read existing code and documentation before proposing anything
- State understanding: "I understand you want X. This affects Y and Z."
- Identify affected files, patterns, conventions, dependencies
- Surface open questions — ask, don't assume
- Wait for human to confirm scope

**Gate G1**: Problem understood, affected modules identified, scope confirmed by human.

### Step 2: Exploration — Plan and prototype

- Create plan/spec with: goal, scope (in/out), steps, affected files, risks, acceptance criteria
- Written spec required for: features, architecture changes, complex bugfixes
- Verbal confirmation sufficient for: trivial changes (<10 lines)
- Create ADR if architectural decision is made
- Create prototype for visual/UX work (UI, shaders, 3D scenes)
- Prototype workflow: create → human reviews → feedback → iterate → confirm
- Prototype becomes reference for Production

**Gate G2**: Plan/spec approved, prototype confirmed (where applicable), risks documented.

### Step 3: Production — Build, verify, ship

- Implement step-by-step according to plan
- One step at a time, build after each step
- Minimal changes — only what the plan specifies, no scope expansion
- Validate: build verification, spec comparison, preview comparison (visual), tests
- Compare implementation against prototype, flag deviations
- Commit only when asked, stage specific files (never `git add .`)
- Commit convention for plans: `plan(NNN): <short description>`
- Move completed plan to `context/plans/finished/`
- Update CLAUDE.md and docs if context changed

**Gate G3**: All acceptance criteria fulfilled, build passes, no regressions, human approved.

**Backward jumps allowed**: Production → Exploration (plan wrong), Production → Context (fundamental problem). Forward only with passed gate.

## 6 Cross-Cutting Roles

| Role | Scope |
|------|-------|
| SDLC | Process governance, quality gates, step transitions |
| AI-Plans | Plan/spec artifacts, acceptance criteria, scope management |
| UX-Tooling | Prototypes, preview feedback loops, visual validation |
| DevOps | Build verification, commit workflow, CI/CD |
| Software-Architecture | ADRs, pattern enforcement, design decisions |
| Context-Engineering | CLAUDE.md, context hierarchy, documentation maintenance |

## AI Behavior

### MUST

- Begin every task by reading existing code and CLAUDE.md
- Ask open questions instead of assuming
- Wait for human scope confirmation before proceeding
- Create plan/spec before any code
- Wait for human approval before proceeding to next step
- Proceed step-by-step according to plan
- Verify build after each step
- Check each acceptance criterion individually
- Follow existing patterns and conventions

### MUST NOT

- Skip Context and jump to code
- Expand scope ("I also improved X while I was at it")
- Assume requirements without checking
- Write a plan AND immediately implement it
- Skip prototype for visual output
- Proceed without human approval
- Commit or push without being asked
- Force-push or skip git hooks
- Add docstrings/comments/types to unchanged code
- Over-engineer, add feature flags, or create premature abstractions
- Commit code that does not compile

## When Steps May Be Abbreviated

| Scenario | Allowed |
|----------|---------|
| Small bugfix (<10 lines) | Exploration verbal, UX-Tooling omitted |
| Technical refactoring | UX-Tooling omitted |
| Visual feature (UI, shader) | No step skippable |
| Architecture decision | UX-Tooling omitted, ADR mandatory |
| Spike / exploration | Context + Exploration only, no Production |

## Context Hierarchy

```
CLAUDE.md (project root)          ← always read
├── context/architecture/         ← for architecture changes
├── context/adr/                  ← for architecture decisions
├── context/guidelines/           ← development rules
├── context/plans/                ← active plans
│   └── finished/                 ← completed plans
└── context/specs/                ← feature specifications
```

## Project Structure

```
<project>/
├── CLAUDE.md                     ← references this framework
├── context/
│   ├── architecture/
│   ├── adr/
│   ├── guidelines/
│   ├── plans/
│   │   └── finished/
│   └── specs/
└── src/
```

## Integration

No submodule or fork needed. Add this to your project's CLAUDE.md:

```markdown
## Development Process

This project follows the [chevp-ai-framework](https://github.com/chevp/chevp-ai-framework).
Read and follow: https://chevp.github.io/chevp-ai-framework/chevp-ai-framework.md

### Steps (sequential, not skippable)
1. **Context** — Understand problem, gather context, confirm scope
2. **Exploration** — Create plan/spec, prototype (where applicable), obtain approval
3. **Production** — Implement according to plan, validate, deliver

### Rules
- No code without a prior spec (Exploration)
- No production code without prototype confirmation (where applicable)
- No commit without validation (Production)
- When uncertain: STOP and ask
```

The URL points to this file. Claude reads it via `WebFetch` at conversation start and follows the rules. No local copy needed.

## Modular Composition

The framework is composable: Core ⊕ Domain ⊕ External Knowledge (RAG).

| Layer | Role | Stability |
|-------|------|-----------|
| Core (this framework) | Process, lifecycle, guardrails | High — rarely changes |
| Domain Frameworks | Domain-specific patterns and constraints | Medium — evolves with domain |
| External Knowledge (RAG) | Real-time or proprietary context | Dynamic |

Projects can **tighten** framework rules but never **loosen** them.
