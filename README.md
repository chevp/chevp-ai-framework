# chevp-ai-framework

> AI-assisted Software Development Lifecycle Framework

A structured process for human-AI (Claude) collaboration in software development.

## Why?

Vibe Coding is not progress — it is technical recklessness. AI writes code, but it does not take responsibility. This framework defines clear steps, quality gates, and responsibilities.

## Lifecycle: 3 Steps

![chevp-ai-framework](chevp-ai-framework.png)

Each step produces defined artifacts. No step is skipped.

### Steps

| Step | Purpose |
|------|---------|
| [Context](01-context/) | Understand the problem, gather context, confirm scope |
| [Exploration](02-exploration/) | Plan the solution, prototype, validate the approach |
| [Production](03-production/) | Build, verify, ship |

### Roles (cross-cutting)

| Role | Scope |
|------|-------|
| **SDLC** | Process governance, quality gates, step transitions |
| **AI-Plans** | Plan/spec artifacts, acceptance criteria, scope management |
| **UX-Tooling** | Prototypes, screenshot feedback loops, visual validation |
| **DevOps** | Build verification, commit workflow, CI/CD |
| **Software-Architecture** | ADRs, pattern enforcement, design decisions |
| **Context-Engineering** | CLAUDE.md, context hierarchy, what AI must read |

See [LIFECYCLE.md](LIFECYCLE.md) for the full steps × roles matrix.

## Quick Start

1. Read [LIFECYCLE.md](LIFECYCLE.md) for the overall overview
2. Copy [templates/claude-md-template.md](templates/claude-md-template.md) as `CLAUDE.md` into your project
3. Reference this framework in your project's CLAUDE.md

## Structure

```
01-context/       — Step 1: Understand the problem
02-exploration/   — Step 2: Plan and prototype
03-production/    — Step 3: Build, verify, ship
templates/        — Templates for all artifacts
guidelines/       — Cross-cutting quality rules
integration/      — Integration into existing projects
```

## Principles

- **Prototype ≠ Production** — Quickly generated code must be reviewed
- **Context is mandatory** — AI without context invents things
- **Incremental** — Small steps with validation after each step
