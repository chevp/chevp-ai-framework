# UX-Tooling in Production

> Validate the visual result against the prototype.

## Responsibilities

- Compare implementation against the UX prototype
- Run screenshot feedback loops during implementation
- Ensure visual correctness before delivery

## Screenshot Validation Workflow

```
1. Run build
2. Take screenshot
3. Compare with UX prototype from Exploration
4. Feedback: Does it match? Deviations?
5. If corrections needed → fix and re-validate
```

## AI Behavior

### MUST
- Request or generate a screenshot after every major visual change
- Compare implementation screenshots against the prototype
- Flag visual deviations to the human
- Iterate until visual result matches prototype

### MUST NOT
- Skip visual validation for UI/shader/scene work
- Declare "done" without screenshot comparison
- Ignore visual deviations

## Checklist

- [ ] Screenshot taken of implementation
- [ ] Compared against prototype from Exploration
- [ ] Visual result matches (or deviations are approved by human)
