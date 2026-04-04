---
description: Record a human approval/acceptance for an artifact (ADR, CTX, EXP, PRD) and append it to governance-log.md.
argument-hint: <artifact-id> [note]
---

Record a human approval for artifact: $ARGUMENTS

This is a **human-only** action. When invoked, you are acting as a scribe for the human — you do not decide whether approval is warranted, you only record the decision the human has just made by invoking this command.

## Steps

1. **Parse the argument**: first token is the artifact id (e.g. `ADR-0007`, `EXP-012`, `CTX-003`, `PRD-008`). Remainder is an optional note.

2. **Locate the artifact file** by id. Search conventional locations: `context/adrs/`, `context/plans/`, `01-context/`, `02-exploration/`, `03-production/`, `docs/adrs/`.

3. **Read the artifact** and verify its provenance frontmatter exists. If it is missing, STOP and report — the artifact must be converted to the provenance schema first (see [guidelines/architecture-governance.md](../guidelines/architecture-governance.md)).

4. **Ask the human** to confirm their identifier (name/handle) if not already known in this conversation or project CLAUDE.md.

5. **Update the frontmatter**:
   - `status:` → `accepted` for ADRs, `approved` for CTX/EXP/PRD
   - `decided-by:` → `human`
   - `approved-by:` → the human's identifier
   - `approved-at:` → today's date (YYYY-MM-DD)

6. **Append one line** to `governance-log.md` at the repo root (create it if missing):
   ```
   <YYYY-MM-DD>  <GATE|ADR>  <ID>  proposed:<ai|human|pair>  <approved|accepted>:<name>  "<note>"
   ```
   - `GATE` = `G1` for CTX, `G2` for EXP, `G3` for PRD. `ADR` for ADRs.

7. **Show the diff** to the human before writing. After writing, confirm the append to `governance-log.md`.

## Rules

- NEVER run this command on behalf of the AI. This command records a **human** decision.
- NEVER overwrite an existing `approved-by` — if one is already set, the artifact is already approved. Report and stop.
- The `governance-log.md` file is append-only. Never rewrite prior lines.
- If the artifact's `proposed-by` is empty, fill it with a best-effort guess (`ai` if the conversation shows AI drafted it) and flag this to the human.
