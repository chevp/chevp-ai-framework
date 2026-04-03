# ADR Template

> Architecture Decision Record. Location: `context/adr/ADR-NNN-<description>.md`

```markdown
# ADR-NNN: <Decision Title>

## Status
<Proposed | Accepted | Deprecated | Superseded by ADR-NNN>

## Context
What problem needs to be solved? What constraints exist?

## Decision
What was decided?

## Alternatives

### Alternative A: <Name>
- Pros: ...
- Cons: ...

### Alternative B: <Name>
- Pros: ...
- Cons: ...

## Consequences

### Positive
- ...

### Negative
- ...

### Risks
- ...
```

## ADR Lifecycle

| Transition | Trigger | Rule |
|------------|---------|------|
| **Proposed → Accepted** | Human confirms the decision during Context or Exploration | AI proposes, human approves |
| **Accepted → Superseded** | A new ADR addresses the same decision space | Old ADR must be marked `Superseded by ADR-NNN`; new ADR must reference the old one |
| **Accepted → Deprecated** | Decision is no longer relevant (e.g., module removed) | AI flags during drift detection; human confirms |

### AI Behavior for ADR Lifecycle

- **Before creating a new ADR**: AI must check existing ADRs for overlapping decision space. If found, the new ADR supersedes the old one — not duplicates it.
- **During drift detection**: If the codebase no longer reflects an Accepted ADR, AI must flag it for review (deprecate or supersede).
- **ADR status changes require human approval** — AI proposes, human confirms.
