# Step 1: Context

> Understand the problem before proposing solutions.

## Goal

Understand the problem, gather context, define scope. Every change begins with understanding.

## When

Always. No exceptions.

## Inputs

- User requirement (feature, bug, idea)
- Existing code / architecture
- CLAUDE.md and project documentation

## Activities

- Explore and understand the codebase
- Identify existing patterns, conventions, and dependencies
- Capture constraints and open questions
- Formulate scope clearly

## Outputs

- Clear problem description (1-2 sentences)
- List of affected components/modules
- Open questions resolved with the human
- Human-confirmed scope

## Roles Active in This Step

| Role | Responsibility |
|------|---------------|
| [SDLC](sdlc.md) | Process governance, scope confirmation |
| [AI-Plans](ai-plans.md) | Problem formulation, initial scope definition |
| [Software-Architecture](software-architecture.md) | Codebase analysis, dependency mapping |
| [Context-Engineering](context-engineering.md) | What AI must read, context hierarchy |

## Quality Gate G1: Context Complete

- [ ] Problem is understood and can be described in 1-2 sentences
- [ ] Affected files/modules are identified
- [ ] Existing patterns are understood
- [ ] Dependencies are known
- [ ] All open questions are resolved with the human
- [ ] Human has confirmed scope

**Only proceed to [Exploration](../02-exploration/) after G1 is passed.**
