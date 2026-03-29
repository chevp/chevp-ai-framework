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

## How It Works

The `@url` directive in CLAUDE.md tells Claude to fetch the framework reference at conversation start. The URL points to a single auto-generated file (`dist/chevp-ai-framework.md`) that is built from all framework source files by `scripts/build_dist.py` and published via GitHub Pages on every push to `main`.

- No submodule, no fork, no local copy needed
- Consumer projects always get the latest version
- The framework is fully loaded into Claude's context automatically (~263 lines, ~9 KB, ~2,300 tokens)
- Alternative: use the raw GitHub URL: `@url https://raw.githubusercontent.com/chevp/chevp-ai-framework/main/dist/chevp-ai-framework.md`

## Effectiveness

CLAUDE.md works because:
1. Claude reads it automatically at every conversation
2. `@url` fetches the full framework — no manual sync needed
3. It lives in the repo and is versioned
4. Every AI agent (including parallel ones) reads the same rules
5. Process changes are git commits (reviewable)