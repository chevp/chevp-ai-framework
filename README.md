# chevp-ai-framework

**AI writes the code. You stay in control.**

Three steps. Three checkpoints. No surprise commits.

A simple workflow that lets AI do the heavy lifting — and lets you stop it before it ships something you didn't agree to. Works with Claude Code, Cursor, or any AI assistant that can read Markdown.

> 📖 [Full website with examples →](https://chevp.github.io/chevp-ai-framework/)

---

## What it looks like

A real exchange. The AI announces what it's about to do, then waits for you.

```
You: Add Google OAuth login to the app.

AI:  [Step 1: Understand]
     Before I write any code, here's what this will touch:
       • New files: auth/google.ts, routes/oauth.ts
       • Schema change: add oauth_provider column to users
       • New dependency: passport-google-oauth20
       • 3 existing tests need updating

     Does this scope look right?
     → [Yes, proceed] [Adjust scope] [Cancel]
```

The AI cannot move forward until you click. The same checkpoint repeats before planning, and again before any code reaches your repo.

---

## How it works

Three steps, each ending with a checkpoint you control.

<p align="center">
  <img src="images/chevp-ai-framework-v2.png" alt="The three-step lifecycle" width="680" />
</p>

| Step | What happens | What you see |
|:-----|:-------------|:-------------|
| **1. Understand** ([01-context/](01-context/)) | The AI reads your code and confirms what the task actually is — in your terms, not its assumptions. | A short problem description, affected files, agreed scope. |
| **2. Plan** ([02-exploration/](02-exploration/)) | The AI proposes how to solve it — sometimes with a clickable prototype — before writing real code. | A written plan, an optional prototype, a record of any architectural decisions. |
| **3. Build** ([03-production/](03-production/)) | Only now does the AI write production code — following the plan you approved, nothing more. | Working code, passing tests, a clean commit. |

### The three checkpoints

| | Question | When |
|:-|:---------|:-----|
| **Checkpoint 1** | Did we understand the task? | Before any planning starts. |
| **Checkpoint 2** | Is the plan good? | Before any production code is written. |
| **Checkpoint 3** | Does it actually work? | Before the change is considered done. |

Each checkpoint is enforced by a dedicated **gatekeeper** subagent (`gatekeeper-g1/g2/g3`) that returns `pass | conditional-pass | block` along with findings. Anything found out of scope becomes a `PROP-NNN` proposal in the backlog — out-of-scope items never disappear.

For the full matrix (roles, deliverables, evidence requirements, kill criteria), see [LIFECYCLE.md](LIFECYCLE.md). For the operating principle, see [guidelines/uncertainty-reduction.md](guidelines/uncertainty-reduction.md).

---

## The four rules

Everything else follows from these.

| Rule | Why |
|:-----|:----|
| **Context before code** | AI without context invents things. The first step is always understanding. |
| **A prototype is not the product** | Quickly generated code must be reviewed and understood before it ships. |
| **Small steps, with stops** | Validate after each step. No silent leaps from idea to merged code. |
| **The human decides** | The AI suggests. You approve. The responsibility never moves. |

---

## Quick Start

Pick the path that matches you.

### I want to try it (2 minutes)

Open your project's `CLAUDE.md` (or create one) and paste in this single line:

```markdown
@url https://chevp.github.io/chevp-ai-framework/chevp-ai-framework.md
```

That's it. Ask the AI to do something. It will announce its step and wait for your approval. No fork, no submodule, no install.

### I want the full setup

For a project where you'll keep plans, specs, and decisions versioned in git:

1. Add the `@url` reference above to `CLAUDE.md`.
2. Create the artifact directory:
   ```bash
   mkdir -p context/{architecture,adr,guidelines,plans/finished,specs}
   ```
3. *Optional:* install the [Claude Code plugin](#plugin-layer-claude-code-optional) for slash commands and automatic gate enforcement.

See [integration/](integration/) for project-specific patterns.

---

## Plugin Layer (Claude Code, optional)

The Markdown files in this repo are the **source of truth**. On top of them, a thin Claude Code plugin layer turns the framework into callable surface area.

| Layer | Path | Purpose |
|:------|:-----|:--------|
| Slash commands | [commands/](commands/) | `/context`, `/explore`, `/produce`, `/gate-check`, `/new-adr`, `/approve`, `/promote`, `/reject`, `/gate-override` |
| Subagents | [agents/](agents/) | `gatekeeper-g1/g2/g3` (gate validators with proposal-spawning), `architecture-reviewer` |
| Skills | [skills/](skills/) | Template-driven artifact creation: `create-ctx-plan`, `create-exp-plan`, `create-adr` |
| Hooks | [hooks/](hooks/) | `mode-context.py` (per-turn lifecycle reminder), `gate-check.py` (blocks code writes without approved plan), `provenance-check.py` (enforces non-empty evidence blocks) |

The plugin makes gate enforcement **mechanical** rather than relying solely on AI discipline. Without it, the framework still works — Claude reads the markdown files via `@url`.

```
/plugin install chevp-ai-framework
```

(Or reference this repo as a local plugin source during development.)

---

## Repository Structure

```
01-context/       Step 1 — Understand the system and problem
02-exploration/   Step 2 — Plan features and prototype
03-production/    Step 3 — Build, verify, ship
templates/        Plan, spec, ADR, CLAUDE.md, prototype templates
guidelines/       Cross-cutting quality rules
integration/      Integration into existing projects
docs/             Website + machine-readable AI reference
.claude-plugin/   Claude Code plugin manifest (optional)
commands/         Slash commands (plugin layer)
agents/           Subagents (plugin layer)
skills/           Skills wrapping templates (plugin layer)
hooks/            Python scripts for mechanical gate enforcement
```

---

## Domain Extension

The framework is **generic, reusable, and domain-agnostic** by design. For domain-specific projects, layer a `domain-ai-framework` on top:

<p align="center">
  <img src="images/domain-ai-framework.png" alt="Domain AI Framework Architecture" width="680" />
</p>

- **chevp-ai-framework** — the core lifecycle. Generic, reusable.
- **domain-ai-framework** — adds specialized rules, templates, and conventions for a field (e.g. game development, UI work, data pipelines).
- **Project framework** — concrete projects (e.g. `nuna-ai-framework`) that inherit the domain layer and produce real artifacts.

Projects can **tighten** framework rules, but never loosen them.

---

## Honest answers

**Won't this slow me down?**
On small tasks, yes — a one-line fix doesn't need three checkpoints, and you can skip the framework for those. On real work it's faster overall: the 30-second scope check at the start saves you from rolling back a half-finished feature the AI invented in a direction you didn't want.

**Do I need Claude Code specifically?**
No. The framework is plain Markdown that any AI assistant can read. Claude Code gets a plugin with extras, but the workflow is portable.

**What about quick reads or one-line fixes?**
Reading code, explaining things, answering questions — all free. The framework only kicks in when the AI is about to **create, edit, or delete** a file.

**Is this just process bureaucracy?**
The whole framework is three steps and three checkpoints. That's the surface. Everything else (templates, role definitions, deeper docs) is optional structure for when you want it.

---

## What this framework is *not*

| Misconception | Reality |
|:--------------|:--------|
| **A CLI tool or automation engine** | There is no binary to install, no commands to run. The AI internalizes the process and enforces it through conversation. |
| **A spec-driven approach** | The spec is not the input — it's an artifact that emerges during step 1. The process drives everything; specs are intermediate products. |
| **A CI/CD pipeline or workflow engine** | Pipelines execute predefined steps mechanically. This framework relies on an intelligent executor (the AI) that infers intent and adapts — while the process provides the guardrails. |
| **A replacement for human judgment** | The AI enforces the process and produces artifacts. The human decides, approves, and bears responsibility. |

---

## License

[MIT License](LICENSE) — © 2025 Patrice Chevillat
