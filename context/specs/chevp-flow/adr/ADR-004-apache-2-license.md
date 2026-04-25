---
id: ADR-004
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

# ADR-004: Apache-2.0 license for chevp-flow

## Status

Proposed

## Context

`chevp-flow` is a public OSS project (CTX-002 Audience: third-party developers). A license must be set before the GitHub repo is made public; downstream adopters need clear redistribution terms and patent posture. Three permissive options were considered: Apache-2.0, MIT, and MPL-2.0.

The framework `chevp-ai-framework` is itself a process framework with potential adopters in regulated and enterprise contexts (CTX-002 Why-now: validate portability, OSS adoption). License posture matters more than for a hobby tool.

## Decision

Apply the **Apache License, Version 2.0** to all source code, vendored prompts and templates in the chevp-flow repository. Include a `LICENSE` file at repo root and a `NOTICE` file for any third-party components that require attribution (Cobra, Charm libraries, Docker SDK).

## Alternatives

### Alternative A: Apache-2.0 (chosen)
- Pros:
  - Explicit patent grant — protects adopters from contributor patent claims
  - Standard for OSS frameworks in enterprise contexts
  - Compatible with most other permissive licenses
  - Required attribution + change notices clarify provenance
- Cons:
  - More boilerplate (`NOTICE` file, longer header convention)
  - Slightly heavier than MIT for tiny utilities

### Alternative B: MIT
- Pros: Maximally permissive; minimal boilerplate; popular for small CLI tools
- Cons:
  - No patent grant — adopters in patent-sensitive domains (large enterprises) may hesitate
  - Less coverage of contributor expectations than Apache-2.0

### Alternative C: MPL-2.0
- Pros: File-level copyleft preserves modifications to MPL files while allowing combination with proprietary code
- Cons:
  - Unusual for CLI tools — adoption signal would be ambiguous
  - File-level copyleft adds review overhead for contributors
  - Compatibility complexity in mixed-licence projects

## Consequences

### Positive
- Adoption-friendly for enterprise users worried about patents
- Industry-standard for framework projects (Cobra is Apache-2.0; Bubble Tea is MIT but compatible)
- Clear contributor terms; contributor license agreement typically not needed (DCO-style is sufficient)

### Negative
- `NOTICE` file maintenance: every dependency requiring attribution must be tracked
- Header text in source files is longer than MIT

### Risks
- **R-ADR-004-1**: Forgetting to track NOTICE entries for new dependencies. Mitigation: pre-release checklist; `goreleaser` step that validates all deps' licenses.
- **R-ADR-004-2**: License incompatibility with a future dependency. Mitigation: review every new dep at PR time; reject GPL/AGPL transitively.

## Cross-references
- Parent: [CTX-002](../../../plans/CTX-002-chevp-flow-cli.md) — License row
- Resolves: CTX-002 Q1
- Related: ADR-003 (tech stack — Cobra/Charm/Docker SDK licenses must be NOTICE-compatible; all are)
