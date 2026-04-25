---
name: chevp-flow CLI
type: spec
status: draft
proposed-by: ai
decided-by: —
approved-by: —
approved-at: —
date: 2026-04-24
parent-ctx: CTX-002
---

# chevp-flow Specification

> Specification for the `chevp` CLI binary that implements the chevp-ai-framework lifecycle as a portable, single-binary tool. Parent: [CTX-002](../../plans/CTX-002-chevp-flow-cli.md). Contract source: extracted from `commands/`, `hooks/`, `agents/`, `skills/`, `guidelines/architecture-governance.md`, `guidelines/uncertainty-reduction.md` (see CTX-002 Artifacts to Read/Verify).

## Overview

`chevp` is the binary; `chevp-flow` is the repo and Go module. The CLI mirrors the framework's nine slash commands, three hooks, three gatekeeper subagents and four skills as native Go subcommands, file-write guards and subprocess invocations. AI generation is delegated to `claude -p` (Pfad 2); the CLI is the deterministic wrapper that enforces provenance, parses verdicts and surfaces interactive approvals.

## Requirements

### Functional

1. **Artifact lifecycle ops** — read/write CTX, EXP, PRD, ADR, PROP markdown artifacts with strict YAML frontmatter parsing/serialization, preserving field order
2. **Mode-explicit commands** — `chevp context …`, `chevp exploration …`, `chevp production …` (no inference; per Q6)
3. **Claude subprocess runtime** — wrap `claude -p --output-format stream-json` with structured event consumption; surface streaming output via Bubble Tea
4. **Provenance enforcement** — port `provenance-check.py` logic into `internal/state/provenance.go`; refuse to write `decided-by`, `approved-by`, `approved-at`, `status: approved|accepted`, and `proposed-by: human` from any non-approve command
5. **Gate validation** — `chevp gate-check {G1|G2|G3}` invokes the corresponding gatekeeper subagent (vendored prompt from `embed.FS`), parses verdict block (`VERDICT: pass|conditional-pass|block`), parses spawned `PROP-NNN` entries
6. **Plan Proposal handling** — write PROP files to `context/plans/proposals/`, drive Huh form for triage (promote/reject/defer), append `governance-log.md`
7. **Append-only governance log** — `governance-log.md` writes are append-only; never rewrite existing lines
8. **ADR creation** — `chevp adr new "<title>"` instantiates `context/adrs/ADR-NNNN.md` from vendored template
9. **Approval flow** — `chevp approve <id> [note]` is the *only* path that may set human-decision fields; refuses if `approved-by` already set
10. **Markdown rendering** — Glamour for all CLI output (verdicts, summaries, status)
11. **Status query** — `chevp status` reports active step, last gate verdict, open Q-blocks, kill criteria reminders

### Non-functional

- **Single static binary** — `goreleaser` produces darwin/linux artifacts (amd64+arm64); no runtime deps beyond `claude` and `git`
- **Cold start** ≤ 100ms for non-claude commands (`status`, `approve`)
- **No network** beyond what `claude -p` already does
- **Cross-platform** — macOS + Linux at v1; Windows deferred
- **Stable on `claude -p` JSON schema fluctuations** — message types versioned; integration test fixtures pinned
- **Reproducible gatekeeper output** — vendored prompts via `embed.FS`; user can pin chevp-ai-framework version per chevp release

## Design

### Data Model

**Artifact frontmatter (governed by `guidelines/architecture-governance.md`):**

```yaml
---
id: CTX-NNN | EXP-NNN | PRD-NNN | ADR-NNNN | PROP-NNN
type: CTX | EXP | PRD | ADR | SPEC | PROP
status: draft | proposed | approved | accepted | superseded | deprecated
proposed-by: ai | pair          # CLI may write only these two
decided-by: —                   # human-only; CLI refuses to set
approved-by: —                  # human-only; CLI refuses to set
approved-at: —                  # human-only; CLI refuses to set
evidence:                       # required for CTX/EXP/PRD; gatekeeper validates
  hypothesis: <falsifiable belief>
  result: <observable fact>
  reasoning: <bridge → action>
---
```

