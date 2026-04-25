---
id: CTX-002
type: CTX
status: approved
proposed-by: ai
decided-by: chevp
approved-by: chevp
approved-at: 2026-04-25
date: 2026-04-24
evidence:
  hypothesis: A standalone CLI wrapping `claude -p` (Pfad 2) can mechanize the lifecycle (Context → Exploration → Production with G1/G2/G3) outside the Claude-Code-interactive flow, validating the framework's portability claim by being its first concrete adapter. Initial tech-stack lean was Python.
  result: Through Q1-Q7 + SQ1-SQ5 resolution and a mid-Context tech-stack pivot from Python to Go + Charm, the design converged on a tightly bounded shape — five v1 commands (init/status/approve/gate-check/new-adr), explicit per-step command paths, Pfad-2 subprocess for Max-subscription compatibility, and embed.FS-vendored subagent prompts. The 'process-driven, not spec-driven' tension was preserved by structurally requiring dialogue rounds in `chevp context init` rather than one-shot generation (R7 mitigation). Six fundamental ADRs (001-006) memorialise the design decisions; one parallel chevp-ai-framework work item (Adapter-Contract document) is queued.
  reasoning: Scope is safe to confirm at G1 because (a) the command surface is bounded by Q5; (b) all human-only frontmatter fields are denied to the CLI by porting `provenance-check.py` semantics into `internal/state/provenance.go`; (c) Kill Criterion ('gate-approvals become routine') is named and observable; (d) the top-3 risks (R1 schema-drift, R2 subagent-context-loss, R3 provenance-bruch) all have concrete spike-or-mitigation paths assigned for Exploration; (e) the Adapter-Contract dependency is acknowledged as parallel framework work.
---

# CTX-002: chevp-flow — CLI adapter for the chevp-ai-framework lifecycle

## Task

Design and build `chevp-flow`, a Go CLI (binary name: `chevp`) that mechanizes the chevp-ai-framework lifecycle (3 steps × 3 gates) by wrapping the `claude` CLI as a subprocess. Distributed as an independent public OSS GitHub repository (`chevp-flow`), consumed by `chevp-ai-framework` itself as a git submodule for dogfooding. Tech-stack: Go + Cobra (CLI args) + Charm Stack (Bubble Tea TUI, Huh forms, Glamour markdown rendering).

## Why now

The framework's lifecycle is currently enforced via two layers: human discipline + the Claude-Code plugin layer (`hooks/`, `agents/`, `skills/`, `commands/`). Both bind the framework to a single interactive surface. Pain points that have accumulated:

- Lifecycle cannot be applied from terminal-only / CI flows
- External adopters must adopt Claude Code wholesale to follow the process
- The framework author cannot dogfood the lifecycle outside interactive chat
- "Tool-independence" remains an assertion, not a demonstrated property

The framework has stabilized to v1 (CTX-001 finished, plugin layer in production, lifecycle proven internally). It is the right moment to extract the contract into a separate tool — both to validate portability and to provide a non-Claude-Code installation surface.

## Decisions captured pre-G1

| Bereich | Decision |
|---------|----------|
| Tech-Stack | **Go + Charm Stack** (Cobra for CLI args, Bubble Tea for TUI, Huh for forms, Glamour for markdown) |
| Go floor | 1.22+ |
| Auth-Pfad | Pfad 2 — `claude -p` subprocess, JSON streaming |
| Repo-Lokation | Separate public GitHub repo: `chevp-flow` |
| Binary name | `chevp` (matches gh/kubectl/helm pattern: short binary, descriptive repo) |
| License | Apache-2.0 |
| Distribution | Single binary via Homebrew (`brew install chevp`) + GitHub Releases + `go install` + git submodule into chevp-ai-framework |
| Submodule path | `tools/chevp-flow/` |
| Module layout | Single Go module (no internal split for v1) |
| CLI-Modus | Async file-based (git-style: command → file diff → `approve` command); Huh forms used for interactive gate prompts |
| Mode handling | Explicit per command path (`chevp context init`, `chevp exploration plan`, etc.) |
| v1 command surface | `init`, `status`, `approve`, `gate-check`, `new-adr` |
| Subagent prompts | Vendored, version-pinned to a chevp-ai-framework release tag (Go embed.FS) |
| Kill Criterion | "Gate-approvals become routine" — framework would be self-defeating |
| Docker scope | Only gatekeeper subagents (read-only, deterministic); native Go Docker SDK |
| Audience | OSS / third-party developers (public repo) |

