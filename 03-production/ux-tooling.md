# UX-Tooling in Production

> Validate the result against the prototype.

## Responsibilities

- Compare implementation against the UX prototype
- Run preview feedback loops during implementation
- Ensure the result matches expectations before delivery

## Preview Validation Workflow

```
1. Run build / generate output
2. Capture a preview (render, browser view, physical sample, etc.)
3. Compare with prototype from Exploration
4. Feedback: Does it match? Deviations?
5. If corrections needed → fix and re-validate
```

## AI Behavior

### MUST
- Request or generate a preview after every major change
- Compare the implementation result against the prototype
- Flag deviations to the human
- Iterate until the result matches the prototype

### MUST NOT
- Skip validation for visual or physical output
- Declare "done" without comparing against the prototype
- Ignore deviations

## Checklist

- [ ] Preview captured of the implementation result
- [ ] Compared against prototype from Exploration
- [ ] Result matches (or deviations are approved by human)
