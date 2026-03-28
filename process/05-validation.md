# Phase 5: Validation

> Vertraue, aber pruefe.

## Wann

Nach jeder Implementation, vor dem Commit.

## Validierungs-Methoden

| Methode | Wann |
|---------|------|
| Build-Verifizierung | Immer |
| Screenshot-Vergleich | Bei visuellem Output |
| Spec-Abgleich | Immer (alle Akzeptanzkriterien pruefen) |
| Tests | Wenn Test-Suite vorhanden |
| Manuelle Pruefung | Bei komplexer Logik |

## Screenshot-Validation

Bei visuellem Output:

```
1. Build ausfuehren
2. Screenshot erstellen
3. Vergleich mit UX-Prototyp
4. Feedback: Stimmt ueberein? Abweichungen?
5. Falls Korrekturen → zurueck zu Implementation
```

## Spec-Abgleich

Jedes Akzeptanzkriterium aus der Spec einzeln durchgehen:

```
- [ ] Kriterium 1 → Erfuellt? Wo im Code?
- [ ] Kriterium 2 → Erfuellt? Wo im Code?
```

## Rueckspruenge

- **Kleine Korrektur**: Zurueck zu Phase 4, Fix, erneut validieren
- **Plan stimmt nicht**: Zurueck zu Phase 2, Plan anpassen
- **Grundlegendes Problem**: Zurueck zu Phase 1, neu bewerten

## Quality Gate

- [ ] Build erfolgreich
- [ ] Alle Akzeptanzkriterien erfuellt
- [ ] Visuelles Ergebnis stimmt (falls anwendbar)
- [ ] Keine Regressionen
- [ ] Mensch hat abgenommen