# Software-Architecture in Production

> Follow existing patterns. No new decisions here.

## Responsibilities

- Enforce existing patterns and conventions during implementation
- Prevent over-engineering and scope creep
- Ensure code quality matches the project's standards

## Rules

- Use existing patterns — do not introduce new ones
- Follow conventions found during Context
- Minimal changes — only what the plan specifies
- No abstractions for hypothetical future requirements

## Anti-Patterns

| Mistake | Better |
|---------|--------|
| "I also refactored X while I was at it" | Only implement the plan |
| Over-engineering / feature flags | Minimal solution |
| Backwards-compatibility hacks | Simply change the old code |
| 3 similar lines → premature abstraction | 3 lines are OK |
| Keep `_unused` variables | Delete them |

## AI Behavior

### MUST
- Read existing code before modifying it
- Follow patterns identified during Context
- Keep changes minimal and plan-scoped

### MUST NOT
- "Improve" code that is not in scope
- Add docstrings, comments, or type annotations to unchanged code
- Add error handling for impossible scenarios
- Create helpers/utilities for one-time operations
- Introduce new patterns without an ADR

## Checklist

- [ ] Existing patterns are followed
- [ ] No over-engineering
- [ ] No scope expansion beyond the plan
- [ ] No new patterns introduced without justification
