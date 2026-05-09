#!/usr/bin/env python3
"""
PreToolUse hook for Write/Edit: blocks production-code writes if no approved EXP plan exists.

Heuristic gate enforcement:
- Writes to framework artifacts (plans, specs, ADRs, templates, docs, hooks, commands,
  agents, skills, README, CLAUDE.md, .md files) are ALWAYS allowed — they are process
  artifacts or documentation.
- Writes to source files (code) require an approved EXP plan to exist in a conventional
  location. If none is found, the hook emits a warning (permissionDecision: "ask")
  asking the user to confirm.

This is a safety net, not a hard lock — the user can always approve. The goal is to
surface skipped steps, not to prevent all code edits.
"""
import json
import sys
from pathlib import Path

# Extensions we treat as process artifacts / docs — never blocked.
DOC_EXTENSIONS = {".md", ".mdx", ".txt", ".rst", ".json", ".yaml", ".yml", ".toml"}

# Directory names whose contents we treat as process artifacts.
PROCESS_DIRS = {
    ".claude-plugin",
    "commands",
    "agents",
    "skills",
    "hooks",
    "templates",
    "guidelines",
    "01-context",
    "02-exploration",
    "03-production",
    "context",
    "docs",
    "integration",
}

# Locations where we look for EXP plans.
EXP_PLAN_GLOBS = [
    "context/plans/EXP-*.md",
    "02-exploration/exp-plans/EXP-*.md",
    "plans/EXP-*.md",
    "**/EXP-*.md",
]


def is_process_artifact(file_path: Path) -> bool:
    if file_path.suffix.lower() in DOC_EXTENSIONS:
        return True
    parts_lower = {p.lower() for p in file_path.parts}
    return bool(parts_lower & PROCESS_DIRS)


def find_approved_exp_plan(cwd: Path) -> bool:
    """Return True if at least one EXP plan exists. Approval detection is best-effort."""
    for pattern in EXP_PLAN_GLOBS:
        for candidate in cwd.glob(pattern):
            try:
                text = candidate.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue
            lowered = text.lower()
            if "status:" in lowered and ("approved" in lowered or "accepted" in lowered):
                return True
    return False


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0  # fail open

    tool_input = payload.get("tool_input", {}) or {}
    file_path_str = tool_input.get("file_path") or ""
    if not file_path_str:
        return 0

    file_path = Path(file_path_str)
    cwd = Path(payload.get("cwd") or ".")

    if is_process_artifact(file_path):
        return 0  # allow silently

    if find_approved_exp_plan(cwd):
        return 0  # G2 likely passed, allow

    # Code write without an approved EXP plan -> ask the user.
    output = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": (
                "chevp-ai-framework: No approved EXP plan found. "
                "Production code should only be written after G2 is passed. "
                "Confirm to proceed, or run /gate-check G2 first."
            ),
        }
    }
    print(json.dumps(output))
    return 0


if __name__ == "__main__":
    sys.exit(main())
