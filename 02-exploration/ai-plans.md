# AI-Plans in Exploration

> Plan and specify concrete features before writing code.
> The AI enters Exploration mode automatically for this role. Optional prefix: `chp-exploration:`. AI plans, prototypes, and documents. No production code.

## Responsibilities

- Create concrete **feature** implementation plans with defined steps
- Define scope boundaries and acceptance criteria
- Identify risks and alternatives
- List affected files and expected changes

**Important**: System Spec and Architecture belong to Context (Step 1). This step focuses on **feature-level** planning only.

## Artifact Types

### Plan (PLAN-NNN-*.md)
For concrete implementation tasks with defined steps. See [plan-template](../templates/plan-template.md).

### Spec
For detailed feature specifications. See [spec-template](../templates/spec-template.md).

### Architecture Decision Record (ADR-NNN-*.md)
Only for **new** decisions arising during exploration. Fundamental ADRs belong in Context. See [adr-template](../templates/adr-template.md).

### Informal Spec
For small changes, a verbal description in chat is sufficient — but the human must confirm.

## AI Behavior

### MUST
- Verify that System Spec + Architecture from Context are current before planning
- Formulate steps concretely enough for direct implementation
- List all affected files
- Name alternatives where appropriate
- Define clear acceptance criteria
- Wait for approval before writing code

### MUST NOT
- Write a plan AND immediately implement it
- Write production code (wrong mode — that belongs to Production)
- Hide risks
- Secretly expand scope
- Leave acceptance criteria vague
- Re-create system-level artifacts that should already exist from Context

## Checklist

- [ ] System Spec and Architecture from Context are verified as current
- [ ] Feature plan/spec exists (file or chat confirmation)
- [ ] Steps are actionable and ordered
- [ ] Affected files are listed
- [ ] Scope and non-scope are explicit
- [ ] Risks are documented
- [ ] Acceptance criteria are defined
- [ ] Human has granted approval