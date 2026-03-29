#!/usr/bin/env python3
"""
build_dist.py — Generates dist/chevp-ai-framework.md from source files.

Reads the structured markdown files in the repo and assembles a single
dense, machine-readable reference file for AI consumption.

Design goals:
  - Strictly structured (Context / Exploration / Production)
  - Rule-based, not verbose
  - Modular and chunkable
  - Optimized for token efficiency

Each output section has a designated authority file.

Usage:
    python scripts/build_dist.py           # build to dist/
    python scripts/build_dist.py --check   # verify output matches existing dist/
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MAX_LINES = 360  # Compact runtime file with efficiency rules + AI modes + prompt structure


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

def read_file(rel_path: str) -> str:
    return (REPO_ROOT / rel_path).read_text(encoding="utf-8")


def extract_section(text: str, heading: str, level: int = 2) -> str:
    """Extract content under a heading until the next heading of same or higher level."""
    prefix = "#" * level
    # Match heading with optional bold/formatting
    pattern = rf"^{prefix}\s+\**{re.escape(heading)}\**\s*$"
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if re.match(pattern, line, re.IGNORECASE):
            start = i + 1
            break
    if start is None:
        return ""
    end = len(lines)
    for i in range(start, len(lines)):
        if re.match(rf"^#{{{1},{level}}}\s+", lines[i]):
            end = i
            break
    return "\n".join(lines[start:end]).strip()


def extract_table(text: str, heading: str, level: int = 2) -> str:
    """Extract a markdown table under a heading."""
    section = extract_section(text, heading, level)
    table_lines = [l for l in section.splitlines() if l.strip().startswith("|")]
    return "\n".join(table_lines)


def extract_checklist(text: str, heading: str, level: int = 2) -> list[str]:
    """Extract - [ ] checklist items under a heading."""
    section = extract_section(text, heading, level)
    items = []
    for line in section.splitlines():
        m = re.match(r"^-\s+\[[ x]\]\s+(.+)$", line.strip())
        if m:
            items.append(m.group(1))
    return items


def extract_code_block(text: str, starts_with: str) -> str:
    """Extract the first fenced code block whose content starts with a given string."""
    in_block = False
    block_lines = []
    for line in text.splitlines():
        if line.strip().startswith("```") and in_block:
            break
        if in_block:
            block_lines.append(line)
        if line.strip().startswith("```") and not in_block:
            in_block = True
    content = "\n".join(block_lines).strip()
    if content.startswith(starts_with):
        return content
    return ""


# ---------------------------------------------------------------------------
# Source files
# ---------------------------------------------------------------------------

SRC = {
    "claude_md": read_file("CLAUDE.md"),
    "lifecycle": read_file("LIFECYCLE.md"),
    "ctx_readme": read_file("01-context/README.md"),
    "ctx_sdlc": read_file("01-context/sdlc.md"),
    "ctx_plans": read_file("01-context/ai-plans.md"),
    "ctx_arch": read_file("01-context/software-architecture.md"),
    "ctx_ce": read_file("01-context/context-engineering.md"),
    "exp_readme": read_file("02-exploration/README.md"),
    "exp_sdlc": read_file("02-exploration/sdlc.md"),
    "exp_plans": read_file("02-exploration/ai-plans.md"),
    "exp_ux": read_file("02-exploration/ux-tooling.md"),
    "exp_arch": read_file("02-exploration/software-architecture.md"),
    "exp_ce": read_file("02-exploration/context-engineering.md"),
    "prod_readme": read_file("03-production/README.md"),
    "prod_sdlc": read_file("03-production/sdlc.md"),
    "prod_plans": read_file("03-production/ai-plans.md"),
    "prod_devops": read_file("03-production/devops.md"),
    "prod_ux": read_file("03-production/ux-tooling.md"),
    "prod_arch": read_file("03-production/software-architecture.md"),
    "prod_ce": read_file("03-production/context-engineering.md"),
    "guide_collab": read_file("guidelines/ai-collaboration.md"),
    "guide_ctx": read_file("guidelines/context-management.md"),
    "integration": read_file("integration/claude-md-integration.md"),
}


# ---------------------------------------------------------------------------
# Section builders
# ---------------------------------------------------------------------------

def build_header() -> str:
    return """\
