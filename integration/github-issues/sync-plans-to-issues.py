#!/usr/bin/env python3
"""
sync-plans-to-issues.py — mirror chevp-ai-framework plan files to GitHub Issues.

Reads `.plan-sync.json` from the current working directory (or the path passed
as the first positional argument), iterates the configured plan directories,
and creates one GitHub Issue per plan file. Idempotent: existing issues with
the same title are skipped (or updated, with --update).

Source-of-truth is the plan file. Issues are mirrors used for tracking and
discussion only — they intentionally link back to the file rather than
duplicating its content.

Requires: gh (authenticated), Python 3.8+. No third-party dependencies.

Usage:
    sync-plans-to-issues.py [--config PATH] [--dry-run] [--limit N] [--update]

See: integration/github-issues/README.md
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


# ---------- frontmatter parsing ------------------------------------------------

FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict[str, str]:
    """Parse simple `key: value` YAML frontmatter. No nested structures."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    out: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and value and not key.startswith(" "):
            out[key] = value
    return out


def first_h1(text: str) -> str | None:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None


# ---------- plan model ---------------------------------------------------------


@dataclass
class Plan:
    path: Path
    rel_path: str
    dir_phase: str          # name of containing directory (always set)
    phase: str              # effective phase (from frontmatter or dir, per cfg)
    frontmatter: dict[str, str]
    title_line: str | None

    @property
    def paragraph(self) -> str | None:
        return self.frontmatter.get("paragraph")

    @property
    def flat_id(self) -> str | None:
        return self.frontmatter.get("id")

    @property
    def type(self) -> str | None:
        t = self.frontmatter.get("type")
        return t.lower() if t else None

    @property
    def title(self) -> str:
        return (
            self.frontmatter.get("title")
            or self.title_line
            or self.path.stem
        )

    def issue_title(self, fmt: str) -> str:
        ident = self.paragraph or self.flat_id or self.path.stem
        return fmt.replace("{{id}}", ident).replace("{{title}}", self.title)


def _effective_phase(frontmatter: dict[str, str], dir_phase: str, cfg: dict) -> str:
    """Resolve the effective phase from frontmatter or directory, per cfg."""
    lcfg = cfg.get("labels", {})
    if lcfg.get("phase_from_frontmatter"):
        field = lcfg.get("phase_frontmatter_field", "status")
        value = frontmatter.get(field)
        if value:
            return value.lower()
    return dir_phase


def load_plans(plan_dirs: Iterable[str], project_root: Path, cfg: dict) -> list[Plan]:
    plans: list[Plan] = []
    phase_include = cfg.get("phase_include")  # optional whitelist
    for d in plan_dirs:
        dir_path = project_root / d
        if not dir_path.is_dir():
            print(f"warn: plan dir not found: {d}", file=sys.stderr)
            continue
        dir_phase = dir_path.name
        for f in sorted(dir_path.glob("*.md")):
            text = f.read_text(encoding="utf-8")
            fm = parse_frontmatter(text)
            phase = _effective_phase(fm, dir_phase, cfg)
            if phase_include and phase not in phase_include:
                continue
            plans.append(
                Plan(
                    path=f,
                    rel_path=str(f.relative_to(project_root)),
                    dir_phase=dir_phase,
                    phase=phase,
                    frontmatter=fm,
                    title_line=first_h1(text),
                )
            )
    return plans


# ---------- label derivation ---------------------------------------------------


def derive_labels(plan: Plan, cfg: dict) -> list[str]:
    lcfg = cfg.get("labels", {})
    labels: list[str] = []
    if plan.type and lcfg.get("type_prefix") is not None:
        labels.append(f"{lcfg['type_prefix']}{plan.type}")
    # Phase label: emit if either phase_from_dir or phase_from_frontmatter is set.
    # plan.phase has already been resolved per cfg in _effective_phase().
    if (lcfg.get("phase_from_dir") or lcfg.get("phase_from_frontmatter")) \
            and lcfg.get("phase_prefix") is not None:
        labels.append(f"{lcfg['phase_prefix']}{plan.phase}")
    if lcfg.get("area_from_paragraph") and plan.paragraph:
        m = re.match(r"§(\d+)", plan.paragraph)
        if m:
            chapter = m.group(1)
            prefix = lcfg.get("area_prefix", "area:")
            slug = (lcfg.get("area_names") or {}).get(chapter)
            label = f"{prefix}§{chapter}-{slug}" if slug else f"{prefix}§{chapter}"
            labels.append(label)
    labels.extend(cfg.get("extra_labels", []))
    return labels


# ---------- gh wrappers --------------------------------------------------------


def gh(*args: str, check: bool = True, capture: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["gh", *args],
        check=check,
        text=True,
        capture_output=capture,
    )


def existing_issues(repo: str) -> dict[str, dict]:
    """Return mapping of title -> {number, labels[]} for all issues in repo."""
    result = gh(
        "issue", "list",
        "--repo", repo,
        "--state", "all",
        "--limit", "1000",
        "--json", "number,title,labels",
    )
    out: dict[str, dict] = {}
    for item in json.loads(result.stdout or "[]"):
        out[item["title"]] = {
            "number": item["number"],
            "labels": [lab["name"] for lab in item.get("labels", [])],
        }
    return out


def managed_label_prefixes(cfg: dict) -> list[str]:
    """Label prefixes the script considers under its control (used by --update)."""
    lcfg = cfg.get("labels", {})
    prefixes: list[str] = []
    for key in ("type_prefix", "phase_prefix", "area_prefix"):
        p = lcfg.get(key)
        if p:
            prefixes.append(p)
    return prefixes


