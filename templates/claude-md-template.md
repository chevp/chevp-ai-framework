# CLAUDE.md Template

> Copy this template as `CLAUDE.md` into your project root and customize it.

```markdown
# CLAUDE.md — <Project Name>

## Development Process

This project follows the [chevp-ai-framework](https://github.com/chevp/chevp-ai-framework).
@url https://chevp.github.io/chevp-ai-framework/chevp-ai-framework.md

### Steps (sequential, not skippable)
1. **Context** — System spec, architecture, ADRs, context inventory, confirm scope
2. **Exploration** — Feature plan/spec, prototype (where applicable), obtain approval
3. **Production** — Implement per plan, validate, deliver

### Gates (blockers)
- **G1**: System Spec + Architecture + ADRs + Context Inventory, scope confirmed
- **G2**: Plan/spec approved, prototype confirmed (where applicable)
- **G3**: All criteria fulfilled, build passes, human approved

### Rules
- No code without spec — no production without prototype (where applicable)
- Gates are blockers — when uncertain: STOP and ask

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