**Governance-log line (tab-separated, append-only):**

```
<YYYY-MM-DD>  <GATE|ADR|PROP>  <id>  proposed:<ai|human|pair>  <action>:<actor>  "<note>"
```

**Gatekeeper verdict (parsed from claude output):**

```
GATEKEEPER: G1|G2|G3
PLAN: <id>
VERDICT: pass | conditional-pass | block
FINDINGS: …
EVIDENCE-BLOCK CHECK: …
SPAWNED PLAN PROPOSALS (max 5): …
NEXT ACTION: …
```

### Interfaces

**CLI command tree (Cobra):**

```
chevp
├── context init <intent>        seed CTX-NNN draft
├── context status               current Context-step state
├── exploration plan             create EXP-NNN (requires G1 pass)
├── exploration status
├── production start             create PRD-NNN (requires G2 pass)
├── production status
├── adr new "<title>"            create ADR-NNNN
├── gate-check {G1|G2|G3}        run gatekeeper subagent
├── approve <id> [note]          human-only; sign artifact
├── promote <PROP-id>            human-only; promote proposal to plan
├── reject <PROP-id> <reason>    human-only; reject proposal
├── status                       global state across all steps
└── version
```

**Public Go API surface (`pkg/`):** none in v1 (reserved; private internals only).

**Internal package interfaces:**

```go
// internal/runtime
type Message struct {
    Type    string          // "text", "tool_use", "result", ...
    Content json.RawMessage
}
func RunClaude(ctx context.Context, prompt string, opts ClaudeOpts) (<-chan Message, error)
func RunSubagent(ctx context.Context, name string, plan PlanRef) (Verdict, []Proposal, error)

// internal/state
type Artifact struct { Frontmatter map[string]any; Body string }
func Read(path string) (Artifact, error)
func Write(path string, a Artifact) error      // applies provenance.Validate before write
func ValidateProvenance(prev, next Artifact, mode WriteMode) error  // ports provenance-check.py

// internal/gates
type Verdict struct { Gate, Plan, Status string; Findings []Finding; Evidence EvidenceCheck; Proposals []Proposal; NextAction string }
func Check(ctx context.Context, gate Gate, plan PlanRef) (Verdict, error)

// internal/tui
func RenderMarkdown(s string) string                            // Glamour
func ConfirmApproval(prompt string) (bool, string, error)       // Huh form
func TriageProposals(props []Proposal) (TriageResults, error)   // Huh multi-select
```

**Subprocess wire format:** `claude -p --output-format stream-json --input <stdin> --append-system-prompt <vendored-prompt>` — events are line-delimited JSON; CLI parses each line into a `Message`.

### Flow

**Flow A — `chevp context init "auth for API"`**

1. Verify cwd has framework structure (presence of `context/plans/` or sentinel)
2. Scan `context/plans/` for next free `CTX-NNN`
3. Build prompt: vendored CTX template + `create-ctx-plan` skill content + user intent
4. Invoke `RunClaude(...)`; stream output via Bubble Tea progress view
5. Receive final markdown; parse frontmatter via `state.Read` semantics
6. Run `state.ValidateProvenance` in **AI write-mode** — must reject if AI-set decided-by/approved-by
7. Write `context/plans/CTX-NNN-<slug>.md`
8. Render summary via Glamour
9. Print: `Drafted CTX-NNN. Edit as needed, then run "chevp gate-check G1".`

**Flow B — `chevp gate-check G1`**

1. Locate active CTX plan (latest `status: draft|proposed` in `context/plans/`)
2. Load `embed.FS:prompts/gatekeeper-g1.md`
3. `RunSubagent("gatekeeper-g1", plan)` → returns parsed `Verdict`
4. Render verdict via Glamour
5. Branch on `Verdict.Status`:
   - `block` → exit code 1; list unmet criteria; suggest fixes
   - `conditional-pass` → write `PROP-NNN` files, drive Huh triage (promote/reject/defer per proposal), append governance-log
   - `pass` → exit 0; print `Run "chevp approve <id>" to sign G1`
