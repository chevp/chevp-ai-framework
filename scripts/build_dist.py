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
MAX_LINES = 700  # Compact runtime file with efficiency rules + AI modes + prompt structure + governance extensions + §1.1 thinking & learning layer


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
    "guide_governance": read_file("guidelines/architecture-governance.md"),
    "guide_uncertainty": read_file("guidelines/uncertainty-reduction.md"),
    "guide_granularity": read_file("guidelines/plan-granularity.md"),
    "challenger": read_file("02-exploration/challenger.md"),
    "integration": read_file("integration/claude-md-integration.md"),
}


# ---------------------------------------------------------------------------
# Section builders
# ---------------------------------------------------------------------------

def build_header() -> str:
    return """\
# chevp-ai-framework

> PROCESS: Context (G1) → Exploration (G2) → Production (G3). Sequential. Gates are blockers.
> RULE: No code without spec. No delivery without validation. AI owns the process — infers mode, enforces gates, blocks violations. Human approves transitions on **evidence** (`hypothesis` / `result` / `reasoning`), not rubber-stamp.
> LOOP: Every Exploration produces an `insights.md`. Every plan has `Kill Criteria`. Every plan is critiqued by an internal **Challenger** before G2. Out-of-scope items become `PROP-NNN` proposals — they never disappear.
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

### Mixed-Intent Resolution

When a message contains signals for multiple modes, the AI decomposes intents, sequences them by lifecycle order (earlier first), executes the earliest mode's portion, and stops at the gate boundary — stating what remains.

### Adaptive Mode-Awareness Header

Header detail adapts to context: **Full** (mode + reasoning + gate progress) on mode changes, gate transitions, or blocking. **Short** (mode confirmation only) when continuing work in the same mode. The header is the AI's responsibility.

### Gatekeeper Behavior

AI acts as an autonomous process enforcer. AI blocks requests that belong to a later mode when the gate is not passed. AI states the specific missing prerequisites and actively helps the user complete them. AI proposes forward transitions when all gate criteria are satisfied.

### Mode Transitions

`Context ──[G1 + Human]──→ Exploration ──[G2 + Human]──→ Production ──[G3 + Human]──→ Done`

Backward jumps: Production → Exploration (plan wrong), Exploration → Context (requirements misunderstood).

### Production → Exploration Fallback

During Production, AI MUST propose fallback to Exploration when: plan is incomplete/ambiguous, technical constraint makes the approach unviable, or human requests a scope change. AI stops, states the trigger, and asks before continuing.

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

Exploration runs in **two sub-modes**, in this order:

| Sub-mode | Goal | Fidelity | Output |
|----------|------|----------|--------|
| **Exploration-A — Problem Exploration** | *Understand* the problem in motion | Low (sketches, throwaway scripts, paper, single-screen demos) | A confirmed framing of the problem — and a *retired* hypothesis or two |
| **Exploration-B — Solution Exploration** | *Decide* between concrete solutions | High enough to compare (≥2 candidates side-by-side) | A chosen approach with documented trade-offs |

A plan declares its sub-mode via the frontmatter field `exploration-mode: A | B`. Skipping A and going straight to B is allowed only when [hypotheses.md](../templates/hypotheses-template.md) already records the problem framing as `confirmed`.

### Deliverables

1. **Feature Plan/Spec** with `exploration-mode: A | B` — written for features/complex changes, verbal for trivial (<10 lines)
2. **ADR** — only for new decisions (fundamental ADRs belong in Context)
3. **UX Prototype** — A: low-fidelity (Problem); B: ≥2 comparable candidates (Solution)
4. **Challenger output** — top-3 failure modes, ≥2 alternatives, strongest counter-argument (mandatory before G2)
5. **`insights.md`** — Learning Loop artifact recording which hypotheses were confirmed/killed (mandatory before G2)

### Spec Required?

{spec_table}

### Prototype Required?

{proto_table}

### Prototype Workflow

1. AI creates prototype as separate file → 2. Human reviews → 3. Feedback + iterate → 4. Human confirms → 5. Prototype becomes Production reference

### Efficiency: Template-First Deliverables

Use existing templates (`context/plans/EXP-NNN-*.md`, `context/adr/ADR-NNN-*.md`) to structure deliverables. Auto-fill fields from Context artifacts, ask only about gaps. Human verifies deviations, not boilerplate.

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
6. Verify architecture-to-code alignment (drift detection) before implementing

### Decision Comments

When a code change has a non-obvious reason, add a brief inline comment explaining the reason directly — no references to plans, ADRs, or external artifacts. The comment must be self-contained.

### Validation

{validation_table}

### Commit Rules

- Stage specific files only (never `git add .`)
- Meaningful messages (what + why)
- Plan commits: `ctx(NNN):`, `exp(NNN):`, `prd(NNN):`
- Never commit/push without being asked
- Never force-push or skip hooks
- Never commit non-compiling code

### Anti-Patterns

{antipattern_table}

### Post-Delivery

- Move plans to `context/plans/finished/` (PRD + EXP)
- Update CLAUDE.md if context changed
- Write ADR if architecture decision made
- Flag outdated docs

### Gate G3

{gate_bullets}

BLOCKER — all criteria required. **Single-pass check**: verify each criterion once. Do not re-evaluate unless the human flags an issue."""


