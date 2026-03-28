# UX-Tooling in Exploration

> See first, then build.

## Responsibilities

- Create prototypes for visual/UX validation
- Run screenshot feedback loops with the human
- Iterate until the human confirms the visual direction

## Prototype Forms

| Domain | Prototype Form | Tool |
|--------|---------------|------|
| Shader / VFX | GLSL prototype | Shadertoy |
| UI / Layout | HTML/CSS mockup | Browser / Codepen |
| 3D Scene | Scene JSON + screenshot | Nuna Renderer |
| Data flow | Diagram | Mermaid / ASCII |

See [ux-prototype-template](../templates/ux-prototype-template.md) for the artifact structure.

## Workflow

```
1. AI creates prototype based on spec
2. Human reviews visually (screenshot, preview)
3. Human gives feedback ("more to the left", "darker", "different layout")
4. AI iterates
5. Human confirms: "This is how it should look"
6. Prototype becomes reference for Production
```

## Screenshot Feedback Loop

- **Without screenshot**: AI guesses at coordinates → many failed attempts
- **With screenshot**: AI sees the problem → 1-2 corrections

AI must request or generate a screenshot after every major visual change.

## AI Behavior

### MUST
- Create prototype as a separate file (not directly modify production code)
- Ask for screenshot/preview after each iteration
- Iterate until human is satisfied

### MUST NOT
- Skip prototype for visual output
- Commit prototype directly as production code
- Continue without visual feedback

## Checklist

- [ ] Prototype exists as a separate file
- [ ] Human has visually confirmed ("this is how it should look")
- [ ] Insights have been fed back into spec/plan
