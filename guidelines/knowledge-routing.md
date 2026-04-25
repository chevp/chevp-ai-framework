---
name: Knowledge Routing
description: Project- and reference-knowledge produced inside the framework must land in a governance-eligible artifact, not in free-form memory
type: guideline
---

# Guideline: Knowledge Routing

**Rule:** Every piece of knowledge produced while working inside this framework has exactly one correct destination. Memory is reserved for `type: user` and `type: feedback`. Knowledge of `type: project` or `type: reference` MUST be written to a governance-eligible artifact — ADR, Context Inventory entry, plan amendment, or `insights.md` pointer — never directly to a memory file.

**Why:** Memory is friction-less by design — no gate, no `evidence:` block, no Provenance entry. When project- or reference-knowledge is captured there, it bypasses Rule 7 ("Decisions are signed") and Rule 8 ("Approval requires evidence"). Two failure modes follow: (1) decisions become invisible because they live in a file the next session may never read; (2) `insights.md` becomes a black hole that absorbs content which should have been an ADR or a plan-section. The framework's purpose is to reduce uncertainty *visibly*, and visibility requires that learnings land where Gatekeepers and Challengers can see them.

**How to apply:**
1. Before saving a memory, classify the content using the routing table below
2. If `type` would be `project` or `reference`, route to the matching artifact instead
3. If the content is a learning *about an existing plan*, append it to that plan and update the plan's `evidence:` block — do not create a parallel memory note
4. `insights.md` entries are *pointers* to where the learning landed (ADR-NNN, CTX-NNN §X.Y, Context Inventory entry), not the learning itself
5. The `Challenger` role checks "was project- or reference-knowledge written to memory since the last gate?" — Gatekeepers block transitions where the answer is yes

## Routing table

| Knowledge kind | Destination | Memory type allowed? |
|---|---|---|
| User role / preferences / working style | `memory/` | ✅ `user` |
| Correction or validated approach for future sessions | `memory/` | ✅ `feedback` |
| Architectural decision (any "we will / we will not …") | new ADR via `/new-adr` | ❌ |
| Domain or system fact (how the system *is*) | Context Inventory entry | ❌ |
| Learning that confirms / refutes a plan hypothesis | plan `evidence:` block + plan body | ❌ |
| Surprise discovered during Exploration or Production | `insights.md` (as pointer to where it landed) | ❌ |
| External system pointer (Linear board, dashboard URL) | Context Inventory `external-references` section | ❌ |
| Fact that changes scope of an active plan | plan amendment (with Provenance) | ❌ |

## Decision tree

```
Is the knowledge about the human (role, preference, correction)?
├── Yes → memory (type: user or feedback). Done.
└── No  → it is project / reference knowledge.
         │
         ├── Does it state a decision ("we will / we will not …")?
         │   └── Yes → ADR.
         │
         ├── Does it describe how the system is, or where to find something?
         │   └── Yes → Context Inventory entry.
         │
         ├── Does it confirm, refute, or extend an active plan's hypothesis?
         │   └── Yes → that plan's body + evidence: block.
         │
         └── Is it a surprise that does not yet have a home?
             └── Yes → insights.md, as a pointer that names the future home
                       ("→ to be promoted to ADR-014 in next gate").
```

## Examples

**Correctly routed**

| Observation | Where it goes | Why not memory |
|---|---|---|
| "User prefers terse responses, no trailing summaries" | `memory/feedback_terse_responses.md` | About the human — memory is correct |
| "Module X loads its config from `~/.foo/config.json`, not from the project root" | Context Inventory | Domain fact about the system |
| "We chose AskUserQuestion over inline prompts because Rule 13 forbids prose decisions" | ADR | Architectural decision |
| "Hypothesis H2 from CTX-007 was refuted by the spike" | CTX-007 body + `evidence:` block | Plan-bound learning |
| "Discovered during Production that file watcher races on macOS" | `insights.md` → "promote to ADR after Production" | Surprise needing a home |

**Anti-patterns (knowledge written to memory instead of routed)**

| Bad | Why it fails | Correct destination |
|---|---|---|
| Memory: "Project decided to use Bun instead of Node" | Architectural decision without Provenance | ADR |
| Memory: "Tests live in `__tests__/` next to source" | Derivable from repo state; pollutes memory | Nothing — read the code |
| Memory: "EXP-012's prototype showed users prefer Variant B" | Evidence detached from the plan that produced it | EXP-012 `evidence:` block |
| `insights.md`: "Learned that flag system is brittle" with no pointer | Sink, not index — Challenger cannot trace the learning | `insights.md` pointer → new ADR or new CTX item |

## Anti-patterns

| Anti-pattern | Why it breaks the rule |
|---|---|
| Project knowledge saved as `type: project` memory | Bypasses Provenance and Evidence — the framework cannot see it |
| `insights.md` containing free-form prose | Sink behavior — content that should be an ADR or plan-section never gets promoted |
| Memory entry that duplicates a Context Inventory fact | Two sources of truth; the memory copy will drift |
| "Save this for later" memory note for active-plan content | Dodges the active plan's `evidence:` block — Rubber-stamp risk at the next gate |
| Architectural decision recorded only in a memory file | No `/approve` path, no signed decision — Rule 7 violation |

## Relation to other guidelines

| Guideline | Relation |
|---|---|
| [architecture-governance](architecture-governance.md) | Provenance enforces *who decided*; this guideline enforces *where the decision is recorded* |
| [uncertainty-reduction](uncertainty-reduction.md) | `evidence:` block is the recording mechanism — this guideline ensures evidence is not lost to memory |
| [context-management](context-management.md) | Context Inventory is one of the destinations in the routing table |
| [ai-collaboration](ai-collaboration.md) | Challenger checklist gains a memory-routing audit step |

## Operational hooks (future work, out of scope for this guideline)

- `hooks/memory-route-check.py` — intercept memory writes with `type: project|reference` and force an `AskUserQuestion` classification
- Gatekeeper-G1/G2/G3 — read `MEMORY.md` diff since the last gate; block transitions where forbidden types appear
- Challenger checklist — add: "was project- or reference-knowledge written to memory since the last gate?"

These belong in a separate CTX/EXP plan; this guideline only defines the *rule*.
