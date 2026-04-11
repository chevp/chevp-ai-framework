# GitHub Issues Integration

> Mirror chevp-ai-framework plan files (`context/plans/**/*.md`) to GitHub
> Issues. The plan file remains the source-of-truth — issues are
> automatically generated mirrors used for tracking and discussion.

## Why

The framework's lifecycle (Context → Exploration → Production) is plan-driven.
Plans live as markdown files in `context/plans/<phase>/`. Most teams also
want a Kanban-style overview, ad-hoc discussion threads, and assignee/label
filtering — exactly what GitHub Issues provides.

Rather than maintaining issues by hand (drift) or moving plans into Issues
(loses git history and review workflow), this integration **mirrors** plans
into Issues idempotently:

- one Issue per plan file
- Issue body = link to file (no content duplication, no drift)
- labels derived from frontmatter (`type:prd`, `phase:backlog`, `area:§5`, …)
- re-running the script skips existing issues (or updates them with `--update`)

This is the executable counterpart to the conceptual integration docs in
[../kanban.md](../kanban.md) and [../scrum.md](../scrum.md).

## Requirements

- [`gh`](https://cli.github.com/) CLI, authenticated against the target repo
- Python 3.8+ (stdlib only — no third-party deps)
- A plan layout matching the framework template
  ([../../templates/plan-template.md](../../templates/plan-template.md)) —
  either flat (`id: PRD-NNN`) or paragraph (`paragraph: §X.Y`) numbering

## Setup (per consuming project)

1. Copy [.plan-sync.example.json](.plan-sync.example.json) to your project
   root as `.plan-sync.json`:
   ```bash
   cp ../chevp-ai-framework/integration/github-issues/.plan-sync.example.json .plan-sync.json
   ```
2. Edit `.plan-sync.json` — set `repo`, `repo_url_prefix`, and
   `plan_dirs` to match your project.
3. Dry-run to preview:
   ```bash
   python3 ../chevp-ai-framework/integration/github-issues/sync-plans-to-issues.py --dry-run --limit 3
   ```
4. Run for real:
   ```bash
   python3 ../chevp-ai-framework/integration/github-issues/sync-plans-to-issues.py
   ```

## Configuration reference

```json
{
  "repo": "owner/repo",
  "repo_url_prefix": "https://github.com/owner/repo",
  "plan_dirs": ["context/plans/backlog", "context/plans/active"],
  "title_format": "{{id}} — {{title}}",
  "labels": {
    "type_prefix": "type:",
    "phase_from_dir": true,
    "phase_prefix": "phase:",
    "area_from_paragraph": true,
    "area_prefix": "area:"
  },
  "extra_labels": ["plan"]
}
```

| Key | Purpose |
|---|---|
| `repo` | `owner/repo` slug passed to `gh --repo` |
| `repo_url_prefix` | Base URL used to build clickable file links in issue bodies |
| `plan_dirs` | Plan directories to scan, relative to project root |
| `title_format` | `{{id}}` resolves to `paragraph` or `id` from frontmatter; `{{title}}` to `title` (or H1 fallback) |
| `phase_include` | Optional whitelist of phases to sync (e.g. `["backlog", "active"]`). Plans whose effective phase is not listed are skipped. |
| `labels.type_prefix` | Prefix for the type label (e.g. `type:prd`) — set to empty string to disable |
| `labels.phase_from_dir` | If true, derive a phase label from the plan directory name. Use this with a folder-per-phase layout (`context/plans/backlog/`, `context/plans/active/`). |
| `labels.phase_from_frontmatter` | If true, derive a phase label from the plan's frontmatter. Use this with a flat layout (`context/plans/*.md`) where the phase lives in the frontmatter. Takes precedence over `phase_from_dir` when both are set. |
| `labels.phase_frontmatter_field` | Frontmatter key to read when `phase_from_frontmatter` is true. Default: `status`. |
| `labels.area_from_paragraph` | If true and plan uses paragraph numbering, add an area label for the top-level chapter |
| `labels.area_names` | Optional `{ "<chapter>": "<slug>" }` map. When set, the area label becomes `area:§N-<slug>` (e.g. `area:§5-reports-ci`) instead of just `area:§N`. The §-number stays in the label so sort order is preserved |
| `extra_labels` | Static labels added to every issue (e.g. `plan`) |

Missing labels are created automatically with a neutral grey colour. Adjust
colours afterwards in the GitHub UI if you want.

## CLI

```text
sync-plans-to-issues.py [--config PATH] [--dry-run] [--limit N] [--update]

  --config PATH   path to config file (default: ./.plan-sync.json)
  --dry-run       print what would happen, do not call gh
  --limit N       process at most N plans (useful for testing)
  --update        update body of existing issues with same title
```

Idempotency is title-based: an issue with the exact same title is treated as
the mirror for that plan. Renaming a plan currently produces a new issue —
close the old one manually, or use the `--update` flag combined with a
controlled title change.

### How `--update` reconciles labels

With `--update`, the script not only rewrites the issue body but also
reconciles **managed** labels (those matching `type_prefix`, `phase_prefix`,
`area_prefix`, or listed in `extra_labels`):

- labels currently on the issue that match a managed prefix but are not in
  the desired set → **removed**
- labels in the desired set that are not currently on the issue → **added**
- labels with *no* managed prefix (e.g. `priority:high` added manually) →
  **left untouched**

This lets you change a plan's `status:` in the frontmatter from `backlog` to
`active`, re-run with `--update`, and the `phase:backlog` label is replaced
by `phase:active` automatically — while hand-added labels survive.

## Out of scope (intentionally)

- **Two-way sync.** Issues → plan changes are not mirrored back. Plans are
  the source-of-truth; if you want a discussion to result in plan changes,
  edit the file via the normal review workflow.
- **Project (v2) integration.** Adding issues to GitHub Projects v2 requires
  the `read:project,project` token scope and a richer node/field API. A
  follow-up extension (`integration/github-projects/`) can layer on top of
  this script.
- **Closing issues when plans are deleted/moved.** Manual for now — likely
  cheap to add later if needed.

## Promotion path

This integration was extracted from a single consumer project. If a second
project adopts it, the existing API should already cover it. Open an issue
on `chevp-ai-framework` if your project needs a config knob that isn't here.