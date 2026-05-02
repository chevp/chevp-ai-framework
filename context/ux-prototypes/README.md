# UX-Prototypes

HTML/CSS sketches that explore visual & interaction ideas before they earn an EXP plan.
Each prototype lives in its own subfolder so it can carry its own assets, README and iteration log.

## Index

| Folder | Topic | Status |
|--------|-------|--------|
| [`impressum/`](impressum/) | Impressum / legal page for [chevp.github.io](https://chevp.github.io/) | v1 — pending feedback |

> The Papers prototype was promoted to its own repository: [chevp/chevp-papers](https://github.com/chevp/chevp-papers) · live at <https://chevp.github.io/chevp-papers/>.

## Conventions

- One subfolder per prototype family (`papers/`, `impressum/`, …). When a single prototype grows multiple sibling files (a hub + several detail pages), they share the folder.
- Each folder contains its own `README.md` filled out with the [`templates/ux-prototype-template.md`](../../templates/ux-prototype-template.md) brief — Reference Spec, Prototype Form, Goal, Constraints, References, Iteration Log.
- Prototypes are **pre-G1**: they exist to provoke feedback, not to ship. Promote a settled prototype into a real EXP plan under [`context/plans/`](../plans/) before any production code.
- Static HTML, no build step. Open the file directly in a browser.
