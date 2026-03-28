# Phase 3: UX-Prototype

> Erst sehen, dann bauen.

## Wann

**Pflicht** bei:
- UI-Aenderungen (Layouts, Formulare, Dashboards)
- Shader / visuelle Effekte
- 3D-Szenen und Levels
- Alles wo das Ergebnis visuell beurteilt werden muss

**Optional/Entfaellt** bei:
- Backend-APIs, Datenbank-Migrationen
- Refactoring ohne visuellen Output
- Build-System-Aenderungen

## Prototyp-Formen

| Domaene | Prototyp-Form | Tool |
|---------|---------------|------|
| Shader / VFX | GLSL-Prototyp | Shadertoy |
| UI / Layout | HTML/CSS-Mockup | Browser / Codepen |
| 3D-Szene | Szenen-JSON + Screenshot | Nuna Renderer |
| Datenfluss | Diagramm | Mermaid / ASCII |

## Workflow

```
1. AI erstellt Prototyp basierend auf Spec
2. Mensch reviewed visuell (Screenshot, Preview)
3. Mensch gibt Feedback ("weiter links", "dunkler", "anderes Layout")
4. AI iteriert
5. Mensch bestaetigt: "So soll es aussehen"
6. Prototyp wird Referenz fuer Implementation
```

## Screenshot-Feedback-Loop

Fuer visuelles Development gilt:

- **Ohne Screenshot**: AI raet bei Koordinaten → viele Fehlversuche
- **Mit Screenshot**: AI sieht das Problem → 1-2 Korrekturen

AI muss nach jeder groesseren visuellen Aenderung einen Screenshot anfordern oder erzeugen.

## AI-Verhalten

### MUSS
- Prototyp als separate Datei erstellen (nicht direkt Production Code aendern)
- Nach Screenshot/Preview fragen
- Iterieren bis Mensch zufrieden

### DARF NICHT
- Prototyp ueberspringen bei visuellem Output
- Prototyp direkt als Production Code committen
- Ohne visuelles Feedback weitermachen

## Quality Gate

- [ ] Prototyp existiert als Datei
- [ ] Mensch hat visuell bestaetigt
- [ ] Erkenntnisse sind in Spec/Plan zurueckgeflossen