# Monorepo Integration

> How to integrate the framework into an existing monorepo.

## Recommended Directory Structure

```
<project-root>/
├── CLAUDE.md                    ← Project CLAUDE.md (references framework)
├── context/
│   ├── README.md                ← Overview of context/
│   ├── architecture/            ← Architecture documents
│   ├── adr/                     ← Architecture Decision Records
│   ├── guidelines/              ← Development guidelines
│   ├── plans/                   ← Implementation plans
│   │   └── finished/            ← Completed plans
│   ├── specs/                   ← Feature specifications
│   └── workflows/               ← Recurring workflows
├── src/                         ← Production code
└── ...
```

## Setup

### 1. Create CLAUDE.md

Copy [claude-md-template.md](../templates/claude-md-template.md) as `CLAUDE.md` into the project root.

### 2. Create context/ folder

```bash
mkdir -p context/{architecture,adr,guidelines,plans/finished,specs}
```

### 3. Framework reference in CLAUDE.md

Add the following block to your project CLAUDE.md:

```markdown
## Development Process

This project follows the [chevp-ai-framework](https://github.com/chevp/chevp-ai-framework).
Read and follow: https://chevp.github.io/chevp-ai-framework/chevp-ai-framework.md

Claude MUST follow the 3-step order:
1. Context → 2. Exploration → 3. Production
```

### 4. Customize guidelines

The guidelines in `context/guidelines/` can be project-specific.
Generic guidelines come from the framework, specific ones stay in the project.

## Plan Workflow

Three plan types follow the convention from the framework:

```
CPLAN-NNN-<description>.md             ← Context Plan (open)
PLAN-NNN-<description>.md              ← Feature Plan (open)
PPLAN-NNN-<description>.md             ← Production Plan (open)
finished/CPLAN-FNNN-<description>.md   ← Context Plan (completed)
finished/PLAN-FNNN-<description>.md    ← Feature Plan (completed)
finished/PPLAN-FNNN-<description>.md   ← Production Plan (completed)
```

Commit convention for plan implementation:

```
cplan(NNN): <short description>    ← Context phase
plan(NNN): <short description>     ← Exploration phase
pplan(NNN): <short description>    ← Production phase
```

## AI Modes

Add a Session State block to your project CLAUDE.md to track the current AI mode:

```markdown
## Current Session State
- **Mode**: chp-context | chp-exploration | chp-production
- **Active Plan**: PLAN-NNN (or none)
- **Gate Status**: G1 ○/✓ | G2 ○/✓ | G3 ○/✓
```
