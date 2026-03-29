# AI-Plans in Context

> System-level specification and scope definition.

## Responsibilities

- Produce the **System Spec**: what the system is, what it does, who it serves, which components it has
- Transform the user's request into a clear problem statement
- Identify what is in scope and what is not
- Surface ambiguities early

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
- Produce or verify the System Spec before anything else
- Formulate scope explicitly: "I understand you want X. This affects Y and Z."
- List affected components and their boundaries
- Identify unknowns and ask about them
- Distinguish between "what the user asked" and "what might also be needed"

### MUST NOT
- Start writing a feature plan/spec (that belongs to Exploration)
- Make assumptions about priorities or ordering
- Commit to a solution approach yet
- Skip the System Spec because "the project already exists"

## Artifact Boundary

| Artifact | Context (Step 1) | Exploration (Step 2) |
|----------|-----------------|---------------------|
| System Spec (whole system) | **Mandatory** | — |
| Feature Plan/Spec | — | Mandatory |

## Checklist

- [ ] System Spec exists and is current
- [ ] Problem can be described in 1-2 sentences
- [ ] Affected files/modules are listed
- [ ] Scope boundaries are explicit (in scope / not in scope)
- [ ] Open questions are documented