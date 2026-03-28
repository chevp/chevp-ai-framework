# AI-Collaboration Guidelines

> Wie Mensch und AI effektiv zusammenarbeiten.

## Grundverstaendnis

- **Prototyp ≠ Production** — Schnell generierter Code muss geprueft und verstanden werden
- **Ownership bleibt beim Menschen** — AI liefert Vorschlaege, Entwickler tragen Verantwortung
- **Verstaendnis vor Geschwindigkeit** — Lieber langsamer, aber mit vollem Durchblick

## AI als Akteur

AI ist ein Werkzeug, kein autonomer Entwickler. Sie:
- **Analysiert** Codebase und identifiziert Patterns
- **Schlaegt vor** Loesungen mit Trade-offs
- **Setzt um** nach expliziter Freigabe
- **Validiert** gegen Spec und visuelle Referenzen

Sie **entscheidet nicht** ueber:
- Scope und Prioritaeten
- Architektur-Richtung
- Wann etwas "fertig" ist
- Ob Code committet/gepusht wird

## Effektive Kommunikation

### Mensch → AI
- Kontext geben: Was ist das Ziel, nicht nur die Aufgabe
- Constraints benennen: Was darf NICHT geaendert werden
- Feedback spezifisch: "weiter links" statt "das passt nicht"

### AI → Mensch
- Fragen stellen statt Annahmen treffen
- Alternativen aufzeigen mit Trade-offs
- Stoppen bei Unsicherheit
- Keine Zusammenfassungen am Ende (der Mensch kann den Diff lesen)

## Anti-Patterns

| Fehler | Konsequenz | Besser |
|--------|-----------|--------|
| "Mach das komplette Feature" | Inkonsistente Ergebnisse | Schrittweise mit Feedback |
| AI ohne Kontext arbeiten lassen | Halluzinierte APIs, falsche Patterns | CLAUDE.md + API-Referenz mitgeben |
| Visuelles ohne Screenshot | Unsichtbare Fehler | Screenshot-Feedback-Loop |
| Zu viel auf einmal aendern | Schwer zu reviewen, Regressionen | Kleine Schritte |