# CLAUDE.md Template

> Copy this template as `CLAUDE.md` into your project root and customize it.

```markdown
# CLAUDE.md — <Project Name>

## Development Process

This project follows the [chevp-ai-framework](https://github.com/chevp/chevp-ai-framework).
Read and follow: https://chevp.github.io/chevp-ai-framework/chevp-ai-framework.md

### Steps (sequential, not skippable)
1. **Context** — System spec, architecture, ADRs, context inventory, confirm scope
2. **Exploration** — Create feature plan/spec, prototype (where applicable), obtain approval
3. **Production** — Implement according to plan, validate, deliver

### Quality Gates (blockers)
- **G1**: System Spec + Architecture + ADRs + Context Inventory exist, scope confirmed
- **G2**: Feature plan/spec approved, prototype confirmed (where applicable)
- **G3**: All acceptance criteria fulfilled, build passes, human approved

No code without a prior spec. No production code without a prior UX prototype (where applicable). Gates are blockers — all criteria must be satisfied before transition.

### Roles
Each step involves cross-cutting roles: SDLC, AI-Plans, UX-Tooling, DevOps, Software-Architecture, Context-Engineering.

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