# Demo 1 — Enforcement-Contract

## Architekturfrage
> **Wie erzwingt man Regeln außerhalb des Modells?**

## Worum es geht
Ein Agent *will* schreiben — darf aber nicht, solange kein freigegebener Plan existiert.
Die Regel steckt **nicht** im Prompt (das wäre eine Bitte), sondern in einem
**deklarativen Vertrag**, der *außerhalb der Prompt-Schicht* ausgewertet wird.

Die zentrale Aussage der Demo:
> Erzwingbarkeit ist eine **Architektur-Eigenschaft**, kein Implementierungs-Detail.
> Die Datei [`contract.yaml`](contract.yaml) **ist** der Vertrag — die ausführende Mechanik
> (`check_gate.py`) ist austauschbar und bewusst nebensächlich.

## Dateien
| Datei | Rolle |
|-------|-------|
| [`contract.yaml`](contract.yaml) | Der Vertrag: Auslöser → Bedingung → Verdict. Sprach-/runtime-agnostisch. |
| [`state.json`](state.json) | Der Zustand, gegen den geprüft wird (`plan.approved`). |
| [`check_gate.py`](check_gate.py) | Referenz-Runner (~30 Zeilen, nur stdlib). Liest Vertrag + Zustand, gibt `allow`/`block`. |

## Live-Ablauf (3 Min)

```bash
# 1. Agent will schreiben — Plan ist NICHT freigegeben → block
python check_gate.py Write
#   → BLOCK: Kein freigegebener Plan vorhanden. ...

# 2. Plan freigeben (im echten System: Gate G2 durch den Menschen)
#    state.json: "plan.approved": true setzen
python check_gate.py Write
#   → ALLOW

# 3. Lesezugriff ist nie betroffen
python check_gate.py Read
#   → ALLOW (kein Auslöser im Vertrag)
```

## Was die Zuhörer mitnehmen
- Der **Auslöser** (`on.tool`), die **Bedingung** (`when`) und das **Verdict** sind explizit
  und versionierbar — kein verstecktes Verhalten im Prompt.
- Das Modell kann den Vertrag **nicht umgehen**, weil er außerhalb seiner Reichweite greift.
- Tauscht man `check_gate.py` gegen eine andere Runtime (Hook, Proxy, CI-Step), bleibt der
  Vertrag identisch. *Die Architektur liegt im Vertrag, nicht im Code.*
