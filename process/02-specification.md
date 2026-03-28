# Phase 2: Specification

> Erst denken, dann coden.

## Wann

- **Immer** bei Features, Architektur-Aenderungen, komplexen Bugfixes
- **Optional** bei trivialen Aenderungen (< 10 Zeilen, offensichtliche Loesung)

## Artefakt-Typen

### Plan (PLAN-NNN-*.md)
Fuer konkrete Umsetzungsvorhaben mit definierten Schritten.

```markdown
# PLAN-NNN: <Titel>

## Ziel
Was soll erreicht werden?

## Kontext
Warum ist das noetig? Abhaengigkeiten?

## Scope
- IN Scope: ...
- NICHT in Scope: ...

## Schritte
1. ...
2. ...

## Betroffene Dateien
- `pfad/datei.ext` — Was aendert sich

## Risiken
- ...

## Akzeptanzkriterien
- [ ] ...
```

### Architecture Decision Record (ADR-NNN-*.md)
Fuer Architektur-Entscheidungen mit Alternativen und Trade-offs.

### Spec (informell)
Fuer kleine Aenderungen reicht eine muendliche Beschreibung im Chat — aber der Mensch muss bestaetigen.

## AI-Verhalten

### MUSS
- Schritte konkret genug formulieren fuer direkte Umsetzung
- Betroffene Dateien auflisten
- Alternativen benennen wo sinnvoll
- Auf Freigabe warten bevor Code geschrieben wird

### DARF NICHT
- Plan schreiben UND sofort umsetzen
- Risiken verschweigen
- Scope heimlich erweitern

## Quality Gate

- [ ] Plan/Spec existiert (als Datei oder im Chat bestaetigt)
- [ ] Mensch hat Freigabe erteilt
- [ ] Schritte sind umsetzbar