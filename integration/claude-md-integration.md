# CLAUDE.md Integration

> How CLAUDE.md enforces the framework.

## Why CLAUDE.md?

`CLAUDE.md` is the file that Claude (AI) automatically reads when opening a project.
It is the primary control mechanism for AI behavior in a project.

## Binding Reference

The most important block in every project CLAUDE.md:

```markdown
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

### Roles (cross-cutting across all steps)
SDLC, AI-Plans, UX-Tooling, DevOps, Software-Architecture, Context-Engineering

### Rules
- No code without a prior spec (Exploration)
- No production code without prototype confirmation (where applicable)
- No commit without validation (Production)
- Gates are blockers — all criteria must be satisfied before transition
- When uncertain: STOP and ask
```

## Hierarchy

```
chevp-ai-framework/CLAUDE.md     ← Framework rules (generic)
    ↓ referenced by
<project>/CLAUDE.md               ← Project rules (specific)
    ↓ supplemented by
<project>/context/guidelines/     ← Detailed rules
```

The project can **tighten** framework rules but not **loosen** them.

## Effectiveness

CLAUDE.md works because:
1. Claude reads it automatically at every conversation
2. It lives in the repo and is versioned
3. Every AI agent (including parallel ones) reads the same rules
4. Process changes are git commits (reviewable)