---
id: CTX-001
type: CTX
status: draft
proposed-by: ai
decided-by: —
approved-by: —
approved-at: —
date: 2026-04-10
---

# CTX-001: Reposition & split the GitHub Pages site for clarity and AI-retrievability

## Task

Rework the public site at `chevp.github.io/chevp-ai-framework/` so that it (a) sharpens the positioning of the framework against LangChain/AutoGPT and vibe coding, and (b) splits the current single landing page into smaller, use-case-oriented, AI-retrieval-friendly pages. Focus is *not* on producing more content, but on making existing content more focused, concrete and linkable.

## Why now

User feedback: the current site is conceptually solid but too generic and hard to grasp — both for human outsiders and for AI systems. The framework is categorically different from AI runtimes (LangChain, AutoGPT), but that difference is not communicated. Small, quotable units per URL would massively improve discoverability, citation and AI retrieval.

## Artifacts to Read/Verify

- [x] [CLAUDE.md](../../CLAUDE.md) — core principle, rules, lifecycle summary
- [x] [LIFECYCLE.md](../../LIFECYCLE.md) — full 3×6×3 matrix, gates G1/G2/G3
- [x] [README.md](../../README.md) — longer-form intro
- [x] [docs/index.html](../../docs/index.html) — current single landing page (377 lines, Tailwind CDN, Arctic theme, Glassmorphism)
- [x] [docs/presentation.html](../../docs/presentation.html) — slide deck (out of scope for this CTX)
- [x] [.github/workflows/build-dist.yml](../../.github/workflows/build-dist.yml) — Pages deployment (copies `docs/*.html` + `docs/images/` + `dist/chevp-ai-framework.md` to `_site/`)
- [ ] [guidelines/modular-composition.md](../../guidelines/modular-composition.md) — possibly relevant for the "Components" section
- [ ] [integration/](../../integration/) — source for a future integration page
- [ ] Sibling project sites (e.g. `chevp-workflow`, `nuna-ai-framework`) — check for style and link conventions

## Current state (facts)

- Site = **one** HTML file: `docs/index.html` with sections Hero, Lifecycle, Roles, Domain Extension, Principles, Quick Start, Repository Structure.
- Build is dead simple: `build-dist.yml` just `cp`s files into `_site/`. Adding new pages only requires new `cp` lines (or a glob).
- Content source-of-truth lives in the repo markdown (`CLAUDE.md`, `LIFECYCLE.md`, `README.md`) — the HTML is a hand-written summary, not generated.
- There is no static site generator, no templating, no component reuse. Each new page would be a standalone `.html`.

## Positioning (to be confirmed at G1)

The framework should be explicitly positioned as **a process framework for human+AI software development**, not as an AI runtime or agent library.

Key differentiation table (to appear prominently on the landing page):

| | LangChain / AutoGPT | chevp-ai-framework |
|---|---|---|
| Category | Runtime / libraries for AI agents | Process framework for human+AI software dev |
| What it builds | AI applications | Accountable software *with* AI assistance |
| Runs where | In production | In the dev loop (Claude Code, Cursor, …) |
| Solves | "How do I build an agent?" | "How do I prevent vibe coding?" |

Headline sentence candidate: *"This is not an AI runtime. It's a process framework that makes AI-assisted coding accountable."*

## Target site structure (draft)

Every page follows the same skeleton: **1-sentence definition (bold, top) → What → Why → How (concrete example) → When to use / not use → Related**.

```
/ (index.html)              Landing: problem, positioning, "not LangChain", CTA
/what-is-it.html            Definition, category, boundary vs AI runtimes
/how-it-works.html          3 steps, gates G1-G3, modes, roles — condensed
/use-cases/
  bug-fix.html              Walkthrough: bug report → Context → fix
  new-feature.html          Walkthrough: idea → spec → prototype → code
  refactoring.html          Walkthrough with ADR
  legacy-onboarding.html    Context-inventory as entry point
/vs/
  langchain.html            "Different category — here's why"
  vibe-coding.html          "What you lose without a process"
  spec-driven.html          Process-driven vs spec-driven
/components/
  context-step.html
  exploration-step.html
  production-step.html
  gates.html
  modes.html
  roles.html
/integration.html           Quick Start (moves out of landing)
```

