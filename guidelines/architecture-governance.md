---
name: Architecture-Governance
description: Every decision artifact records who proposed it and who decided it, making the human/AI split auditable
type: guideline
---

# Guideline: Architecture-Governance

**Rule:** Every governed artifact (ADR, CTX-plan, EXP-plan, PRD-plan, spec) carries a provenance block stating who **proposed** it, who **decided** it, and when. AI may only set `proposed-by`; only a human may set `decided-by` / `approved-by` / `approved-at`.

**Why:** The framework's 5th core rule says *ownership stays with the human*. Without an explicit record of who decided what, that ownership is implicit and unauditable — "the AI did it" and "the human approved it" become indistinguishable in the history. Provenance turns the human/AI boundary from a convention into a queryable fact.

**How to apply:** When AI creates or modifies a governed artifact, it fills `proposed-by: ai` and leaves the decision fields blank. A human crosses a gate or accepts a decision by running `/approve <artifact-id>` (or by manually filling the fields) — this is the only path from `proposed` to `approved`. Every gate crossing and ADR acceptance is appended to `governance-log.md`. Writes to production code are blocked when the referenced EXP plan has no `approved-by` set.

## Approval requires Evidence

Provenance answers *who decided*. Evidence answers *on what basis*. Both are required — the framework treats either alone as governance failure.

Every governed artifact's frontmatter MUST include an `evidence:` block with three fields:

```yaml
evidence:
  hypothesis: <what we believed before this gate>
  result:     <what we observed>
  reasoning:  <why that justifies the transition>
```

A `status: approved` artifact whose `evidence` block is empty, contains only `—`, or repeats the plan's Goal verbatim is a governance violation. The gatekeeper subagents (`gatekeeper-g1/g2/g3`) refuse to issue a `pass` verdict against such artifacts. The `/approve` command MUST refuse to advance status if the evidence block is unfilled, instead returning the human to the plan to complete it.

This is the operational meaning of "approval ≠ rubber-stamp". A human who clicks `/approve` is asserting *I read the evidence and find it sufficient*, not *I trust the AI*.

## Provenance frontmatter schema

Every governed artifact must include:

```yaml
---
id: <ID>                 # e.g. ADR-0007, EXP-012, CTX-003
type: <ADR|CTX|EXP|PRD|SPEC>
status: draft            # draft | proposed | approved | accepted | superseded | deprecated
proposed-by: ai          # ai | human | pair
decided-by: —            # human (required when status advances past proposed)
approved-by: —           # human identifier (name, handle, email)
approved-at: —           # ISO date YYYY-MM-DD
supersedes: —            # optional, prior artifact id
---
```

## Status transitions

| From → To | Who | How |
|-----------|-----|-----|
| (none) → `draft` | ai or human | Artifact is created |
| `draft` → `proposed` | ai or human | Artifact is complete enough to review |
| `proposed` → `approved` / `accepted` | **human only** | Via `/approve <id>` or manual edit |
| `accepted` → `superseded` | human | New artifact supersedes it |
| `accepted` → `deprecated` | human | AI flags drift; human confirms |

AI **MUST NOT** write `decided-by`, `approved-by`, or `approved-at`. If AI finds these fields populated in its own output, that is a bug — revert.

## The governance log

A single append-only file `governance-log.md` at the repo root (or `context/governance-log.md` if context lives in a subfolder) records every gate crossing and every ADR acceptance:

```
2026-04-04  G1   CTX-003   proposed:ai    approved:lunral   "context inventory complete"
2026-04-04  ADR  ADR-0007  proposed:ai    accepted:lunral   "use Postgres for primary storage"
2026-04-05  G2   EXP-012   proposed:ai    approved:lunral   "prototype validated"
2026-04-05  G3   PRD-008   proposed:pair  approved:lunral   "ships, all AC met"
```

One line per event. Never rewrite past lines. This is the authoritative audit trail — the frontmatter of individual artifacts can be lost or moved, but this log stays coherent.

## Git-level provenance

- AI-assisted commits already carry `Co-Authored-By: Claude …`.
- Commits that cross a gate or accept an ADR SHOULD include a `Decided-By:` trailer naming the human:
  ```
  Decided-By: lunral <lunral@…>
  ```
- Query: `git log --grep="Decided-By"` lists every human decision point.

## Enforcement

Mechanical checks live in [hooks/provenance-check.py](../hooks/provenance-check.py):

- Writes to production code are blocked (or asked) when the referenced EXP plan has no `approved-by`.
- Writes to ADR/plan files that would set `status: accepted|approved` without `decided-by: human` are blocked.
- Writes that set `proposed-by: human` by AI are flagged — AI may only set `proposed-by: ai` or `proposed-by: pair`.

