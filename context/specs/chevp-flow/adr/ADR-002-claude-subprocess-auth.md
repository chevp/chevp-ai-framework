---
id: ADR-002
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

# ADR-002: Pfad 2 — `claude -p` subprocess for AI generation

## Status

Proposed

## Context

`chevp-flow` needs to invoke Claude for AI-generated content (CTX drafts, gatekeeper verdicts, ADR bodies, EXP plans, PROP triage suggestions). Three paths to Claude exist:

1. **Pfad 1 — Claude Agent SDK** (TypeScript / Python). Uses the user's logged-in Claude Code authentication; covered by Claude Code Max subscription. Brings subagents, MCP, hooks, tool-use as first-class primitives.
2. **Pfad 2 — `claude -p` subprocess.** Shell out to the `claude` CLI with `--output-format stream-json`. Same Max-subscription auth as Pfad 1. Slightly coarser layer.
3. **Pfad 3 — Anthropic API direct** (`anthropic-sdk-go`). Separate token billing, full control, provider-agnostic.

Constraints:
- Tech stack is Go (per ADR-003); Claude Agent SDK is TS/Python only — Pfad 1 is unavailable except by spawning a TS subprocess (defeats purpose).
- `anthropic-sdk-go` is younger and more boilerplate-heavy for streaming + tool-use than the TS SDK.
- Claude Code Max subscription should "just work" for the framework author and other Max users (CTX-002 Audience requirement).

## Decision

Adopt **Pfad 2** — invoke the `claude` CLI as a subprocess with `--output-format stream-json`. The CLI is responsible for parsing line-delimited JSON events, streaming progress to the TUI (Bubble Tea), and producing the final artifact body.

Pfad 3 is **deferred to v2** as an optional fallback for non-Claude-Code environments. Pfad 1 is structurally unavailable in Go and not pursued.

## Alternatives

### Alternative A: Pfad 1 — Claude Agent SDK
- Pros: Subagents, MCP, hooks built-in; richest API
- Cons: TS/Python only; calling from Go would mean spawning a TS runtime — operationally absurd

### Alternative B: Pfad 2 — `claude -p` subprocess (chosen)
- Pros:
  - Max subscription gilt directly (zero token billing for subscription holders)
  - `claude` is a single binary already on the user's PATH
  - Stream-json schema is documented and stable enough
  - Claude Code's subagents and MCP are still indirectly leveraged via `--append-system-prompt`
- Cons:
  - Tight coupling to `claude -p` JSON schema (versioning risk)
  - Manual Go struct definitions per message type (R9)
  - No first-class tool-use API; tools handled by the spawned `claude` instance

### Alternative C: Pfad 3 — `anthropic-sdk-go`
- Pros: Provider-agnostic groundwork; fine-grained control over caching, thinking, batch
- Cons:
  - Separate token billing (would split the OSS audience into "subscription users" and "API-key users")
  - SDK is younger; streaming + tool-use need more boilerplate
  - Would still need a parallel system-prompt loader, since chevp-ai-framework subagent prompts are file-level

## Consequences

### Positive
- Max-subscription users get full functionality with no extra setup
- Implementation simplicity (single subprocess wire format)
- Subagents (gatekeeper-g1/g2/g3) work via `--append-system-prompt` — same path as Claude Code itself

### Negative
- Hard dependency on `claude` CLI being installed and authenticated
- Schema fluctuations in `claude -p` output require pinned minimum version + integration test fixtures
- No machine-readable structured tool-use; we synthesize tool calls via output parsing

### Risks
- **R-ADR-002-1** (= CTX-002 R1): `claude -p` schema/auth flow changes break the CLI. Mitigation: pin minimum version; integration tests against latest; declare supported version range in `version.go`.
- **R-ADR-002-2**: Users without Claude Code installed cannot use chevp-flow. Mitigation: clear error message + install instructions; defer Pfad 3 to v2 as fallback.
- **R-ADR-002-3** (= CTX-002 R8): If Pfad 3 ever needs adding (provider switch, non-Claude environments), `anthropic-sdk-go` immaturity costs more than expected. Acceptance: deferred risk; revisit at v2 planning.

## Cross-references
- Parent: [CTX-002](../../../plans/CTX-002-chevp-flow-cli.md) — Auth-Pfad row
- Related: ADR-003 (tech stack — drives Pfad 1 unavailability)
- Risks: CTX-002 R1, R8, R9