def build_uncertainty_layer() -> str:
    return """\
## Uncertainty Reduction (the operating principle)

The framework's purpose is **not to ship code** — it is to reach the moment when shipping is the *least uncertain remaining option*. Every step must measurably reduce uncertainty before the team is allowed to advance.

### Per-step contract

| Step | Must reduce | Recorded in |
|------|------------|-------------|
| **Context** | Uncertainty about *what* the problem is and *who* has it | Problem Statement, Hypotheses, Risks (uncertainty triplet), `evidence:` block in CTX plan |
| **Exploration-A** | Uncertainty about *whether the problem framing is right* | Updated Hypotheses (`confirmed`/`killed`), `insights.md` |
| **Exploration-B** | Uncertainty about *which solution is best* | Side-by-side prototype comparison, ADR, `insights.md`, Challenger output |
| **Production** | Uncertainty about *whether the chosen solution actually ships* | Validation results, updated `insights.md`, regression checks |

### Evidence Block — operational form of every gate transition

Every governed plan carries this in its frontmatter:

```yaml
evidence:
  hypothesis: <what we believed before this gate>
  result:     <what we observed>
  reasoning:  <why that justifies the transition>
```

Three rules: `hypothesis` must be falsifiable (not a goal restatement); `result` must be observable (not "team agreed"); `reasoning` must bridge result → action (proceed / fall back / kill). Empty or boilerplate evidence is a **gate failure** — Gatekeeper subagents refuse `pass` and `/approve` refuses to advance status. See [guidelines/uncertainty-reduction.md](guidelines/uncertainty-reduction.md).

### Kill Criteria — uncertainty's exit door

Every plan **must** include a `## Kill Criteria` section answering: *what evidence would tell us this plan should not advance?* A plan without kill criteria is a note, not a plan. Bad: "if it does not work". Good: "if benchmark X exceeds 200ms after Step 3"; "if user testing in Exploration-A reveals nobody uses the feature".

### Learning Loop — every Exploration produces an `insights.md`

The lifecycle is a **loop, not a pipeline**. Every Exploration phase MUST produce an `insights.md` before G2 can pass. The file records which hypotheses were confirmed/killed/inconclusive, what surprised the team, what is now believed, what is still unknown, and the consequence for the plan (proceed / adjust / kill / fall back to Context). An empty insights file is a G2 blocker."""


def build_challenger_role() -> str:
    return """\
## Challenger Role (mandatory before G2)

Without an internal sceptic, the AI proposes and the human approves — the only friction is the human's vigilance. The Challenger role moves friction *into* the AI, where it is cheap.

Before requesting G2 approval, the AI MUST produce a Challenger block in (or alongside) the EXP plan with **exactly three** sections:

1. **Top-3 ways this approach could fail** — concrete failure modes specific to *this* plan, *this* code, *this* user. Each names what breaks (an observable), the cheapest signal, and what we would do.
2. **Two alternative approaches** — at least two genuinely different alternatives that were considered and rejected, each with sketch + rejection reason + condition under which we would re-open them.
3. **Strongest counter-argument** — one paragraph stating the case *against* the chosen approach, in the first person, as charitably as possible. Strawman = automatic fail.

### Anti-pattern: generic Challenger output

Generic objections like "schedule slip", "scope creep", "we could use a different library" apply to every plan and carry no information. Gatekeeper-G2 flags these as `failure-modes: generic` and issues an automatic `block`. Regenerate with concrete content.

See [02-exploration/challenger.md](02-exploration/challenger.md) for examples of good vs. bad Challenger output."""


