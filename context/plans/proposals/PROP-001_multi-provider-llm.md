---
id: PROP-001
type: proposal
proposed-by: ai
source-gate: G1
source-plan: CTX-002
suggested-type: ctx
status: deferred
date: 2026-04-24
---

# PROP-001: Multi-provider LLM support for chevp-flow (Pfad 3 / `anthropic-sdk-go` and beyond)

## Trigger

CTX-002 §"Likely NOT in scope" explicitly excludes "Multi-provider LLM support (OpenAI, etc.) — Claude only in v1". ADR-002 defers Pfad 3 (`anthropic-sdk-go`) to v2 and acknowledges R8 (CTX-002 R8): the Go SDK is younger and more boilerplate-heavy than TS/Python equivalents. Without multi-provider support, the framework's "tool-independence" claim remains under-tested.

## Suggested Goal

Spike a Pfad-3 fallback path in chevp-flow that uses `anthropic-sdk-go` (and optionally a second provider behind a `Runtime` interface) so the CLI can run in environments without Claude Code installed, validating the framework's portability against a non-Claude-Code surface.

## Why now / why later

**Later.** Becomes "now" when (a) `anthropic-sdk-go` reaches feature parity with the TS SDK on streaming + tool-use, OR (b) a concrete adoption request from a non-Claude-Code user materialises, OR (c) chevp-flow v1 ships and the kill-criterion ("gate-approvals become routine") proves false (i.e. the framework has earned its keep), making investment in v2 worthwhile.

## Suggested Kill Criterion

This proposal becomes obsolete if (a) Anthropic stops shipping the `claude` CLI, forcing migration regardless, OR (b) chevp-flow v1 fails to attract users — in which case multi-provider support is solving a problem nobody has.

## Estimated effort

Medium — a clean `Runtime` interface in `internal/runtime/` plus a parallel `internal/runtime/api/` package, integration tests against both paths, doc updates.

## Notes

The framework's tool-independence claim was the original Why-now in CTX-002. Until at least one non-Claude-Code adapter exists (whether Pfad 3 in chevp-flow itself or a separate adapter like chevp-cursor), that claim is unproven. PROP-003 explores the alternate route (separate adapter); this proposal explores the in-place route.
