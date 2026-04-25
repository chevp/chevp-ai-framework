---
id: PROP-002
type: proposal
proposed-by: ai
source-gate: G1
source-plan: CTX-002
suggested-type: exp
status: deferred
date: 2026-04-24
---

# PROP-002: Windows support spike for chevp-flow

## Trigger

CTX-002 §"Risks we accept knowingly" states "v1 is mac/linux only. Reason: solo dogfooding context." SPEC §"Out of Scope" similarly excludes Windows. Go cross-compilation makes Windows support cheap *in principle*, but the `claude -p` subprocess invocation, file-path handling (forward vs. back-slashes), TTY detection (per SQ1), and Docker SDK behaviour on Windows are all untested.

## Suggested Goal

Add `windows/amd64` and `windows/arm64` to the goreleaser matrix for chevp-flow v1.x, then run the existing integration test suite on Windows to surface platform-specific failures (path handling, subprocess spawning, Charm rendering on `cmd.exe` vs Windows Terminal, Huh form keybindings).

## Why now / why later

**Later** — v1 release first on mac/linux to validate core flows. Becomes "now" when (a) a Windows user files a usable issue with reproduction, OR (b) chevp-flow gains traction and Windows-shaped audiences (corporate dev environments) become a meaningful adopter share.

## Suggested Kill Criterion

This proposal becomes obsolete if no Windows adoption signal arrives in the first 6 months post-v1, OR if WSL2 adoption among target users makes native Windows support unnecessary (most pain points evaporate inside WSL2).

## Estimated effort

Small for the build matrix + smoke tests; Medium if surface-level bugs in path handling or Charm rendering require fixes.

## Notes

Cross-compilation is one line of YAML in `.goreleaser.yml`. The actual cost is testing — without a Windows machine and CI integration, this proposal can't fully execute. Suggest pairing with GitHub Actions Windows runners (free for public repos).
