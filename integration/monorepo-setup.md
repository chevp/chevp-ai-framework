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
│   ├── guidelines/              ← Development guidelines + extension points
│   │   ├── architecture-invariants.md  ← (optional) Layer rules, forbidden patterns
│   │   ├── review-criteria.md          ← (optional) What to check at each gate
│   │   ├── testing-strategy.md         ← (optional) When/what tests are required
│   │   └── ...                         ← See LIFECYCLE.md § Extension Points
│   ├── plans/                   ← Implementation plans (CTX/EXP/PRD)
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
CTX-NNN-<description>.md               ← Context Plan (open)
EXP-NNN-<description>.md              ← Feature Plan (open)
PRD-NNN-<description>.md              ← Production Plan (open)
finished/CTX-FNNN-<description>.md    ← Context Plan (completed)
finished/EXP-FNNN-<description>.md    ← Feature Plan (completed)
finished/PRD-FNNN-<description>.md    ← Production Plan (completed)
```

Commit convention for plan implementation:

```
ctx(NNN): <short description>      ← Context phase
exp(NNN): <short description>      ← Exploration phase
prd(NNN): <short description>      ← Production phase
```

## Extension Points

The framework defines optional extension points that projects can activate by creating files in `context/guidelines/`. If a file exists, the AI enforces it. See [LIFECYCLE.md § Project-Specific Extension Points](../LIFECYCLE.md#project-specific-extension-points) for the full list.

## AI Mode Tracking

The AI automatically detects and tracks the current lifecycle mode. No manual session state block is needed in your project CLAUDE.md. The AI will announce its detected mode at the start of each response.

The AI infers the mode automatically from user intent — no manual mode declarations needed.
