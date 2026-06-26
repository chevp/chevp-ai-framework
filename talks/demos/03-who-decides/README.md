# Demo 3 — Who-Decides

## Architekturfrage
> **Wer trifft Entscheidungen?**

## Worum es geht
Derselbe Task, zwei Architekturen. Der Unterschied ist *nicht* das Modell — sondern **wer
den Kontrollfluss bestimmt**:

| `orchestrated.py` | `model_driven.py` |
|---|---|
| Der **Workflow** entscheidet die Reihenfolge | Das **Modell** entscheidet den nächsten Schritt |
| feste Stages: explore → plan → verify → apply | wählt pro Schritt frei aus den Aktionen |
| **reproduzierbar** — gleicher Trace bei jedem Lauf | **driftet** — anderer Trace, kann `verify` überspringen |
| vorhersagbar, starr | flexibel, unvorhersehbar |

Das ist das **Determinismus ↔ Autonomie**-Spektrum, konkret gemacht. Beide haben ihre
Berechtigung — die Architekturarbeit ist, jeden Teilschritt *bewusst* einzuordnen:

> Modell entscheiden lassen bei **Exploration, Klassifikation, Synthese**.
> Deterministisch orchestrieren bei **Deployment, Merge, Delete** — überall, wo das Ergebnis
> reproduzierbar und auditierbar sein muss.

## Dateien
| Datei | Rolle |
|-------|-------|
| [`orchestrated.py`](orchestrated.py) | Workflow entscheidet: feste Stage-Pipeline. Gleicher Trace bei jedem Lauf. |
| [`model_driven.py`](model_driven.py) | „Modell" entscheidet pro Schritt (hier gemockt). Trace driftet zwischen Läufen. |

> Beide Skripte sind **gemockt** — keine echte LLM-Anbindung nötig. Es geht ausschliesslich
> um den **Kontrollfluss**, nicht um die Qualität der Schritte.

## Live-Ablauf (3 Min)

```bash
# Orchestriert: zweimal laufen lassen -> identischer Trace
python orchestrated.py
python orchestrated.py

# Model-driven: zweimal laufen lassen -> unterschiedlicher Trace,
# manchmal fehlt 'verify' (genau das Risiko unkontrollierter Autonomie)
python model_driven.py
python model_driven.py
```

## Was die Zuhörer mitnehmen
- „Wer entscheidet?" ist **die** Architekturfrage — und sie wird **pro Teilschritt** beantwortet.
- Determinismus kauft **Reproduzierbarkeit & Audit**; Autonomie kauft **Flexibilität**.
- Ein driftender Trace, der `verify` überspringt, zeigt: Autonomie ohne Leitplanken verliert
  Garantien, die man an kritischen Stellen (Deploy/Merge/Delete) braucht.
