# Domain Patterns Template

> Domain-extension artifact. Location: `context/domain-patterns.md` (in a project that extends the framework into a specific domain).
> Purpose: Capture **what people in this domain repeatedly get wrong**, so the AI can warn before the team walks into the same wall again.

```markdown
---
name: <Domain> Patterns
type: domain-patterns
status: living           # living | snapshot
proposed-by: pair        # ai | human | pair
date: YYYY-MM-DD
---

# Domain Patterns — <Domain Name>

## Typical Users
Who works in this domain? What is their mental model? What language do they use?

| Persona | Mental Model | Vocabulary | Frustration Points |
|---------|--------------|------------|---------------------|
| ... | ... | ... | ... |

## Typical Misassumptions
The mistakes that *experienced* practitioners still make. Each entry is a trap, not a beginner error.

| # | Misassumption | Why people believe it | What is actually true |
|---|---------------|----------------------|----------------------|
| 1 | "X scales linearly" | naive extrapolation from 10 → 100 | "It hits a wall at ~5k because of Y" |

## Recurring Problems
The shape of the problems that keep showing up across projects in this domain. Each entry is a *pattern*, not a single bug.

| # | Problem Pattern | Where it shows up | Default response |
|---|----------------|-------------------|------------------|
| 1 | "User gets lost in the 3D viewport" | First-time editors | Provide a 2D minimap + reset-camera shortcut |

## Vocabulary
Domain-specific terms with one-line definitions. Disambiguates words that mean different things across teams.

| Term | Meaning in this domain | Common confusion |
|------|------------------------|------------------|
| ... | ... | ... |
```

## Why this artifact exists

The framework's [Domain Extension](../README.md#domain-extension) layer was originally described as **rules + templates** — a technical mechanism. That description left out the most valuable thing a domain extension should carry: the *failure history* of working in the domain.

The Domain Patterns file is the place where the team writes down its hard-won knowledge about *how this domain actually behaves* — the misassumptions that survived previous projects, the user frustrations that recur regardless of feature set, the vocabulary traps. It is read by the AI in Context phase and used by the Challenger to find non-obvious failure modes in Exploration.

Without this file, every project re-discovers the same domain pitfalls.

## How it relates to other artifacts

| Artifact | Relation |
|----------|----------|
| [problem-statement-template](problem-statement-template.md) | Personas and frustrations help fill "Who has the problem?" |
| [hypotheses-template](hypotheses-template.md) | Misassumptions become hypotheses to test |
| [risks-template](risks-template.md) | Recurring problems become default risks |
| Challenger output | Challenger consults this file when generating top-3 failure modes |
| Project CLAUDE.md | References this file from the Domain section |

## Living document

`status: living` means this file is *expected* to grow as the team learns. Append entries; do not rewrite history. When a misassumption is finally retired, mark it as such (`(retired YYYY-MM-DD)`) but do not delete it — the next newcomer will thank you.

## Example entries (3D scene editor domain)

> **Misassumption — "Users will rotate the camera with right-click."**
> Why people believe it: every CAD tool does this.
> What is actually true: ~70% of first-time editors come from Blender/Maya defaults and expect middle-mouse-orbit. We lose them in the first minute if we do not detect both bindings.

> **Recurring problem — "Scene complexity explodes between week 2 and week 4."**
> Where it shows up: every editor we have shipped.
> Default response: hard cap on visible draw calls, with a warning UI when the limit is approached. Do NOT silently degrade — users blame the editor.
