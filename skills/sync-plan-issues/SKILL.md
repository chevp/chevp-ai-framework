---
name: sync-plan-issues
description: Use when the user wants to mirror chevp-ai-framework plan files (context/plans/**/*.md) to GitHub Issues, or says "sync plans", "issue für §X.Y", "plans als issues anlegen", "create issues from plans", "spiegle backlog nach github". Wraps integration/github-issues/sync-plans-to-issues.py.
---

# Sync Plan Files to GitHub Issues

Mirrors plan files in `context/plans/<phase>/` to GitHub Issues, one issue
per plan. Source-of-truth stays the markdown file; the issue body links
back to it. Idempotent — re-running skips existing issues.

## When to trigger

- User asks to "sync plans", "create issues for backlog", "alle plans als
  github issues", "mirror plans to issues", or similar
- User asks to create an issue for a specific plan (e.g. "issue für §5.2")
- After a batch of new plans was added and the user wants the tracking
  board updated

## Prerequisites

1. The project has a `.plan-sync.json` at its root (see
   [../../integration/github-issues/.plan-sync.example.json](../../integration/github-issues/.plan-sync.example.json)).
   If missing, **stop and offer to create one** based on the project's
   `CLAUDE.md` and existing `context/plans/` layout. Do not guess `repo`
   or `repo_url_prefix` — ask.
2. `gh` is authenticated against the target repo (`gh auth status`).
3. Plan files use the framework template's frontmatter
   ([../../templates/plan-template.md](../../templates/plan-template.md)) —
   either `id:` (flat) or `paragraph:` (paragraph numbering), plus
   `type:` and ideally `title:`.

## Steps

1. **Verify config exists.** If not, create one with the user (ask for
   `repo` slug; default `plan_dirs` to `["context/plans/backlog", "context/plans/active"]`).
2. **Always dry-run first**:
   ```bash
   python3 path/to/chevp-ai-framework/integration/github-issues/sync-plans-to-issues.py --dry-run --limit 3
   ```
   Show the user 2–3 example issue titles + labels and confirm they look
   right before going wider.
3. **Then run for the full set** (without `--limit`) once the user
   approves the dry-run output.
4. **For a single plan** (e.g. "issue für §5.2"): use `--limit 1` after
   temporarily reducing `plan_dirs` to the directory containing that
   plan, OR fall back to a direct `gh issue create` with the same title
   format the script would produce. Prefer the script for consistency.

## Safety

- This calls `gh issue create` and `gh label create` — both are
  user-visible writes to GitHub. Always confirm intent before the first
  non-dry-run invocation.
- Never add `--update` without explicit user request — it overwrites
  existing issue bodies.
- If the dry-run shows zero plans discovered, stop and investigate the
  `plan_dirs` config rather than assuming success.

## Reference

- Script + full docs: [../../integration/github-issues/README.md](../../integration/github-issues/README.md)
- Conceptual integration: [../../integration/kanban.md](../../integration/kanban.md)