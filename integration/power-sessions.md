# Power Sessions

> Synchronous 2-hour sessions with defined roles for team-scale task execution.

## Principle

The default mode of the framework is **1 developer + AI, asynchronous**. Power Sessions are the team-scale alternative: a focused 2-hour session where the right people are in the room to complete one lifecycle step together.

Power Sessions solve the team-scale context problem — instead of documenting everything for async consumption, the expertise is live and available.

## When to Use Power Sessions

| Situation | Default (1 Dev + AI) | Power Session |
|-----------|----------------------|---------------|
| Small task, single domain | Yes | Overkill |
| Cross-domain task (backend + frontend + infra) | Possible but slow | Yes — bring all domains |
| Task with unclear requirements | Possible with async PO input | Yes — PO in the room |
| Architecture-impacting change | Possible if architect reviews async | Yes — architect decides live |
| Onboarding a new team member | Slow | Yes — knowledge transfer is immediate |

**Rule of thumb**: Use a Power Session when the task requires knowledge from more than one person to complete a step.

## Format

One session = one lifecycle step. A task that needs all three steps requires three sessions (not necessarily on the same day).

### CTX Session (2h) — Understand

| Aspect | Detail |
|--------|--------|
| **Goal** | Pass G1: Context-Plan confirmed, System Spec + Architecture verified, scope confirmed |
| **Roles** | Developer (drives AI), Domain Expert (answers business questions), Architect (verifies architecture) |
| **AI role** | Reads codebase, produces artifacts, asks structured questions to the room |
| **Output** | All CTX artifacts produced and confirmed. G1 passed. |

Typical flow:
1. Developer states the task (5 min)
2. AI enters Context mode, produces Context-Plan (10 min)
3. Domain Expert answers open questions, clarifies scope (20 min)
4. AI produces/verifies System Spec + Architecture (30 min)
5. Architect reviews, corrects if needed (20 min)
6. Scope confirmation — all participants agree (15 min)
7. G1 checkpoint — verify all criteria (10 min)
8. Buffer (10 min)

### EXP Session (2h) — Plan

| Aspect | Detail |
|--------|--------|
| **Goal** | Pass G2: Feature plan approved, prototype confirmed (if applicable), acceptance criteria defined |
| **Roles** | Developer (drives AI), Lead Dev (reviews plan feasibility), UX Designer (if visual — reviews prototype) |
| **AI role** | Creates plan, iterates on feedback, produces prototype if needed |
| **Output** | Approved EXP plan, prototype (if applicable). G2 passed. |

Typical flow:
1. AI reads CTX artifacts, enters Exploration mode (5 min)
2. AI produces feature plan draft (15 min)
3. Lead Dev reviews feasibility, identifies risks (20 min)
4. AI iterates on plan based on feedback (15 min)
5. If visual: AI creates prototype, UX Designer reviews (30 min)
6. Acceptance criteria defined collaboratively (15 min)
7. Plan approval — all participants agree (10 min)
8. G2 checkpoint (5 min)
9. Buffer (5 min)

### PRD Session (2h) — Build

| Aspect | Detail |
|--------|--------|
| **Goal** | Pass G3: Code implemented, validated, committed |
| **Roles** | Developer (drives AI), Reviewer (reviews code live), QA (if complex — validates acceptance criteria) |
| **AI role** | Implements plan step by step, runs build after each step |
| **Output** | Production code, all acceptance criteria passed. G3 passed. |

Typical flow:
1. AI reads EXP plan, produces PRD plan (10 min)
2. Developer approves PRD plan (5 min)
3. AI implements step by step, Reviewer watches (60 min)
4. Build verification after each step (included in implementation time)
5. Acceptance criteria check — QA validates if present (15 min)
6. Code review by Reviewer (15 min)
7. G3 checkpoint + commit (10 min)
8. Buffer (5 min)

## Roles Reference

| Role | When Needed | Responsibility |
|------|-------------|----------------|
| **Developer** | Every session | Drives the AI, makes implementation decisions |
| **Domain Expert** | CTX sessions | Answers business questions, confirms scope |
| **Architect** | CTX sessions, EXP if architecture-impacting | Reviews architecture alignment, ADR decisions |
| **Lead Dev** | EXP sessions | Reviews plan feasibility, identifies technical risks |
| **UX Designer** | EXP sessions (visual tasks only) | Reviews prototypes, provides design feedback |
| **Reviewer** | PRD sessions | Live code review during implementation |
| **QA** | PRD sessions (complex tasks) | Validates acceptance criteria |

Not every role is needed in every session. The Developer decides who to invite based on the task.

## Scheduling Patterns

| Pattern | When |
|---------|------|
| **3 sessions, 3 days** | Standard — one step per day, artifacts settle overnight |
| **3 sessions, 1 day** | Urgent — full lifecycle in 6h with breaks between sessions |
| **CTX + EXP same day, PRD next day** | Common — understanding and planning flow naturally, implementation benefits from a fresh start |
| **Only CTX as session, rest async** | When only the context-gathering needs multiple people |

## Combining with Async Work

Power Sessions do not replace async work — they complement it:

```
                Async (1 Dev + AI)     Power Session (Team)
Small task:     CTX → EXP → PRD       —
Medium task:    —                      CTX → EXP → PRD
Mixed:          —                      CTX (session) → EXP + PRD (async)
```

The decision of async vs. session is per-step, not per-task. A task might have a CTX Power Session (because scope is unclear) followed by async EXP and PRD (because the developer can handle those alone).

## Anti-Patterns

| Mistake | Why It Fails |
|---------|-------------|
| Inviting everyone to every session | Too many voices — sessions stall. Invite only the roles needed for the specific step |
| No preparation — participants arrive cold | Wasted session time on context that could have been read beforehand. Share the task description before the session |
| Skipping gate checks because "we're all here" | Gates exist precisely for collaborative settings — they ensure nothing is forgotten in the energy of the session |
| Using Power Sessions for trivial tasks | Overhead of coordination exceeds the task's complexity. Reserve for cross-domain or unclear tasks |
| Trying to do all 3 steps in one 2h session | Steps have different cognitive demands. Rushing creates poor artifacts. One step per session |