URLs are deep-linkable, each page carries one idea → AI retrieval friendly.

## Phase 1 scope proposal (to be confirmed)

Don't build all ~15 pages at once. Ship a **minimum viable split** first, validate the pattern, then expand:

**Phase 1 (5 pages):**
1. New `/` — shortened landing with problem + positioning + differentiation table + CTAs
2. `/what-is-it.html`
3. `/how-it-works.html`
4. `/use-cases/bug-fix.html` (one concrete walkthrough)
5. `/vs/langchain.html` (the single most important "vs" page)

**Phase 2** (later): remaining use cases, remaining vs pages, components split.

## Open Questions (for the human to decide at G1)

- [ ] **Q1 — Positioning frame**: confirm *"different category, not a competitor"* framing against LangChain/AutoGPT? (AI recommendation: yes.)
- [ ] **Q2 — Walkthrough sourcing**: should use-case walkthroughs use **real examples** from existing projects (e.g. `nuna`) or stay **generic**? (AI recommendation: real — more convincing, but needs your approval for exposure.)
- [ ] **Q3 — Phase 1 scope**: start with the 5-page MVP above, or go straight to the full structure? (AI recommendation: MVP.)
- [ ] **Q4 — Language**: English for all new pages? (AI recommendation: yes, matches existing site.)
- [ ] **Q5 — Tech**: separate `.html` files in the same Arctic/Glass style, manually kept in sync (no SSG)? (AI recommendation: yes — minimal change to build pipeline.)
- [ ] **Q6 — Landing content fate**: may I move "Roles", "Domain Extension", "Repository Structure" sections **off** the landing into dedicated pages, leaving the landing lean? (AI recommendation: yes.)
- [ ] **Q7 — Presentation**: leave `docs/presentation.html` untouched in this CTX? (AI recommendation: yes, out of scope.)
- [ ] **Q8 — Source-of-truth risk**: the HTML will duplicate content from `CLAUDE.md`/`LIFECYCLE.md`. Accept the manual-sync drift risk for now, or introduce a generator in a later CTX? (AI recommendation: accept for now, track as follow-up.)

## Scope Boundaries (Draft)

**Likely in scope**
- Rewriting `docs/index.html` into a lean landing
- Creating new `.html` pages under `docs/` for Phase 1
- Updating [.github/workflows/build-dist.yml](../../.github/workflows/build-dist.yml) to include the new pages (single glob or explicit `cp` lines)
- Adding cross-navigation (header links, "Related" footers)
- Adding a shared CSS/JS snippet if trivially extractable — **optional**, only if it doesn't explode scope

**Likely NOT in scope**
- Any change to `docs/presentation.html`
- Introducing a static site generator (Jekyll, MkDocs, Astro, …)
- Rewriting `CLAUDE.md`, `LIFECYCLE.md`, `README.md` content
- Changing the framework itself (lifecycle, gates, roles)
- Translations
- SEO/OG-image work beyond what the current page has
- Phase 2 pages (remaining use cases, vs, components)

**Uncertain / needs human input**
- Whether real-project walkthroughs are acceptable (Q2)
- Whether a follow-up CTX should introduce a generator (Q8)
- Whether `/components/*` should exist at all or be folded into `/how-it-works` (defer to Phase 2)

## Confirmation Needed (for G1)

Before moving to Exploration, the human must confirm:

1. **Positioning**: the "different category, not a competitor" framing against LangChain/AutoGPT.
2. **Phase 1 scope**: the 5-page MVP (landing, what-is-it, how-it-works, 1 use case, 1 vs page) — or an alternative scope.
3. **Walkthrough sourcing**: generic vs real-project examples.
4. **Tech & language**: plain `.html` in the current style, English.
5. **Landing content fate**: which sections may be moved off the current landing.
6. **Out-of-scope acknowledgement**: presentation.html, SSG, content rewrites of CLAUDE.md/LIFECYCLE.md are not touched.

Once confirmed, the next step is an Exploration plan (`EXP-NNN`) containing the per-page content outlines, the navigation graph, the exact build-workflow diff, and a minimal visual prototype of the new landing.
