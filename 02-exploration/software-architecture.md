# Software-Architecture in Exploration

> New design decisions happen here — fundamental decisions were made in Context.

## Responsibilities

- Create ADRs when **new** architectural decisions arise during feature planning
- Evaluate design alternatives with trade-offs
- Ensure the chosen approach fits existing architecture (established in Context)
- Document risks and consequences

**Important**: Fundamental ADRs (language, protocol, structure) belong in Context. This step handles only decisions that emerge during feature exploration.

## When Is an ADR Needed in Exploration?

- New integration pattern for a specific feature
- Technology choice for a feature component
- Data model extension
- Any feature-level decision that is hard to reverse

## AI Behavior

### MUST
- Reference the Architecture document from Context
- Present alternatives with pros/cons
- Document the chosen approach and the reasoning
- Reference existing ADRs for consistency
- Highlight trade-offs honestly

### MUST NOT
- Make architecture decisions silently
- Ignore existing patterns without justification
- Skip trade-off analysis
- Re-decide fundamental questions already settled in Context ADRs

## Checklist

- [ ] Architecture document from Context has been referenced
- [ ] Alternatives have been evaluated
- [ ] Trade-offs are documented
- [ ] ADR is written (if applicable)
- [ ] Decision is consistent with existing architecture and ADRs