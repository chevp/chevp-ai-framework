# Phase 1: Discovery

> Problem verstehen bevor Loesungen vorgeschlagen werden.

## Wann

Immer. Jede Aenderung beginnt mit Verstaendnis.

## AI-Verhalten

### MUSS
- Bestehenden Code lesen bevor Aenderungen vorgeschlagen werden
- Offene Fragen stellen statt Annahmen treffen
- Betroffene Module und Abhaengigkeiten identifizieren
- Scope klar formulieren: "Ich verstehe, du willst X. Das betrifft Y und Z."

### DARF NICHT
- Code vorschlagen ohne den bestehenden Code gelesen zu haben
- Annahmen ueber Architektur treffen ohne zu pruefen
- Scope eigenmaeachtig erweitern ("Ich habe auch gleich X verbessert")

## Kontext-Sammlung

AI muss vor dem Arbeiten folgenden Kontext haben:

| Kontext | Quelle | Pflicht |
|---------|--------|---------|
| Was ist das Projekt | CLAUDE.md | Immer |
| Architektur | context/architecture/ | Bei Struktur-Aenderungen |
| Bisherige Entscheidungen | context/adr/ | Bei Architektur-Fragen |
| Laufende Plaene | context/plans/ | Bei Feature-Arbeit |
| Guidelines | context/guidelines/ | Immer |
| Bestehender Code | Direkt lesen | Immer |

## Checkliste

- [ ] Problem kann in 1-2 Saetzen beschrieben werden
- [ ] Betroffene Dateien sind identifiziert
- [ ] Bestehende Patterns sind verstanden
- [ ] Abhaengigkeiten sind bekannt
- [ ] Offene Fragen sind mit dem Menschen geklaert
- [ ] Scope ist vom Menschen bestaetigt