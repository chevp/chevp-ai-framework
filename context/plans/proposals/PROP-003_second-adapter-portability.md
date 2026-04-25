---
id: PROP-003
type: proposal
proposed-by: ai
source-gate: G1
source-plan: CTX-002
suggested-type: ctx
status: deferred
date: 2026-04-24
---

# PROP-003: Second adapter (IDE plugin or Web UI) to validate Adapter-Contract portability

## Trigger

CTX-002 §"Likely NOT in scope" excludes "Web UI / dashboard", "Team collaboration / multi-user state", "IDE/editor plugins". ADR-006 declares the Adapter-Contract spec as a chevp-ai-framework artifact (Confirmation Needed #6) so multiple adapters can conform. But until a *second* concrete adapter exists, the contract is unverified — chevp-flow alone cannot prove portability, only assert it.

## Suggested Goal

Once Adapter-Contract v1.0 ships in chevp-ai-framework, scope a second concrete adapter — either chevp-vscode (VS Code extension that drives the lifecycle from the editor sidebar), chevp-web (browser dashboard), or chevp-cursor (Cursor-native plugin) — and validate that the Adapter-Contract is implementable without modification.

## Why now / why later

**Later.** Becomes "now" only after (a) Adapter-Contract v1.0 is published in chevp-ai-framework, AND (b) chevp-flow has shipped at least v1.0 (its own dogfooding has surfaced contract-clarification issues), AND (c) an adopter cohort exists for the second surface (otherwise it's solo theatre).

## Suggested Kill Criterion

This proposal becomes obsolete if Adapter-Contract v1.0 itself never stabilises (i.e. the framework can't articulate its own contract), OR if chevp-flow proves so dominant that no second adapter is needed for portability proof.

## Estimated effort

Large — depending on surface chosen. VS Code extension is the lightest (≈1-2 weeks); web UI is biggest (own backend, auth, UX). Should be its own multi-step CTX/EXP/PRD pipeline, not attempted as a single plan.

## Notes

This is the *operational* validation of the framework's "tool-independence" claim. PROP-001 explores the same goal in-place (multi-provider in chevp-flow); PROP-003 explores a second tool/surface. They are complementary, not redundant — and one or both should eventually happen for the claim to be honest.
