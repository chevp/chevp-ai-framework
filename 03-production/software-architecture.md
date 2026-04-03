# Software-Architecture in Production

> Follow existing patterns. No new decisions here.

## Responsibilities

- Enforce existing patterns and conventions during implementation
- Prevent over-engineering and scope creep
- Ensure code quality matches the project's standards

## Architecture Drift Detection

Before implementing, the AI **must** verify that the Architecture document still matches the actual codebase. If drift is detected since Context, the AI must propose a backward jump to Context to update the Architecture document before continuing.

## Rules

- Use existing patterns — do not introduce new ones
- Follow conventions found during Context
- Minimal changes — only what the plan specifies
- No abstractions for hypothetical future requirements

## Decision Comments

When a code change has a **non-obvious reason**, the AI must add a brief inline comment that explains the reason directly — without referencing plans, ADRs, or any external artifacts. The comment must be self-contained and understandable on its own.

**When to add**: Only when the "why" is not evident from reading the code itself.
**When NOT to add**: Obvious changes, trivial logic, self-documenting code.

Examples:

```
// timeout 30s instead of default 10s — upstream API has cold-start latency up to 25s
client.setTimeout(30_000);

// rate limit 5 req/s per user — brute-force protection for login endpoint
rateLimiter.configure(5, PER_SECOND);

// sorted descending — most recent entries must appear first in the feed
results.sort(byDate, DESC);
```

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
- **Verify architecture-to-code alignment** before implementing (drift detection)
- Read existing code before modifying it
- Follow patterns identified during Context
- Keep changes minimal and plan-scoped
- **Add a self-contained inline comment when a code change has a non-obvious reason**

### MUST NOT
- "Improve" code that is not in scope
- Add docstrings, comments, or type annotations to unchanged code
- Add error handling for impossible scenarios
- Create helpers/utilities for one-time operations
- Introduce new patterns without an ADR
- **Implement an architectural decision that has no corresponding ADR** — if the implementation requires a decision not covered by an existing ADR, the AI must stop and propose a fallback to Exploration to create the ADR first
- **Reference plans, ADRs, or external artifacts in inline code comments**

## Checklist

- [ ] Architecture drift detection passed
- [ ] Existing patterns are followed
- [ ] No over-engineering
- [ ] No scope expansion beyond the plan
- [ ] No new patterns introduced without justification
