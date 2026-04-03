# Context-Engineering in Exploration

> Plans and specs become part of the project context.

## Responsibilities

- Store plans and specs in the correct location within the project
- Keep references between artifacts consistent
- Ensure new plans/specs are discoverable by future AI agents

## Where to Store Artifacts

```
context/
├── plans/            — EXP-NNN-<description>.md
│   └── finished/     — EXP-FNNN-<description>.md (completed)
├── specs/            — Feature specifications
├── adr/              — ADR-NNN-<description>.md
└── architecture/     — Architecture overview documents
```

## Multi-Agent Artifact Naming

When multiple agents work in parallel on the same repository, artifact IDs must be unique per branch to prevent collisions at merge time:

- Use **task-scoped prefixes** in artifact names: `EXP-NNN-<task-keyword>-<description>.md`
- Assign **non-overlapping number ranges** per agent (e.g., Agent A: 100–199, Agent B: 200–299) or use the branch/task name as disambiguator
- At merge time, the human resolves any numbering conflicts

## AI Behavior

### MUST
- Store plans/specs in `context/` following naming conventions
- Cross-reference related artifacts (plan → ADR, spec → prototype)
- Ensure naming conventions are followed (EXP-NNN, ADR-NNN)
- Verify that Context Inventory from Step 1 is still current
- Use unique, task-scoped artifact IDs when working on a feature branch (multi-agent scenarios)

### MUST NOT
- Store plans/specs in ad-hoc locations
- Leave artifacts without clear naming
- Create duplicate artifacts
- Use artifact IDs that could collide with parallel agents' artifacts
- Overwrite Context-phase artifacts (System Spec, Architecture) without going back to Context

## Checklist

- [ ] Plan/spec is stored in the correct directory
- [ ] Naming convention is followed
- [ ] Cross-references between artifacts are correct
