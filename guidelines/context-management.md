---
name: Context Management
description: AI without context invents things — context is mandatory before any change
type: guideline
---

# Guideline: Context Management

**Rule:** The AI must read the required context (CLAUDE.md, plans, ADRs, affected code) before modifying anything, and must keep context artifacts up to date when things change.

**Why:** AI without context invents APIs, reinvents existing patterns, and contradicts prior decisions. The context hierarchy exists to ground the AI in the project's current reality.

**How to apply:** For every task, read at minimum the project's CLAUDE.md. Add plans/specs for feature work, ADRs and architecture docs for architecture changes, existing code for code changes, and a preview of current state for visual/physical output. Never skip context to save time. Respect artifact ownership in multi-agent setups.

## Context Hierarchy

```
CLAUDE.md (project root)
├── context/architecture/     — Architecture overview
├── context/adr/              — Decisions made
├── context/guidelines/       — Development guidelines
├── context/plans/            — Active and completed plans
├── context/specs/            — Feature specifications
└── <domain-specific>/        — API references, templates, etc.
```

## What AI MUST Read

| Situation | Minimum Context |
|-----------|----------------|
| Any work | CLAUDE.md |
| Feature work | + relevant plan/spec |
| Architecture change | + ADRs + architecture docs |
| Code change | + existing code that is affected |
| Visual / physical output | + preview of current state |

## CLAUDE.md Maintenance

Every active project needs a CLAUDE.md with:
- What is the project (1-2 sentences)
- Current state
- File system overview
- Technical constraints
- Decisions made

This file is the briefing for every AI agent.

## Shared vs. Branch-Local Artifacts

In multi-agent setups, artifacts fall into two categories:

| Category | Artifacts | Rules |
|----------|-----------|-------|
| **Shared** (live on main) | CLAUDE.md, System Spec, Software Architecture | Read-only during feature work. Modified only via PR after merge. Never edited in parallel by multiple agents. |
| **Branch-local** (live on feature branch) | Plans (CTX/EXP/PRD), Feature Specs, ADRs | Created and owned by the agent on its branch. Merged into main via PR. Conflicts resolved by the human. |

**Rule**: Shared artifacts are the single source of truth. If an agent discovers that a shared artifact is outdated, it flags the issue — it does not modify the artifact on its feature branch. Updates to shared artifacts happen on main after the PR is merged.

## Context Rules

1. **Read before write** — Read existing code before modifying it
2. **Use API references** — Do not invent functions that do not exist
3. **Use templates as a guide** — Follow existing patterns, do not invent new ones
4. **Keep context up to date** — Update CLAUDE.md and docs when things change
5. **Respect artifact ownership** — In multi-agent setups, do not modify another agent's branch-local artifacts
