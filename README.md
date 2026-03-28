# chevp-ai-framework

> AI-assisted Software Development Lifecycle Framework

Ein strukturierter Prozess fuer die Zusammenarbeit von Mensch und AI (Claude) bei der Softwareentwicklung.

## Warum?

Vibe Coding ist kein Fortschritt — es ist technischer Leichtsinn. AI schreibt Code, aber sie uebernimmt keine Verantwortung. Dieses Framework definiert klare Phasen, Quality Gates und Verantwortlichkeiten.

## Lifecycle

```
Discovery → Specification → UX-Prototype → Implementation → Validation → Delivery
```

Jede Phase produziert definierte Artefakte. Keine Phase wird uebersprungen.

## Schnellstart

1. Lies [process/LIFECYCLE.md](process/LIFECYCLE.md) fuer den Gesamtueberblick
2. Kopiere [artifacts/claude-md-template.md](artifacts/claude-md-template.md) als `CLAUDE.md` in dein Projekt
3. Verweise in deiner Projekt-CLAUDE.md auf dieses Framework

## Struktur

```
process/          — Lifecycle-Phasen im Detail
artifacts/        — Templates fuer alle Artefakte
guidelines/       — Qualitaetsregeln
integration/      — Einbindung in bestehende Projekte
```

## Prinzipien

- **Prototyp ≠ Production** — Schnell generierter Code muss geprueft werden
- **Kontext ist Pflicht** — AI ohne Kontext erfindet Dinge
- **Inkrementell** — Kleine Schritte mit Validation nach jedem Schritt