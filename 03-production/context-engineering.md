# Context-Engineering in Production

> Keep project context up to date after delivery.

## Responsibilities

- Update CLAUDE.md if project context has changed
- Write ADR if an architecture decision was made during Production
- Ensure documentation reflects the delivered changes

## Post-Delivery Updates

| Document | Update When |
|----------|------------|
| CLAUDE.md | Project context, architecture, or conventions changed |
| ADR | An architecture decision was made or revised |
| context/architecture/ | Structural changes were delivered |
| context/guidelines/ | New conventions were established |

## AI Behavior

### MUST
- Check if CLAUDE.md needs updating after delivery
- Flag documentation that has become outdated
- Update plan status (move to `finished/`)

### MUST NOT
- Skip documentation updates
- Leave stale context for future AI agents
- Create unnecessary documentation

## Checklist

- [ ] CLAUDE.md is current
- [ ] ADR written if architecture decision was made
- [ ] Plan moved to `finished/` (if plan-based)
- [ ] No stale documentation remains
