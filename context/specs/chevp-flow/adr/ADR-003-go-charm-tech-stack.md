---
id: ADR-003
type: ADR
status: proposed
proposed-by: ai
decided-by: —
approved-by: —
approved-at: —
supersedes: —
parent-ctx: CTX-002
parent-spec: context/specs/chevp-flow/README.md
date: 2026-04-24
---

# ADR-003: Go 1.22+ with Charm Stack as tech stack

## Status

Proposed

## Context

`chevp-flow` is a CLI tool that:
- Orchestrates LLM subprocess calls (Pfad 2 per ADR-002)
- Parses + writes markdown with strict YAML frontmatter
- Renders rich terminal output (status, verdicts, summaries)
- Drives interactive forms at gate-approval and proposal-triage points
- Optionally containerises gatekeeper subagents (Docker)
- Must be installable with one command and run as a single binary

Three tech stacks were considered: Python (Typer + Rich + uv), TypeScript (Bun + Ink + Commander), and Go (Cobra + Charm Stack). The discussion in CTX-002 narrowed down via tradeoff analysis; the human's final decision moved from an initial Python lean to **Go + Charm Stack**.

## Decision

Adopt **Go 1.22+** with the following library set:

- **Cobra** — command tree, args parsing, help generation
- **Bubble Tea** — TUI framework for streaming-claude progress views
- **Huh** — interactive forms (single-select, multi-select, text input) for gate approvals and proposal triage; semantically maps to the framework's `AskUserQuestion` pattern (Rule #13)
- **Glamour** — markdown rendering for verdicts, summaries, status output
- **Native Go Docker SDK** (`github.com/docker/docker/client`) — gatekeeper container isolation (per Q3 docker scope)
- **`embed.FS` (stdlib)** — vendor subagent prompts and templates into the binary (per ADR-005)

Go floor: **1.22** (range-over-func stable, generics mature, broad distribution availability).

## Alternatives

### Alternative A: Python (Typer + Rich + uv)
- Pros: Anthropic-SDK-Python rich; familiar to AI-tool builders; Pydantic for parsing
- Cons:
  - Single-binary distribution awkward (PyInstaller / shiv / uv tool install — none as clean as a Go binary)
  - Runtime install friction (Python interpreter required on user machines)
  - Cold-start slower than Go
- **Rejected after initial selection** — single-binary distribution and Docker SDK ergonomics tipped the choice

### Alternative B: Go + Charm Stack (chosen)
- Pros:
  - Single static binary via `goreleaser` (mac/linux amd64+arm64)
  - `brew install chevp` is genuinely trivial
  - Native Docker SDK (Docker itself is Go) — first-class gatekeeper containers
  - Huh forms map cleanly to `AskUserQuestion` UX pattern
  - Cold-start ≤ 100ms easily achievable
  - Bubble Tea handles streaming-claude UX natively
- Cons:
  - `anthropic-sdk-go` is younger and more boilerplate-heavy for streaming/tool-use (R8) — partially mitigated because we use Pfad 2 (subprocess), not the SDK
  - Manual Go structs for `claude -p` JSON events (vs Python Pydantic conveniences) (R9)
  - Smaller AI/LLM ecosystem in Go (fewer reference implementations)

### Alternative C: TypeScript (Bun + Ink + Commander)
- Pros: Anthropic SDK most polished in TS; MCP is TS-native; `bun build --compile` for single-file binaries
- Cons:
  - Bun ecosystem still maturing; single-binary story weaker than Go
  - Cross-platform Docker SDK in Node not as native as Go
  - Adoption surface narrower (Go is more universal for CLI tooling)
- **Rejected** — Go's single-binary + Docker-native combination won

## Consequences

### Positive
- `brew install chevp` works on day one
- Cross-compilation built into Go toolchain — multi-arch releases via goreleaser
- Native Docker SDK simplifies the Q3 gatekeeper-container path
- Huh forms produce gate-approval UX that matches the framework's clickable-decisions model (Rule #13)

### Negative
- More verbose JSON parsing than Python (`encoding/json` + manual struct tags vs Pydantic)
- AI-ecosystem reference code in Go is sparser; some patterns must be invented locally
- If we ever want Pfad 3, `anthropic-sdk-go` is less rich than TS SDK (deferred via ADR-002)

### Risks
- **R-ADR-003-1** (= CTX-002 R8): `anthropic-sdk-go` immaturity — deferred risk
- **R-ADR-003-2** (= CTX-002 R9): JSON-stream parsing verbosity — mitigated by central message-type package + integration test fixtures
- **R-ADR-003-3**: Smaller AI ecosystem in Go means more local invention. Acceptance: chevp-flow is intentionally narrow in scope; we don't need the broader AI ecosystem.

## Cross-references
- Parent: [CTX-002](../../../plans/CTX-002-chevp-flow-cli.md) — Tech-Stack row
- Drives: ADR-002 (Pfad 1 unavailable in Go), ADR-005 (embed.FS vendoring is Go-native)
- Risks: CTX-002 R8, R9
