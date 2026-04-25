---
id: ADR-001
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

# ADR-001: Async file-based CLI architecture

## Status

Proposed

## Context

`chevp-flow` needs an interaction model for the human ↔ AI ↔ governance dialogue that the framework demands. Two viable shapes exist:

1. **Async file-based** — commands mutate markdown artifacts in place; the user reviews changes via editor diff (or `git diff`); explicit follow-up commands (`approve`, `gate-check`, `promote`) advance state. Mirrors `git`'s working model.
2. **Sync REPL** — `chevp` opens an interactive session and blocks on user input; closer to chat experience.

The framework's source-of-truth already lives in markdown files, gates already require human approval as discrete events, and Rule #13 (clickable decisions, `AskUserQuestion` pattern) suggests interactive prompts at decision points only. CI integration and editor-based workflows are explicit goals (CTX-002 Audience: OSS / third-party developers).

## Decision

Adopt the **async file-based** model. Commands are short-lived processes that read state from disk, invoke `claude -p` if AI generation is needed, write resulting artifacts, and exit. Interactive prompts (Huh forms) appear only at gate transitions and proposal triage — and even there, they can be skipped via flags for full automation.

## Alternatives

### Alternative A: Async file-based (chosen)
- Pros:
  - Matches markdown-as-source-of-truth (no daemon, no in-memory state)
  - Trivial CI integration (`chevp gate-check G1` returns exit code)
  - Editor diff review is a natural step
  - Concurrent runs are user-supervised (same as `git`)
  - Each command is independently testable and idempotent
- Cons:
  - Full Context-step flow takes more user steps than a chat
  - Initial UX may feel verbose to chat-acclimatised users

### Alternative B: Sync REPL
- Pros:
  - Closer to Claude Code's chat experience
  - Fewer commands for casual use
- Cons:
  - Hard to script / integrate into CI
  - Conflicts with editor-based workflow (no diff review pause)
  - Concurrent invocations = locking complexity
  - Doesn't match `git` mental model the framework already invokes

### Alternative C: Hybrid (TUI by default, --batch flag for scripting)
- Pros: best of both
- Cons: two code paths, double the test surface; v1 over-engineering risk (R4)

## Consequences

### Positive
- Single-binary delivery makes sense (no daemon to manage)
- Provenance enforcement is mechanical (each `Write` validates frontmatter)
- The framework's existing slash-command verbs (`approve`, `promote`, `reject`) translate directly to subcommands

### Negative
- Users coming from chat workflows must adjust to file-mediated dialogue
- "Status" must be derivable from disk only (no session memory)

### Risks
- **R-ADR-001-1**: If the approval flow takes >2× the clicks of chat for routine tasks, users will resist (kill criterion: "gate-approvals become routine" already covers this — if mechanical churn dominates, the framework itself fails, not the CLI shape)
- **R-ADR-001-2**: Editor diff review depends on user discipline; without it, the gate becomes a rubber stamp

## Cross-references
- Parent: [CTX-002](../../../plans/CTX-002-chevp-flow-cli.md)
- Spec section: [Module Structure](../README.md#module-structure)
- Maps to CTX-002 decision: "CLI-Modus = Async file-based (git-style)"
