# Context-Plan Template

> For the Context phase (Step 1). Location: `context/plans/CTX-NNN-<description>.md`
> Mode: Context

```markdown
---
id: CTX-NNN
type: CTX
status: draft            # draft | proposed | approved
proposed-by: ai          # ai | human | pair
decided-by: —            # human (required at G1)
approved-by: —           # human identifier
approved-at: —           # YYYY-MM-DD
evidence:
  hypothesis: —          # what we initially believed about the system/problem
  result: —              # what reading + uncertainty triplet revealed
  reasoning: —           # why scope is now safe to confirm
---

# CTX-NNN: <Context-Plan Title>

## Task
What is the user requesting? (1-2 sentences)

## Artifacts to Read/Verify
- [ ] CLAUDE.md
- [ ] System Spec — exists? current?
- [ ] Software Architecture — exists? current?
- [ ] ADRs — which ones are relevant?
- [ ] Existing code in affected area

## Uncertainty Triplet (G1 prerequisite)
- [ ] **Problem Statement** drafted — see [problem-statement-template](problem-statement-template.md)
- [ ] **Hypotheses** drafted (≥2) — see [hypotheses-template](hypotheses-template.md)
- [ ] **Risks** drafted (≥3) — see [risks-template](risks-template.md)

## Open Questions
- [ ] Question 1
- [ ] Question 2

## Scope Boundaries (Draft)
- **Likely in scope**: ...
- **Likely NOT in scope**: ...
- **Uncertain / needs human input**: ...

## Confirmation Needed
What specifically must the human confirm before proceeding to Exploration?

## Kill Criteria
- When does this Context effort itself become wasted? (e.g., "if we cannot answer the top-3 risks within N reads, escalate instead of producing a fake System Spec")
```

## Naming Convention

- Open: `CTX-NNN-<description>.md` (three digits, sequential)
- Completed: `finished/CTX-FNNN-<description>.md`

## Abbreviation

For small changes (< 10 lines), a verbal Context-Plan is sufficient — but the human must still confirm scope.

## Provenance

Frontmatter governed by [architecture-governance](../guidelines/architecture-governance.md). G1 requires `status: approved` with `approved-by` filled (via `/approve CTX-NNN`).
