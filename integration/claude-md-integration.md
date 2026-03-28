# CLAUDE.md Integration

> Wie CLAUDE.md das Framework durchsetzt.

## Warum CLAUDE.md?

`CLAUDE.md` ist die Datei die Claude (AI) automatisch liest wenn sie ein Projekt oeffnet.
Sie ist das primaere Steuerungs-Instrument fuer AI-Verhalten in einem Projekt.

## Verbindlicher Verweis

Der wichtigste Block in jeder Projekt-CLAUDE.md:

```markdown
## Entwicklungsprozess

Dieses Projekt folgt dem [chevp-ai-framework](https://github.com/chevp/chevp-ai-framework) Lifecycle.

### Phasen (sequentiell, nicht ueberspringbar)
1. **Discovery** — Problem verstehen, Kontext sammeln
2. **Specification** — Plan/Spec erstellen, Freigabe einholen
3. **UX-Prototype** — Visuelles Feedback (Pflicht bei UI/Shader/Szenen)
4. **Implementation** — Production Code laut Plan
5. **Validation** — Build, Screenshot-Vergleich, Spec-Abgleich
6. **Delivery** — Commit, Doku nachziehen

### Regeln
- Kein Code ohne vorherige Spec (Phase 2)
- Kein Production Code ohne Prototyp-Bestaetigung (Phase 3, wo anwendbar)
- Kein Commit ohne Validation (Phase 5)
- Bei Unsicherheit: STOPP und fragen
```

## Hierarchie

```
chevp-ai-framework/CLAUDE.md     ← Framework-Regeln (generisch)
    ↓ wird referenziert von
<projekt>/CLAUDE.md               ← Projekt-Regeln (spezifisch)
    ↓ wird ergaenzt durch
<projekt>/context/guidelines/     ← Detail-Regeln
```

Das Projekt kann Framework-Regeln **verschaerfen** aber nicht **aufweichen**.

## Effektivitaet

CLAUDE.md wirkt weil:
1. Claude liest es automatisch bei jeder Konversation
2. Es steht im Repo und wird versioniert
3. Jeder AI-Agent (auch parallele) liest dieselben Regeln
4. Aenderungen am Prozess sind Git-Commits (reviewbar)