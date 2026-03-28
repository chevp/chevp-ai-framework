# CLAUDE.md — chevp-ai-framework

This is a process framework for AI-assisted software development.
It defines the overarching lifecycle that Claude must follow in all projects.

## Core Rules

1. **Steps are sequential** — No step may be skipped
2. **Human decides** — At every step transition, the human must explicitly confirm
3. **Context before code** — AI writes no production code without a prior spec
4. **Prototype before production** — Validate UX prototypes before implementing (where applicable)
5. **Ownership stays with the human** — AI delivers suggestions, developers bear responsibility

## Lifecycle: 3 Steps × 6 Roles

```
1. Context → 2. Exploration → 3. Production
```

Within each step, 6 cross-cutting roles operate:
**SDLC** · **AI-Plans** · **UX-Tooling** · **DevOps** · **Software-Architecture** · **Context-Engineering**

Full matrix: [LIFECYCLE.md](LIFECYCLE.md)

## Documentation

| Folder | Content |
|--------|---------|
| [01-context/](01-context/) | Step 1: Understand problem, gather context |
| [02-exploration/](02-exploration/) | Step 2: Plan, prototype, validate approach |
| [03-production/](03-production/) | Step 3: Build, verify, ship |
| [templates/](templates/) | Templates for plans, specs, ADRs, CLAUDE.md, prototypes |
| [guidelines/](guidelines/) | Cross-cutting quality rules for AI collaboration |
| [integration/](integration/) | How to integrate the framework into projects |
