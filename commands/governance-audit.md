---
description: Run a content-level governance audit on the whole repo (ADR drift, undocumented patterns, obsolete ADRs) and append the result summary to governance-log.md.
argument-hint: [note]
---

Run a governance audit. Optional note: $ARGUMENTS

This command delegates to the [governance-auditor](../agents/governance-auditor.md) subagent and records the audit event in `governance-log.md`. It is read-only with respect to code, ADRs, and invariants — it produces findings, never fixes.

Specified by [ADR-001](../context/adr/ADR-001-content-oriented-governance.md).

## Steps

1. **Invoke `governance-auditor`** with no arguments. The auditor:
   - Reads `context/guidelines/architecture-invariants.md` (if present)
   - Scans all `accepted` ADRs under `context/adr/` and `context/specs/*/adr/`
   - Runs the three mandatory checks: ADR-drift, undocumented patterns, obsolete ADRs
   - Returns a structured `GOVERNANCE-AUDIT` block

2. **Display the auditor output** to the human verbatim. Do not summarize away findings.

3. **Append one line** to `governance-log.md` at the repo root:
   ```
   <YYYY-MM-DD>  AUDIT  —  proposed:ai  decided:—  "<N> BLOCK / <M> CONCERN findings, <K> obsolete ADR candidates. <note>"
   ```
   - Replace `<N>`, `<M>`, `<K>` with the counts from the auditor output
   - The `decided:—` placeholder is intentional — the audit itself isn't a decision; the human follows up with `/approve`, `/reject`, or `/supersede` on individual findings
   - If the human passed a note via `$ARGUMENTS`, append it after the counts

4. **Suggest next actions** based on the findings:
   - For each `BLOCK`: name a concrete remediation (`/supersede ADR-NNN`, fix code at file:line, or document as accepted exception)
   - For each `CONCERN`: triage into a follow-up plan or accept and ignore
   - For each `OBSOLETE-ADR-CANDIDATE`: confirm with the human before any status change

## Rules

- This command does NOT change any ADR status, code file, or invariants file. It only reads and appends one log line.
- Never invoke this command's append step without first showing the auditor output. The log line is the receipt; the findings are the substance.
- If the auditor returns `INVARIANTS-FILE: MISSING`, still append the audit event — the missing-file finding is itself the audit result.
- `governance-log.md` is append-only. Never rewrite prior lines.
- This is a manual-trigger command. There is no automatic schedule — that decision is delegated to the user via [/loop](https://docs.anthropic.com/) or `/schedule` if recurring audits are desired.

## When to run

| Trigger | Why |
|---------|-----|
| Weekly / per release | Routine drift detection |
| After any ADR is `accepted`, `superseded`, or `deprecated` | Verify the change is reflected (or not) in code |
| Before a major refactor | Establish baseline |
| Before bumping a framework or library version that ADRs depend on | Detect what will break |

## See also

- [agents/governance-auditor.md](../agents/governance-auditor.md) — the subagent that does the work
- [templates/architecture-invariants-template.md](../templates/architecture-invariants-template.md) — input schema
- [guidelines/architecture-governance.md](../guidelines/architecture-governance.md) §Content Governance — the rules this command operationalizes
- [context/adr/ADR-001-content-oriented-governance.md](../context/adr/ADR-001-content-oriented-governance.md) — origin decision
