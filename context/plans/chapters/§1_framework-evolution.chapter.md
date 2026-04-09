---
id: §1
name: framework-evolution
description: Strukturelle Weiterentwicklung von chevp-ai-framework selbst — Lifecycle, Gates, Rollen, Templates
type: chapter
status: active
---

# §1 Framework Evolution

## Goal

Die strukturelle Weiterentwicklung von `chevp-ai-framework` selbst organisieren — d.h. Änderungen an der Lifecycle (Context/Exploration/Production), an Gates, Rollen, Templates und Guidelines. Pläne in diesem Kapitel verändern den Prozess, mit dem alle anderen Projekte arbeiten.

## Scope

- Lifecycle-Erweiterungen (neue Sub-Modi, neue Pflicht-Artefakte)
- Gate-Definitionen (G1/G2/G3) und ihre Validierung
- Rollen-Modell (Cross-Cutting-Roles)
- Templates für Pläne, Specs, ADRs, Chapters
- Guidelines (Memory-Style-Format)
- Plugin-Layer-Sync (Hooks, Slash-Commands, Subagents) — sofern Lifecycle-relevant
- Meta: Pilot-Anwendung des Frameworks auf sich selbst

## Guiding Questions

- Welche strukturelle Lücke macht den Prozess heute schwächer als nötig?
- Reduziert die Änderung **Unsicherheit**, oder nur Aufwand?
- Bleibt die Lifecycle (3 Steps) intakt — oder bricht der Vorschlag das Fundament?
- Was ist das **Kill-Criterion** für eine vorgeschlagene Erweiterung?
- Wie lässt sich die Änderung auf das Framework selbst (Self-Hosting) testen, bevor sie an Consumer-Repos ausgerollt wird?
