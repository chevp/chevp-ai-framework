---
name: create-adr
description: Use when the user wants to record an architecture decision, says "write an ADR", "new ADR", "document this decision", or when a non-trivial architectural choice is made during Context or Exploration that future contributors need to understand.
---

# Create Architecture Decision Record (ADR)

ADRs capture architectural decisions with their context, alternatives, and consequences.

## When to trigger

- A fundamental architectural choice is being made (Context step — required for G1)
- A new decision arises during Exploration (as needed for G2)
- User explicitly asks to document a decision

## Steps

1. **Read the template**: [templates/adr-template.md](../../templates/adr-template.md).
2. **Find the ADR directory** (`context/adrs/`, `docs/adrs/`, or per project CLAUDE.md).
3. **Determine next number** (ADR-NNNN format, zero-padded).
4. **Fill in**:
   - Title (short, decision-focused, e.g. "Use PostgreSQL for primary storage")
   - Status: `Proposed` (becomes `Accepted` after human approval)
   - Context: the forces at play, constraints, requirements
   - Decision: what was decided, stated clearly
   - Alternatives considered (at least one)
   - Consequences: positive AND negative, short-term AND long-term
5. **Check** with `architecture-reviewer` subagent if the decision might conflict with existing ADRs.
6. **Confirm** path and content with user before writing.

## Rules

- Never mark an ADR `Accepted` without explicit human approval.
- One decision per ADR.
- Supersede rather than edit accepted ADRs: if a decision changes, write a new ADR with `Status: Accepted, supersedes ADR-XXXX` and update the old one to `Superseded by ADR-YYYY`.
