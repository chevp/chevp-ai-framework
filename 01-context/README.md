# Step 1: Context

> Understand the system and the problem before proposing solutions.
> The AI enters Context mode automatically when it detects the user wants to understand the system or start a new task. In this mode, AI reads, verifies, and asks. No code, no feature plans.

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
| 1 | **Context-Plan (CTX)** | Lightweight plan: what to read/verify, open questions, draft scope boundaries |
| 2 | **Problem Statement** | Who has the problem? What does not work today? Why does it matter? Why now? — see [problem-statement-template](../templates/problem-statement-template.md) |
| 3 | **Hypotheses** | What we *think* could be true and what could solve the problem; each hypothesis carries a cheapest test and a kill criterion — see [hypotheses-template](../templates/hypotheses-template.md) |
| 4 | **Risks** | Where we might be wrong, top-3 expensive failure modes, counter-evidence we may be ignoring — see [risks-template](../templates/risks-template.md) |
| 5 | **System Spec** | What the system is, what it does, who it serves, which components it has |
| 6 | **Software Architecture** | High-level architecture: layers, modules, communication paths, technology stack |
| 7 | **ADRs** | Architecture Decision Records for all fundamental design decisions |
| 8 | **Context Inventory** | Catalogue of existing artifacts: code, docs, schemas, conventions, dependencies |
| 9 | **Scope Confirmation** | Only after 1–8: confirm scope with the human |

The three new artifacts (**Problem Statement**, **Hypotheses**, **Risks**) form the **uncertainty triplet**. Together they make Context the place where uncertainty is explicitly catalogued — not assumed away. See [guidelines/uncertainty-reduction.md](../guidelines/uncertainty-reduction.md).

For small changes (< 10 lines), deliverables 1-3 may already exist. In that case, **read and verify** them — do not skip them.

**Efficiency: Verify Once per Session** — If deliverables already exist and have not changed since last verified in this session, confirm they exist and are current in one sentence. Only re-read if the human modifies key artifacts or flags them as outdated.

## Activities

- Produce Context-Plan as the first activity
- Read CLAUDE.md and project documentation
- Explore and understand the codebase
- Identify existing patterns, conventions, and dependencies
- Produce System Spec, Architecture doc, and fundamental ADRs (if they don't exist yet)
- Catalogue existing artifacts (Context Inventory)
- Capture constraints and resolve open questions with the human
- Formulate scope and obtain **explicit human confirmation**

## Outputs

- Context-Plan (confirmed by human)
- **Problem Statement** (uncertainty triplet)
- **Hypotheses** (uncertainty triplet)
- **Risks** (uncertainty triplet)
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

- [ ] Context-Plan exists and is confirmed by human
- [ ] **Problem Statement** exists, all five questions answered concretely
- [ ] **Hypotheses** exist (≥2 hypothesised solutions, each with cheapest test + kill criterion)
- [ ] **Risks** exist (≥3 risks rated, top-3 expensive failure modes called out)
- [ ] System Spec exists (what the system is, who it serves, which components)
- [ ] Software Architecture is documented (layers, modules, communication)
- [ ] ADRs exist for fundamental decisions (why this language, protocol, structure)
- [ ] Existing artifacts are catalogued (code, docs, schemas, conventions)
- [ ] Problem is understood and can be described in 1-2 sentences
- [ ] Affected files/modules are identified
- [ ] Existing patterns are understood
- [ ] Dependencies are known
- [ ] All open questions are resolved with the human
- [ ] **Human has explicitly confirmed scope** *(evidence-based: hypothesis / result / reasoning recorded — see [guidelines/uncertainty-reduction.md](../guidelines/uncertainty-reduction.md))*

**BLOCKER: Do NOT proceed to [Exploration](../02-exploration/) until every checkbox is satisfied.**