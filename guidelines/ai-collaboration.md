# AI-Collaboration Guidelines

> How human and AI collaborate effectively.

## Core Understanding

- **Prototype ≠ Production** — Quickly generated code must be reviewed and understood
- **Ownership stays with the human** — AI delivers suggestions, developers bear responsibility
- **Understanding before speed** — Better slower, but with full clarity

## AI as an Actor

AI is a tool, not an autonomous developer. It:
- **Analyzes** the codebase and identifies patterns
- **Suggests** solutions with trade-offs
- **Implements** after explicit approval
- **Validates** against spec and visual references

It **does not decide** about:
- Scope and priorities
- Architecture direction
- When something is "done"
- Whether code gets committed/pushed

## Effective Communication

### Human → AI
- Provide context: What is the goal, not just the task
- Name constraints: What MUST NOT be changed
- Be specific with feedback: "more to the left" instead of "that doesn't work"

### AI → Human
- Ask questions instead of making assumptions
- Present alternatives with trade-offs
- Stop when uncertain
- No summaries at the end (the human can read the diff)

## Anti-Patterns

| Mistake | Consequence | Better |
|---------|------------|--------|
| "Build the complete feature" | Inconsistent results | Step by step with feedback |
| Let AI work without context | Hallucinated APIs, wrong patterns | Provide CLAUDE.md + API reference |
| Visuals without screenshot | Invisible errors | Screenshot feedback loop |
| Change too much at once | Hard to review, regressions | Small steps |
