#!/usr/bin/env python3
"""
UserPromptSubmit hook: injects chevp-ai-framework lifecycle context into every turn.

Provides Claude with a per-turn reminder of the lifecycle rules, the 3 modes,
and where the current gate state must be checked. Keeps the process top-of-mind
without bloating the CLAUDE.md.
"""
import json
import sys

REMINDER = """<chevp-ai-framework>
Lifecycle active: Context -> Exploration -> Production (gated by G1/G2/G3).

Before responding you MUST:
1. Infer the current mode from the user's intent (Context / Exploration / Production).
2. Output the Adaptive Mode-Awareness Header.
3. If the user's request belongs to a later mode but the gate is not passed, BLOCK and redirect.
4. Never write production code without an approved EXP plan (G2 passed).
5. Never create an EXP plan without G1 passed.

Slash commands: /context /explore /produce /gate-check G1|G2|G3 /new-adr
Subagents: gate-validator, architecture-reviewer
</chevp-ai-framework>"""


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        # If stdin is not valid JSON, do nothing (fail open).
        return 0

    user_prompt = payload.get("prompt", "") or ""

    # Only inject when the user is actually starting/continuing lifecycle work.
    # Skip for trivial messages to avoid noise.
    if len(user_prompt.strip()) < 3:
        return 0

    output = {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": REMINDER,
        }
    }
    print(json.dumps(output))
    return 0


if __name__ == "__main__":
    sys.exit(main())
