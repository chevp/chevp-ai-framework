# UX-Prototypes — Papers

HTML prototypes for the **Papers** concept: short, abstract-style notes published on the homepage, one idea per paper. Lives next to [Lab](../../docs/lab.html) — Lab is for executable experiments, Papers are for citable ideas.

Open prototypes directly in the browser:

- [`index.html`](index.html) — Paper Hub (volume index)
- [`paper-001-context-as-wiki.html`](paper-001-context-as-wiki.html) — first paper, two-column body

---

## UX-Prototype: Paper Hub

### Reference Spec
Concept introduced in this conversation. No formal CTX/EXP plan yet — this is pre-G1 sketching. Promote into [`context/plans/proposals/`](../plans/proposals/) once the format settles.

### Prototype Form
Static HTML/CSS, no JS. Single file, self-contained styles, Google Fonts only.

### Goal
Answer one question: **does the academic paper aesthetic carry a list of short notes without feeling pretentious?** Sub-questions:

- Is the volume/issue framing (Volume I — 2026) inviting or stiff?
- Does the entry list scan? Do the IDs (PPR-NNN, NOTE) work as light typographic anchors?
- Does the page co-exist with the dark/arctic look of the existing site, or fight it?

### Constraints
- Viewport: 760 px reading column, full-bleed background.
- Color scheme: warm paper (`#fbfaf6`), dark ink (`#1f1d1a`), oxblood accent (`#7a3b2e`).
- Type: EB Garamond for body & display, Inter for UI/meta, JetBrains Mono for IDs/code.
- Interaction: hover-only — no JS state, no animations beyond link underline.

### References
- The existing dark site for contrast — [`docs/index.html`](../../docs/index.html), [`docs/lab.html`](../../docs/lab.html).
- arxiv.org listing pages and the Stripe Press catalogue for the abstract-list pattern.

### Iteration Log

#### v1 — 2026-05-02
- Created: hub with masthead, two-column "about", one volume section listing 3 papers + 1 note.
- Feedback: _pending_

---

## UX-Prototype: Paper 001 — Context-Files as a Wiki

### Reference Spec
Content overlaps with the Lab proposal in [`docs/lab.html`](../../docs/lab.html). The paper is the abstract form of the same idea — Lab shows it running, Paper makes it citable. Not yet a formal EXP plan.

### Prototype Form
Static HTML/CSS, no JS. Two-column reading body once past the abstract, with `column-span: all` for figures, tables, and the pull quote.

### Goal
Answer: **does the two-column academic layout work for one of these abstract notes at ~1000 words?** Sub-questions:

- Is the abstract+sections+references structure heavyweight for the content, or just right?
- Do the spanning blocks (Fig. 1, Tab. 1, pull quote) read or interrupt?
- Is the trade-off `pros-cons` block enough Challenger-shaped self-critique inside a paper?

### Constraints
- Viewport: 760 px column, two text columns at ≥720 px viewport, single column below.
- Color scheme: same warm paper palette as the hub.
- Section model: Title block · Abstract (boxed) · 8 numbered sections · References. Mandatory **§6 Kill Criteria** — every paper must declare when the idea is dead.
- Interaction: none beyond links.

### References
- arxiv preprints (single-column variant of NeurIPS/ICML papers).
- Stripe Press long-form essays for serif/two-column readability.
- The framework's own [`templates/ux-prototype-template.md`](../../templates/ux-prototype-template.md) for the brief structure.

### Iteration Log

#### v1 — 2026-05-02
- Created: Title block, abstract, 8 sections, figure (folder tree), URL-map table, pull quote, pros/cons trade-offs, kill criteria, references.
- Feedback: _pending_

---

## Open questions (for the next iteration)

- **Naming.** `PPR-NNN` is fine, but should notes (`NOTE`, `N·1`) get a separate scheme or share the counter?
- **Hosting.** Do papers ship as standalone HTML in `docs/papers/`, or do they get folded into the Lab/Docusaurus subsite once that is real? (If the latter, paper-001 becomes self-referential — neat or weird?)
- **Mandatory sections.** §6 Kill Criteria is borrowed from the framework's plan template. Should every paper carry it, or only proposal-shaped papers?
- **Index growth.** At ~30 papers the flat list breaks down. When does the Hub need filters / categories / a year scroller?
