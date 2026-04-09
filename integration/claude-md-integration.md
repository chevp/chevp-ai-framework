# CLAUDE.md Integration

> How CLAUDE.md enforces the framework.

## Why CLAUDE.md?

`CLAUDE.md` is the file that Claude (AI) automatically reads when opening a project.
It is the primary control mechanism for AI behavior in a project.

## Binding Reference

The most important block in every project CLAUDE.md — place it at the top, before any project-specific content:

```markdown
## STOP — Before Any Change

DO NOT create, edit, or delete any file before:
1. The chevp-ai-framework has been loaded:
   @url https://chevp.github.io/chevp-ai-framework/chevp-ai-framework.md
2. The AI has determined the current lifecycle step (Context / Exploration / Production) and announced it
```

## Hierarchy

```
chevp-ai-framework/CLAUDE.md     ← Framework rules (generic)
    ↓ referenced by
<project>/CLAUDE.md               ← Project rules (specific)
    ↓ supplemented by
<project>/context/guidelines/     ← Detailed rules
```

The project can **tighten** framework rules but not **loosen** them.

## Domain Extension: Patterns over Rules

A domain extension is more than a folder of rules and templates. The most valuable thing a domain layer can carry is its **failure history** — the typical users, the typical misassumptions, and the recurring problems that every project in the domain rediscovers.

Capture this in a `context/domain-patterns.md` file based on [domain-patterns-template](../templates/domain-patterns-template.md). The file:

- Names the **personas** (who works in the domain, what mental model they use)
- Lists **typical misassumptions** (mistakes even experienced practitioners make)
- Catalogues **recurring problem patterns** (problems that show up regardless of feature set)
- Defines **vocabulary** that disambiguates domain-specific words

The Context phase reads it. The Challenger reads it when generating top-3 failure modes. New team members read it before their first plan. Without this artifact, every project re-discovers the same domain pitfalls — and the AI cannot help, because it only sees the current code.

> **Rule of thumb:** if the domain has burned the team more than once, write a pattern. If it has only burned them once, write a risk in the next plan instead.

## How It Works

The `@url` directive in CLAUDE.md tells Claude to fetch the framework reference at conversation start. The URL points to a single auto-generated file (`dist/chevp-ai-framework.md`) that is built from all framework source files by `scripts/build_dist.py` and published via GitHub Pages on every push to `main`.

- No submodule, no fork, no local copy needed
- Consumer projects always get the latest version
- The framework is fully loaded into Claude's context automatically (~263 lines, ~9 KB, ~2,300 tokens)
- Alternative: use the raw GitHub URL: `@url https://raw.githubusercontent.com/chevp/chevp-ai-framework/main/dist/chevp-ai-framework.md`

## Effectiveness

CLAUDE.md works because:
1. Claude reads it automatically at every conversation
2. `@url` fetches the full framework — no manual sync needed
3. It lives in the repo and is versioned
4. Every AI agent (including parallel ones) reads the same rules
5. Process changes are git commits (reviewable)

## Alternative: Claude Code Plugin

For Claude Code users, the framework is also available as a **plugin** that adds an executable layer on top of the markdown files:

- **Slash commands** (`/context`, `/explore`, `/produce`, `/gate-check`, `/new-adr`) make mode transitions explicit instead of relying on intent inference.
- **Subagents** (`gate-validator`, `architecture-reviewer`) validate gates and enforce architectural invariants as isolated specialists.
- **Skills** (`create-ctx-plan`, `create-exp-plan`, `create-adr`) trigger template-driven artifact creation.
- **Hooks** enforce gates mechanically: a `PreToolUse` hook on `Write`/`Edit` asks for confirmation when production code is written without an approved EXP plan; a `UserPromptSubmit` hook injects the lifecycle reminder every turn.

**When to use the plugin**: when you want **mechanical** gate enforcement rather than AI-discipline-based enforcement, or when the team prefers explicit slash commands over intent inference.

**When to stick with `@url` CLAUDE.md**: when working in environments without Claude Code plugin support, or when you want the lightest possible integration.

Both paths use the same lifecycle, templates, and deliverables. They differ only in how the process is *executed*.

See the top-level [README.md — Plugin Layer](../README.md#plugin-layer-claude-code-optional) for installation.