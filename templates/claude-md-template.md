# CLAUDE.md Template

> Copy this template as `CLAUDE.md` into your project root and customize it.

```markdown
# CLAUDE.md — <Project Name>

## Development Process

This project follows the [chevp-ai-framework](https://github.com/chevp/chevp-ai-framework) lifecycle.
Claude MUST follow the 3-step order:

1. **Context** — Understand problem, gather context, confirm scope
2. **Exploration** — Create plan/spec, prototype (where applicable), obtain approval
3. **Production** — Implement, validate, deliver

No code without a prior spec. No production code without a prior UX prototype (where applicable).

### Roles
Each step involves cross-cutting roles: SDLC, AI-Plans, UX-Tooling, DevOps, Software-Architecture, Context-Engineering.
See [LIFECYCLE.md](https://github.com/chevp/chevp-ai-framework/blob/main/LIFECYCLE.md) for the full matrix.

## What Is This Project?

<1-3 sentences: What does the project do, for whom, why>

## Architecture

<High-level architecture, key decisions>

## Documentation

| Folder | Content |
|--------|---------|
| context/plans/ | Implementation plans |
| context/adr/ | Architecture Decision Records |
| context/guidelines/ | Development guidelines |

## Build Commands

<How to build the project>

## Conventions

<Project-specific rules that AI must follow>
```
