---
description: Override a Gatekeeper "block" verdict on a plan with an explicit reason. Documents the override in the plan's frontmatter and the governance log.
argument-hint: <plan-id> <reason>
---

Override the Gatekeeper verdict on plan $ARGUMENTS.

This is a **human-only** action that exists for one reason: the Gatekeepers can be wrong. When the human disagrees with a `block` verdict, the human may proceed — but the override is recorded so future review can detect Gatekeeper drift or misuse.

## Steps

1. **Parse the argument**: first token is the plan id (`§<n>`, `EXP-NNN`, `CTX-NNN`, `PRD-NNN`); the remainder is the override reason (mandatory).

2. **Locate the plan file** in `context/plans/active/`, `context/plans/`, or its `finished/`/`archived/` variant.

3. **Locate the latest Gatekeeper verdict** for this plan in the conversation or in `governance-log.md`. If no recent `block` verdict exists, STOP and ask the human to run `/gate-check` first — overrides only apply to actual blocks.

4. **Update the plan frontmatter** with an override block:
   ```yaml
   gatekeeper-override:
     gate: G1 | G2 | G3
     blocked-by: <which finding(s) the gatekeeper raised>
     overridden-by: <human>
     overridden-at: <YYYY-MM-DD>
     reason: <full reason from argument>
   ```
   Append to the existing `gatekeeper-override:` list if one is already present (overrides accumulate).

5. **Append to `governance-log.md`**:
   ```
   <YYYY-MM-DD>  GATE-OVERRIDE  <plan-id>  <gate>  blocked:gatekeeper  overridden:<human>  "<reason>"
   ```

6. **Do NOT modify** `decided-by` / `approved-by` / `approved-at`. An override does not approve the plan — it only allows progression. The human still has to run `/approve` separately to record the approval.

7. **Show the diff** to the human before writing. After writing, remind: "Override recorded. Run `/approve <plan-id>` separately to record the approval."

## Rules

- Override without a reason is forbidden.
- Overrides accumulate — never overwrite an existing override block.
- If the same plan has been overridden 3+ times across different gates, flag this to the human as a likely sign that either the plan is fundamentally wrong or the Gatekeeper is misconfigured.
- An override does NOT bypass the `evidence:` block requirement. If the Gatekeeper blocked because the evidence is empty, the human must still fill it before `/approve`.
- Querying overrides: `grep "GATE-OVERRIDE" governance-log.md` lists every override event for audit.
