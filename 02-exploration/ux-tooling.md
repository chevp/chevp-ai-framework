# UX-Tooling in Exploration

> See first, then build.

## Responsibilities

- Create prototypes for visual/functional validation
- Run preview feedback loops with the human
- Iterate until the human confirms the direction

## Prototype Forms

| Domain | Prototype Form | Approach |
|--------|---------------|----------|
| UI / Layout | HTML/CSS mockup or web components | Browser-based prototype or design tool |
| Visual output (graphics, effects) | Rendered preview | Editor or local preview |
| Interactive / spatial content | Scene or model + rendered preview | Engine, renderer, or tool preview |
| Data flow / architecture | Diagram | Diagramming tool or ASCII sketch |

See [ux-prototype-template](../templates/ux-prototype-template.md) for the artifact structure.

## Workflow

```
1. AI creates prototype based on spec
2. Human reviews the result (preview, render, physical sample)
3. Human gives feedback ("more to the left", "darker", "different layout")
4. AI iterates
5. Human confirms: "This is how it should look / work"
6. Prototype becomes reference for Production
```

## Preview Feedback Loop

For any product with a visual or physical result:

- **Without preview**: AI guesses at parameters → many failed attempts
- **With preview**: AI sees the problem → 1-2 corrections

AI must request or generate a preview after every major change. This applies equally to screen-based UIs, rendered 3D models, printed outputs, or any other presentable artifact.

## AI Behavior

### MUST
- Create prototype as a separate file (not directly modify production code)
- Ask for a preview/render after each iteration
- Iterate until human is satisfied

### MUST NOT
- Skip prototype for visual or physical output
- Commit prototype directly as production code
- Continue without feedback on the result

## Checklist

- [ ] Prototype exists as a separate file
- [ ] Human has confirmed the result ("this is how it should look / work")
- [ ] Insights have been fed back into spec/plan
