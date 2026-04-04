---
name: Plan Granularity
description: Plans must match their type, size range, and minimum-substance requirements
type: guideline
---

# Guideline: Plan Granularity

**Rule:** Every plan has a type (CTX, EXP, PRD) that sets its phase and size range, a structured header, and at least five substance elements (Goal, Scope, Steps, Affected Files, Acceptance Criteria). Plans outside those bounds must be corrected before approval.

**Why:** Thin plans are not actionable; bloated plans are not reviewable. Without explicit type and size discipline, plans either under-specify the work or cover too many concerns at once, causing G2 approvals that the team cannot actually honor.

**How to apply:** Pick the plan type from the scenario table. Keep the plan within its size range, split by concern when it exceeds the maximum, expand when it falls below the minimum. Fill all five substance elements before requesting G2. Declare dependencies explicitly. Search existing plans to avoid duplicates.

## Plan Types

Each plan has a type that determines its lifecycle phase and expected scope:

| Type | Phase | Purpose | Size Range |
|------|-------|---------|------------|
| **CTX** | Context | Architecture understanding, data models, concept docs | 150–500 lines |
| **EXP** | Exploration | Feature specs, prototyping, new systems | 150–500 lines |
| **PRD** | Production | Bugfixes, refactoring, cleanup, migrations | 100–400 lines |

### Type Selection

| Scenario | Type |
|----------|------|
| New feature: plan and specify | **EXP** |
| Architecture documentation, concept clarification | **CTX** |
| Architecture decision with ADR | **CTX** (+ ADR) |
| Bugfix with more than 10 lines | **PRD** |
| Refactoring / cleanup / migration | **PRD** |
| Trivial change (< 10 lines) | No plan — verbal confirmation is sufficient |

---

## Size Limits

Plans that fall outside their size range must be corrected before approval:

| Condition | Action |
|-----------|--------|
| **Below minimum** | Plan is too thin — expand with design rationale, affected files, concrete steps, and acceptance criteria. If it cannot be expanded meaningfully, treat it as a micro-plan (verbal). |
| **Above maximum** | Plan covers too much — split into 2–3 focused plans with explicit dependencies between them. |

### Split Guidelines

When a plan exceeds the maximum, split by **concern**, not by arbitrary size:

| Domain | Split Strategy |
|--------|---------------|
| Protocol + Client + Server | Separate plans per layer |
| UI + Backend | Separate plans per stack |
| Architecture + Implementation | CTX for design, PRD for execution |
| Multiple independent subsystems | One plan per subsystem |

After splitting, each resulting plan must be self-contained: independently reviewable, independently implementable, and independently testable.

---

## Plan Header

Every plan must include a structured header after the H1 title:

```markdown
# EXP-042: Feature Title

## Type: EXP
## Status: draft
## Depends-on: CTX-037, EXP-041
## Blocks: PRD-050
```

### Status Values

| Status | Meaning |
|--------|---------|
| `draft` | Plan is being written, not yet approved |
| `approved` | Human has approved (G2 passed) |
| `in-progress` | Plan is currently being implemented |
| `done` | Plan is complete, can be moved to `finished/` |
| `superseded` | Plan has been replaced by a newer plan |

### Dependency Fields

| Field | Meaning | Required |
|-------|---------|----------|
| `Depends-on` | Plans that must be completed before this one can start | Recommended |
| `Blocks` | Plans that are waiting for this plan to complete | Optional |

Rules:
- Use `—` when no dependencies exist: `## Depends-on: —`
- Multiple plans are comma-separated: `## Depends-on: CTX-061, EXP-062`
- When a plan's status changes, check and update dependent plans
- Circular dependencies indicate a design problem — resolve by splitting or reordering

---

## Minimum Substance

A plan must contain at least these five elements to pass G2:

| Element | Requirement |
|---------|-------------|
| **Goal** | Concrete, measurable outcome (2–3 sentences, not an essay) |
| **Scope** | Both IN scope and NOT in scope, with cross-references to related plans where boundaries overlap |
| **Steps** | At least 3 implementation-ready steps |
| **Affected Files** | At least 1 concrete file path |
| **Acceptance Criteria** | At least 2 verifiable criteria |

Plans missing any of these elements are notes, not plans. They must either be expanded to meet the minimum or treated as verbal micro-plans.

---

## Duplicate Prevention

Before creating a new plan:

1. **Search** existing plans (active and finished) for overlapping scope
2. **If full overlap**: Extend the existing plan instead of creating a new one
3. **If partial overlap**: Document the boundary explicitly in the Scope section — reference the other plan by ID (e.g., "Skia rendering is covered in EXP-063")
4. **If superseding**: Set the old plan's status to `superseded` and reference the new plan

---

## Naming Convention

```
<TYPE>-<NNN>-<description>.md
```

- **TYPE**: `CTX`, `EXP`, or `PRD`
- **NNN**: Three-digit sequential number
- **description**: Lowercase, hyphen-separated
- Completed plans: `finished/<TYPE>-<NNN>-<description>.md`

---

## Updated Plan Template

```markdown
# <TYPE>-NNN: <Plan Title>

## Type: <CTX|EXP|PRD>
## Status: draft
## Depends-on: —
## Blocks: —

## Goal
What should be achieved? (2–3 sentences, concrete and measurable)

## Context
Why is this needed? What existing systems are affected?

## Scope

### IN Scope
- What is included

### NOT in Scope
- What is explicitly excluded
- Cross-reference to other plans where boundaries overlap: "See EXP-063 for Skia rendering"

## Steps
1. Step 1
2. Step 2
3. ...

## Affected Files
- `path/to/file.ext` — What will be changed

## Risks
| Risk | Mitigation |
|------|------------|
| ... | ... |

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2
```

---

## Summary

| Rule | Purpose |
|------|---------|
| Size limits per type | Prevents both under-specified and over-scoped plans |
| Minimum substance (5 elements) | Ensures every plan is actionable |
| Dependency fields | Makes plan ordering explicit |
| Duplicate prevention | Avoids redundant or conflicting plans |
| Split by concern | Keeps plans focused and independently reviewable |
