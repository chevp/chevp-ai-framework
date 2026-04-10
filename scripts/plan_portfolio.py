#!/usr/bin/env python3
"""Render an effort x value portfolio heatmap for active/backlog plans.

Scans context/plans/ (or a directory passed as argv[1]) for markdown files
with YAML frontmatter, filters to active/backlog plans, and writes a PNG
quadrant chart (Quick Wins / Big Bets / Fill-ins / Time Sinks).

Frontmatter fields read:
    effort: 1-5   (optional) x-axis
    value:  1-5   (optional) y-axis
    risk:   1-5   (optional) bubble size, defaults to 2
    status:       filter; keeps {active, backlog, draft, proposed, approved}
    type:         color (ctx/exp/prd)
    id / paragraph: label

Plans missing effort or value land in an "unscored" strip on the right margin.

Usage:
    python scripts/plan_portfolio.py [plans_dir] [output_png]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("error: PyYAML required (pip install pyyaml)")

try:
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle
except ImportError:
    sys.exit("error: matplotlib required (pip install matplotlib)")


ACTIVE_STATUS = {"active", "backlog", "draft", "proposed", "approved"}

TYPE_COLOR = {
    "ctx": "#8b5cf6",
    "exp": "#2563eb",
    "prd": "#16a34a",
    "task": "#64748b",
}
UNSCORED_COLOR = "#d1d5db"

FM_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)


def load_plan(path: Path) -> dict | None:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None
    m = FM_RE.match(text)
    if not m:
        return None
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return None
    if not isinstance(fm, dict):
        return None

    ident = fm.get("paragraph") or fm.get("id") or path.stem
    ptype = str(fm.get("type", "")).lower() or "task"
    status = str(fm.get("status", "draft")).lower()

    return {
        "id": str(ident),
        "type": ptype,
        "status": status,
        "effort": _coerce_score(fm.get("effort")),
        "value": _coerce_score(fm.get("value")),
        "risk": _coerce_score(fm.get("risk")) or 2,
        "path": path,
    }


def _coerce_score(v) -> int | None:
    if v is None or v == "—":
        return None
    try:
        n = int(v)
    except (TypeError, ValueError):
        return None
    return n if 1 <= n <= 5 else None


def collect(plans_dir: Path) -> list[dict]:
    if not plans_dir.exists():
        sys.exit(f"error: {plans_dir} does not exist")
    plans = []
    for path in sorted(plans_dir.rglob("*.md")):
        p = load_plan(path)
        if p and p["status"] in ACTIVE_STATUS:
            plans.append(p)
    return plans


def render(plans: list[dict], out: Path) -> None:
    scored = [p for p in plans if p["effort"] and p["value"]]
    unscored = [p for p in plans if not (p["effort"] and p["value"])]

    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_facecolor("#ffffff")

    # Quadrant tints (data coordinates) so structure is visible even when empty.
    quadrants = [
        (0.5, 3.0, 2.5, 2.5, "#dcfce7"),  # Quick Wins  (low effort, high value)
        (3.0, 3.0, 2.5, 2.5, "#dbeafe"),  # Big Bets    (high effort, high value)
        (0.5, 0.5, 2.5, 2.5, "#fef9c3"),  # Fill-ins    (low effort, low value)
        (3.0, 0.5, 2.5, 2.5, "#fee2e2"),  # Time Sinks  (high effort, low value)
    ]
    for x, y, w, h, color in quadrants:
        ax.add_patch(Rectangle((x, y), w, h, facecolor=color,
                               alpha=0.7, zorder=0, edgecolor="none"))

    ax.axvline(3, color="#9ca3af", lw=1.2, zorder=1)
    ax.axhline(3, color="#9ca3af", lw=1.2, zorder=1)
    for x, y, label in [
        (1.5, 4.8, "Quick Wins"),
        (4.2, 4.8, "Big Bets"),
        (1.5, 1.2, "Fill-ins"),
        (4.2, 1.2, "Time Sinks"),
    ]:
        ax.text(x, y, label, color="#9ca3af", fontsize=11,
                fontweight="bold", ha="center")

    for p in scored:
        ax.scatter(
            p["effort"], p["value"],
            s=120 + p["risk"] * 80,
            c=TYPE_COLOR.get(p["type"], "#64748b"),
            alpha=0.65, edgecolors="white", linewidth=1.5, zorder=3,
        )
        ax.annotate(
            p["id"], (p["effort"], p["value"]),
            fontsize=7, xytext=(8, 5), textcoords="offset points",
            color="#111827", zorder=4,
        )

    for i, p in enumerate(unscored):
        ax.scatter(
            6.1, 1 + (i * 4.0 / max(len(unscored), 1)),
            s=80, c=UNSCORED_COLOR, alpha=0.7,
            edgecolors="white", linewidth=1, zorder=3,
        )
        ax.annotate(
            p["id"], (6.1, 1 + (i * 4.0 / max(len(unscored), 1))),
            fontsize=6, xytext=(8, 0), textcoords="offset points",
            color="#6b7280", zorder=4,
        )
    if unscored:
        ax.text(6.1, 5.3, "unscored", color="#9ca3af", fontsize=9,
                ha="center", style="italic")

    ax.set_xlim(0.5, 7.5 if unscored else 5.5)
    ax.set_ylim(0.5, 5.5)
    ax.set_xticks([1, 2, 3, 4, 5])
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_xlabel("Aufwand  →", fontsize=11)
    ax.set_ylabel("Wert  →", fontsize=11)
    ax.set_title(
        f"Plan Portfolio  —  {len(scored)} scored  /  {len(unscored)} unscored  "
        f"/  {len(plans)} total",
        fontsize=13, pad=15,
    )

    handles = [
        plt.scatter([], [], s=120, c=color, alpha=0.65,
                    edgecolors="white", label=label.upper())
        for label, color in TYPE_COLOR.items()
    ]
    ax.legend(handles=handles, loc="upper left", frameon=False, fontsize=9)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    out.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out, dpi=150, bbox_inches="tight")
    print(f"wrote {out}  ({len(plans)} active plans)")


def main() -> int:
    plans_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("context/plans")
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("context/plan-portfolio.png")
    plans = collect(plans_dir)
    if not plans:
        print(f"no active plans found in {plans_dir}")
        return 0
    render(plans, out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
