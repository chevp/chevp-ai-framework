# Demo 3 — Verification-Capsule

## Architekturfrage
> **Wie kapselt man Verifikation?**

## Worum es geht
Verifikation ist im Agenten-System eine eigene, **gekapselte Einheit** — kein Nebeneffekt
irgendwo im Hauptlauf. Ein spezialisierter **Gatekeeper-Subagent** mit isoliertem Kontext
prüft *ein* Artefakt und liefert ein **strukturiertes Verdict** zurück: `pass | conditional |
block` nach festem Schema — **nicht** Fließtext.

Die zentrale Aussage der Demo:
> Verifikation wird *deklariert, nicht programmiert*. Der Prüfer ist in **Markdown** definiert
> ([`gatekeeper.md`](gatekeeper.md)); sein Output ist gegen ein **Schema** validierbar
> ([`verdict.schema.json`](verdict.schema.json)). Damit wird Verifikation **komponierbar,
> testbar und automatisierbar** — ein Freitext-„sieht gut aus" wäre keins davon.

## Dateien
| Datei | Rolle |
|-------|-------|
| [`gatekeeper.md`](gatekeeper.md) | Der Subagent: Rolle, Prüfkriterien, Output-Vertrag. In Markdown, nicht in Code. |
| [`verdict.schema.json`](verdict.schema.json) | Das Schema, das jedes Verdict erfüllen muss. |
| [`sample-plan.md`](sample-plan.md) | Beispiel-Input: ein Plan mit **leerem Evidence-Block** (Verstoß). |
| [`sample-verdict.json`](sample-verdict.json) | Beispiel-Output: das strukturierte `block`-Verdict dazu. |
| [`validate_verdict.py`](validate_verdict.py) | Mini-Validator (stdlib): prüft ein Verdict gegen das Schema. |

## Live-Ablauf (3 Min)
1. [`sample-plan.md`](sample-plan.md) zeigen — der Evidence-Block ist leer (Kill-Kriterium fehlt).
2. [`gatekeeper.md`](gatekeeper.md) zeigen — der Prüfer ist *deklariert*: feste Kriterien,
   fester Output-Vertrag.
3. [`sample-verdict.json`](sample-verdict.json) als das Ergebnis zeigen — maschinenlesbar.
4. Validieren, dass das Verdict dem Vertrag entspricht:
   ```bash
   python validate_verdict.py sample-verdict.json
   #   → OK: Verdict entspricht dem Schema (verdict=block, 2 Findings)
   ```

## Was die Zuhörer mitnehmen
- Ein **Freitext-Verdict** ist nicht automatisierbar — ein **strukturiertes** schon
  (Gate-Logik, Dashboards, CI können darauf reagieren).
- Der Prüfer hat **eigenen Kontext** (single responsibility) und ist damit unabhängig testbar.
- Verifikation ist ein **Baustein**, kein Bauchgefühl — sie lässt sich vor jedes Gate hängen.