def build_gatekeeper_layer() -> str:
    return """\
## Gatekeeper Subagents + Plan Proposal Loop

Gate enforcement is delegated to **three specialised, read-only subagents**:

| Agent | Validates | Spawns proposals from |
|-------|-----------|----------------------|
| `gatekeeper-g1` | Context → Exploration | NOT-in-Scope items in CTX plan |
| `gatekeeper-g2` | Exploration → Production | NOT-in-Scope items + Challenger-identified failure modes in EXP plan |
| `gatekeeper-g3` | Production → Done | Follow-up items surfaced during Production (TODOs, deferred refactors, new bugs) |

Each Gatekeeper produces **three pflicht-outputs**:

1. **Verdict**: `pass` | `block` | `conditional-pass`
2. **Findings**: concrete satisfied/missing/generic items (each pointing at a file/line)
3. **Spawned Plan Proposals** (`PROP-NNN`): for each out-of-scope item or failure mode, a structured stub for human triage

Gatekeepers are **read-only**. They do not write or modify plans — they propose. Approval stays with the human.

### Plan Proposal Loop — out-of-scope items never disappear

Items in a plan's NOT-in-Scope section, plus Challenger-identified failure modes, become `PROP-NNN` Plan Proposals in `context/plans/proposals/`. The human triages each one:

| Command | Effect |
|---------|--------|
| `/promote PROP-NNN` | Convert to a real CTX/EXP/PRD plan (AI generates the stub from the proposal) |
| `/defer PROP-NNN` | Keep in proposals folder, revisit at next G1 |
| `/reject PROP-NNN <reason>` | Move to `proposals/rejected/` with reason recorded |
| `/gate-override <plan-id> <reason>` | Override a Gatekeeper `block` verdict (logged in plan frontmatter and `governance-log.md`) |

**Bounds (anti-spam):**
- **Max 5 proposals per gate-check** — excess goes into a single Sammel-Notiz paragraph in the verdict report
- **90-day auto-defer** — proposals still `pending-human-review` after 90 days are automatically moved to `deferred` at next G1 review
- **Human-only promotion** — AI may propose but never promote; promotion is always a human decision

### `conditional-pass` — the cheap way through

A Gatekeeper may issue `conditional-pass` when all gate criteria are met **AND** all out-of-scope items are filed as proposals. This means: tightly-scoped plans no longer cost the team anything — the things you cut survive as proposals instead of being lost or causing scope bloat.

See [agents/gatekeeper-g1.md](agents/gatekeeper-g1.md), [agents/gatekeeper-g2.md](agents/gatekeeper-g2.md), [agents/gatekeeper-g3.md](agents/gatekeeper-g3.md), [templates/plan-proposal-template.md](templates/plan-proposal-template.md)."""


def build_governance_layer() -> str:
    return """\
## Decision Governance + Provenance

Every governed artifact (ADR, CTX, EXP, PRD, spec) carries a provenance frontmatter block:

```yaml
proposed-by: ai          # ai | human | pair
decided-by: —            # human (required when status advances past proposed)
approved-by: —           # human identifier
approved-at: —           # YYYY-MM-DD
```

**AI MUST NOT write `decided-by`, `approved-by`, or `approved-at`.** Only the human, via `/approve <artifact-id>`, may set decision fields. This is the only path from `proposed` to `approved`. Every gate crossing and ADR acceptance is appended to `governance-log.md` (one line per event, append-only).

### Approval requires Evidence

Provenance answers *who decided*; the `evidence:` block answers *on what basis*. Both are required — either alone is governance failure. A `status: approved` artifact with empty/boilerplate `evidence:` is a violation. The `/approve` command refuses to advance status if the evidence block is unfilled.

This is the operational meaning of "approval ≠ rubber-stamp": a human who clicks `/approve` is asserting *I read the evidence and find it sufficient*, not *I trust the AI*.

See [guidelines/architecture-governance.md](guidelines/architecture-governance.md)."""


