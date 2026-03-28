# AI-Assisted Development Lifecycle

## Ueberblick

```
┌─────────────┐     ┌────────────────┐     ┌───────────────┐
│ 1. Discovery│────→│2. Specification│────→│3. UX-Prototype│
└─────────────┘     └────────────────┘     └───────────────┘
                                                    │
┌─────────────┐     ┌────────────────┐              │
│ 6. Delivery │←────│ 5. Validation  │←─────────────┘
└─────────────┘     └────────────────┘     ┌────────────────┐
                           ↑               │4. Implementation│
                           └───────────────└────────────────┘
```

Jede Phase hat:
- **Eingabe**: Was wird benoetigt
- **Ausgabe**: Was wird produziert (Artefakte)
- **Quality Gate**: Was muss erfuellt sein bevor die naechste Phase beginnt
- **Rollen**: Wer entscheidet (Mensch vs. AI)

---

## Phase 1: Discovery

**Ziel:** Problem verstehen, Kontext sammeln, Scope definieren.

### Eingabe
- User-Anforderung (Feature, Bug, Idee)
- Bestehender Code / Architektur

### Aktivitaeten
- Codebase explorieren und verstehen
- Bestehende Patterns und Konventionen identifizieren
- Abhaengigkeiten und Constraints erfassen
- Offene Fragen formulieren

### Ausgabe
- Klare Problembeschreibung
- Liste betroffener Komponenten
- Offene Fragen (falls vorhanden)

### Quality Gate
- [ ] Problem ist verstanden und kann in 1-2 Saetzen beschrieben werden
- [ ] Betroffene Dateien/Module sind identifiziert
- [ ] Alle offenen Fragen sind geklaert
- [ ] Mensch hat Scope bestaetigt

### Rollen
| Aufgabe | Verantwortlich |
|---------|---------------|
| Anforderung formulieren | Mensch |
| Codebase analysieren | AI |
| Scope festlegen | Mensch (final) |

---

## Phase 2: Specification

**Ziel:** Loesung spezifizieren bevor Code geschrieben wird.

### Eingabe
- Discovery-Ergebnisse
- Bestehende Architektur-Docs (context/, ADRs)

### Aktivitaeten
- Plan oder Spec erstellen (je nach Umfang)
- Schritte definieren
- Betroffene Dateien und erwartete Aenderungen auflisten
- Risiken und Alternativen benennen
- ADR erstellen falls architekturelle Entscheidung

### Ausgabe
- **Kleiner Scope**: Kurzer Plan mit Schritten
- **Grosser Scope**: Vollstaendige Spec (PLAN-NNN-*.md)
- **Architektur-Entscheidung**: ADR

### Quality Gate
- [ ] Plan/Spec ist geschrieben und liegt im Repo
- [ ] Schritte sind konkret genug fuer Umsetzung
- [ ] Scope und Nicht-Scope sind klar definiert
- [ ] Mensch hat Plan/Spec reviewed und freigegeben

### Rollen
| Aufgabe | Verantwortlich |
|---------|---------------|
| Plan/Spec entwerfen | AI |
| Trade-offs aufzeigen | AI |
| Freigabe erteilen | Mensch |

---

## Phase 3: UX-Prototype

**Ziel:** Visuelles oder funktionales Feedback vor Production Code.

> Diese Phase ist optional fuer rein technische Aenderungen (Refactoring, Backend-APIs).
> Sie ist Pflicht fuer alles mit visuellem Output (UI, Shader, Szenen, Layouts).

### Eingabe
- Freigegebene Spec / Plan
- Design-Referenzen (falls vorhanden)

### Aktivitaeten
- Prototyp erstellen (Shadertoy, Figma-Skizze, HTML-Mockup, etc.)
- Screenshot / Preview generieren
- AI-Feedback auf Basis des visuellen Outputs
- Iterieren bis Mensch zufrieden

### Ausgabe
- Prototyp-Datei(en)
- Screenshot(s) als Referenz
- Mensch-Bestaetigung: "So soll es aussehen"

### Quality Gate
- [ ] Prototyp existiert und ist sichtbar/testbar
- [ ] Mensch hat visuell bestaetigt
- [ ] Erkenntnisse aus Prototyp sind in Spec zurueckgeflossen (falls noetig)

