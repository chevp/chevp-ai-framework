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

## Multi-Agent Setup

Multiple AI agents can work in parallel on the same project, each following the full lifecycle independently.

### Prerequisites

- Each agent works on its own **feature branch**
- Each agent works in its own **working directory** (git worktree or separate clone)
- All agents read the same **CLAUDE.md** and the same framework

### Setup with Git Worktrees

```bash
# Main working directory
cd <project-root>

# Create worktrees for parallel agents
git worktree add ../project-agent-a feature/auth
git worktree add ../project-agent-b feature/dashboard
git worktree add ../project-agent-c feature/csv-import
```

Each worktree is a separate directory with its own branch — a separate Claude Code session (or Agent SDK instance) connects to each.

### Assigning Tasks to Agents

Each agent receives a task with clear scope boundaries:

```
Agent A: "Implement OAuth2 login — backend only, no frontend"
Agent B: "Build metrics dashboard — frontend only, uses existing API"
Agent C: "Optimize CSV import — performance only, no schema changes"
```

The human ensures scopes do not overlap. Overlapping scopes lead to merge conflicts.

### Gate Review Workflow

```
Agent A: [Context] ────→ G1 ready ──→ human reviews ──→ approved ──→ [Exploration] ...
Agent B: [Context] ──→ G1 ready ──→ human reviews ──→ approved ──→ [Exploration] ...
Agent C: [Context] ─────→ G1 ready ──→ human reviews ──→ approved ──→ [Exploration] ...
```

Gates arrive asynchronously. The human reviews and approves each gate independently. Agents continue working after approval without waiting for other agents.

### Merge Order

After all agents complete Production (G3 passed):
1. Merge the branch with fewest conflicts first
2. Rebase remaining branches onto updated main
3. Resolve conflicts — especially in shared artifacts (CLAUDE.md, Architecture, ADRs)
4. Run integration tests after each merge

### Cleanup

```bash
# After merging, remove worktrees
git worktree remove ../project-agent-a
git worktree remove ../project-agent-b
git worktree remove ../project-agent-c
```
