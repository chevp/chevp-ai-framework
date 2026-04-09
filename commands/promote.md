---
description: Promote a Plan Proposal (PROP-NNN) to a real CTX/EXP/PRD plan in its suggested chapter.
argument-hint: <PROP-id> [target-chapter]
---

Promote Plan Proposal $ARGUMENTS to a real plan.

This is a **human-only** action. When invoked, you act as a scribe for the human's promotion decision — you do not decide whether the proposal is worth promoting, you only record and execute the conversion the human has just authorised.

## Steps

1. **Parse the argument**: first token is the `PROP-NNN` id; optional second token overrides the proposal's `suggested-chapter`.

2. **Locate the proposal file**: search `context/plans/proposals/PROP-NNN_*.md`. If not found, STOP and report.

3. **Read the proposal frontmatter** and extract:
   - `suggested-type` (`ctx` / `exp` / `prd`)
   - `suggested-chapter` (or use the override from the argument)
   - `Trigger`, `Suggested Goal`, `Suggested Kill Criterion`

4. **Verify the chapter exists**: look up `context/plans/chapters/§<n>_*.chapter.md`. If missing, ask the human whether to create the chapter first.

5. **Generate the new plan**:
   - **If the project uses §-numbering**: create `context/plans/active/§<chapter>.<next>_<slug>.<type>.md` using the matching template (`plan-template.md` § variant). Find the next free number in the chapter; never reuse numbers.
   - **If the project uses flat numbering**: create `context/plans/<TYPE>-<NNN>-<slug>.md` using the flat template variant. Use the next free `<NNN>` for that type.
   - Pre-fill `Goal` from the proposal's `Suggested Goal`
   - Pre-fill `Kill Criteria` from the proposal's `Suggested Kill Criterion`
   - Set `proposed-by: pair` (the AI scribed it, the human authorised it)
   - Leave `decided-by`, `approved-by`, `approved-at` blank — the new plan still needs `/approve` after it is fleshed out
   - Reference the source proposal in a "Provenance" note: `Promoted from PROP-NNN on <date>`

6. **Move the proposal**: move the original `PROP-NNN_<slug>.md` to `proposals/promoted/PROP-NNN_<slug>.md` and update its frontmatter (`status: promoted`, add `promoted-to: <new plan id>`).

7. **Append to `governance-log.md`**:
   ```
   <YYYY-MM-DD>  PROP  PROP-NNN  proposed:ai  promoted:<human>  "→ <new-plan-id>"
   ```

8. **Show the diff** to the human before writing. Confirm the new plan path after writing.

## Rules

- NEVER promote on behalf of the AI — promotion is the operational form of human prioritisation.
- NEVER drop the link from the new plan back to the source `PROP-NNN` — traceability matters.
- If the proposal has been auto-deferred (status `deferred` for >90 days), warn the human and ask for explicit re-confirmation before promoting.
- The new plan starts in `status: draft` and `exploration-mode: —` (if EXP) — flesh it out, then run `/approve` separately.
