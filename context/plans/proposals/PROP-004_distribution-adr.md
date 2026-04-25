---
id: PROP-004
type: proposal
proposed-by: ai
source-gate: G1
source-plan: CTX-002
suggested-type: exp
status: deferred
date: 2026-04-24
---

# PROP-004: Distribution-strategy ADR (Homebrew tap + goreleaser config + signing posture)

## Trigger

CTX-002 §"Next steps after G1" lists Distribution as a deferred ADR: "Distribution — Homebrew + GitHub Releases + go install + git submodule". ADR-004 (license) is in scope at G1, but the *concrete* distribution mechanics (Homebrew tap layout, goreleaser matrix, code-signing for macOS notarization, checksums, SBOM) are not. SPEC §"Non-functional" mentions `goreleaser` but does not pin its config.

## Suggested Goal

Within the chevp-flow Exploration step, draft a dedicated ADR (ADR-007 in chevp-flow's own ADR sequence once the repo is created) that pins: Homebrew tap repository path, goreleaser matrix targets (darwin/linux × amd64/arm64), macOS notarization stance (Apple Developer ID or skip), Linux package formats (tarball + .deb? + .rpm?), checksum publication, SBOM generation, and signing posture (cosign? gpg? unsigned?).

## Why now / why later

**Now-ish for Exploration** — this is not a v1.0 release blocker, but cannot be deferred past the first public binary release. Belongs in the Exploration step of chevp-flow itself, before any production code is written.

## Suggested Kill Criterion

This proposal becomes obsolete only by being completed (it's not optional — chevp-flow needs *some* distribution decision before public release).

## Estimated effort

Small — one ADR plus a working `.goreleaser.yml`. Most decisions are straightforward (no notarization at v1; no signing at v1; tarball-only Linux at v1; Homebrew tap at github.com/chevp/homebrew-tap).

## Notes

Already declared as deferred-to-Exploration in CTX-002. This proposal exists to ensure it doesn't get lost in the EXP-step queue and to set kill-criterion explicitly.
