# context/lab

Experimental Docusaurus subsite for the chevp-ai-framework.

This folder is the **source**. The build output lives at the repo root in `docs/flow/` so GitHub Pages serves it at <https://chevp.github.io/chevp-ai-framework/flow/>.

See [`docs/lab.html`](../../docs/lab.html) on the live site for the full concept guide.

## Layout

```
context/lab/
├── docusaurus.config.js
├── sidebars.js
├── package.json
├── src/
│   ├── components/PlanList.tsx     ← filters plans by frontmatter `status`
│   └── css/custom.css
└── docs/                           ← all markdown content
    ├── intro.md
    ├── plans/
    │   ├── _category_.json
    │   ├── index.mdx               ← filtered list driven by status frontmatter
    │   └── p-<N>-<slug>/{context,exploration,insights,production}.md
    ├── decisions/d-<N>-<slug>.md   ← ADRs
    ├── lifecycle/                  ← framework concepts
    ├── gates/
    ├── guidelines/
    ├── agents/
    └── commands/
```

The folder structure under `plans/` is **flat** — no `active/` or `finished/` subfolder. `status` is a frontmatter property; the `/plans/` index page filters live.

## ID scheme

Two flat global counters:

| Prefix | Used for | Examples |
|--------|----------|----------|
| `P-<N>` | Plans | `P-1`, `P-32` |
| `D-<N>` | Decisions / ADRs | `D-1`, `D-123` |

No categories. No padding. No reuse, even after a plan is killed.

## Setup

Requires Node >= 18.

```bash
cd context/lab
npm install
```

## Develop

Live-reload at <http://localhost:3000>:

```bash
npm run start
```

## Build

Writes static HTML into `../../docs/flow/`:

```bash
npm run build
```

After building, the GitHub Pages site picks up the new `docs/flow/` content on the next push to `main`.

## Preview the production build

```bash
npm run serve
```

## Authoring with the agent

Use the `lab-curator` subagent (see [`agents/lab-curator.md`](../../agents/lab-curator.md)) to:

- scaffold a new plan (`P-<N>`) or decision (`D-<N>`) with the next free number
- promote a plan from one phase to the next
- change a plan's `status` (frontmatter edit only — never a folder rename)
- validate frontmatter and sidebar order
- run a build and report broken links

The agent is the only safe path to modify `context/lab/` — it enforces the ID scheme, the frontmatter rules, and the **no-folder-rename** invariant for status.

## Hard boundaries

- `context/lab/` is the only source for Lab content.
- `docs/flow/` is the only output target.
- `context/plans/`, `context/adr/`, `context/specs/` and `docs/*.html` are **off-limits** for the Lab. They live in the legacy §-numbering scheme and stay untouched until the experiment is validated.
- Status changes never rename or move a folder — only the `status` frontmatter field is edited.

## Kill criteria

The Lab is deleted (and the static HTML pages remain the canonical doc site) if any of the following hold after 4 weeks of trial use:

- authoring a plan in the Lab takes longer than the markdown-only flow;
- the build output bloats the repo by &gt; 50 MB;
- search/navigation in the Lab is not measurably better than `grep` over `context/plans/`;
- the `status` frontmatter filter proves harder to use than just naming subfolders `active/` / `finished/` after all.

Tracked in `context/lab/docs/plans/p-1-lab-bootstrap/`.
