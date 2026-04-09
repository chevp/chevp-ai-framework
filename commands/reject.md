---
description: Reject a Plan Proposal (PROP-NNN) with an explicit reason and archive it under proposals/rejected/.
argument-hint: <PROP-id> <reason>
---

Reject Plan Proposal $ARGUMENTS.

This is a **human-only** action. The AI scribes the rejection — it does not decide whether the proposal should be rejected.

## Steps

1. **Parse the argument**: first token is `PROP-NNN`; the remainder is the rejection reason (mandatory — proposals cannot be rejected silently).

2. **Locate the proposal file** in `context/plans/proposals/PROP-NNN_*.md`. If not found, STOP and report.

3. **Update the frontmatter**:
   ```yaml
   status: rejected
   rejected-by: <human>
   rejected-at: <YYYY-MM-DD>
   rejection-reason: <full reason from argument>
   ```

4. **Move the file** to `context/plans/proposals/rejected/PROP-NNN_<slug>.md`. Never delete — rejected proposals remain queryable history.

5. **Append to `governance-log.md`**:
   ```
   <YYYY-MM-DD>  PROP  PROP-NNN  proposed:ai  rejected:<human>  "<reason>"
   ```

6. **Show the diff** to the human before writing.

## Rules

- A rejection without a reason is forbidden — proposals carry uncertainty cost; the rejection reason is the only thing that prevents the same idea from coming back as a duplicate.
- NEVER reuse a rejected `PROP-NNN` id for a new proposal.
- A rejected proposal can be re-opened **only** by the human, by editing the frontmatter back to `pending-human-review` and noting the re-open reason. The AI may not resurrect rejected proposals.
- If the rejection reason matches a previously rejected proposal's reason, flag the duplicate to the human.