6. **Never auto-approve** — pass verdict only suggests next manual action

**Flow C — `chevp approve CTX-NNN`**

1. Load artifact via `state.Read`
2. Verify `approved-by` is empty (`—`); else fail with "already approved"
3. Read `git config user.name` for actor identity
4. Apply mutations:
   - `status: draft → approved`
   - `decided-by: <git-user>`
   - `approved-by: <git-user>`
   - `approved-at: <today YYYY-MM-DD>`
5. `state.ValidateProvenance` in **human approve-mode** — these writes are *only* allowed via this command path (validated by call-site flag)
6. `state.Write` artifact
7. Append `governance-log.md` line: `<date>  G1  CTX-NNN  proposed:ai  approved:<user>  "<note>"`
8. Render confirmation via Glamour

**Flow D — `chevp promote PROP-012`**

Mirrors `commands/promote.md` exactly: read proposal, scan for next plan id, instantiate from template with proposal `Goal`/`Kill Criteria`, set `proposed-by: pair`, write new plan, move proposal to `proposals/promoted/`, append governance-log.

### Module Structure

```
chevp-flow/                            (repo root)
├── cmd/chevp/main.go                  Cobra root, wires subcommands
├── internal/
│   ├── cli/                           Cobra command definitions (one file per top-level group)
│   │   ├── context.go
│   │   ├── exploration.go
│   │   ├── production.go
│   │   ├── adr.go
│   │   ├── gatecheck.go
│   │   ├── approve.go
│   │   ├── promote.go
│   │   ├── reject.go
│   │   └── status.go
│   ├── runtime/                       claude -p wrapper
│   │   ├── claude.go                  RunClaude streaming
│   │   ├── messages.go                stream-json type defs
│   │   └── subagent.go                RunSubagent (loads embed.FS prompt)
│   ├── state/                         markdown + frontmatter ops
│   │   ├── artifact.go                Read/Write, frontmatter (yaml.Node for order preservation)
│   │   ├── provenance.go              ValidateProvenance (port of provenance-check.py)
│   │   ├── evidence.go                evidence-block validators (used by gatekeeper)
│   │   └── governance_log.go          append-only writer
│   ├── gates/                         gatekeeper invocation + verdict parsing
│   │   ├── verdict.go                 parse "GATEKEEPER:/VERDICT:/FINDINGS:" blocks
│   │   ├── proposal.go                parse PROP-NNN spawns; write PROP files
│   │   └── checker.go                 Check(gate, plan)
│   ├── tui/                           Charm wrappers
│   │   ├── render.go                  Glamour
│   │   ├── forms.go                   Huh forms (approval, triage)
│   │   └── progress.go                Bubble Tea progress view for streaming claude
│   └── docker/                        native Go Docker SDK
│       └── gatekeeper.go              optional --docker flag for gate-check
├── prompts/                           embed.FS, vendored from chevp-ai-framework
│   ├── gatekeeper-g1.md
│   ├── gatekeeper-g2.md
│   ├── gatekeeper-g3.md
│   └── skills/
│       ├── create-adr.md
│       ├── create-ctx-plan.md
│       └── create-exp-plan.md
├── templates/                         embed.FS, vendored
│   ├── context-plan-template.md
│   ├── plan-template.md
│   ├── adr-template.md
│   └── plan-proposal-template.md
├── version.go                         build-tag-injected version + chevp-ai-framework pinned tag
├── go.mod                             go 1.22
├── LICENSE                            Apache-2.0
├── README.md
├── CHANGELOG.md
└── .goreleaser.yml                    multi-arch binary releases
```

### State Machine

The CLI is stateless across invocations; **state lives in the markdown files**. Each command:

