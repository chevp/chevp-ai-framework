# Quality Gates

> Kein Phasen-Uebergang ohne bestandenes Gate.

## Uebersicht

| Phase-Uebergang | Gate |
|-----------------|------|
| Discovery → Specification | Scope bestaetigt, Fragen geklaert |
| Specification → UX-Prototype | Plan/Spec freigegeben |
| UX-Prototype → Implementation | Visuell bestaetigt |
| Implementation → Validation | Build erfolgreich, nur Plan-Scope |
| Validation → Delivery | Alle Akzeptanzkriterien erfuellt |

## Gate-Details

### G1: Discovery abgeschlossen
- [ ] Problem in 1-2 Saetzen beschreibbar
- [ ] Betroffene Module identifiziert
- [ ] Offene Fragen geklaert
- [ ] Mensch hat Scope bestaetigt

### G2: Specification freigegeben
- [ ] Plan/Spec existiert (Datei oder Chat-Bestaetigung)
- [ ] Schritte sind konkret und umsetzbar
- [ ] Scope und Nicht-Scope definiert
- [ ] Mensch hat freigegeben

### G3: Prototyp bestaetigt
- [ ] Prototyp existiert als Datei
- [ ] Mensch hat visuell bestaetigt ("so soll es aussehen")
- [ ] Erkenntnisse in Spec zurueckgeflossen
- [ ] (Entfaellt bei nicht-visuellen Aenderungen)

### G4: Implementation abgeschlossen
- [ ] Build erfolgreich
- [ ] Nur Aenderungen aus Plan/Spec
- [ ] Bestehende Patterns eingehalten
- [ ] Kein Over-Engineering

### G5: Validation bestanden
- [ ] Alle Akzeptanzkriterien erfuellt
- [ ] Visuell korrekt (falls anwendbar)
- [ ] Keine Regressionen
- [ ] Mensch hat final abgenommen

## Eskalation bei Gate-Failure

Wenn ein Gate nicht bestanden wird:
1. **Kleine Korrektur noetig**: In aktueller Phase fixen, Gate erneut pruefen
2. **Grundlegendes Problem**: Zurueck zur vorherigen Phase
3. **Scope aendert sich**: Zurueck zu Discovery