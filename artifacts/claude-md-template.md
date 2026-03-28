# CLAUDE.md Template

> Kopiere diese Vorlage als `CLAUDE.md` in dein Projekt-Root und passe sie an.

```markdown
# CLAUDE.md — <Projektname>

## Entwicklungsprozess

Dieses Projekt folgt dem [chevp-ai-framework](https://github.com/chevp/chevp-ai-framework) Lifecycle.
Claude MUSS die Phasen-Reihenfolge einhalten:
1. Discovery → 2. Spec → 3. UX-Prototype → 4. Implementation → 5. Validation → 6. Delivery

Kein Code ohne vorherige Spec. Kein Production Code ohne vorherigen UX-Prototyp (wo anwendbar).

## Was ist dieses Projekt?

<1-3 Saetze: Was macht das Projekt, fuer wen, warum>

## Architektur

<Grobe Architektur, wichtigste Entscheidungen>

## Dokumentation

| Ordner | Inhalt |
|--------|--------|
| context/plans/ | Umsetzungsplaene |
| context/adr/ | Architecture Decision Records |
| context/guidelines/ | Entwicklungsrichtlinien |

## Build Commands

<Wie baut man das Projekt>

## Konventionen

<Projekt-spezifische Regeln die AI einhalten muss>
```