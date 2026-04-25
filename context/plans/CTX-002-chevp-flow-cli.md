---
id: CTX-002
type: CTX
status: draft
proposed-by: ai
decided-by: —
approved-by: —
approved-at: —
date: 2026-04-24
evidence:
  hypothesis: A standalone Python CLI wrapping `claude -p` can mechanize the lifecycle (Context → Exploration → Production with G1/G2/G3) outside the Claude-Code-interactive flow, validating the framework's portability claim by being its first concrete adapter.
  result: —
  reasoning: —
---

# CTX-002: chevp-flow — CLI adapter for the chevp-ai-framework lifecycle

## Task

Design and build `chevp-flow`, a Python CLI that mechanizes the chevp-ai-framework lifecycle (3 steps × 3 gates) by wrapping the `claude` CLI as a subprocess. Distributed as an independent public OSS GitHub repository, consumed by `chevp-ai-framework` itself as a git submodule for dogfooding.

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
| Tech-Stack | Python (Typer + Rich + uv) |
| Auth-Pfad | Pfad 2 — `claude -p` subprocess, JSON streaming |
| Repo-Lokation | Separate public GitHub repo: `chevp-flow` |
| Distribution | PyPI (`pip install chevp-flow`) + git submodule into chevp-ai-framework |
| CLI-Modus | Async file-based (git-style: command → file diff → `approve` command) |
| Kill Criterion | "Gate-approvals become routine" — framework would be self-defeating |
| Docker scope | Only gatekeeper subagents (read-only, deterministic) |
| Audience | OSS / third-party developers (public repo) |

## Artifacts to Read/Verify

- [x] [CLAUDE.md](../../CLAUDE.md) — core principle, 13 rules, lifecycle summary
- [x] [LIFECYCLE.md](../../LIFECYCLE.md) — 3 × 7 × 3 matrix, gates G1/G2/G3
- [ ] [agents/](../../agents/) — `gatekeeper-g1/g2/g3` contracts (subprocess targets)
- [ ] [hooks/](../../hooks/) — `mode-context.py`, `gate-check.py`, `provenance-check.py` (logic the CLI must replicate or invoke)
- [ ] [skills/](../../skills/) — `create-ctx-plan`, `create-exp-plan`, `create-adr` (commands the CLI exposes)
- [ ] [commands/](../../commands/) — slash commands the CLI must mirror in shape
- [x] [templates/](../../templates/) — artifacts the CLI instantiates from
- [ ] [guidelines/architecture-governance.md](../../guidelines/architecture-governance.md) — provenance rules (Rule #7)
- [ ] [guidelines/uncertainty-reduction.md](../../guidelines/uncertainty-reduction.md) — `evidence:` block requirements
- [ ] [.claude-plugin/](../../.claude-plugin/) — manifest, what the plugin layer assumes
- [ ] [chevp.github.io/chevp-workflow/](https://chevp.github.io/chevp-workflow/index.md) — workspace-mode contract (relevant when wiring submodule)

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
| H1 | If we build a Python CLI wrapping `claude -p` and exposing gate-checks as commands, then framework discipline becomes mechanizable in CI and terminal flows, **because the lifecycle is fundamentally a state machine over markdown files**. | Implement `chevp-flow context init "intent"` → generate CTX-NNN draft → diff against what Claude Code produces. | If post-processing the generated draft is needed >30% of the time, abstraction is too thin. |
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
| R7 | Ironically: the "process-driven, not spec-driven" tension surfaces — `chevp-flow context init INTENT` could be misused as one-shot spec generation. | med | high (constitutional) | Structurally enforce the *dialogue* nature of Context: `init` only seeds, requires explicit dialogue rounds before G1. |

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

## Open Questions (for human decision at G1)

- [ ] **Q1 — License**: Apache-2.0 or MIT? (AI recommendation: Apache-2.0 — patent grant matters for OSS framework adoption.)
- [ ] **Q2 — Python floor**: 3.11 or 3.12? (AI recommendation: 3.11 — wider compatibility, still has Self/typing improvements.)
- [ ] **Q3 — Submodule path** in chevp-ai-framework: `tools/chevp-flow/`, `vendor/chevp-flow/`, or `.chevp-flow/`? (AI recommendation: `tools/chevp-flow/` — discoverable, conventional.)
- [ ] **Q4 — Subagent prompts**: vendored into chevp-flow at pinned version, or fetched at runtime from chevp-ai-framework? (AI recommendation: vendored — reproducibility wins for v1; revisit at v2.)
- [ ] **Q5 — v1 command surface**: minimum (`init`, `status`, `approve`, `gate-check`) or include `new-adr`, `propose`, `kill`? (AI recommendation: minimum + `new-adr` — ADRs are needed during Context already.)
- [ ] **Q6 — Mode-inference in CLI**: should commands carry explicit mode (`chevp-flow exploration plan ...`) or infer from current state? (AI recommendation: explicit — non-interactive CLI cannot infer reliably; explicitness matches git's design.)
- [ ] **Q7 — Initial Architecture decision**: monorepo single-package or split into `chevp-flow-core` + `chevp-flow-cli`? (AI recommendation: single package for v1; split only if reuse pressure emerges.)

## Scope Boundaries (Draft)

**Likely in scope**
- Python 3.11+ CLI using Typer + Rich, distributed via uv-buildable wheel
- `claude -p` subprocess wrapper with JSON-stream parser
- v1 command surface: `init`, `status`, `approve`, `gate-check`, `new-adr` (per Q5)
- Markdown-file state layer (`context/`, `exploration/`, `production/`)
- Provenance guardrails (refuse to write human-decision fields)
- One Dockerfile for gatekeeper-subagent isolation
- Apache-2.0 license + minimal `README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`
- Public GitHub repo at `github.com/chevp/chevp-flow` (or similar)
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
- **Fundamental ADRs** drafted (candidates):
  - ADR-001: Async file-based CLI vs. sync REPL
  - ADR-002: Pfad-2 (claude subprocess) vs. Anthropic API direct
  - ADR-003: Submodule + PyPI dual-distribution
  - ADR-004: License choice (per Q1)
  - ADR-005: Subagent-prompt vendoring strategy (per Q4)
  - ADR-006: Adapter-Contract specification (lives in chevp-ai-framework)
- **UX prototype** for the four core commands' CLI output (Rich rendering)
- **Challenger output** — top-3 failure modes, ≥2 alternative architectures (e.g., Go+Cobra, TS+Bun rejected with reasons), strongest counter-argument, product-coherence check
- **`insights.md`** seeded
