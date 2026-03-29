# Step 1: Context

> Understand the system and the problem before proposing solutions.

## Goal

Understand the system, the problem, and the scope. Produce the foundational artifacts that all subsequent work builds on. Every change — no matter how small — begins with understanding.

> **Important:** The Context step is not a project-level phase. Every individual task (feature, bugfix, refactoring) starts at Context, regardless of the project's overall maturity or SDLC stage.

## When

Always. No exceptions. Even trivial changes require reading CLAUDE.md and confirming scope.

## Inputs

- User requirement (feature, bug, idea)
- Existing code / architecture
- CLAUDE.md and project documentation

## Mandatory Deliverables (in order)

| # | Deliverable | Description |
|---|-------------|-------------|
| 1 | **System Spec** | What the system is, what it does, who it serves, which components it has |
| 2 | **Software Architecture** | High-level architecture: layers, modules, communication paths, technology stack |
| 3 | **ADRs** | Architecture Decision Records for all fundamental design decisions |
| 4 | **Context Inventory** | Catalogue of existing artifacts: code, docs, schemas, conventions, dependencies |
| 5 | **Scope Confirmation** | Only after 1-4: confirm scope with the human |

For small changes (< 10 lines), deliverables 1-3 may already exist. In that case, **read and verify** them — do not skip them.

**Efficiency: Verify Once per Session** — If deliverables already exist and have not changed since last verified in this session, confirm they exist and are current in one sentence. Only re-read if the human modifies key artifacts or flags them as outdated.

## Activities

- Read CLAUDE.md and project documentation
- Explore and understand the codebase
- Identify existing patterns, conventions, and dependencies
- Produce System Spec, Architecture doc, and fundamental ADRs (if they don't exist yet)
- Catalogue existing artifacts (Context Inventory)
- Capture constraints and resolve open questions with the human
- Formulate scope and obtain **explicit human confirmation**

## Outputs

- System Spec (written document or verified existing)
- Software Architecture document (written or verified existing)
- ADRs for fundamental decisions (written or verified existing)
- Context Inventory (list of existing artifacts, patterns, conventions)
- Human-confirmed scope

## Roles Active in This Step

| Role | Responsibility |
|------|---------------|
| [SDLC](sdlc.md) | Process governance, scope confirmation, gate enforcement |
| [AI-Plans](ai-plans.md) | System Spec, problem formulation, initial scope definition |
| [Software-Architecture](software-architecture.md) | Architecture document, ADRs, codebase analysis |
| [Context-Engineering](context-engineering.md) | Context Inventory, what AI must read, context hierarchy |

## Quality Gate G1: Context Complete

- [ ] System Spec exists (what the system is, who it serves, which components)
- [ ] Software Architecture is documented (layers, modules, communication)
- [ ] ADRs exist for fundamental decisions (why this language, protocol, structure)
- [ ] Existing artifacts are catalogued (code, docs, schemas, conventions)
- [ ] Problem is understood and can be described in 1-2 sentences
- [ ] Affected files/modules are identified
- [ ] Existing patterns are understood
- [ ] Dependencies are known
- [ ] All open questions are resolved with the human
- [ ] **Human has explicitly confirmed scope**

**BLOCKER: Do NOT proceed to [Exploration](../02-exploration/) until every checkbox is satisfied.**