1. **Reads** the relevant subset of `context/`, `02-exploration/`, `03-production/`, `governance-log.md`
2. **Decides** allowed transitions from frontmatter `status` + provenance fields
3. **Writes** new state via `state.Write` with provenance validation

There is no daemon, no in-memory session, no lock file. Concurrent runs are user-supervised (same as git).

### Error Model

- Exit code 0 — success
- Exit code 1 — gate `block`, validation failure, or human-only field violation
- Exit code 2 — usage error
- Exit code 3 — claude subprocess failure (transient; retryable)
- Exit code 4 — provenance violation (must NOT be auto-retried)

All errors render via Glamour-styled red boxes; machine-readable JSON via `--output json` for CI integration (post-v1).

## Out of Scope

- Multi-provider LLM support (OpenAI, Cohere, Mistral)
- Direct `anthropic-sdk-go` integration (Pfad 3) — deferred until SDK matures
- Web UI / REST API / dashboard
- Team multi-user state, conflict resolution
- Windows support (mac/linux v1 only)
- IDE/editor plugins
- Auto-update of vendored prompts (re-vendor only on chevp release)
- `--output json` machine output (post-v1)
- Plugin system for third-party gatekeepers (post-v1)

## Open Questions (resolved by human via AskUserQuestion on 2026-04-24)

- [x] **SQ1** — `chevp approve` actor detection: **Honor-System + CI-Warning**. Trust `git config user.name`; if `CI=true` env detected, emit warning but do not block.
- [x] **SQ2** — Subagent-prompt update strategy: **Explicit `chevp prompts update --tag <version>`**. No auto-update; CHANGELOG documents the bundled chevp-ai-framework version.
- [x] **SQ3** — Gatekeeper execution default: **Subprocess + `--docker` opt-in flag**. Fast cold-start without Docker dependency at v1.
- [x] **SQ4** — Framework-repo detection: **v1 heuristic** (`context/plans/` exists or sibling), **v2 sentinel** (`.chevp/config.toml`). Avoids migration friction at v1.
- [x] **SQ5** — Offline governance ops: **All non-claude commands work offline**. `approve`, `status`, `promote`, `reject`, `gate-check` operate on local markdown + governance-log.md only; no network.

## Acceptance Criteria for SPEC approval

This spec is ready for G1 sign-off when:

1. The 11 functional requirements above are uncontested (no `[ ]` items remain after triage)
2. The Cobra command tree matches Q5 (`init`, `status`, `approve`, `gate-check`, `new-adr`) plus the necessary supporting commands (`promote`, `reject`, top-level `status`, `version`)
3. The `internal/state` provenance logic is verified to be a strict superset of `provenance-check.py`'s checks
4. The flow examples (A–D) are traced against the existing slash-command behaviors and shown equivalent
5. The five SQ open questions are answered (clickable, post-spec-acceptance)

## Cross-references

- Parent CTX: [CTX-002](../../plans/CTX-002-chevp-flow-cli.md)
- Provenance source: [guidelines/architecture-governance.md](../../../guidelines/architecture-governance.md)
- Evidence source: [guidelines/uncertainty-reduction.md](../../../guidelines/uncertainty-reduction.md)
- Gatekeeper contracts: [agents/gatekeeper-g1.md](../../../agents/gatekeeper-g1.md), [agents/gatekeeper-g2.md](../../../agents/gatekeeper-g2.md), [agents/gatekeeper-g3.md](../../../agents/gatekeeper-g3.md)
- Hook source: [hooks/provenance-check.py](../../../hooks/provenance-check.py), [hooks/gate-check.py](../../../hooks/gate-check.py), [hooks/mode-context.py](../../../hooks/mode-context.py)
- Slash-command sources: [commands/](../../../commands/)
- Skills: [skills/create-ctx-plan/](../../../skills/create-ctx-plan/), [skills/create-exp-plan/](../../../skills/create-exp-plan/), [skills/create-adr/](../../../skills/create-adr/)
