# UX-Prototype — Impressum (chevp.github.io)

Static HTML prototype for the legal "Impressum" page of [chevp.github.io](https://chevp.github.io/).

Open directly in the browser:

- [`index.html`](index.html) — single-page Impressum, *Papers* aesthetic (warm paper, EB Garamond, oxblood accent)

---

## Reference Spec

**Authoritative content source:** [`/Users/chevp/workspace/sites/site-policy/impressum.html`](../../../../../sites/site-policy/impressum.html) — published at
[chevp.github.io/site-policy/impressum.html](https://chevp.github.io/site-policy/impressum.html).
This prototype is **content-faithful**: every paragraph, every heading, the legal regime
(Schweizer Recht), the responsible party (Patrice Chevillat — Software Development —
Switzerland), and the contact-page link are taken verbatim from that file.

The prototype answers a *visual* question only — it does not propose new legal text and
must never drift from the source. If `sites/site-policy/impressum.html` changes, this
prototype must be re-synced.

No formal CTX/EXP plan yet — pre-G1 sketching.

## Prototype Form

Single-file HTML, inline CSS, one tiny inline `<script>` for the copyright year (kept
identical to the source), Google Fonts (EB Garamond + Inter + JetBrains Mono).
Self-contained — could replace `sites/site-policy/impressum.html` if the re-skin is
adopted.

## Goal

Answer: **does the *Papers* warm-paper aesthetic carry a Schweizer Impressum without
making it feel either too playful for a Pflichtangabe or too academic for a
disclaimer?** Sub-questions:

- Does the §-numbered section pattern read naturally for the six-section Schweizer
  layout (Angaben / Kontakt / Verantwortlich / Haftungsausschluss / Haftung für Links /
  Urheberrechte), or does it feel bureaucratic?
- Does the address-card pattern (re-using the `.figure` box from paper-001) work, or is
  it overdesigned for "Patrice Chevillat — Software Development — Switzerland"?
- Is the `PROTOTYPE` notice — styled like the paper abstract — clear enough that no one
  mistakes this for the canonical file at `sites/site-policy/impressum.html`?
- Does the warm palette feel coherent next to the dark
  [`docs/index.html`](../../../docs/index.html) and the existing dark
  `sites/site-policy/impressum.html`, or does the Impressum need to be visually adopted
  into the dark theme later?

## Constraints

- **Content fidelity.** Every paragraph is verbatim from
  [`sites/site-policy/impressum.html`](../../../../../sites/site-policy/impressum.html).
  Wording, ordering, and the link to `contact.html` must not be invented or modernised.
- Viewport: 760 px reading column (matches [`papers/index.html`](../papers/index.html)),
  full-bleed background.
- Color scheme: warm paper palette — `#fbfaf6` background, `#1f1d1a` ink, oxblood
  accent `#7a3b2e`, soft `#b9866b` for ornamental accents (identical CSS variables to
  the Papers prototypes).
- Type: EB Garamond for body & display, Inter for UI/meta and the byline,
  JetBrains Mono for the `PROTOTYPE` tag.
- Sections: 6 numbered (§ 1 – § 6) covering Angaben gemäss Schweizer Recht, Kontakt,
  Verantwortlich für den Inhalt, Haftungsausschluss, Haftung für Links, Urheberrechte.
- Single-column body — no two-column reading flow (the Impressum is too short for the
  paper-001 column treatment).
- Interaction: hover-only — no JS state, only the inline `year` script that the source
  file also carries.

## References

- **Source of truth** —
  [`sites/site-policy/impressum.html`](../../../../../sites/site-policy/impressum.html)
  (the dark-themed published Impressum).
- Sibling Papers prototypes for design language —
  [`../papers/index.html`](../papers/index.html),
  [`../papers/paper-001-context-as-wiki.html`](../papers/paper-001-context-as-wiki.html).
- The current dark chevp.github.io site for the integration question —
  [`docs/index.html`](../../../docs/index.html),
  [`docs/lab.html`](../../../docs/lab.html).
- The framework's [`templates/ux-prototype-template.md`](../../../templates/ux-prototype-template.md)
  for the brief structure used here.

## Iteration Log

### v1 — 2026-05-02

- Created: 7-section Impressum (German TMG / MStV skeleton with placeholder fields),
  dark/arctic palette.
- Feedback: _superseded — wrong legal regime AND wrong content; chevp.github.io is
  Swiss and the canonical text already exists at
  `sites/site-policy/impressum.html`._

### v2 — 2026-05-02

- Re-skinned to the *Papers* warm-paper palette and EB Garamond / Inter / JetBrains
  Mono type stack so the Impressum lives in the same visual family as
  [`../papers/`](../papers/). Title block, byline + `§` ornament, boxed notice, and
  address `.card` pattern borrowed from paper-001.
- Feedback: _superseded — kept the invented German content from v1; still wrong._

### v3 — 2026-05-02

- **Content rewrite** — discarded all invented text. Pulled the six sections, the
  "Patrice Chevillat — Software Development — Switzerland" address block, the
  Kontaktseite link, the Schweizer Haftungsausschluss / Haftung für Links /
  Urheberrechte paragraphs, and the inline copyright-year script verbatim from
  [`sites/site-policy/impressum.html`](../../../../../sites/site-policy/impressum.html).
  Topbar, title block, byline, and notice now declare Schweizer Recht and link the
  canonical source. *Papers* visual treatment kept.
- Feedback: _pending_

---

## Open questions (for the next iteration)

- **Hosting path.** The canonical lives at
  [`sites/site-policy/impressum.html`](../../../../../sites/site-policy/impressum.html).
  If this re-skin is adopted, does it replace the dark version in place, or do both
  coexist (warm for `chevp.github.io`, dark for the `site-policy` subsite)?
- **Datenschutz.** A sibling [`sites/site-policy/privacy.html`](../../../../../sites/site-policy/privacy.html)
  already exists. Should the Papers re-skin sweep all of `site-policy/` (Impressum,
  Privacy, Contact, Terms) or just the Impressum?
- **Language.** Source is German; the rest of chevp.github.io is English. Should a
  re-skin add an EN summary lede, or stay strictly DE like the source?
- **Re-sync trigger.** Who/what notices when `sites/site-policy/impressum.html` is
  edited and this prototype falls out of sync?
