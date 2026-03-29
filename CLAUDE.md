# CLAUDE.md — chevp-ai-framework

This is a process framework for AI-assisted software development.
It defines the overarching lifecycle that Claude must follow in all projects.

## Core Rules

1. **Steps are sequential** — No step may be skipped
2. **Human decides** — At every step transition, the human must explicitly confirm
3. **Context before code** — AI writes no production code without a prior spec
4. **Prototype before production** — Validate UX prototypes before implementing (where applicable)
5. **Ownership stays with the human** — AI delivers suggestions, developers bear responsibility
6. **Gates are blockers** — All criteria must be satisfied before forward transition

## Lifecycle: 3 Steps × 6 Roles

```
1. Context → 2. Exploration → 3. Production
```

### Mandatory Deliverables

| Step | Deliverables |
|------|-------------|
| **Context** | System Spec, Software Architecture, ADRs (fundamental), Context Inventory, Scope Confirmation |
| **Exploration** | Feature Plan/Spec, ADRs (new decisions), UX Prototype (where applicable) |
| **Production** | Production Code, Validation Result, Updated Documentation |

### Quality Gates

| Gate | Transition | Key Rule |
|------|-----------|----------|
| **G1** | Context → Exploration | System Spec + Architecture + ADRs + Context Inventory exist, scope confirmed |
| **G2** | Exploration → Production | Feature plan/spec approved, prototype confirmed (where applicable) |
| **G3** | Production → Done | All acceptance criteria fulfilled, build passes, human approved |

Within each step, 6 cross-cutting roles operate:
**SDLC** · **AI-Plans** · **UX-Tooling** · **DevOps** · **Software-Architecture** · **Context-Engineering**

Full matrix: [LIFECYCLE.md](LIFECYCLE.md)

## Documentation

| Folder | Content |
|--------|---------|
| [01-context/](01-context/) | Step 1: Understand system, gather context, produce foundational artifacts |
| [02-exploration/](02-exploration/) | Step 2: Plan features, prototype, validate approach |
| [03-production/](03-production/) | Step 3: Build, verify, ship |
| [templates/](templates/) | Templates for plans, specs, ADRs, CLAUDE.md, prototypes |
| [guidelines/](guidelines/) | Cross-cutting quality rules for AI collaboration |
| [integration/](integration/) | How to integrate the framework into projects |