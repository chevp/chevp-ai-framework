# Context-Plan Template

> For the Context phase (Step 1). Location: `context/plans/CPLAN-NNN-<description>.md`
> Mode: `chp-context:`

```markdown
# CPLAN-NNN: <Context-Plan Title>

## Task
What is the user requesting? (1-2 sentences)

## Artifacts to Read/Verify
- [ ] CLAUDE.md
- [ ] System Spec — exists? current?
- [ ] Software Architecture — exists? current?
- [ ] ADRs — which ones are relevant?
- [ ] Existing code in affected area

## Open Questions
- [ ] Question 1
- [ ] Question 2

## Scope Boundaries (Draft)
- **Likely in scope**: ...
- **Likely NOT in scope**: ...
- **Uncertain / needs human input**: ...

## Confirmation Needed
What specifically must the human confirm before proceeding to Exploration?
```

## Naming Convention

- Open: `CPLAN-NNN-<description>.md` (three digits, sequential)
- Completed: `finished/CPLAN-FNNN-<description>.md`

## Abbreviation

For small changes (< 10 lines), a verbal Context-Plan is sufficient — but the human must still confirm scope.