# chevp-ai-framework

> PROCESS: Context (G1) → Exploration (G2) → Production (G3). Sequential. Gates are blockers.
> RULE: No code without spec. No delivery without validation. AI owns the process — infers mode, enforces gates, blocks violations. Human approves transitions.
> Source: https://github.com/chevp/chevp-ai-framework — auto-generated, do not edit."""


def build_core_rules() -> str:
    section = extract_section(SRC["claude_md"], "Core Rules")
    # Also include the core principle
    principle = extract_section(SRC["claude_md"], "Core Principle")
    if principle:
        return f"## Core Principle\n\n{principle}\n\n## Core Rules\n\n{section}"
    return f"## Core Rules\n\n{section}"


def build_lifecycle() -> str:
    return """\
## Lifecycle

`Context (G1) → Exploration (G2) → Production (G3) → Done`

Backward jumps allowed. Forward only with passed gate. No jump from Context to Production."""


def build_roles() -> str:
    table = extract_table(SRC["lifecycle"], "Role Definitions")
    return f"## Roles\n\n{table}"


def build_ai_modes() -> str:
    mode_table = extract_table(SRC["lifecycle"], "AI Modes")
    return f"""\
## AI Modes

The AI owns the process. The human writes naturally; the AI infers the mode, enforces gates, and blocks violations — automatically. No structured prompts, mode declarations, or manual state management required.

AI operates in exactly one mode at a time.

{mode_table}

### Mode-Detection Protocol

Priority order: 1. Conversation state (stay in active mode) → 2. Intent classification (signal words) → 3. Default to Context → 4. Block when conflicting (explain missing prerequisites, guide user back).

AI MUST NOT silently switch modes. Any mode change must be announced with reasoning. Forward transitions require human approval.

### Mode-Awareness Header (before every response)

AI outputs a brief natural-language header: detected mode + reasoning, gate progress (what is satisfied / missing), what AI will do next (or why it blocks). This is the AI's responsibility — the human never provides or manages it.

### Gatekeeper Behavior

AI acts as an autonomous process enforcer. AI blocks requests that belong to a later mode when the gate is not passed. AI states the specific missing prerequisites and actively helps the user complete them. AI proposes forward transitions when all gate criteria are satisfied.

### Mode Transitions

`Context ──[G1 + Human]──→ Exploration ──[G2 + Human]──→ Production ──[G3 + Human]──→ Done`

Backward jumps: Production → Exploration (plan wrong), Exploration → Context (requirements misunderstood).

### State Tracking

AI tracks all state internally: current mode, active plan, gate status (G1/G2/G3), human approval. No manual session state, prompt headers, or mode declarations required from the human."""


def build_step_context() -> str:
    readme = SRC["ctx_readme"]
    deliverables = extract_table(readme, "Mandatory Deliverables (in order)")
    gate_items = extract_checklist(readme, "Quality Gate G1: Context Complete")
    gate_bullets = "\n".join(f"- {item}" for item in gate_items)

    min_ctx_table = extract_table(SRC["ctx_ce"], "What AI MUST Read")

    return f"""\
## Step 1: Context

Understand system, problem, scope. Produce foundational artifacts. Every change begins here.

### Deliverables (in order)

{deliverables}

Small changes (<10 lines): read and verify existing deliverables — do not skip.

### Efficiency: Verify Once per Session

If Context deliverables (System Spec, Architecture, ADRs) already exist and have not changed since last verified in this session: **confirm they exist and are current in one sentence** — do not re-read or re-analyze them. Only re-read if the human modifies key artifacts or flags them as outdated.

### Gate G1

{gate_bullets}

BLOCKER — all criteria required.

### Minimum Context

{min_ctx_table}"""


