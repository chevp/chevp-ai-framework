# Architecture-Invariants Template

> Project-level executable invariants. Location: `context/guidelines/architecture-invariants.md`.
> Mode: Context (drafted) / continuously enforced via [governance-auditor](../agents/governance-auditor.md).
> Specified by [ADR-001](../context/adr/ADR-001-content-oriented-governance.md).

This template defines the **content layer** of architecture-governance: machine-checkable assertions about the codebase that bind to accepted ADRs. Where the provenance frontmatter answers *who decided*, the invariants answer *what must hold in the code right now*.

## File Schema

```yaml
---
name: <project-name> architecture invariants
type: invariants
status: draft            # draft | active
proposed-by: ai          # ai | human | pair
decided-by: —            # human (required when status: active)
approved-by: —           # human identifier
approved-at: —           # YYYY-MM-DD
date: YYYY-MM-DD
---

# Architecture Invariants — <Project>

## forbidden-imports
# Modules that must not be imported anywhere in `scope.include`.
- module: <module-name>
  reason: <one line — why this is forbidden>
  binding-adr: ADR-NNN          # the ADR this invariant codifies
  scope:
    include: ["src/**"]
    exclude: ["tests/**", "**/*.md"]

## layer-rules
# Dependency-direction rules between layer roots.
- from: <path-pattern>
  must-not-import-from: [<path-pattern>, <path-pattern>]
  binding-adr: ADR-NNN
  scope:
    include: ["src/**"]
    exclude: ["tests/**"]

## library-whitelist
# For a given role, only these libraries are permitted.
- role: <e.g. http-client | logger | orm>
  allowed: [<lib-a>, <lib-b>]
  binding-adr: ADR-NNN
  scope:
    include: ["src/**"]

## adr-bindings
# Free-form assertions that bind an accepted ADR to checkable claims.
- adr: ADR-NNN
  asserts:
    - "no module imports sqlite3"
    - "config key 'db.engine' equals 'postgres' in all envs"
  locator:
    type: ast-import      # ast-import | grep | config-query
    scope:
      include: ["src/**"]
      exclude: ["tests/**", "**/*.md", "vendor/**"]
    loose: false           # true permits full-text grep; default false
```

## Locator Discipline

Per ADR-001 §Decision-1, locators MUST follow these rules:

| Field | Required | Notes |
|-------|----------|-------|
| `type` | yes | One of `ast-import`, `grep`, `config-query`. Free-text types are rejected. |
| `scope.include` | yes | At least one glob. Empty scope is a configuration error. |
| `scope.exclude` | recommended | Default exclusions: `tests/**`, `**/*.md`, `vendor/**`, `node_modules/**`. |
| `loose` | optional | `false` by default. `true` enables full-text grep — use sparingly; expect false positives. |

**Why this matters:** Without scoped locators, the auditor reports comments, docs, and test files as violations — false-positive flood is the most likely failure mode of this layer (see ADR-001 §Challenger Failure 2).

## Starter Pack — Default Invariants

These ship with the template and apply unless explicitly removed. They encode hygiene that is true for almost every project; comment them out per-project if not desired.

```yaml
forbidden-imports:
  - module: <none — projects fill this from their ADRs>
    reason: <ADR-bound only>
    binding-adr: <required>
    scope: { include: ["src/**"], exclude: ["tests/**"] }

# 1. No print/console-log debugging in production code paths
- forbidden-pattern: "print\\(|console\\.log\\("
  reason: "Debug output leaks to production logs"
  scope: { include: ["src/**"], exclude: ["src/cli/**", "tests/**"] }

# 2. No TODO/FIXME without issue reference
- pattern-requires: "TODO|FIXME"
  must-match: "(TODO|FIXME)\\([A-Z]+-\\d+\\)"
  reason: "Untracked TODOs become permanent debt"
  scope: { include: ["src/**"] }

# 3. No direct database imports in UI/presentation layer
layer-rules:
  - from: ui/**
    must-not-import-from: [db/**, sqlalchemy, prisma, knex]
    reason: "UI must go through the service layer"
    scope: { include: ["src/**"], exclude: ["tests/**"] }
```

These three are opt-out, not opt-in (per ADR-001 §Decision-1 starter-pack mitigation). A project that wants `print()` in non-CLI code edits the entry; a project that wants direct DB imports in UI removes the rule and documents the deviation in an ADR.

## How `binding-adr` works

Every non-starter invariant SHOULD reference an `accepted` ADR. This couples the invariant to a decision that has passed a gate, so:

- The invariant has documented provenance (the ADR explains *why*)
- If the ADR is `superseded` or `deprecated`, the invariant becomes a candidate for retirement
- The [governance-auditor](../agents/governance-auditor.md) can detect orphan invariants (no `binding-adr`) and orphan ADRs (no invariant binds them)

Starter-pack invariants are exempt — they encode hygiene that pre-dates any ADR.

## Lifecycle

| Transition | Trigger | Rule |
|------------|---------|------|
| `draft` → `active` | Human runs `/approve` against the file | All entries must validate against this template's schema |
| `active` invariant added | New ADR accepted that needs code-level binding | Author SHOULD add the binding; auditor flags missing binding |
| `active` invariant retired | Bound ADR is `superseded` or `deprecated` | Auditor flags; human removes or rewrites the entry |

## Anti-patterns

| Anti-pattern | Why it breaks the artifact |
|--------------|---------------------------|
| Invariant without `binding-adr` (outside starter pack) | Decision provenance is missing — no way to audit *why* the rule exists |
| `loose: true` as default | False-positive flood; auditor signal degrades fast |
| Empty `scope.include` | Validator can't know where to search; either everything or nothing fails |
| Locator type `custom` / `regex` / unenumerated | Each project invents its own dialect; auditor consistency lost |
| Updating an invariant without bumping the bound ADR | Decision-of-record drifts away from what is enforced |

## How it relates to other artifacts

| Artifact | Relation |
|----------|----------|
| [ADR template](adr-template.md) | Each accepted ADR may produce one or more invariants here |
| [agents/architecture-reviewer](../agents/architecture-reviewer.md) | Reads this file when reviewing individual changes |
| [agents/governance-auditor](../agents/governance-auditor.md) | Reads this file when auditing the whole repo (drift detection) |
| [guidelines/architecture-governance](../guidelines/architecture-governance.md) | This template implements the "Content Governance" section |
| `governance-log.md` | Audit runs append findings as `AUDIT` events |
