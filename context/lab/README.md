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
├── src/css/custom.css
└── docs/                     ← all markdown content
    ├── intro.md
    ├── plans/active/<id>-<slug>/{context,exploration,insights,production}.md
    ├── decisions/            ← ADRs
    ├── lifecycle/            ← framework concepts
    ├── gates/
    ├── guidelines/
    ├── agents/
    └── commands/
```

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

- scaffold a new plan in the right category
- promote a plan from one phase to the next
- validate frontmatter and sidebar order
- run a build and report broken links

The agent is the only safe path to modify `context/lab/` — it enforces the ID scheme and frontmatter rules.

## Hard boundaries

- `context/lab/` is the only source for Lab content.
- `docs/flow/` is the only output target.
- `context/plans/`, `context/adr/`, `context/specs/` and `docs/*.html` are **off-limits** for the Lab. They live in the legacy §-numbering scheme and stay untouched until the experiment is validated.

## Kill criteria

The Lab is deleted (and the static HTML pages remain the canonical doc site) if any of the following hold after 4 weeks of trial use:

- authoring a plan in the Lab takes longer than the markdown-only flow;
- the build output bloats the repo by &gt; 50 MB;
- search/navigation in the Lab is not measurably better than `grep` over `context/plans/`;
- the category taxonomy needs more than two extensions in the trial period.

Tracked in `context/lab/docs/plans/active/fw-01-lab-bootstrap/`.
