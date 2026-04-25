---
id: ADR-005
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

# ADR-005: Vendor subagent prompts via Go `embed.FS`, pinned to chevp-ai-framework release tag

## Status

Proposed

## Context

`chevp-flow` invokes the framework's three gatekeeper subagents (`gatekeeper-g1`, `gatekeeper-g2`, `gatekeeper-g3`) and four skills (`create-ctx-plan`, `create-exp-plan`, `create-adr`, `sync-plan-issues`). These live as markdown files in `chevp-ai-framework/agents/` and `chevp-ai-framework/skills/`. The CLI must access their text at runtime to construct the `--append-system-prompt` argument to `claude -p`.

Three sourcing strategies are possible:

1. **Vendored at build time** via Go `embed.FS`, pinned to a specific chevp-ai-framework release tag.
2. **Runtime fetch** from the user's local chevp-ai-framework repo (via the submodule path `tools/chevp-flow/`).
3. **Hybrid** — vendored by default, runtime override via `--framework-path` flag.

The framework can evolve faster than chevp-flow ships (R6 in CTX-002). At the same time, single-binary distribution (per ADR-003) implies the binary should work without external file dependencies.

## Decision

Use **Go `embed.FS` to vendor subagent prompts and skill instructions into the chevp-flow binary at build time**. The vendored set is pinned to a specific chevp-ai-framework release tag, recorded in `version.go` as `frameworkVersion` and surfaced via `chevp version`.

Re-vendoring is performed only via the explicit `chevp prompts update --tag <release-tag>` command (resolved as SQ2). On `chevp upgrade`, the bundled prompts come along with the binary upgrade — no live fetching, no surprise content drift.

A future enhancement (post-v1, see ADR-005's Consequences) may add `chevp prompts check` to warn when the bundled framework tag is older than 30 days.

## Alternatives

### Alternative A: Vendored `embed.FS`, version-pinned (chosen)
- Pros:
  - Reproducible verdicts (the same chevp-flow binary always runs the same prompts)
  - Offline-capable (per SQ5 — gate-check works without network beyond `claude -p`)
  - Single-binary integrity preserved
  - Drift is deliberate: user must run `chevp prompts update --tag` to get newer prompts
- Cons:
  - Drift accumulates if user doesn't update — a chevp-flow released 6 months ago won't see new gates added in chevp-ai-framework v1.4
  - Re-vendoring is a maintenance task each chevp release

### Alternative B: Runtime fetch from submodule
- Pros: Always current; no re-vendoring needed
- Cons:
  - Requires the user to have `chevp-ai-framework` checked out (breaks standalone install)
  - Network or filesystem dependency for every `gate-check` invocation
  - "Same binary, different verdict" possible — undermines reproducibility

### Alternative C: Hybrid (vendored + `--framework-path` override)
- Pros: Default ergonomics + power-user override
- Cons:
  - Two code paths to test
  - Mixed mode: which prompts are running becomes hard to debug
  - v1 over-engineering risk (R4)

## Consequences

### Positive
- chevp-flow binary is fully self-contained
- Verdicts are reproducible across users with the same binary
- Implementation is straightforward — `//go:embed prompts/*.md skills/**/*.md` in one file
- Update path is explicit and traceable (`CHANGELOG.md` records each prompt-update tag)

### Negative
- Maintenance overhead: each chevp-flow release coordinates with a chevp-ai-framework tag
- Drift between framework and CLI is possible if user lags on updates
- Bundled binary size grows with prompt volume (acceptable; prompts are kilobytes)

### Risks
- **R-ADR-005-1** (= CTX-002 R6): adapter-contract drift over time — mitigated by `version.go` declaring supported framework version range; `chevp gate-check` warns if range exceeded
- **R-ADR-005-2**: Bug in vendored prompt requires patch release of chevp-flow (cannot be hotfixed by user). Acceptance: same as any binary tool; mitigated by clear release cadence

## Implementation notes

```go
// internal/runtime/prompts.go
package runtime

import "embed"

//go:embed prompts/*.md prompts/skills/*.md
var Prompts embed.FS
```

Build-time check: a Make target `make verify-prompts` confirms `prompts/` directory contents match a known checksum from a chevp-ai-framework release tag. Mismatch fails the build.

## Cross-references
- Parent: [CTX-002](../../../plans/CTX-002-chevp-flow-cli.md) — Subagent-prompts row, Q4
- Resolves: CTX-002 Q4, SPEC SQ2
- Related: ADR-003 (Go tech stack enables embed.FS), ADR-006 (Adapter-Contract — versioning lives there)
- Risks: CTX-002 R6
