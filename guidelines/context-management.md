# Context Management

> AI without context invents things. Context is mandatory.

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

## Context Rules

1. **Read before write** — Read existing code before modifying it
2. **Use API references** — Do not invent functions that do not exist
3. **Use templates as a guide** — Follow existing patterns, do not invent new ones
4. **Keep context up to date** — Update CLAUDE.md and docs when things change
