---
id: ADR-006
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

# ADR-006: Adapter-Contract specification lives in chevp-ai-framework

## Status

Proposed

## Context

`chevp-flow` is the **first concrete adapter implementation** of chevp-ai-framework's lifecycle. CTX-002's framing positions chevp-flow as a portability proof — the Markdown core is tool-agnostic, the plugin layer is Claude-Code-specific, and chevp-flow validates that the core can be driven from a separate tool.

For a *second* adapter (chevp-cursor, chevp-aider, chevp-cli-bare, etc.) to be possible, the framework must expose an explicit, versioned **Adapter-Contract**: the set of behaviours a tool must implement to be a conforming adapter. Without it:
- Each adapter would re-derive the contract by reading source files (duplicated effort, drift risk)
- Framework changes would silently break existing adapters
- The "tool-independence" claim remains an assertion

The contract describes:
1. Mode-switching semantics (Context / Exploration / Production gating)
2. Artifact frontmatter schema and field allowlist/denylist (Rule #7)
3. `evidence:` block validation rules
4. Gatekeeper invocation interface (input plan + artifacts → verdict + proposals)
5. `governance-log.md` append-only contract
6. PROP-NNN spawn rules (max 5 per gate, format)

## Decision

The **Adapter-Contract specification lives in `chevp-ai-framework`** (not in chevp-flow), at `01-context/adapter-contract.md` (parallel to existing files like `software-architecture.md`). chevp-flow references it by path + framework version.

Each conforming adapter declares:

```
adapter-contract-version: v1.0   # in adapter's manifest / version.go
chevp-ai-framework-tag: v1.3.0   # release this contract was implemented against
```

`chevp-flow` checks at startup: if its declared `chevp-ai-framework-tag` is older than the user's local chevp-ai-framework repo (when running as submodule), emit a `WARNING: framework version drift` message.

## Alternatives

### Alternative A: Contract in chevp-ai-framework (chosen)
- Pros:
  - Canonical location — the framework owns its own contract
  - Multiple adapters can conform without copying
  - Versioned alongside the framework itself
  - Existing 01-context/ structure is the natural home
- Cons:
  - Cross-repo coordination needed for any contract change
  - Contract changes block adapter releases until adapters update

### Alternative B: Contract in chevp-flow (rejected)
- Pros: Co-located with first implementation
- Cons:
  - Couples contract to first adapter; second adapter would have to copy or reference
  - Implies chevp-flow is "the canonical adapter" — undermines tool-independence claim
  - Contract changes are hidden in implementation repo

### Alternative C: Separate `chevp-adapter-spec` repo
- Pros: Maximum decoupling; adapters depend on a stable spec
- Cons:
  - Three repos to coordinate (framework, spec, adapter) — over-engineering for v1
  - Spec without an implementation is hard to validate
  - Versioning multiplies (framework version × spec version × adapter version)

## Consequences

### Positive
- Future adapters (chevp-cursor, chevp-aider, etc.) have a single contract to implement
- Framework changes that affect adapters are deliberate and discoverable (contract-version bump)
- "Tool-independence" claim becomes operationally meaningful, not aspirational

### Negative
- Parallel work item: drafting the Adapter-Contract document is part of CTX-002's scope (per CTX-002 Confirmation Needed #6) and falls back into chevp-ai-framework's own Context-step queue
- Cross-repo PR coordination when contract evolves

### Risks
- **R-ADR-006-1**: Contract drift between what the framework actually enforces and what the contract says. Mitigation: contract document is reviewed alongside framework changes; gatekeeper-g1 includes a "contract-conformance" check at G1 of any framework-modifying CTX.
- **R-ADR-006-2**: Adapter-contract-version becomes a versioning bureaucracy. Mitigation: keep it minimal — bump only on breaking changes; semantic versioning with strict rules.

## Implementation note

The Adapter-Contract document itself is **out of scope for chevp-flow**. It is a chevp-ai-framework artifact that must be drafted in parallel before chevp-flow's own G2 in Exploration. CTX-002 already declares this in its "Confirmation Needed #6" and "Likely in scope" sections.

## Cross-references
- Parent: [CTX-002](../../../plans/CTX-002-chevp-flow-cli.md) — Confirmation Needed #6, "Adapter-Contract parallel work"
- Future location: `01-context/adapter-contract.md` (to be drafted)
- Related: ADR-005 (vendoring binds chevp-flow to a specific framework version)
- Risks: CTX-002 R6
