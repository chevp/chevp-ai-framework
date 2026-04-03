# Software-Architecture in Context

> Architecture document and fundamental ADRs — before any solution is proposed.

## Responsibilities

- Produce the **Software Architecture** document: layers, modules, communication paths, technology stack
- Produce **ADRs** for all fundamental design decisions
- Analyze the codebase to understand existing architecture
- Identify affected modules and their dependencies
- Recognize existing patterns, conventions, and constraints

## Software Architecture Document (Mandatory Deliverable)

The Architecture document covers:
- High-level layers and modules
- Communication paths (internal and external)
- Technology stack
- Key constraints and trade-offs

For existing projects: verify the architecture document is still accurate. Update if needed.

## ADRs — Architecture Decision Records (Mandatory Deliverable)

Fundamental decisions that must be recorded as ADRs in Context:
- Why this language / framework?
- Why this protocol / communication pattern?
- Why this structure / module layout?
- Why this data model / storage approach?

These are **system-level** decisions. Feature-level decisions belong in Exploration.

Template: [adr-template](../templates/adr-template.md)

## Architecture Drift Detection

Before proceeding, the AI **must** verify that the Architecture document still matches the actual codebase. If drift is detected (e.g., modules added/removed, communication paths changed, technology stack updated), the Architecture document must be updated **before** any other work continues.

This is a process rule, not a domain rule — it ensures the documented architecture remains a reliable source of truth.

## AI Behavior

### MUST
- Produce or verify the Architecture document before any solution is proposed
- **Verify architecture-to-code alignment** (drift detection) before proceeding
- Produce or verify fundamental ADRs
- Read existing code before proposing any changes
- Identify patterns and conventions used in the project
- Map dependencies that could be affected
- Check existing ADRs for prior decisions on this area

### MUST NOT
- Make assumptions about architecture without reading the code
- Propose architectural changes during Context (solution design belongs to Exploration)
- Overlook existing conventions
- Skip ADRs because "the decisions are obvious"
- **Proceed with outdated Architecture documentation when drift is detected**

## Artifact Boundary

| Artifact | Context (Step 1) | Exploration (Step 2) |
|----------|-----------------|---------------------|
| Architecture Document | **Mandatory** | — |
| ADRs (fundamental decisions) | **Mandatory** | Only for new decisions arising during exploration |

## Architecture Invariants (Extension Point)

Projects **may** define architecture invariants in `context/guidelines/architecture-invariants.md`. If this file exists, the AI **must** check every invariant when making or reviewing code changes.

The framework defines the mechanism — the invariants themselves are project-specific. Examples of what projects might define:
- Layer dependency rules (e.g., "UI must not import from DB directly")
- Forbidden patterns (e.g., "no God objects", "no Service Locator")
- Module boundary rules (e.g., "module A must not depend on module B")

## Checklist

- [ ] Architecture document exists and is current (drift detection passed)
- [ ] Fundamental ADRs are written
- [ ] Existing code in the affected area has been read
- [ ] Patterns and conventions are identified
- [ ] Dependencies are mapped
- [ ] Relevant existing ADRs have been reviewed