def build_step_exploration() -> str:
    readme = SRC["exp_readme"]
    spec_table = extract_table(SRC["exp_sdlc"], "When Is a Written Spec Required?")
    proto_table = extract_table(SRC["exp_sdlc"], "When Is a Prototype Required?")
    gate_items = extract_checklist(readme, "Quality Gate G2: Exploration Complete")
    gate_bullets = "\n".join(f"- {item}" for item in gate_items)

    return f"""\
## Step 2: Exploration

Plan concrete features, prototype where applicable. System architecture is from Context — this step is feature-level.

### Deliverables

1. **Feature Plan/Spec** — written for features/complex changes, verbal for trivial (<10 lines)
2. **ADR** — only for new decisions (fundamental ADRs belong in Context)
3. **UX Prototype** — mandatory for visual output

### Spec Required?

{spec_table}

### Prototype Required?

{proto_table}

### Prototype Workflow

1. AI creates prototype as separate file → 2. Human reviews → 3. Feedback + iterate → 4. Human confirms → 5. Prototype becomes Production reference

### Efficiency: Template-First Deliverables

Use existing templates (`context/plans/PLAN-NNN-*.md`, `context/adr/ADR-NNN-*.md`) to structure deliverables. Auto-fill fields from Context artifacts, ask only about gaps. Human verifies deviations, not boilerplate.

### Gate G2

{gate_bullets}

BLOCKER — all criteria required."""


def build_step_production() -> str:
    readme = SRC["prod_readme"]
    validation_table = extract_table(SRC["prod_sdlc"], "Validation Methods")
    antipattern_table = extract_table(SRC["prod_arch"], "Anti-Patterns")
    gate_items = extract_checklist(readme, "Quality Gate G3: Production Complete")
    gate_bullets = "\n".join(f"- {item}" for item in gate_items)

    return f"""\
## Step 3: Production

Implement plan, validate, deliver. Nothing more, nothing less.

### Prerequisites

G1 + G2 deliverables verified. If missing: go back.

### Efficiency: Stable Plan Rule

If the approved plan has not changed since G2: execute directly — do not re-analyze goals, re-evaluate alternatives, or re-justify the approach. Only re-check the plan if the human updates it or a backward jump occurs.

### Rules

1. One step at a time
2. Build after each step
3. Minimal changes — plan only
4. No scope expansion
5. Validate every acceptance criterion

### Validation

{validation_table}

### Commit Rules

- Stage specific files only (never `git add .`)
- Meaningful messages (what + why)
- Plan commits: `cplan(NNN):`, `plan(NNN):`, `pplan(NNN):`
- Never commit/push without being asked
- Never force-push or skip hooks
- Never commit non-compiling code

### Anti-Patterns

{antipattern_table}

### Post-Delivery

- Move plans to `context/plans/finished/` (PPLAN + PLAN)
- Update CLAUDE.md if context changed
- Write ADR if architecture decision made
- Flag outdated docs

### Gate G3

{gate_bullets}

BLOCKER — all criteria required. **Single-pass check**: verify each criterion once. Do not re-evaluate unless the human flags an issue."""


