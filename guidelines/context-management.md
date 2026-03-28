# Context Management

> AI ohne Kontext erfindet Dinge. Kontext ist Pflicht.

## Kontext-Hierarchie

```
CLAUDE.md (Projekt-Root)
├── context/architecture/     — Architektur-Ueberblick
├── context/adr/              — Getroffene Entscheidungen
├── context/guidelines/       — Entwicklungsrichtlinien
├── context/plans/            — Laufende und abgeschlossene Plaene
├── context/specs/            — Feature-Spezifikationen
└── <domain-specific>/        — API-Referenzen, Templates, etc.
```

## Was AI lesen MUSS

| Situation | Mindest-Kontext |
|-----------|----------------|
| Jede Arbeit | CLAUDE.md |
| Feature-Arbeit | + relevanter Plan/Spec |
| Architektur-Aenderung | + ADRs + Architecture-Docs |
| Code-Aenderung | + bestehender Code der betroffen ist |
| Visuelles | + Screenshot des aktuellen Stands |

## CLAUDE.md Pflege

Jedes aktive Projekt/Game braucht eine CLAUDE.md mit:
- Was ist das Projekt (1-2 Saetze)
- Aktueller Stand
- Dateisystem-Uebersicht
- Technische Constraints
- Getroffene Entscheidungen

Diese Datei ist das Briefing fuer jeden AI-Agent.

## Kontext-Regeln

1. **Lesen vor Schreiben** — Bestehenden Code lesen bevor er geaendert wird
2. **API-Referenz nutzen** — Keine Funktionen erfinden die nicht existieren
3. **Templates als Vorlage** — Bestehende Patterns einhalten, nicht neue erfinden
4. **Kontext aktuell halten** — CLAUDE.md und Docs nachziehen bei Aenderungen