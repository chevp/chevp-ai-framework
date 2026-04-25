---
id: EXP-001
type: EXP
status: draft
proposed-by: ai
decided-by: —
approved-by: —
approved-at: —
depends-on: CTX-002
blocks: PRD-001
exploration-mode: A
parent-ctx: CTX-002
parent-spec: context/specs/chevp-flow/README.md
date: 2026-04-25
evidence:
  hypothesis: The architecture pinned by ADRs 001–006 (async file-based CLI, Pfad-2 subprocess, Go+Charm, embed.FS vendoring, Adapter-Contract location) is implementable in 2–3 weeks of solo work without architectural surprises that force re-opening Context. The exploration validates the chosen path by building a working prototype of the four core flows (init / gate-check / approve / promote) end-to-end.
  result: —
  reasoning: —
---

# EXP-001: chevp-flow architecture exploration

## Goal

Validate the architectural design pinned by [ADR-001](../adr/ADR-001-async-file-based-cli.md) through [ADR-006](../adr/ADR-006-adapter-contract-location.md) by producing an implementation-ready Go prototype that exercises the four core flows of the System Spec end-to-end (`chevp context init`, `chevp gate-check G1`, `chevp approve <id>`, `chevp promote PROP-NNN`). Output: working binary + integration tests + Challenger output + `insights.md` capturing what the prototype taught us.

## Context

CTX-002 was approved at G1 on 2026-04-25, signed by `chevp`. Six fundamental ADRs pin: async file-based interaction model, `claude -p` subprocess as auth path, Go 1.22+ with Charm Stack, Apache-2.0 license, subagent-prompt vendoring via Go `embed.FS`, and the Adapter-Contract location in chevp-ai-framework. The System Spec at [context/specs/chevp-flow/README.md](../README.md) gives the rough Module Structure. This Exploration tightens the rough structure into precise package boundaries, function signatures, error-type taxonomy, integration-test fixtures, and a working prototype.

`exploration-mode: A` — the architectural choices are pinned; the exploration is **hypothesis-validation** (does the chosen architecture survive contact with `claude -p` reality?), not solution-comparison. If the prototype reveals a load-bearing decision was wrong, fall back to Context (per CLAUDE.md fallback rule).

## Vision Alignment

- **Outcome this serves** — First concrete instantiation of the Adapter-Contract; dogfooding loop for the framework author. Note: this work alone does **not** *validate* tool-independence — validation requires a second adapter or external adoption signal (see PROP-001 / PROP-003). EXP-001 is the *necessary first step toward* tool-independence, not the proof of it. Revised from initial framing per Challenger §"Product-Coherence Check #1".
- **Builds on** — CTX-002, ADRs 001–006, SPEC. **Contradicts** — none.
- **Problem evidence** — *Hypothetical.* No external adopter has yet asked for this; the framework author wants a dogfooding loop. Honest motivation: as much for the author's intellectual integrity (being able to demonstrate the contract is implementable) as for measurable end-user value. Per Challenger §"Counter-Argument" — naming this openly rather than disguising it.

## Scope

### IN Scope

- Concrete Go package layout with all v1 files, public APIs, and exported types
- Error-type taxonomy (sentinel errors, wrapped errors, exit-code mapping per SPEC §Error Model)
- Bubble Tea progress model for streaming `claude -p` output
- Integration-test fixtures: 5–10 captured `claude -p --output-format stream-json` outputs covering happy-path + error cases
- Unit-test parity check: Go `internal/state/provenance.go` vs. Python `hooks/provenance-check.py` on shared fixture set
- Goreleaser config skeleton (`.goreleaser.yml`) for darwin/linux × amd64/arm64
- One end-to-end working prototype: `chevp context init "test intent"` actually invokes `claude -p`, generates a valid CTX file, and round-trips through frontmatter validation
- Prototype of `chevp gate-check G1` that runs the gatekeeper-g1 vendored prompt and parses the verdict
- Prototype of `chevp approve CTX-NNN` that signs frontmatter + appends governance-log
- One Huh-form prototype: PROP triage flow
- Glamour rendering for verdicts and status output
- `insights.md` capturing surprises, refuted assumptions, and product-coherence observations
- Challenger output (top-3 failure modes, ≥2 alternative architectures rejected with reasons, counter-argument paragraph, product-coherence check)

### NOT in Scope

