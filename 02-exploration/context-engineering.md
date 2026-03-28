# Context-Engineering in Exploration

> Plans and specs become part of the project context.

## Responsibilities

- Store plans and specs in the correct location within the project
- Keep references between artifacts consistent
- Ensure new plans/specs are discoverable by future AI agents

## Where to Store Artifacts

```
context/
├── plans/            — PLAN-NNN-<description>.md
│   └── finished/     — PLAN-FNNN-<description>.md (completed)
├── specs/            — Feature specifications
├── adr/              — ADR-NNN-<description>.md
└── architecture/     — Architecture overview documents
```

## AI Behavior

### MUST
- Store plans/specs in `context/` following naming conventions
- Cross-reference related artifacts (plan → ADR, spec → prototype)
- Ensure naming conventions are followed (PLAN-NNN, ADR-NNN)

### MUST NOT
- Store plans/specs in ad-hoc locations
- Leave artifacts without clear naming
- Create duplicate artifacts

## Checklist

- [ ] Plan/spec is stored in the correct directory
- [ ] Naming convention is followed
- [ ] Cross-references between artifacts are correct
