# Context-Engineering in Context

> What AI must read and catalogue before any work begins.

## Responsibilities

- Ensure AI has gathered the minimum required context
- Produce the **Context Inventory**: catalogue of existing artifacts
- Follow the context hierarchy
- Verify that CLAUDE.md and relevant documentation are loaded

## Context Inventory (Mandatory Deliverable)

A catalogue of what exists in the project:
- Existing code modules and their purpose
- Documentation files and their state (current / outdated)
- Schemas, APIs, protocols in use
- Conventions and naming patterns
- Dependencies (internal and external)

This inventory becomes the foundation for scope confirmation.

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
- Produce a Context Inventory (catalogue existing artifacts)
- Verify that context is current (not outdated)

### MUST NOT
- Work without reading CLAUDE.md
- Invent APIs or functions without checking references
- Assume context from a previous conversation is still valid
- Skip the Context Inventory because "the project is small"

## Checklist

- [ ] CLAUDE.md has been read
- [ ] Relevant context files are loaded
- [ ] Context Inventory is produced (existing artifacts catalogued)
- [ ] Context is verified as current