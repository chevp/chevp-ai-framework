---
id: PROP-005
type: proposal
proposed-by: ai
source-gate: G1
source-plan: CTX-002
suggested-type: exp
status: deferred
date: 2026-04-24
---

# PROP-005: Re-evaluate single Go module vs. split (`chevp-flow-core` library + `chevp-flow-cli`)

## Trigger

CTX-002 Q7 resolved as "Single package for v1; split deferred until reuse pressure emerges." This proposal exists to make the deferral explicit and to set the trigger condition under which the split becomes worth doing.

## Suggested Goal

In the chevp-flow Exploration step (or later), evaluate whether internals (`internal/state`, `internal/gates`, `internal/runtime`) should be hoisted to a public `pkg/` library so other adapters or in-process integrations can reuse them — specifically, whether splitting into `chevp-flow-core` (library) + `chevp-flow-cli` (binary) carries less cost than one of the alternatives (re-implementation per adapter, gRPC API, plugin interface).

## Why now / why later

**Later.** Becomes "now" when (a) at least one other adapter is being designed and would benefit from in-process Go-library reuse (e.g. PROP-003 produces a Go-based adapter), OR (b) chevp-flow itself outgrows single-binary scope and needs internal modularisation, OR (c) a third party requests a Go SDK to embed framework-conformance checks in their tooling.

## Suggested Kill Criterion

This proposal becomes obsolete if no second consumer ever materialises — single-package wins by default if no reuse pressure exists. Re-evaluate annually; if still no signal at chevp-flow v2.0, mark this proposal `rejected` with reason "no demand surfaced".

## Estimated effort

Small — one ADR + a refactor PR. Go's internal/-to-pkg promotion is well-understood; the work is in the API design, not the move.

## Notes

Premature split is a documented YAGNI failure mode in Go ecosystems (kubernetes-style "everything is a module" leads to versioning hell). The decision rule encoded here is **proven demand, not anticipated demand**.
