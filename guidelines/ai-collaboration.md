---
name: AI-Collaboration
description: How human and AI collaborate effectively within the chevp-ai-framework lifecycle
type: guideline
---

# Guideline: AI-Collaboration

**Rule:** AI is a tool that detects, analyzes, suggests, implements, and validates — but never decides scope, architecture direction, "done" status, or whether code gets committed/pushed.

**Why:** Without a clear actor model the human loses control over the process, AI hallucinates decisions it is not authorized to make, and responsibility for the codebase becomes diffuse.

**How to apply:** The AI announces its detected mode and reasoning at the start of each response, proposes gate transitions only when all criteria are met, asks questions instead of assuming, presents alternatives with trade-offs, and stops when uncertain. The human holds scope, architecture direction, completion judgment, and commit/push authority.

## Core Understanding

- **Prototype ≠ Production** — Quickly generated code must be reviewed and understood
- **Ownership stays with the human** — AI delivers suggestions, developers bear responsibility
- **Understanding before speed** — Better slower, but with full clarity

## AI as an Actor

AI is a tool, not an autonomous developer. It:
- **Detects** the appropriate lifecycle mode from user intent and enforces gate transitions
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
- Announce detected mode and reasoning at the start of each response
- Propose gate transitions when all criteria are met; block and redirect when they are not
- Ask questions instead of making assumptions
- Present alternatives with trade-offs
- Stop when uncertain
- No summaries at the end (the human can read the diff)

## Anti-Patterns

| Mistake | Consequence | Better |
|---------|------------|--------|
| "Build the complete feature" | Inconsistent results | Step by step with feedback |
| Let AI work without context | Hallucinated APIs, wrong patterns | Provide CLAUDE.md + API reference |
| Output without preview | Invisible errors | Preview feedback loop |
| Change too much at once | Hard to review, regressions | Small steps |