def build_ai_behavior() -> str:
    # Compact table format — faster to parse, less redundancy with step sections.
    return """\
## AI Rules

### MUST

| Rule | When |
|------|------|
| Infer mode from user intent and conversation history; announce detected mode with reasoning before acting | Always |
| Block forward transitions when gate criteria are not met; state specific missing prerequisites | Always |
| Guide user toward completing missing prerequisites (don't just block — help) | Always |
| Propose gate transitions when all criteria are satisfied | Always |
| Read existing code and CLAUDE.md before any work | Always |
| Ask questions instead of assuming | Always |
| Wait for explicit human approval at every gate | Always |
| Follow existing patterns and conventions | Always |
| Produce Context-Plan (CPLAN) as first activity | Context |
| Produce/verify System Spec, Architecture, ADRs, Context Inventory | Context |
| State understanding and surface ambiguities | Context |
| Wait for explicit scope confirmation | Context |
| Create feature plan/spec before any code | Exploration |
| Define acceptance criteria | Exploration |
| Create and iterate prototype for visual output until confirmed | Exploration |
| Produce Production-Plan (PPLAN) and get human approval before any code | Production |
| Verify G1 + G2 deliverables before starting | Production |
| Implement step-by-step per plan, build-verify after each step | Production |
| Check each acceptance criterion individually | Production |
| Stage specific files only, commit only when asked | Production |
| Move completed plans to `finished/` (PPLAN + PLAN), update docs | Production |

### MUST NOT

- Silently switch modes without announcing
- Require the human to declare modes, manage state, or use structured prompts
- Skip steps, gates, or modes
- Expand scope ("I also improved X")
- Assume requirements without checking
- Write plan AND immediately implement
- Write production code in Context or Exploration mode
- Create feature plans in Production mode
- Start implementing without approved Production-Plan (PPLAN)
- Skip prototype for visual output
- Commit/push without being asked, force-push, or skip hooks
- Commit non-compiling code
- Add docstrings/comments/types to unchanged code
- Over-engineer, premature abstractions, feature flags
- Introduce new patterns without ADR
- Re-analyze artifacts that haven't changed since last verification
- Re-justify decisions already approved at a prior gate"""


def build_abbreviations() -> str:
    table = extract_table(SRC["lifecycle"], "When Steps May Be Abbreviated")
    return f"""\
## Abbreviations

{table}

No step skipped entirely. Human approval always required.

### Micro-Plans for Trivial Changes

For changes <10 lines with verbal confirmation: use a one-line plan (goal + affected file + acceptance criterion) instead of a full plan document. Implement in a single pass — no multi-step iteration needed."""


def build_context_hierarchy() -> str:
    return """\
## Context Hierarchy

```
CLAUDE.md (project root)          ← always read first
├── context/architecture/         ← for architecture changes
├── context/adr/                  ← architecture decisions
├── context/plans/ (+ finished/)  ← CPLAN/PLAN/PPLAN artifacts
└── context/specs/                ← feature specifications
```"""


# ---------------------------------------------------------------------------
# Assembly
# ---------------------------------------------------------------------------

def build() -> str:
    sections = [
        build_header(),
        build_core_rules(),
        build_lifecycle(),
        build_roles(),
        build_ai_modes(),
        build_step_context(),
        build_step_exploration(),
        build_step_production(),
        build_ai_behavior(),
        build_abbreviations(),
        build_context_hierarchy(),
    ]
    return "\n\n---\n\n".join(sections) + "\n"


def main():
    output = build()
    lines = output.splitlines()

    if len(lines) > MAX_LINES:
        print(
            f"ERROR: Output is {len(lines)} lines (max {MAX_LINES}). "
            "Trim source content.",
            file=sys.stderr,
        )
        sys.exit(1)

    out_dir = REPO_ROOT / "dist"
    out_file = out_dir / "chevp-ai-framework.md"

    if "--check" in sys.argv:
        if out_file.exists():
            existing = out_file.read_text(encoding="utf-8")
            if existing == output:
                print("OK: dist/chevp-ai-framework.md is up to date.")
                sys.exit(0)
            else:
                print("DRIFT: dist/chevp-ai-framework.md differs.", file=sys.stderr)
                sys.exit(1)
        else:
            print("MISSING: dist/chevp-ai-framework.md", file=sys.stderr)
            sys.exit(1)

    out_dir.mkdir(parents=True, exist_ok=True)
    out_file.write_text(output, encoding="utf-8")
    byte_count = len(output.encode("utf-8"))
    print(f"Built: dist/chevp-ai-framework.md ({len(lines)} lines, {byte_count} bytes)")


if __name__ == "__main__":
    main()
