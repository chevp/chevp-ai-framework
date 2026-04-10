---
description: Render an effort x value heatmap of all active/backlog plans as PNG.
argument-hint: "[plans_dir] [output_png]"
---

Run `python scripts/plan_portfolio.py $ARGUMENTS` from the project root.

The script scans `context/plans/` (or the directory passed as the first argument),
filters to active/backlog plans (`status ∈ {active, backlog, draft, proposed, approved}`),
and writes a quadrant chart PNG showing effort (x) × value (y), with bubble size =
risk and color = plan type (CTX/EXP/PRD).

Plans missing `effort` or `value` in their frontmatter land in a grey "unscored"
strip at the right edge — these remain optional fields, no gate enforcement.

Default output: `context/plan-portfolio.png`.

After the script completes, report the output path and the scored/unscored counts
to the user. Do not modify any plan files.