## Artifacts to Read/Verify

- [x] [CLAUDE.md](../../CLAUDE.md) — core principle, 13 rules, lifecycle summary
- [x] [LIFECYCLE.md](../../LIFECYCLE.md) — 3 × 7 × 3 matrix, gates G1/G2/G3
- [x] [agents/](../../agents/) — `gatekeeper-g1/g2/g3` contracts; verdict format, blocking conditions, max-5 PROP rule extracted
- [x] [hooks/](../../hooks/) — `mode-context.py`, `gate-check.py`, `provenance-check.py`; field denylist (`decided-by`, `approved-by`, `approved-at`, `status: approved|accepted`) extracted; production-write block heuristic extracted
- [x] [skills/](../../skills/) — `create-ctx-plan`, `create-exp-plan`, `create-adr`, `sync-plan-issues`; invocation patterns extracted
- [x] [commands/](../../commands/) — all 9 slash commands (approve, context, explore, gate-check, gate-override, new-adr, produce, promote, reject); side effects + frontmatter mutations extracted
- [x] [templates/](../../templates/) — artifacts the CLI instantiates from
- [x] [guidelines/architecture-governance.md](../../guidelines/architecture-governance.md) — Rule #7 enforcement: AI may set `proposed-by: ai|pair`, never `human`; never sets `decided-by`/`approved-by`/`approved-at` or `status: approved|accepted`
- [x] [guidelines/uncertainty-reduction.md](../../guidelines/uncertainty-reduction.md) — `evidence:` block: hypothesis (falsifiable), result (observable), reasoning (bridge → action); generic content = automatic G1/G2/G3 block
- [x] [.claude-plugin/plugin.json](../../.claude-plugin/plugin.json) — manifest registers `mode-context.py` (UserPromptSubmit), `gate-check.py` + `provenance-check.py` (PreToolUse on Write/Edit)
- [ ] [chevp.github.io/chevp-workflow/](https://chevp.github.io/chevp-workflow/index.md) — workspace-mode contract (relevant when wiring submodule; deferred until Production-step submodule integration)

## Problem Statement (embedded — Uncertainty Triplet, G1 prerequisite)

**Who has the problem?**
Two distinct user groups: (a) the framework author, who currently must use Claude Code's interactive chat to apply the lifecycle to his own projects — no batch, no CI, no terminal-only flow; (b) external developers evaluating the framework, who are forced to adopt Claude Code as a precondition.

**What does not work today?**
The lifecycle's mechanical guarantees (mode inference, gate enforcement, provenance checks) are implemented as Claude-Code-specific Python hooks. There is no way to: (1) run a gate-check from CI, (2) instantiate a CTX/EXP/PRD plan from the terminal, (3) invoke gatekeeper-subagents non-interactively, (4) apply the framework in a non-Claude-Code editor.

**Why does it matter?**
Framework adoption is bottlenecked. Without a portable adapter, "tool-independence" is unsubstantiated, and the framework's claim to be a *process* framework — orthogonal to tools — is not yet demonstrated. Cost: stalled OSS adoption; the author's own ability to dogfood is constrained to interactive chat.

**Why now?**
v1 of the framework has stabilized. CTX-001 (site reposition) is finished. The plugin layer is in production. Lifecycle is proven on internal projects. Without a second adapter, drift between "framework theory" and "Claude-Code implementation" will calcify.

**Out-of-scope problems (intentionally)**
- Multi-provider LLM support (OpenAI, etc.) — Claude only in v1
- Editor/IDE plugins
- Web UI, dashboards, team collaboration
- Windows support
- Rewriting chevp-ai-framework's existing plugin layer
- Adding new framework features

## Hypotheses

| # | Hypothesis | Cheapest test | Kill criterion |
|---|-----------|--------------|----------------|
| H1 | If we build a Go CLI wrapping `claude -p` and exposing gate-checks as commands, then framework discipline becomes mechanizable in CI and terminal flows, **because the lifecycle is fundamentally a state machine over markdown files**. | Implement `chevp context init "intent"` → generate CTX-NNN draft → diff against what Claude Code produces. | If post-processing the generated draft is needed >30% of the time, abstraction is too thin. |
| H2 | If we choose async file-based interaction (git-style), then the CLI integrates naturally with editor + CI workflows, **because all state already lives in markdown files**. | Implement only `init`, `approve g1`, `status`; run one real CTX cycle end-to-end. | If approval flow takes more clicks than chat (>2×), reconsider Hybrid mode. |
| H3 | If we containerize only gatekeeper-subagents, we get reproducibility where it matters without DX overhead, **because gatekeepers are read-only/deterministic and benefit from isolation, while interactive commands do not**. | Dockerize one gatekeeper; benchmark cold-start vs. native. | If cold-start >5s, fall back to native invocation with optional `--docker` flag. |

**What we deliberately do NOT yet assume**
- That `claude -p` JSON-output schema is stable across versions (track upstream)
- That gatekeeper subagent prompts can be vendored into the CLI without drift (Q4)
- That the CLI's command surface should mirror existing slash commands 1:1 (rationalization may be warranted)

## Risks

| # | Risk | Likelihood | Cost | Mitigation / early signal |
|---|------|-----------|------|---------------------------|
| R1 | `claude -p` schema or auth flow changes break the CLI. | med | high | Pin minimum Claude Code version; parse defensively; integration tests against latest; declare supported version range. |
| R2 | Gatekeeper-subagents are Claude-Code-native and lose context when invoked via subprocess. | med | high | Spike one gatekeeper end-to-end **before G2**; if context-loss material, vendor full prompts + tool definitions. |
| R3 | CLI accidentally writes human-decision fields (`decided-by`, `approved-by`), breaking Rule #7 / provenance. | high w/o guardrails | high | Hardcode field allowlist; refuse writes; reuse `provenance-check.py` logic as library. |
| R4 | Solo over-engineering / bikeshedding. | high | med | Hard MVP scope (≤8 commands v1); Kill Criterion enforced. |
| R5 | Submodule integration friction for contributors. | med | low-med | Document both `pip install` and submodule path; CI test both. |
| R6 | Adapter contract drift — framework evolves faster than CLI. | high over time | med | Declare adapter-contract-version in chevp-ai-framework; CLI announces compatibility range. |
| R7 | Ironically: the "process-driven, not spec-driven" tension surfaces — `chevp context init INTENT` could be misused as one-shot spec generation. | med | high (constitutional) | Structurally enforce the *dialogue* nature of Context: `init` only seeds, requires explicit dialogue rounds before G1. |
| R8 | `anthropic-sdk-go` is younger and less feature-rich than the TS/Python SDK; if we ever add Pfad 3 (direct API) for fallback or non-Claude-Code envs, more boilerplate for streaming/tool-use. | med (deferred) | low-med | v1 stays on Pfad 2 only; Pfad 3 deferred until SDK matures or proven need. Re-evaluate at v2 planning. |
| R9 | Go's JSON-stream parsing of `claude -p` output is more verbose than Python (no Pydantic). Manual struct definitions per message type. | high | med | Define stable message-type structs in one package; integration tests against current `claude -p` output samples; pin minimum Claude Code version. |

### Top-3 expensive failure modes
1. **R3 — Provenance-Bruch** (constitutional violation, high prob without guardrails)
2. **R2 — Subagent-Kompatibilität** (gates become weaker if context lost)
3. **R7 — Spec-driven slide** (would invalidate the framework's own premise)

### Counter-evidence we are not ignoring
Earlier in this design conversation the AI itself raised the spec-driven tension. The user chose not to reframe the question, but the tension didn't disappear — it shows up as R7. The CLI must demonstrate that "process-driven" survives in non-interactive form, or the project disproves the framework.

### Risks we accept knowingly
- v1 supports only Claude / Claude Code (not OpenCode, Cursor, raw API). Reason: validate the adapter contract on one tool first.
- v1 is mac/linux only. Reason: solo dogfooding context.
- Subagent prompts vendored at pinned version (drift accepted in exchange for reproducibility). Reason: Reproducibility > freshness for v1.

## Open Questions (resolved by human via AskUserQuestion on 2026-04-24)

- [x] **Q1 — License**: **Apache-2.0** chosen.
- [x] **Q2-revised — Go floor**: **Go 1.22** chosen (range-over-func, generics stable, broad adoption). Original Python-3.11 answer superseded by tech-stack switch.
- [x] **Q3 — Submodule path**: **`tools/chevp-flow/`** chosen.
- [x] **Q4 — Subagent prompts**: **vendored, version-pinned** to a chevp-ai-framework release tag (now via Go `embed.FS`).
- [x] **Q5 — v1 command surface**: **`init`, `status`, `approve`, `gate-check`, `new-adr`** (minimum + ADR support).
- [x] **Q6 — Mode-inference**: **explicit per command path** (no inference; `chevp context init`, `chevp exploration plan`, …).
- [x] **Q7 — Module layout**: **single Go module** for v1; split deferred until reuse pressure emerges.

### Tech-Stack Switch (2026-04-24)

After Q1–Q7 resolution, the human decided to switch from Python to Go + Charm Stack. Rationale:
- Single binary distribution (`brew install chevp`) eliminates Python-runtime install friction
- Native Go Docker SDK simplifies the gatekeeper-container path
- Huh forms map naturally to the framework's `AskUserQuestion` clickable-decisions pattern (Rule #13)
- Acknowledged tradeoff: `anthropic-sdk-go` is younger and more boilerplate-heavy for streaming (captured as R8/R9)

This switch supersedes prior Python-related decisions but does NOT change: Auth-Pfad (still Pfad 2), CLI-Modus (still async file-based), command surface, subagent vendoring, mode handling, kill criterion, docker scope, repo location, license, submodule path, module layout principle.

All scope confirmation items below #5 are now satisfied (license, submodule path, command surface, vendoring, mode handling, module layout). Q2 must be re-asked for Go version floor before G1. Frontmatter `decided-by`/`approved-by` remain `—` until G1 itself is signed.

## Scope Boundaries (Draft)

**Likely in scope**
- Go 1.22+ CLI using Cobra (commands) + Charm Stack (Bubble Tea TUI, Huh forms, Glamour markdown rendering)
- Single static binary distribution: Homebrew tap + GitHub Releases (goreleaser) + `go install`
- `claude -p` subprocess wrapper with JSON-stream parser (manual struct definitions in one package)
- v1 command surface: `init`, `status`, `approve`, `gate-check`, `new-adr` (per Q5)
- Markdown-file state layer (`context/`, `exploration/`, `production/`)
- Provenance guardrails (refuse to write human-decision fields — port logic from `provenance-check.py`)
- Native Go Docker SDK for gatekeeper-subagent isolation
- Vendored gatekeeper prompts via Go `embed.FS`, pinned to chevp-ai-framework release tag
- Apache-2.0 license + minimal `README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`
- Public GitHub repo at `github.com/chevp/chevp-flow`
- Submodule integration into chevp-ai-framework at `tools/chevp-flow/` (per Q3)
- Adapter-contract document in chevp-ai-framework (parallel work)

**Likely NOT in scope**
- Multi-provider LLM support
- Web UI / dashboard
- Team collaboration / multi-user state
- Windows support
- IDE/editor plugins
- Rewriting chevp-ai-framework's plugin layer
- New framework features (this is a tool for the existing framework)
- Migration scripts from interactive Claude-Code state to CLI state

**Out-of-scope items become proposals (per Rule #12)**
The Gatekeeper at G1 will spawn `PROP-NNN` files for any of the above that the human wants tracked instead of permanently dropped.

**Uncertain / needs human input**
- Whether subagent prompts are vendored (Q4)
- License choice (Q1)
- Whether to also publish `chevp-flow-core` as a library (Q7)

## Confirmation Needed (for G1)

Before moving to Exploration, the human must confirm:

1. **Problem framing** — Claude-Code-coupling is the actual blocker, CLI-as-adapter is the right shape (vs. e.g., browser extension, IDE plugin).
2. **Decisions table** above (tech, auth path, repo, distribution, CLI-mode, docker scope) — frozen for v1.
3. **Kill Criterion** — "Gate-approvals become routine" is the abort signal.
4. **Out-of-scope acknowledgement** — multi-provider, web UI, Windows, plugin-layer rewrite are not in v1.
5. **License + Python floor + submodule path + command surface + subagent vendoring + mode inference** — answers to Q1–Q7.
6. **Adapter-Contract parallel work** — that chevp-ai-framework will gain an explicit adapter-contract document during this CTX, since chevp-flow is its first concrete adapter.

## Kill Criteria (for this Context effort itself)

- If **R2 (subagent-kompatibilität)** cannot be resolved with a one-day spike before G1 confirms, **escalate** — gates without working gatekeepers are fake gates, and the project would be defective by construction.
- If after drafting the System Spec the v1 command surface exceeds 8 commands, **reduce ruthlessly** or split into v1/v2 release plan.
- If during Hypothesis-H1 testing the CLI-generated CTX draft requires post-processing >30% of the time, **abandon thin-wrapper approach** — the abstraction is wrong, not just buggy.

## Next steps after G1

Once confirmed, the next deliverables move to Exploration (CTX → EXP transition):

- **EXP-NNN-chevp-flow-architecture** — module layout (command-layer / runtime-layer / state-layer / gate-layer / docker-layer), data flow, error model
- **Fundamental ADRs** drafted ✅ (six in `context/specs/chevp-flow/adr/`):
  - [ADR-001](../specs/chevp-flow/adr/ADR-001-async-file-based-cli.md) — Async file-based CLI architecture
  - [ADR-002](../specs/chevp-flow/adr/ADR-002-claude-subprocess-auth.md) — Pfad 2 (`claude -p` subprocess) as auth strategy
  - [ADR-003](../specs/chevp-flow/adr/ADR-003-go-charm-tech-stack.md) — Go 1.22+ with Charm Stack (Cobra/Bubble Tea/Huh/Glamour)
  - [ADR-004](../specs/chevp-flow/adr/ADR-004-apache-2-license.md) — Apache-2.0 license
  - [ADR-005](../specs/chevp-flow/adr/ADR-005-vendored-prompts-embed-fs.md) — Subagent-prompt vendoring via Go `embed.FS`
  - [ADR-006](../specs/chevp-flow/adr/ADR-006-adapter-contract-location.md) — Adapter-Contract spec lives in chevp-ai-framework
- **Deferred to Exploration**: Distribution-strategy ADR (Homebrew + goreleaser concrete config), Module-internal-API ADR (if reuse pressure emerges)
- **UX prototype** for the four core commands' CLI output (Glamour markdown + Bubble Tea status views)
- **Challenger output** — top-3 failure modes, ≥2 alternative architectures (e.g., Python+Typer, TS+Bun rejected with reasons), strongest counter-argument, product-coherence check
- **`insights.md`** seeded
