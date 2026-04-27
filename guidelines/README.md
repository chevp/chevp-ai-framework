# guidelines/

Framework-level rules for `chevp-ai-framework`. Each file is a single, focused guideline.

## File format

Every guideline uses memory-style frontmatter plus a **Rule / Why / How to apply** header, mirroring Claude's memory conventions:

```markdown
---
name: <Guideline name>
description: <one-line description>
type: guideline
---

# Guideline: <Title>

**Rule:** <the rule stated plainly>

**Why:** <reason>

**How to apply:** <concrete application — when/where this kicks in>

## <Additional sections as needed>
```

The **Rule / Why / How to apply** block is the minimum. Add sections only where they pay for themselves (tables, examples, anti-patterns, context rules).

## Canonical format

The format is defined canonically by [chevp-workflow/guidelines/README.md](https://github.com/chevp/chevp-workflow/blob/main/guidelines/README.md). This repo adopts it verbatim. When the canonical format changes, updates propagate here via a workspace plan under [chevp-workflow](https://github.com/chevp/chevp-workflow).

## Current guidelines

| File | Rule |
|:-----|:-----|
| [ai-collaboration.md](ai-collaboration.md) | AI is a tool — detects, suggests, implements. The human decides scope, architecture, "done", and commits |
| [context-management.md](context-management.md) | Read required context before any change; keep context artifacts up to date |
| [plan-granularity.md](plan-granularity.md) | Plans must match their type, size range, and minimum-substance requirements |
| [architecture-governance.md](architecture-governance.md) | Every governed artifact records who proposed and who decided it; `/approve` is the only path to human-signed decisions |
| [cross-platform.md](cross-platform.md) | If a project targets desktop + mobile, platform parity is enforced from commit #1 — no retrofit |
| [paragraph-numbering.md](paragraph-numbering.md) | Hierarchical §-numbering for plans — stable, tree-structured IDs organized by thematic chapters |
<<<<<<< Updated upstream
| [knowledge-routing.md](knowledge-routing.md) | Project- and reference-knowledge must land in a governance-eligible artifact (ADR, Context Inventory, plan, `insights.md` pointer) — never in free-form memory |
=======
| [ask-user-question.md](ask-user-question.md) | Every question to the user goes through `AskUserQuestion` with concrete clickable options — no free-text questions buried in prose |
>>>>>>> Stashed changes
