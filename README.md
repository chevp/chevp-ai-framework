# chevp-ai-framework

**A process-driven lifecycle for AI-assisted software development.**

> Vibe Coding is not progress — it's technical recklessness.
> AI writes code, but it doesn't take responsibility. This framework does.

---

## Lifecycle

<p align="center">
  <img src="images/chevp-ai-framework-v2.png" alt="chevp-ai-framework" width="680" />
</p>
 
<table>
  <tr>
    <th>Step</th>
    <th>Purpose</th>
    <th>Mandatory Deliverables</th>
  </tr>
  <tr>
    <td><strong><a href="01-context/">Context</a></strong></td>
    <td>Understand the system and problem, catalogue uncertainty</td>
    <td>Problem Statement, Hypotheses, Risks (uncertainty triplet), System Spec, Architecture, ADRs, Context Inventory, Scope Confirmation</td>
  </tr>
  <tr>
    <td><strong><a href="02-exploration/">Exploration (A → B)</a></strong></td>
    <td><strong>A:</strong> Understand the problem in motion · <strong>B:</strong> Decide between concrete solutions</td>
    <td>Feature Plan/Spec with <code>exploration-mode</code>, UX Prototype, Challenger output, <code>insights.md</code></td>
  </tr>
  <tr>
    <td><strong><a href="03-production/">Production</a></strong></td>
    <td>Build, verify, ship — and update insights with reality</td>
    <td>Production code, validation result, updated documentation, updated <code>insights.md</code></td>
  </tr>
</table>

Quality gates **G1**, **G2**, **G3** enforce **evidence-based** human approval at every transition. Each gate is checked by a dedicated **Gatekeeper subagent** (`gatekeeper-g1/g2/g3`) that returns a verdict (`pass | conditional-pass | block`), findings, and **Spawned Plan Proposals** (`PROP-NNN`) for any out-of-scope items it found. Out-of-scope items never disappear — they become triageable backlog. See [LIFECYCLE.md](LIFECYCLE.md) for the full matrix and [guidelines/uncertainty-reduction.md](guidelines/uncertainty-reduction.md) for the operating principle.

---

## Roles

Seven cross-cutting roles operate within each step:

| Role | Scope |
|:-----|:------|
| **SDLC** | Process governance, quality gates, step transitions |
| **AI-Plans** | Plan/spec artifacts, acceptance criteria, scope management |
| **UX-Tooling** | Prototypes, preview feedback loops, visual/physical validation |
| **DevOps** | Build verification, commit workflow, CI/CD |
| **Software-Architecture** | ADRs, pattern enforcement, design decisions |
| **Context-Engineering** | CLAUDE.md, context hierarchy, what AI must read |
| **Challenger** | Internal sceptic — top-3 failure modes, ≥2 alternatives, strongest counter-argument before G2 |

---

## Quick Start

Add this block to your project's `CLAUDE.md`:

```markdown
## Before Writing Code

Reads, greps and explanations are always free. Before you **create, edit or delete** any file:
1. Load the framework:
   @url https://chevp.github.io/chevp-ai-framework/chevp-ai-framework.md
2. Announce the inferred lifecycle step (Context / Exploration / Production)
```

Then create the context directory structure:

```bash
mkdir -p context/{architecture,adr,guidelines,plans/finished,specs}
```

That's it. Claude loads the framework automatically via `@url`, detects the current lifecycle mode from your intent, and enforces the lifecycle as an autonomous gatekeeper. No manual mode flags or prompt headers required. See [integration/](integration/) for details.

---

## Repository Structure

```
01-context/       Step 1 — Understand the system and problem
02-exploration/   Step 2 — Plan features and prototype
03-production/    Step 3 — Build, verify, ship
templates/        Plan, spec, ADR, CLAUDE.md, prototype templates
guidelines/       Cross-cutting quality rules
integration/      Integration into existing projects
docs/             Machine-readable AI reference
.claude-plugin/   Claude Code plugin manifest (optional)
commands/         Slash commands (plugin layer)
agents/           Subagents (plugin layer)
skills/           Skills wrapping templates (plugin layer)
hooks/            Python scripts for mechanical gate enforcement
```

