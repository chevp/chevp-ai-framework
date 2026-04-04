# ADR Template

> Architecture Decision Record. Location: `context/adr/ADR-NNN-<description>.md`

```markdown
---
id: ADR-NNN
type: ADR
status: draft            # draft | proposed | accepted | superseded | deprecated
proposed-by: ai          # ai | human | pair
decided-by: —            # human (required when status advances past proposed)
approved-by: —           # human identifier
approved-at: —           # YYYY-MM-DD
supersedes: —            # optional prior ADR id
---

# ADR-NNN: <Decision Title>

## Status
<Proposed | Accepted | Deprecated | Superseded by ADR-NNN>

(Status here mirrors the frontmatter `status` field. The frontmatter is the source of truth for governance — see [guidelines/architecture-governance.md](../guidelines/architecture-governance.md).)

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
- **Provenance is mechanical**: AI may only set `proposed-by`. The `decided-by`, `approved-by`, and `approved-at` fields are written by a human via the `/approve <ADR-id>` slash command. See [guidelines/architecture-governance.md](../guidelines/architecture-governance.md).
