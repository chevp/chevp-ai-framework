# AI-Plans in Context

> System-level specification and scope definition.
> The AI enters Context mode automatically for this role. AI reads, verifies, and asks. No code, no feature plans.

## Responsibilities

- Produce the **Context-Plan** as the first activity
- Produce the **System Spec**: what the system is, what it does, who it serves, which components it has
- Transform the user's request into a clear problem statement
- Identify what is in scope and what is not
- Surface ambiguities early

## Context-Plan (Mandatory Deliverable)

The Context-Plan is a lightweight plan that guides the Context phase. It answers:
- What is the user requesting?
- Which artifacts need to be read/verified?
- What open questions exist?
- What are the draft scope boundaries?
- What must the human confirm?

For small changes (< 10 lines), a verbal Context-Plan is sufficient.

Template: [context-plan-template](../templates/context-plan-template.md)

## System Spec (Mandatory Deliverable)

The System Spec answers:
- What is this system?
- Who does it serve?
- What are its core components / modules?
- What are its boundaries (what it is NOT)?

For existing projects: verify the System Spec is still accurate. Update if needed.

Template: [spec-template](../templates/spec-template.md)

## AI Behavior

### MUST
- Produce a Context-Plan as the first activity
- Produce or verify the System Spec before anything else
- Formulate scope explicitly: "I understand you want X. This affects Y and Z."
- List affected components and their boundaries
- Identify unknowns and ask about them
- Distinguish between "what the user asked" and "what might also be needed"

### MUST NOT
- Start writing a feature plan/spec (wrong mode — that belongs to Exploration)
- Write production code (wrong mode — that belongs to Production)
- Make assumptions about priorities or ordering
- Commit to a solution approach yet
- Skip the System Spec because "the project already exists"

## Artifact Boundary

| Artifact | Context (Step 1) | Exploration (Step 2) | Production (Step 3) |
|----------|-----------------|---------------------|---------------------|
| Context-Plan (CTX) | **Mandatory** | — | — |
| System Spec (whole system) | **Mandatory** | — | — |
| Feature Plan/Spec (EXP) | — | **Mandatory** | — |
| Production-Plan (PRD) | — | — | **Mandatory** |

## Checklist

- [ ] Context-Plan exists and is confirmed by human
- [ ] System Spec exists and is current
- [ ] Problem can be described in 1-2 sentences
- [ ] Affected files/modules are listed
- [ ] Scope boundaries are explicit (in scope / not in scope)
- [ ] Open questions are documented