---

## Plugin Layer (Claude Code, optional)

The markdown files above are the **source of truth**. On top of them, a thin Claude Code plugin layer provides an executable interface:

| Layer | Files | Purpose |
|-------|-------|---------|
| Slash Commands | [commands/](commands/) | `/context`, `/explore`, `/produce`, `/gate-check`, `/new-adr`, `/approve`, `/promote`, `/reject`, `/gate-override` |
| Subagents | [agents/](agents/) | `gatekeeper-g1` / `gatekeeper-g2` / `gatekeeper-g3` (specialised gate validators with proposal-spawning), `architecture-reviewer` (enforces invariants/ADRs) |
| Skills | [skills/](skills/) | Template-driven artifact creation (`create-ctx-plan`, `create-exp-plan`, `create-adr`) |
| Hooks | [hooks/](hooks/) | `mode-context.py` injects lifecycle reminder every turn; `gate-check.py` blocks code writes without an approved EXP plan; `provenance-check.py` enforces non-empty `evidence:` blocks |

The plugin makes Gate-Enforcement **mechanical** (via hooks) rather than relying solely on AI discipline. Without the plugin, the framework still works — Claude reads the markdown files via `@url` or project references.

Install (once `chevp-ai-framework` is on a marketplace):
```
/plugin install chevp-ai-framework
```

Or use locally during development by referencing this repo as a plugin source.

---

## Domain Extension

The chevp-ai-framework is designed as a **generic, reusable, domain-agnostic** core. For domain-specific projects, it can be extended through a **domain-ai-framework** layer.

<p align="center">
  <img src="images/domain-ai-framework.png" alt="Domain AI Framework Architecture" width="680" />
</p>

The architecture follows a layered approach:

- **chevp-ai-framework** (bottom layer) — The core lifecycle with Context, Exploration, and Production. Generic and reusable across all domains.
- **domain-ai-framework** (middle layer) — A domain-specific extension that adds specialized rules, templates, and conventions for a particular field (e.g., Game, UI, Data Pipelines, or any custom domain).
- **Project frameworks** (top layer) — Concrete project frameworks (e.g., `nuna-ai-framework`) that inherit from the domain layer and produce the final artifacts for human and AI collaboration.

This layered model ensures that domain-specific knowledge (scenes, NPCs, components, pipelines, schemas) lives in the right place — separate from the universal process rules, but built on top of them.

Projects can **tighten** framework rules but never **loosen** them.

---

## Principles

| Principle | Why |
|:----------|:----|
| **Prototype ≠ Production** | Quickly generated code must be reviewed and understood |
| **Context is mandatory** | AI without context invents things |
| **Incremental** | Small steps with validation after each step |
| **Human decides** | AI suggests, the developer bears responsibility |
| **Gates are blockers** | No forward movement without all criteria satisfied |

---

## What This Framework Is Not

| Misconception | Reality |
|:--------------|:--------|
| **A CLI tool or automation engine** | This is a thinking model and process framework. There is no binary to install, no commands to run. The AI internalizes the process and enforces it through conversation. |
| **A spec-driven approach** | The spec is not the input — it is an artifact that emerges during the Context step. The process (3 steps + quality gates) drives everything; specs are intermediate products. |
| **A CI/CD pipeline or BPM workflow** | Pipelines and workflow engines execute predefined steps mechanically. This framework relies on an intelligent executor (the AI) that infers intent, adapts to context, and makes judgment calls — while the process provides guardrails. |
| **A replacement for human judgment** | The AI enforces the process and produces artifacts. The human decides, approves, and bears responsibility. |

---

## License

This project is licensed under the [MIT License](LICENSE).