### Rollen
| Aufgabe | Verantwortlich |
|---------|---------------|
| Prototyp erstellen | AI |
| Visuell beurteilen | Mensch |
| Iterationen anfordern | Mensch |

---

## Phase 4: Implementation

**Ziel:** Production-ready Code schreiben, der dem Plan folgt.

### Eingabe
- Freigegebener Plan / Spec
- UX-Prototyp als visuelle Referenz (falls vorhanden)

### Aktivitaeten
- Schrittweise Umsetzung laut Plan
- Build-Verifizierung nach jedem Schritt
- Bestehende Patterns und Konventionen einhalten
- Keine Scope-Erweiterung

### Ausgabe
- Production Code
- Aktualisierte Tests (falls relevant)

### Quality Gate
- [ ] Code kompiliert / Build ist erfolgreich
- [ ] Nur Aenderungen die im Plan stehen
- [ ] Bestehende Patterns eingehalten
- [ ] Kein Over-Engineering, keine Extra-Features

### Rollen
| Aufgabe | Verantwortlich |
|---------|---------------|
| Code schreiben | AI |
| Code reviewen | Mensch |
| Build pruefen | AI + Mensch |

---

## Phase 5: Validation

**Ziel:** Sicherstellen dass die Umsetzung korrekt ist.

### Eingabe
- Implementierter Code
- Spec / Plan als Referenz
- UX-Prototyp als visuelle Referenz

### Aktivitaeten
- Screenshot-Feedback-Loop (bei visuellem Output)
- Tests ausfuehren
- Spec-Abgleich: Ist alles umgesetzt?
- Edge-Cases pruefen

### Ausgabe
- Validierungsergebnis (bestanden / Korrekturen noetig)
- Falls Korrekturen: Zurueck zu Phase 4

### Quality Gate
- [ ] Alle Akzeptanzkriterien aus Spec erfuellt
- [ ] Visuelles Ergebnis stimmt mit Prototyp ueberein (falls anwendbar)
- [ ] Keine Regressionen
- [ ] Mensch hat final abgenommen

### Rollen
| Aufgabe | Verantwortlich |
|---------|---------------|
| Tests ausfuehren | AI |
| Screenshots pruefen | Mensch + AI |
| Finale Abnahme | Mensch |

---

## Phase 6: Delivery

**Ziel:** Aenderung committen, dokumentieren, abschliessen.

### Eingabe
- Validierter Code
- Abgeschlossene Spec / Plan

### Aktivitaeten
- Commit auf main (mit aussagekraeftiger Message)
- Plan als finished markieren (falls Plan-basiert)
- CLAUDE.md aktualisieren (falls relevant)
- Dokumentation nachziehen (falls noetig)

### Ausgabe
- Commit(s) auf main
- Plan in `finished/` verschoben
- Aktuelle Dokumentation

### Quality Gate
- [ ] Commit ist auf main
- [ ] Plan-Status aktualisiert
- [ ] Keine offenen TODOs

### Rollen
| Aufgabe | Verantwortlich |
|---------|---------------|
| Commit erstellen | AI (nach Aufforderung) |
| Push-Entscheidung | Mensch |

---

## Wann welche Phase uebersprungen werden darf

| Szenario | Ueberspringbar |
|----------|---------------|
| Kleiner Bugfix (< 10 Zeilen) | Phase 2 (Spec) kann muendlich sein, Phase 3 (Prototyp) entfaellt |
| Rein technisches Refactoring | Phase 3 (Prototyp) entfaellt |
| Visuelles Feature (UI, Shader) | Keine Phase ueberspringbar |
| Architektur-Entscheidung | Phase 3 kann entfallen, aber ADR ist Pflicht |
| Exploration / Spike | Nur Phase 1 + 3, kein Production Code |

---

## Iteration

Der Lifecycle ist nicht streng linear. Rueckspruenge sind erlaubt:

- **Validation → Implementation**: Korrekturen noetig
- **Implementation → Specification**: Plan muss angepasst werden
- **UX-Prototype → Specification**: Prototyp zeigt dass Spec nicht stimmt
- **Specification → Discovery**: Neue Erkenntnisse aendern den Scope

Aber: **Vorwaerts nur mit Quality Gate.** Kein Sprung von Discovery zu Implementation.