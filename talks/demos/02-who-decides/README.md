# Demo 2 — Who-Decides

## Architekturfrage
> **Wer trifft Entscheidungen?**

## Worum es geht
Derselbe Task, zwei Architekturen. Der Unterschied ist *nicht* das Modell — sondern **wer
den Kontrollfluss bestimmt**:

| Kontrollfluss A — der Workflow | Kontrollfluss B — das Modell |
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

## Dateien (deklarativ — kein Code)
| Datei | Rolle |
|-------|-------|
| [`orchestrated.flow.md`](orchestrated.flow.md) | Kontrollfluss A: Workflow besitzt die Reihenfolge. Identischer Trace bei jedem Lauf. |
| [`model-driven.flow.md`](model-driven.flow.md) | Kontrollfluss B: Modell wählt je Schritt. Trace driftet, kann `verify` überspringen. |

> Beide Flows sind **konzeptionell** — keine LLM-Anbindung nötig. Es geht ausschliesslich um
> den **Kontrollfluss**, nicht um die Qualität der Schritte. Die vorbereiteten Traces in
> beiden Dateien sind die Screencast-Vorlage.

## Live-Ablauf (3 Min) — ohne Code
1. [`orchestrated.flow.md`](orchestrated.flow.md) zeigen — zwei Läufe, **identischer** Trace,
   `verify` immer dabei. → *reproduzierbar*.
2. [`model-driven.flow.md`](model-driven.flow.md) zeigen — zwei Läufe, **unterschiedlicher**
   Trace, Lauf 2 überspringt `verify`. → *Drift, Garantie verloren*.
3. Pointe: derselbe Aktionsraum, nur **wer entscheidet** ist anders — und das verändert die
   Garantien.

## Was die Zuhörer mitnehmen
- „Wer entscheidet?" ist **die** Architekturfrage — und sie wird **pro Teilschritt** beantwortet.
- Determinismus kauft **Reproduzierbarkeit & Audit**; Autonomie kauft **Flexibilität**.
- Ein driftender Trace, der `verify` überspringt, zeigt: Autonomie ohne Leitplanken verliert
  Garantien, die man an kritischen Stellen (Deploy/Merge/Delete) braucht.
