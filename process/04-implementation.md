# Phase 4: Implementation

> Plan ist Plan, nicht mehr und nicht weniger.

## Wann

Nachdem Spec freigegeben und (falls anwendbar) Prototyp bestaetigt wurde.

## Regeln

1. **Ein Schritt nach dem anderen** — Nicht alles auf einmal
2. **Build nach jedem Schritt** — Kompiliert es noch?
3. **Minimale Aenderungen** — Nur was der Plan vorsieht
4. **Bestehende Patterns nutzen** — Keine neuen Patterns einfuehren
5. **Keine Scope-Erweiterung** — Plan ist Plan

## AI-Verhalten

### MUSS
- Bestehenden Code lesen bevor er geaendert wird
- Schrittweise vorgehen laut Plan
- Build-Erfolg verifizieren
- Bei Problemen: Ursache analysieren, nicht Symptome behandeln
- Bei Blockern: Stoppen und Menschen fragen

### DARF NICHT
- Code "verbessern" der nicht im Scope liegt
- Docstrings, Kommentare oder Type-Annotations zu unveraendertem Code hinzufuegen
- Error-Handling fuer unmoeglich Szenarien einbauen
- Helper/Utilities fuer einmalige Operationen erstellen
- Abstractions erstellen fuer hypothetische zukuenftige Anforderungen

## Anti-Patterns

| Fehler | Besser |
|--------|--------|
| "Ich habe auch gleich X refactored" | Nur Plan umsetzen |
| Over-Engineering / Feature Flags | Minimale Loesung |
| Backwards-Compatibility Hacks | Alten Code einfach aendern |
| 3 aehnliche Zeilen → Abstraction | 3 Zeilen sind OK |
| `_unused` Variablen behalten | Loeschen |

## Quality Gate

- [ ] Code kompiliert
- [ ] Nur Plan-Aenderungen umgesetzt
- [ ] Bestehende Patterns eingehalten
- [ ] Kein Over-Engineering