def build_ai_behavior() -> str:
    # Compact table format — faster to parse, less redundancy with step sections.
    return """\
## AI Rules

### MUST

| Rule | When |
|------|------|
| Infer mode from user intent and conversation history; output adaptive header (full on changes, short when continuing) | Always |
| Decompose mixed-intent messages by lifecycle order; execute earliest mode first, stop at gate boundary | Always |
| Block forward transitions when gate criteria are not met; state specific missing prerequisites | Always |
| Guide user toward completing missing prerequisites (don't just block — help) | Always |
| Propose gate transitions when all criteria are satisfied | Always |
| Read existing code and CLAUDE.md before any work | Always |
| Ask questions instead of assuming | Always |
| Wait for explicit human approval at every gate | Always |
| Follow existing patterns and conventions | Always |
| Produce Context-Plan (CTX) as first activity | Context |
| Produce/verify System Spec, Architecture, ADRs, Context Inventory | Context |
| Produce the **uncertainty triplet** — Problem Statement, Hypotheses (≥2), Risks (≥3) | Context |
| State understanding and surface ambiguities | Context |
| Wait for explicit scope confirmation | Context |
| Create feature plan/spec before any code | Exploration |
| Declare `exploration-mode: A` (Problem) or `B` (Solution) in the EXP frontmatter | Exploration |
| Define acceptance criteria | Exploration |
| Define **Kill Criteria** (when do we abandon?) | Exploration |
| Create and iterate prototype for visual output until confirmed | Exploration |
| Produce **Challenger output** before requesting G2 (top-3 failure modes, ≥2 alternatives, counter-argument) | Exploration |
| Produce **`insights.md`** before requesting G2 (which hypotheses confirmed/killed, what surprised us, consequence) | Exploration |
| Fill the `evidence:` frontmatter block with non-empty, non-generic `hypothesis` / `result` / `reasoning` before requesting any gate | Always |
| Invoke the matching Gatekeeper subagent (`gatekeeper-g1/g2/g3`) before proposing any forward transition | Always |
| Spawn `PROP-NNN` Plan Proposals for out-of-scope items and challenger-identified failure modes (max 5 per gate-check) | Always |
| Produce Production-Plan (PRD) and get human approval before any code | Production |
| Update `insights.md` with implementation surprises before requesting G3 | Production |
| Verify G1 + G2 deliverables before starting | Production |
| Implement step-by-step per plan, build-verify after each step | Production |
| Propose fallback to Exploration when plan is incomplete, approach is unviable, or scope changes | Production |
| Check each acceptance criterion individually | Production |
| Stage specific files only, commit only when asked | Production |
| Move completed plans to `finished/` (PRD + EXP), update docs | Production |
| Verify architecture-to-code alignment (drift detection) before implementing | Production |
| Add self-contained inline comment when a code change has a non-obvious reason | Production |

### MUST NOT

- Silently switch modes without announcing
- Require the human to declare modes, manage state, or use structured prompts
- Skip steps, gates, or modes
- Expand scope ("I also improved X")
- Assume requirements without checking
- Write plan AND immediately implement
- Write production code in Context or Exploration mode
- Create feature plans in Production mode
- Start implementing without approved Production-Plan (PRD)
- Skip prototype for visual output
- Commit/push without being asked, force-push, or skip hooks
- Commit non-compiling code
- Add docstrings/comments/types to unchanged code
- Over-engineer, premature abstractions, feature flags
- Introduce new patterns without ADR
- Re-analyze artifacts that haven't changed since last verification
- Re-justify decisions already approved at a prior gate
- Reference plans, ADRs, or external artifacts in inline code comments
- Write `decided-by`, `approved-by`, or `approved-at` fields — those are human-only
- Approve a gate with an empty or boilerplate `evidence:` block
- Approve a plan that has no `Kill Criteria` section
- Submit generic Challenger output ("schedule slip", "scope creep", "use a different framework") — auto-block
- Promote, defer, or reject `PROP-NNN` proposals on the human's behalf
- Skip `insights.md` at the end of an Exploration phase
- Spawn more than 5 `PROP-NNN` proposals per single gate-check (excess goes into a Sammel-Notiz paragraph)"""


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
├── context/guidelines/           ← extension points (if present, AI must enforce)
├── context/plans/ (+ finished/)  ← CTX/EXP/PRD artifacts
└── context/specs/                ← feature specifications
```

## Extension Points

Projects may activate optional extensions by creating files in `context/guidelines/`. If a file exists, the AI must read and enforce it:

- `architecture-invariants.md` — layer rules, forbidden patterns, dependency direction
- `review-criteria.md` — what the human reviewer checks at each gate
- `testing-strategy.md` — when/what tests are required
- `risk-classification.md` — severity levels, how risk affects process depth"""


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
        build_uncertainty_layer(),
        build_challenger_role(),
        build_gatekeeper_layer(),
        build_governance_layer(),
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
