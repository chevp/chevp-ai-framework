# AI-Plans in Exploration

> Plan and specify the solution before writing code.

## Responsibilities

- Create concrete implementation plans with defined steps
- Define scope boundaries and acceptance criteria
- Identify risks and alternatives
- List affected files and expected changes

## Artifact Types

### Plan (PLAN-NNN-*.md)
For concrete implementation tasks with defined steps. See [plan-template](../templates/plan-template.md).

### Spec
For detailed feature specifications. See [spec-template](../templates/spec-template.md).

### Architecture Decision Record (ADR-NNN-*.md)
For architecture decisions with alternatives and trade-offs. See [adr-template](../templates/adr-template.md).

### Informal Spec
For small changes, a verbal description in chat is sufficient — but the human must confirm.

## AI Behavior

### MUST
- Formulate steps concretely enough for direct implementation
- List all affected files
- Name alternatives where appropriate
- Define clear acceptance criteria
- Wait for approval before writing code

### MUST NOT
- Write a plan AND immediately implement it
- Hide risks
- Secretly expand scope
- Leave acceptance criteria vague

## Checklist

- [ ] Plan/spec exists (file or chat confirmation)
- [ ] Steps are actionable and ordered
- [ ] Affected files are listed
- [ ] Scope and non-scope are explicit
- [ ] Risks are documented
- [ ] Acceptance criteria are defined
- [ ] Human has granted approval
