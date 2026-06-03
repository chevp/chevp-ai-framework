---
id: p-5-exploration
title: Exploration
sidebar_position: 1
plan_id: P-5
plan_slug: plugin-and-consumer-rollout
phase: exp
status: active
created: 2026-04-10
legacy_id: §1.2
exploration-mode: A
depends-on: P-4
proposed-by: ai
decided-by: "—"
approved-by: "—"
approved-at: "—"
evidence:
  hypothesis: "—"
  result: "—"
  reasoning: "—"
gatekeeper-override: []
---

# P-5 Plugin Layer & Consumer-Repo Rollout for P-4

## Goal
Take the structural changes from [P-4](../p-4-thinking-learning-upgrade/exploration) and operationalise them across (a) the Claude Code plugin layer (`hooks/`, mechanical enforcement) and (b) consumer repositories that depend on `chevp-ai-framework` (`chevp-workflow`, project repos). Until this plan ships, P-4 is markdown-only and depends on AI discipline alone.

## Context
P-4 is a documentation- and template-level upgrade. It introduces:
- New mandatory artifacts (Problem Statement, Hypotheses, Risks, `insights.md`)
- A new `evidence:` frontmatter block on every plan
- Three new Gatekeeper subagents (`gatekeeper-g1/g2/g3`)
- New slash commands (`/promote`, `/reject`, `/gate-override`)
- A new role (Challenger) and a new guideline (`uncertainty-reduction.md`)

None of these are mechanically enforced yet. `hooks/provenance-check.py` does not yet block writes when `evidence:` is empty. `hooks/gate-check.py` does not yet refuse production-code writes when no Gatekeeper verdict has been recorded. Consumer repos still use the old templates and have no chapter for "framework evolution" of their own.

This plan starts in **Exploration-A** because the open question is *whether the rollout is even feasible at the cost level P-4 implies* — not yet *how* to ship it.

## Scope

### IN Scope
- Audit which `hooks/*.py` need to be updated to enforce the new rules
- Audit which `commands/*.md` (besides the ones added in P-4) need updating
- Identify the minimum-viable consumer rollout: one consumer repo (`misc/chevp-workflow` is the natural pilot) updates its templates, generates one plan under the new format, runs `/gate-check`, and reports back
- Measure: time-to-G2 on a real plan in the pilot consumer repo (kill criterion from P-4)
- Decide whether `exploration-mode` should default to `B` or remain explicit
- Document the migration path for existing CTX/EXP/PRD plans in consumer repos (do they get retrofitted or grandfathered?)

### NOT in Scope
- Rolling out to *all* consumer repos in one go (one pilot first)
- Rewriting hooks for languages other than Python
- Touching `chevp-setup` / `repo-map.json`
- Building dashboards or metrics tooling for proposal-backlog health (a future plan, possibly P-6 or beyond)

## Steps
*(to be filled out after Exploration-A confirms feasibility)*

1. Audit `hooks/provenance-check.py` and `hooks/gate-check.py` against P-4 requirements
2. Pick the pilot consumer repo and confirm with the human
3. Run a dry-run `/gate-check G2` on P-4 itself (using the new gatekeeper-g2 subagent) and record proposals
4. Migrate one real plan in the pilot repo to the new format
5. Time the migration; check against the P-4 kill criterion
6. Decide pass/fall-back/kill

## Affected Files
*(provisional — to be confirmed after Exploration-A)*
- [hooks/provenance-check.py](../../../../../hooks/provenance-check.py)
- [hooks/gate-check.py](../../../../../hooks/gate-check.py)
- `misc/chevp-workflow/...` (pilot consumer)

## Risks
| Risk | Mitigation |
|------|------------|
| P-4 cost is higher than the kill criterion allows | This plan starts in Exploration-A precisely to find out cheaply |
| Consumer repos already have plans in the old format | Grandfather rule: old plans remain valid; new plans use the new format |
| Hook updates break existing consumer workflows | Behind a feature flag in `provenance-check.py`; off by default until pilot succeeds |

## Kill Criteria
- If the pilot rollout shows time-to-G2 grows >3× on a real plan in `chevp-workflow`, halt and reopen P-4 for redesign
- If the Gatekeeper-spawned proposals on the pilot repo are dominated by stereotypes ("clean up code", "improve tests"), halt and rework the gatekeeper prompts before continuing rollout
- If the pilot human reviewer reports that filling the `evidence:` block "feels like paperwork without value" on three consecutive plans, halt and re-evaluate the role of evidence in approval

## Acceptance Criteria
- [ ] Audit of hooks and commands complete
- [ ] Pilot consumer repo selected and confirmed
- [ ] Dry-run `/gate-check G2` executed on P-4 — verdict recorded, proposals (if any) filed in `proposals/`
- [ ] At least one plan in the pilot consumer repo runs through G1 → G2 under the new format
- [ ] Time-to-G2 measured and compared to the P-4 kill criterion
- [ ] `insights.md` for P-5 records the verdict (proceed / fall back / kill P-4)
- [ ] Decision recorded in the artifact frontmatter + git history (`Decided-By:` trailer)