- Production code beyond prototype scope (full v1 polish, error messages, edge-case handling) — moves to PRD-001
- Adapter-Contract document in chevp-ai-framework (parallel framework work; separate plan in chevp-ai-framework's own queue)
- Distribution-strategy ADR (PROP-004, deferred for chevp-flow's own EXP queue once repo exists)
- Gatekeeper Docker isolation (deferred; subprocess default per SQ3)
- Multi-provider LLM support (PROP-001, deferred)
- Windows support (PROP-002, deferred)
- Submodule integration into chevp-ai-framework (Workspace-mode work; happens after chevp-flow repo is created in PRD-001)
- Homebrew tap creation (deferred to first release in PRD-001)
- Auto-update mechanism (`chevp prompts update --tag` is post-v1 polish)

### REMOVED / Obsoleted

— (greenfield project; nothing to remove)

## Steps

1. **Repo skeleton + Cobra root** — Create chevp-flow directory structure under `context/specs/chevp-flow/prototype/` (NOT a real repo yet; just a build-able skeleton). Implement `cmd/chevp/main.go` and `internal/cli/root.go` (Cobra root with `--help` and `--version`). Verify `go build ./cmd/chevp` succeeds.

2. **State layer — frontmatter parse/serialise** — Implement `internal/state/artifact.go` using `gopkg.in/yaml.v3` `yaml.Node` for field-order preservation. Round-trip test: parse → serialise should produce byte-identical output for a known fixture (10 governed artifacts from chevp-ai-framework).

3. **Provenance enforcement** — Port `hooks/provenance-check.py` logic to `internal/state/provenance.go`. Define `WriteMode` enum (`AIMode`, `ApproveMode`, `OverrideMode`) and a `Validate(prev, next Artifact, mode WriteMode) error` function. Write unit tests with ≥10 fixture cases pulled from the Python reference's test inputs.

4. **Claude runtime — subprocess wrapper** — Implement `internal/runtime/claude.go` with `RunClaude(ctx, prompt, opts) (<-chan Message, error)`. Define `Message` struct types in `internal/runtime/messages.go` for each `--output-format stream-json` event type (`text`, `tool_use`, `result`, `error`, etc.). Capture 5–10 real outputs as fixtures in `testdata/claude/`.

5. **Subagent invocation** — Implement `internal/runtime/subagent.go` with `RunSubagent(ctx, name, plan)`. Vendor gatekeeper-g1.md, gatekeeper-g2.md, gatekeeper-g3.md from chevp-ai-framework into `prompts/` via `//go:embed`. Implement loading + system-prompt-construction.

6. **First flow: `chevp context init`** — Implement `internal/cli/context.go`. End-to-end test: `chevp context init "test intent"` writes a valid CTX-NNN file in a test directory, frontmatter validates against provenance rules, content streams through Bubble Tea progress view.

7. **Second flow: `chevp approve <id>`** — Implement `internal/cli/approve.go`. Honor-System actor detection per SQ1: read `git config user.name`, warn if `CI=true` env. Refuse if `approved-by` already set. Append governance-log entry in canonical format.

8. **Third flow: `chevp gate-check G1`** — Implement `internal/gates/checker.go` and `internal/gates/verdict.go` (parser for the `GATEKEEPER:/VERDICT:/...` block). Test: invoke against CTX-002 itself, expect `conditional-pass` verdict matching the Explore-agent simulation we ran on 2026-04-24/25.

9. **Fourth flow: `chevp promote PROP-NNN`** — Implement `internal/cli/promote.go`. Read proposal, instantiate plan from template, move proposal to `proposals/promoted/`, append governance-log.

10. **TUI polish — Huh + Glamour** — Implement `internal/tui/forms.go` (Huh-based PROP triage) and `internal/tui/render.go` (Glamour wrapper). Prototype the triage flow end-to-end against the 5 PROPs from CTX-002.

11. **Goreleaser config** — Write `.goreleaser.yml` for darwin/linux × amd64/arm64. Verify `goreleaser build --snapshot --clean` produces 4 binaries.

12. **Challenger pass** — Produce `context/specs/chevp-flow/exp/EXP-001.challenger.md` with top-3 failure modes, ≥2 alternative architectures rejected with reasons, counter-argument paragraph, and product-coherence check engaging with the Vision Alignment.

13. **`insights.md`** — Write `context/specs/chevp-flow/insights.md` capturing: which hypothesis from H1/H2/H3 in CTX-002 was refuted/confirmed by prototyping, surprises, and what we now believe about the architecture.

## Affected Files

All files NEW under `context/specs/chevp-flow/prototype/` (Exploration-stage skeleton; will move to its own repo in PRD-001):

- `prototype/cmd/chevp/main.go` — Cobra root entry, version, embed dir registration
- `prototype/internal/cli/root.go` — Cobra root command + persistent flags
- `prototype/internal/cli/context.go` — `chevp context init|status` subcommands
- `prototype/internal/cli/exploration.go` — `chevp exploration plan|status` (skeleton only at EXP-001; full impl deferred)
- `prototype/internal/cli/production.go` — `chevp production start|status` (skeleton only)
- `prototype/internal/cli/adr.go` — `chevp adr new` (skeleton only)
- `prototype/internal/cli/gatecheck.go` — `chevp gate-check {G1|G2|G3}`
- `prototype/internal/cli/approve.go` — `chevp approve <id>`
- `prototype/internal/cli/promote.go` — `chevp promote <PROP-id>`
- `prototype/internal/cli/reject.go` — `chevp reject <PROP-id> <reason>` (skeleton only)
- `prototype/internal/cli/status.go` — `chevp status`
- `prototype/internal/runtime/claude.go` — `RunClaude` streaming
- `prototype/internal/runtime/messages.go` — JSON-stream type defs
- `prototype/internal/runtime/subagent.go` — `RunSubagent`
- `prototype/internal/runtime/prompts.go` — `embed.FS` for vendored prompts
- `prototype/internal/state/artifact.go` — Frontmatter parse/write with `yaml.Node`
- `prototype/internal/state/provenance.go` — Port of `provenance-check.py`
- `prototype/internal/state/evidence.go` — Evidence-block validators
- `prototype/internal/state/governance_log.go` — Append-only writer
- `prototype/internal/gates/checker.go` — Gatekeeper invocation
- `prototype/internal/gates/verdict.go` — Verdict block parser
- `prototype/internal/gates/proposal.go` — PROP-NNN parser + writer
- `prototype/internal/tui/render.go` — Glamour wrapper
- `prototype/internal/tui/forms.go` — Huh forms
- `prototype/internal/tui/progress.go` — Bubble Tea streaming-claude view
- `prototype/prompts/gatekeeper-g{1,2,3}.md` — Vendored from chevp-ai-framework
- `prototype/prompts/skills/{create-ctx-plan,create-exp-plan,create-adr}.md` — Vendored
- `prototype/templates/*.md` — Vendored CTX/EXP/PRD/ADR/PROP templates
- `prototype/testdata/claude/*.jsonl` — Captured `claude -p` output fixtures
- `prototype/testdata/artifacts/*.md` — Reference governed artifacts
- `prototype/.goreleaser.yml`, `prototype/go.mod`, `prototype/go.sum`
- `context/specs/chevp-flow/exp/EXP-001.challenger.md` — Challenger output
- `context/specs/chevp-flow/insights.md` — Learning capture

## Risks

| Risk | Mitigation |
|------|------------|
| `claude -p` JSON-schema is not stable enough for fixture-based testing | Pin minimum `claude` version in `go.mod`/CI; snapshot tests with explicit version bumps; `runtime/messages.go` uses forward-compatible parsing (`json.RawMessage` for unknown event types) |
| Integration tests require `claude` available in CI runner — public CI may not have it | Use `claude --version` probe in test setup; mark integration tests as `//go:build integration` and run locally; CI runs only unit tests |
| Cobra (synchronous) and Bubble Tea (async) integration friction | Use `tea.Program` only for the streaming-claude command; non-streaming commands stay synchronous; document the boundary in `internal/tui/progress.go` |
| Frontmatter field-order preservation with `yaml.v3` is not guaranteed by default | Use `yaml.Node` for parse + serialise (preserves order at node level); round-trip property test against 10 reference artifacts before any other state-layer code lands |
| Go provenance logic diverges from Python original | Cross-check: feed both implementations the same fixture set, diff outputs; ≥10 fixture cases including all denial paths from `provenance-check.py` |
| Vendored prompt drift — chevp-ai-framework evolves between this EXP and PRD-001 | Pin chevp-ai-framework tag in `version.go` at exploration start; re-vendor only if a tag-bump is explicit; per ADR-005 |
| Bubble Tea + Glamour combination produces ANSI escape conflicts on some terminals | Test on at least 3 terminals (iTerm2, Terminal.app, Alacritty); fallback to plain text if `NO_COLOR` env is set |

## Kill Criteria

- **2-week timebox**: If after 2 weeks of solo work the prototype cannot generate a valid CTX file end-to-end via `claude -p` (Step 6), the Pfad-2 hypothesis (ADR-002) is refuted — fall back to Context, evaluate Pfad-3 (`anthropic-sdk-go`) or abandon
- **Frontmatter integrity**: If `yaml.Node` round-trip produces diffs that break provenance-check semantics on >1 of 10 reference fixtures, the YAML-handling approach is wrong — explore alternative (textual line-based parser) or revisit ADR-003
- **Charm cost**: If Cobra + Bubble Tea integration requires >300 lines of plumbing for the four core flows, the Charm stack is over-engineered for v1 — revisit ADR-003, consider plain `fmt.Println` + Glamour-only rendering
- **Provenance parity**: If Go-port provenance violates ≥1 case where Python original holds, port is structurally wrong — block until parity verified
- **Subagent context-loss (R2 from CTX-002, sharpened by Challenger FM-2)**: If gatekeeper-g1 invoked via `claude -p --append-system-prompt` produces materially different verdicts than the Claude-Code-native subagent on the same inputs — operationalised as **>20% finding-level mismatch on any of the 3 reference plans**, or top-level verdict mismatch on any plan — Pfad-2 cannot preserve subagent semantics. Fall back to Context, evaluate vendoring full prompt + tool-defs vs. Pfad-3.

## Acceptance Criteria

- [ ] Prototype binary builds via `go build ./cmd/chevp` on macOS + Linux (no cross-compile failures)
- [ ] `chevp context init "test"` end-to-end produces a valid CTX-NNN markdown file with correct frontmatter (parsed and verified by integration test)
- [ ] `chevp approve CTX-NNN` correctly mutates frontmatter (`status`, `decided-by`, `approved-by`, `approved-at`) + appends governance-log line in canonical format; refuses if `approved-by` already set
- [ ] `chevp gate-check G1` invokes gatekeeper-g1 prompt via `claude -p`, parses verdict, exits with appropriate code. **Verdict-fidelity (sharpened per Challenger FM-2 / Coherence-Check #2):** top-level verdict matches simulation on CTX-002, AND finding-level matches at ≥80% across at least 3 governed plans (CTX-002 + 2 additional plans to be selected during Step 8 — candidates: CTX-001, EXP-001 itself, or a synthetic test plan). Material divergence (>20% finding-level mismatch on any plan) triggers the Kill Criterion §"Subagent context-loss"
- [ ] `chevp promote PROP-NNN` round-trips: reads proposal, creates plan stub, moves proposal to `proposals/promoted/`, appends governance-log
- [ ] Provenance unit tests pass with ≥10 fixture cases; output matches `provenance-check.py` reference on every case
- [ ] `internal/state/artifact.go` round-trips field order on all 10 reference artifacts (byte-identical for properly-ordered inputs)
- [ ] `insights.md` documents at least one hypothesis verdict (H1/H2/H3 from CTX-002 marked `confirmed`/`refuted`/`inconclusive`) and one production-coherence observation
- [ ] [EXP-001.challenger.md](EXP-001.challenger.md) produced with top-3 specific failure modes (not generic), ≥2 alternative architectures rejected with reasons, counter-argument paragraph engaging the Vision Alignment, and a product-coherence check
- [ ] `.goreleaser.yml` `goreleaser build --snapshot --clean` succeeds, producing 4 binaries (darwin × {amd64, arm64}, linux × {amd64, arm64})
- [ ] `evidence:` block populated with non-generic content reflecting what the prototype actually demonstrated

## Cross-references

- Parent: [CTX-002](../../../plans/CTX-002-chevp-flow-cli.md) (G1 approved 2026-04-25)
- Spec: [chevp-flow System Spec](../README.md)
- ADRs: [ADR-001..006](../adr/)
- Risks linked back to CTX-002: R1, R2, R3, R6, R7, R9
- Will block: PRD-001-chevp-flow-v1-release (created at G2 transition)
- Parallel framework work: Adapter-Contract document in chevp-ai-framework `01-context/adapter-contract.md` (separate plan, owned by framework team)
