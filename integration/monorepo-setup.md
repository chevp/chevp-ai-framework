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

Plans follow the convention from the framework:

```
PLAN-NNN-<description>.md       ← Open
finished/PLAN-FNNN-<description>.md  ← Completed
```

Commit convention for plan implementation:

```
plan(NNN): <short description>
```
