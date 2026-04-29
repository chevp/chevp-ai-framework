---
name: write-insights
description: Use when an Exploration cycle is wrapping up and the `insights.md` learning artifact is needed (mandatory before G2), or when Production has revealed implementation surprises that must be appended (Rule 9 / Learning Loop). Trigger phrases: "write insights", "insights file", "what did we learn", "log insights", "update insights with implementation surprises".
---

# Write Insights (Learning Loop)

`insights.md` converts the lifecycle from a one-way pipeline into a loop. It records what was tested, what surprised us, and what we now believe — feeding back into hypotheses and risks for the next cycle.

Mandatory before G2 (initial draft). Updated again after G3 with implementation surprises (Rule 9).

## When to trigger

- An Exploration cycle is approaching G2 and `insights.md` does not yet exist
- A prototype, measurement, or interview has produced findings the user wants captured
- Production / validation surfaced surprises that must be appended (Rule 9)
- User explicitly asks: "write insights", "log learning", "update insights with what we found"

## Steps

1. **Read the template**: [templates/insights-template.md](../../templates/insights-template.md).
2. **Read related artifacts** to ground the insights:
   - The active EXP plan (for hypotheses to test against and the `## Vision Alignment` section)
   - `hypotheses.md` if present
   - Any prototype output, measurements, interview notes, or `## Challenger` block
   - `risks.md` (new surprises become new risks)
3. **Locate the insights file** — typical path: `context/plans/<plan-id>/insights.md` or alongside the EXP plan file. Read CLAUDE.md or ask; do not guess.
4. **Draft** the file satisfying the template's *Minimum Substance*:
   - At least one row in *Hypotheses tested* with non-empty `Result` and `Verdict` (`confirmed` / `refuted` / `inconclusive`)
   - At least one bullet in *What surprised us* — be specific; "nothing surprised us" is itself an insight, but document why
   - At least one bullet in *What we now believe*
   - Open questions in *What we still do not know*
   - **One** of the four *Consequence for the plan* checkboxes ticked (proceed / adjusted / killed / fallback to Context)
5. **Cross-update** dependent artifacts the user agrees to:
   - `hypotheses.md` — mark hypotheses `confirmed` / `killed`
   - `risks.md` — append new failure modes the Exploration uncovered
6. **Confirm** path and content with the user before writing.

## Rules

- Insights are written *during* Exploration, not retro-fitted after G2 approval (the template flags retro-fitting as an anti-pattern).
- "Confirmed everything" is a smell. If every hypothesis is `confirmed` and *What surprised us* is empty, regenerate with sharper questions to the user before saving.
- For G3 updates, append a new dated section rather than rewriting earlier findings — the audit trail matters.
- Status is `draft` until the human confirms; only the human fills `decided-by:` (required at G2).
- If a prior `## Challenger` failure mode came true, record that linkage explicitly — it closes the loop the Challenger opened.

## Output

An `insights.md` file (or an updated one) that satisfies the template's *Minimum Substance* requirements. Status `draft` until human confirmation.
