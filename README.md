# chevp-ai-framework

**A structured lifecycle for AI-assisted software development.**

> Vibe Coding is not progress — it's technical recklessness.
> AI writes code, but it doesn't take responsibility. This framework does.

---

## Lifecycle

<p align="center">
  <img src="images/chevp-ai-framework.png" alt="chevp-ai-framework" width="680" />
</p>

<table>
  <tr>
    <th>Step</th>
    <th>Purpose</th>
    <th>Key Output</th>
  </tr>
  <tr>
    <td><strong><a href="01-context/">Context</a></strong></td>
    <td>Understand the problem, gather context, confirm scope</td>
    <td>Problem description, affected modules, confirmed scope</td>
  </tr>
  <tr>
    <td><strong><a href="02-exploration/">Exploration</a></strong></td>
    <td>Plan the solution, prototype, validate the approach</td>
    <td>Approved plan/spec, prototype, ADR</td>
  </tr>
  <tr>
    <td><strong><a href="03-production/">Production</a></strong></td>
    <td>Build, verify, ship</td>
    <td>Production code, passing tests, commit on main</td>
  </tr>
</table>

Quality gates **G1**, **G2**, **G3** enforce human approval at every transition. See [LIFECYCLE.md](LIFECYCLE.md) for the full matrix.

---

## Roles

Six cross-cutting roles operate within each step:

| Role | Scope |
|:-----|:------|
| **SDLC** | Process governance, quality gates, step transitions |
| **AI-Plans** | Plan/spec artifacts, acceptance criteria, scope management |
| **UX-Tooling** | Prototypes, preview feedback loops, visual/physical validation |
| **DevOps** | Build verification, commit workflow, CI/CD |
| **Software-Architecture** | ADRs, pattern enforcement, design decisions |
| **Context-Engineering** | CLAUDE.md, context hierarchy, what AI must read |

---

## Quick Start

```bash
# 1. Copy the CLAUDE.md template into your project
cp templates/claude-md-template.md <your-project>/CLAUDE.md

# 2. Create the context directory structure
mkdir -p <your-project>/context/{architecture,adr,guidelines,plans/finished,specs}

# 3. Reference the framework in your project's CLAUDE.md
```

See [integration/](integration/) for detailed setup guides.

---

## Repository Structure

```
01-context/       Step 1 — Understand the problem
02-exploration/   Step 2 — Plan and prototype
03-production/    Step 3 — Build, verify, ship
templates/        Plan, spec, ADR, CLAUDE.md, prototype templates
guidelines/       Cross-cutting quality rules
integration/      Integration into existing projects
```

---

## Domain Extension

The chevp-ai-framework is designed as a **generic, reusable, domain-agnostic** core. For domain-specific projects, it can be extended through a **domain-ai-framework** layer.

<p align="center">
  <img src="images/domain-ai-framework.png" alt="Domain AI Framework Architecture" width="680" />
</p>

The architecture follows a layered approach:

- **chevp-ai-framework** (bottom layer) — The core lifecycle with Context, Exploration, and Production. Generic and reusable across all domains.
- **domain-ai-framework** (middle layer) — A domain-specific extension that adds specialized rules, templates, and conventions for a particular field (e.g., Game, UI, Data Pipelines, or any custom domain). Included as a Git submodule.
- **Project frameworks** (top layer) — Concrete project frameworks (e.g., `nuna-ai-framework`) that inherit from the domain layer and produce the final artifacts for human and AI collaboration.

This layered model ensures that domain-specific knowledge (scenes, NPCs, components, pipelines, schemas) lives in the right place — separate from the universal process rules, but built on top of them.

---

## Principles

| Principle | Why |
|:----------|:----|
| **Prototype ≠ Production** | Quickly generated code must be reviewed and understood |
| **Context is mandatory** | AI without context invents things |
| **Incremental** | Small steps with validation after each step |
| **Human decides** | AI suggests, the developer bears responsibility |

---

## License

This project is licensed under the [MIT License](LICENSE).