def reconcile_labels(
    repo: str,
    issue_number: int,
    current: list[str],
    desired: list[str],
    managed_prefixes: list[str],
    extra_labels: list[str],
) -> tuple[list[str], list[str]]:
    """Remove managed labels not in `desired`, add `desired` not in `current`.

    Labels with no managed prefix and not in extra_labels are left untouched —
    so users can hand-add labels (e.g. priority:high) without losing them.
    """
    desired_set = set(desired)
    extra_set = set(extra_labels)

    def is_managed(label: str) -> bool:
        if label in extra_set:
            return True
        return any(label.startswith(p) for p in managed_prefixes)

    to_remove = [lab for lab in current if is_managed(lab) and lab not in desired_set]
    to_add = [lab for lab in desired if lab not in current]

    for lab in to_remove:
        gh("issue", "edit", str(issue_number), "--repo", repo, "--remove-label", lab)
    for lab in to_add:
        gh("issue", "edit", str(issue_number), "--repo", repo, "--add-label", lab)
    return to_add, to_remove


def ensure_labels(repo: str, labels: Iterable[str]) -> None:
    existing = gh("label", "list", "--repo", repo, "--limit", "200", "--json", "name")
    have = {item["name"] for item in json.loads(existing.stdout or "[]")}
    for label in labels:
        if label in have:
            continue
        try:
            gh("label", "create", label, "--repo", repo, "--color", "ededed")
            print(f"  + label created: {label}")
        except subprocess.CalledProcessError as e:
            print(f"  ! label create failed for {label}: {e.stderr}", file=sys.stderr)


def build_body(plan: Plan, cfg: dict) -> str:
    repo_url = cfg.get("repo_url_prefix", "")
    file_link = (
        f"{repo_url.rstrip('/')}/blob/main/{plan.rel_path}"
        if repo_url
        else plan.rel_path
    )
    return (
        f"**Plan-Datei:** [`{plan.rel_path}`]({file_link})\n\n"
        f"**Phase:** `{plan.phase}` · **Type:** `{plan.type or '—'}`\n\n"
        "> Source-of-Truth ist die Datei im Repo. Dieses Issue ist ein "
        "Spiegel für Tracking und Diskussion und wird automatisch via "
        "`sync-plans-to-issues.py` erzeugt.\n"
    )


# ---------- main ---------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", default=".plan-sync.json", help="path to config file (default: .plan-sync.json)")
    ap.add_argument("--dry-run", action="store_true", help="show what would happen, do not call gh")
    ap.add_argument("--limit", type=int, default=0, help="max number of plans to process (0 = all)")
    ap.add_argument("--update", action="store_true", help="update body of existing issues with same title")
    args = ap.parse_args()

    cfg_path = Path(args.config).resolve()
    if not cfg_path.is_file():
        print(f"error: config not found: {cfg_path}", file=sys.stderr)
        return 2
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    project_root = cfg_path.parent

    repo = cfg["repo"]
    plan_dirs = cfg.get("plan_dirs", ["context/plans/backlog", "context/plans/active"])
    title_format = cfg.get("title_format", "{{id}} — {{title}}")

    plans = load_plans(plan_dirs, project_root, cfg)
    if args.limit:
        plans = plans[: args.limit]
    print(f"discovered {len(plans)} plans across {len(plan_dirs)} dirs in {project_root}")

    if not plans:
        return 0

    if args.dry_run:
        print("\n--- DRY RUN ---")
        for p in plans:
            print(f"\n• {p.issue_title(title_format)}")
            print(f"  file: {p.rel_path}")
            print(f"  phase: {p.phase}  (dir: {p.dir_phase})")
            print(f"  labels: {', '.join(derive_labels(p, cfg)) or '—'}")
        return 0

    existing = existing_issues(repo)
    print(f"existing issues in {repo}: {len(existing)}")

    all_labels = sorted({lab for p in plans for lab in derive_labels(p, cfg)})
    if all_labels:
        print(f"ensuring {len(all_labels)} labels exist…")
        ensure_labels(repo, all_labels)

    managed_prefixes = managed_label_prefixes(cfg)
    extra_labels = cfg.get("extra_labels", [])

    created = skipped = updated = 0
    for plan in plans:
        title = plan.issue_title(title_format)
        labels = derive_labels(plan, cfg)
        body = build_body(plan, cfg)

        if title in existing:
            if args.update:
                match = existing[title]
                gh("issue", "edit", str(match["number"]), "--repo", repo, "--body", body)
                added, removed = reconcile_labels(
                    repo, match["number"], match["labels"], labels,
                    managed_prefixes, extra_labels,
                )
                changes = []
                if added:
                    changes.append(f"+{','.join(added)}")
                if removed:
                    changes.append(f"-{','.join(removed)}")
                tag = f" [labels: {' '.join(changes)}]" if changes else ""
                print(f"  ~ updated #{match['number']}: {title}{tag}")
                updated += 1
                continue
            print(f"  = skip (exists): {title}")
            skipped += 1
            continue

        cmd = ["issue", "create", "--repo", repo, "--title", title, "--body", body]
        for lab in labels:
            cmd += ["--label", lab]
        result = gh(*cmd)
        url = result.stdout.strip().splitlines()[-1] if result.stdout else ""
        print(f"  + created: {title}\n      {url}")
        created += 1

    print(f"\ndone — created: {created}, updated: {updated}, skipped: {skipped}")
    return 0


if __name__ == "__main__":
    sys.exit(main())