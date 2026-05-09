#!/usr/bin/env python3
"""
PreToolUse hook for Write/Edit: enforces architecture-governance provenance rules.

Rules enforced:
- AI must not set `decided-by`, `approved-by`, or `approved-at` in artifact frontmatter.
  Those fields are human-only (written via /approve).
- AI must not mark an artifact `status: approved` / `status: accepted` itself.
- An artifact that carries a provenance block must not be downgraded (e.g. AI cannot
  overwrite an existing `approved-by` value).

This is advisory by default (permissionDecision: "ask") — the user can always confirm.
The goal is to surface governance violations, not to hard-lock the editor.

See guidelines/architecture-governance.md for the full rule set.
"""
import json
import re
import sys
from pathlib import Path

# Artifacts governed by provenance. Path parts (case-insensitive).
GOVERNED_DIRS = {
    "adrs", "adr",
    "plans",
    "01-context", "02-exploration", "03-production",
    "ctx-plans", "exp-plans", "prd-plans",
}

# Filename patterns that indicate a governed artifact.
GOVERNED_NAME_RE = re.compile(r"^(ADR|CTX|EXP|PRD)-\d+", re.IGNORECASE)

# Fields AI is not allowed to populate.
HUMAN_ONLY_FIELDS = ("decided-by", "approved-by", "approved-at")

# Statuses AI is not allowed to set directly.
HUMAN_ONLY_STATUSES = ("approved", "accepted")

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)


def is_governed_artifact(file_path: Path) -> bool:
    if file_path.suffix.lower() != ".md":
        return False
    if GOVERNED_NAME_RE.match(file_path.name):
        return True
    parts_lower = {p.lower() for p in file_path.parts}
    return bool(parts_lower & GOVERNED_DIRS)


def is_template(file_path: Path) -> bool:
    parts_lower = {p.lower() for p in file_path.parts}
    return "templates" in parts_lower


def extract_frontmatter(text: str) -> dict:
    m = FRONTMATTER_RE.match(text or "")
    if not m:
        return {}
    fields = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            fields[key.strip().lower()] = value.strip().strip('"').strip("'")
    return fields


def field_is_set(value: str) -> bool:
    """A field is 'set' if it has a concrete value, not the em-dash placeholder."""
    if not value:
        return False
    v = value.strip().strip('"').strip("'")
    return v not in ("", "—", "-", "TBD", "tbd", "null", "None")


def violations(new_text: str, old_text: str) -> list[str]:
    new_fm = extract_frontmatter(new_text)
    old_fm = extract_frontmatter(old_text)

    # Only enforce on files that actually carry a provenance block.
    if not new_fm or "proposed-by" not in new_fm and "status" not in new_fm:
        return []

    problems = []

    # 1. AI must not fill human-only fields that were previously empty.
    for field in HUMAN_ONLY_FIELDS:
        new_val = new_fm.get(field, "")
        old_val = old_fm.get(field, "")
        if field_is_set(new_val) and not field_is_set(old_val):
            problems.append(
                f"`{field}` is human-only — it must be set via `/approve`, not by AI."
            )
        if field_is_set(new_val) and field_is_set(old_val) and new_val != old_val:
            problems.append(
                f"`{field}` was already set to `{old_val}` — AI cannot overwrite human decisions."
            )

    # 2. AI must not move status into an approved/accepted state.
    new_status = (new_fm.get("status") or "").lower()
    old_status = (old_fm.get("status") or "").lower()
    if new_status in HUMAN_ONLY_STATUSES and old_status != new_status:
        problems.append(
            f"`status: {new_status}` is a human decision — use `/approve` to record it."
        )

    # 3. AI may not claim a human as proposer.
    new_proposer = (new_fm.get("proposed-by") or "").lower()
    old_proposer = (old_fm.get("proposed-by") or "").lower()
    if new_proposer == "human" and old_proposer not in ("human", ""):
        problems.append(
            "`proposed-by: human` conflicts with prior value — AI may only set `ai` or `pair`."
        )

    return problems


def read_current(file_path: Path) -> str:
    try:
        return file_path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""


def simulated_new_text(tool_name: str, tool_input: dict, current: str) -> str:
    """Reconstruct what the file would look like after the tool runs."""
    if tool_name == "Write":
        return tool_input.get("content") or ""
    if tool_name == "Edit":
        old = tool_input.get("old_string") or ""
        new = tool_input.get("new_string") or ""
        if tool_input.get("replace_all"):
            return current.replace(old, new)
        return current.replace(old, new, 1) if old else current
    return current


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0  # fail open

    tool_name = payload.get("tool_name") or ""
    tool_input = payload.get("tool_input", {}) or {}
    file_path_str = tool_input.get("file_path") or ""
    if not file_path_str or tool_name not in ("Write", "Edit"):
        return 0

    file_path = Path(file_path_str)

    # Templates carry example frontmatter — skip them.
    if is_template(file_path):
        return 0
    if not is_governed_artifact(file_path):
        return 0

    current = read_current(file_path)
    new_text = simulated_new_text(tool_name, tool_input, current)

    problems = violations(new_text, current)
    if not problems:
        return 0

    reason = (
        "chevp-ai-framework governance violation:\n  - "
        + "\n  - ".join(problems)
        + "\nSee guidelines/architecture-governance.md. "
          "Human decisions flow through `/approve <id>`, not direct edits by AI."
    )
    output = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": reason,
        }
    }
    print(json.dumps(output))
    return 0


if __name__ == "__main__":
    sys.exit(main())
