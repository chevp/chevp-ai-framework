# Plan Proposals

This folder holds **Plan Proposals** (`PROP-NNN`) — lightweight backlog entries spawned by the Gatekeeper subagents when they encounter out-of-scope items or challenger-identified failure modes during a gate check.

See [templates/plan-proposal-template.md](../../../templates/plan-proposal-template.md) for the template and full lifecycle.

## Layout

```
proposals/
├── PROP-NNN_<slug>.md       ← pending or deferred
├── promoted/                 ← promoted proposals (archived stubs for traceability)
└── rejected/                 ← rejected proposals (with reason in frontmatter)
```

## Triage commands

| Command | Effect |
|---------|--------|
| `/promote PROP-NNN` | Convert to a real plan (CTX/EXP/PRD) in the suggested chapter |
| `/defer PROP-NNN` | Keep in this folder; revisit at next G1 |
| `/reject PROP-NNN <reason>` | Move to `rejected/` with reason recorded |
| `/gate-override <reason>` | Override a Gatekeeper `block` verdict (logged in plan frontmatter) |

## Rules

- **Max 5 proposals per gate-check** — prevents spam (excess goes into a single Sammel-Notiz paragraph in the verdict report)
- **90-day auto-defer** — any proposal still `pending-human-review` after 90 days is automatically moved to `deferred` at the next G1 review
- **Human-only promotion** — AI may write proposals but never promote them; promotion is always a human decision
- **No silent rejection** — every rejected proposal carries a reason in frontmatter and is appended to `governance-log.md`
