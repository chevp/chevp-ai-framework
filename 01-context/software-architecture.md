# Software-Architecture in Context

> Codebase analysis, dependency mapping, existing patterns.

## Responsibilities

- Analyze the codebase to understand existing architecture
- Identify affected modules and their dependencies
- Recognize existing patterns, conventions, and constraints
- Review relevant ADRs and architecture documentation

## AI Behavior

### MUST
- Read existing code before proposing any changes
- Identify patterns and conventions used in the project
- Map dependencies that could be affected
- Check existing ADRs for prior decisions on this area

### MUST NOT
- Make assumptions about architecture without reading the code
- Propose architectural changes during Context (that belongs to Exploration)
- Overlook existing conventions

## Checklist

- [ ] Existing code in the affected area has been read
- [ ] Patterns and conventions are identified
- [ ] Dependencies are mapped
- [ ] Relevant ADRs have been reviewed (if they exist)