Human approval flows through `/approve <artifact-id>`, which is the only command authorized to set decision fields and append to `governance-log.md`.

## Governance queries

Treat governance as queryable state:

- *"What has the AI proposed that no human has yet approved?"* → `grep "status: proposed" **/*.md`
- *"Every decision this quarter?"* → `governance-log.md` filtered by date
- *"Did anything reach production without a human approval?"* → any PRD with `status: approved` but empty `approved-by` is a violation

If these queries return something surprising, the governance invariant has been broken.

## Content Governance

Provenance answers *who decided*. Evidence answers *on what basis at the gate*. **Content Governance** answers *does the decision still hold in the code*. Specified by [ADR-001](../context/adr/ADR-001-content-oriented-governance.md).

> Approval ist eine Behauptung an einem Zeitpunkt. Content-Governance prüft, ob die Behauptung über Zeit hält. ADRs ohne Code-Bindung haben kein Drift-Signal — das ist erlaubt, aber dokumentiert.

The framework's first three governance layers (frontmatter, evidence, log) are *Verfahren*. Content Governance adds a *Substanz* layer:

| Mechanism | What it catches | When it runs |
|-----------|-----------------|--------------|
| `architecture-invariants.md` | Machine-checkable assertions bound to accepted ADRs | Authored alongside ADRs, validated at audit time |
| [agents/governance-auditor](../agents/governance-auditor.md) | ADR↔code drift, undocumented patterns, obsolete ADRs | On demand via `/governance-audit`; periodically per project policy |
| `/governance-audit` slash command | Runs the auditor and appends `AUDIT` event to log | Manually triggered |

### How an invariant binds to an ADR

Each non-starter invariant carries a `binding-adr: ADR-NNN` field. This couples the invariant to a decision that has passed a gate, so:

- The invariant has documented provenance (the ADR explains *why*)
- If the bound ADR is `superseded` or `deprecated`, the invariant is a candidate for retirement
- The auditor can detect orphan invariants (no `binding-adr`) and orphan ADRs (no invariant binds an imperative claim from the ADR text)

See [templates/architecture-invariants-template.md](../templates/architecture-invariants-template.md) for the schema.

### Locator discipline

The most likely failure mode of this layer is false-positive flood (per ADR-001 §Challenger Failure 2). The template enforces:

- Locator `type` is enumerated (`ast-import` | `grep` | `config-query`) — no free-text dialects
- `scope.include` is required — empty scope is a configuration error
- `loose: true` (full-text grep) is opt-in, not default

Under-disciplined locators trigger the kill criterion: after three audit runs with >70% false positives or no actionable findings, the auditor is retired and the template kept as documentation-only.

### Audit events in `governance-log.md`

Audits append a dedicated event type:

```
2026-04-25  AUDIT  —  proposed:ai  decided:—  "3 BLOCK / 7 CONCERN findings, 1 obsolete ADR candidate"
```

The `decided:—` placeholder is intentional. An audit is not a decision; it is a measurement. Decisions follow via `/approve`, `/reject`, or supersession on individual findings.

### Content Governance queries

Extending the queryable-state list above:

- *"What `accepted` ADRs have no code binding?"* → grep `accepted` ADRs, cross-reference against `binding-adr:` fields in invariants
- *"What invariants reference a `superseded` or `deprecated` ADR?"* → audit-time orphan check
- *"When did we last audit?"* → tail `governance-log.md` filtered by `AUDIT`
- *"What patterns recur ≥3 times without ADR coverage?"* → governance-auditor's "Undocumented Patterns" output

## Anti-patterns

| Anti-pattern | Why it breaks governance |
|--------------|-------------------------|
| AI edits `approved-by` | Human ownership becomes fiction |
| Skipping `governance-log.md` on gate crossing | Audit trail has holes |
| Marking an artifact `accepted` without running `/approve` | Decision fields drift out of sync with reality |
| Reusing an old artifact's id for a new decision | Supersession chain breaks |
| Squash-merging commits that drop `Decided-By:` trailers | Git-level audit trail is destroyed |
| Approving a plan with empty `evidence:` block | Approval becomes rubber-stamp; the governance/evidence pair collapses |
| Filling `evidence:` with the plan's Goal verbatim | Evidence theater; gatekeeper must reject |
| Invariant without `binding-adr` (outside starter pack) | Decision provenance for the rule is missing |
| Default `loose: true` on locators | False-positive flood; auditor signal degrades fast and the layer self-retires |
| Letting an ADR remain `accepted` after the bound symbol/library is removed | Governance state diverges from code reality |
