# Chapter Template

> For chapter definitions that organize plans thematically. Location: `context/plans/chapters/§<number>_<slug>.chapter.md`
> See [paragraph-numbering](../guidelines/paragraph-numbering.md) for the §-numbering convention.

```markdown
---
id: §<number>
name: <slug-with-hyphens>
description: <one-line description of this chapter's scope>
type: chapter
status: active           # active | archived
---

# §<number> <Chapter Title>

## Goal

What this thematic area aims to achieve. (2–3 sentences)

## Scope

- Topic or sub-plan covered by this chapter
- Another topic
- ...

## Guiding Questions

- What key question should plans in this chapter answer?
- Another guiding question
- ...
```

## Conventions

- Chapter files contain **Goal**, **Scope**, and **Guiding Questions** — no implementation details
- Chapters are orientation maps, not work plans
- Concrete work lives in plan files (`*.ctx.md`, `*.exp.md`, `*.prd.md`) within `active/`, `finished/`, etc.
- Sub-chapters (e.g., `§1.2`) are also chapter files — they refine the scope of their parent

## Naming Convention

```
§<number>_<slug-with-hyphens>.chapter.md
```

- **Top-level**: `§1_infrastructure.chapter.md`
- **Sub-chapter**: `§1.2_deployment.chapter.md`

## Example

```markdown
---
id: §1.2
name: deployment-and-serving
description: Asset pipeline, deployment workflows, and dev servers
type: chapter
status: active
---

# §1.2 Deployment & Serving

## Goal

Provide reliable, reproducible deployment from local dev through CI to production. Developers should be able to serve, build, and deploy with minimal configuration.

## Scope

- Dev server (local HTTP serving with hot reload)
- Asset pipeline (bundling, optimization, cache headers)
- CI/CD integration (build, test, deploy stages)
- Installer packaging (platform-specific distribution)

## Guiding Questions

- How does a developer go from code change to running preview?
- What is the minimal configuration for a new deployment target?
- How are platform-specific packaging concerns isolated from the core build?
```
