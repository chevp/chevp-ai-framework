# Context-Engineering in Context

> What AI must read before any work begins.

## Responsibilities

- Ensure AI has gathered the minimum required context
- Follow the context hierarchy
- Verify that CLAUDE.md and relevant documentation are loaded

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

## AI Behavior

### MUST
- Read CLAUDE.md at the start of every task
- Load relevant context files before analyzing
- Verify that context is current (not outdated)

### MUST NOT
- Work without reading CLAUDE.md
- Invent APIs or functions without checking references
- Assume context from a previous conversation is still valid

## Checklist

- [ ] CLAUDE.md has been read
- [ ] Relevant context files are loaded
- [ ] Context is verified as current
