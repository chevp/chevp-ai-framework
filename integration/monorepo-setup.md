# Monorepo Integration

> Wie du das Framework in ein bestehendes Monorepo einbindest.

## Empfohlene Verzeichnisstruktur

```
<projekt-root>/
├── CLAUDE.md                    ← Projekt-CLAUDE.md (verweist auf Framework)
├── context/
│   ├── README.md                ← Uebersicht ueber context/
│   ├── architecture/            ← Architektur-Dokumente
│   ├── adr/                     ← Architecture Decision Records
│   ├── guidelines/              ← Entwicklungsrichtlinien
│   ├── plans/                   ← Umsetzungsplaene
│   │   └── finished/            ← Abgeschlossene Plaene
│   ├── specs/                   ← Feature-Spezifikationen
│   └── workflows/               ← Wiederkehrende Ablaeufe
├── src/                         ← Production Code
└── ...
```

## Einrichtung

### 1. CLAUDE.md erstellen

Kopiere [claude-md-template.md](../artifacts/claude-md-template.md) als `CLAUDE.md` ins Projekt-Root.

### 2. context/ Ordner anlegen

```bash
mkdir -p context/{architecture,adr,guidelines,plans/finished,specs}
```

### 3. Framework-Verweis in CLAUDE.md

Fuege folgenden Block in deine Projekt-CLAUDE.md ein:

```markdown
## Entwicklungsprozess

Dieses Projekt folgt dem [chevp-ai-framework](https://github.com/chevp/chevp-ai-framework) Lifecycle.
Claude MUSS die Phasen-Reihenfolge einhalten:
1. Discovery → 2. Spec → 3. UX-Prototype → 4. Implementation → 5. Validation → 6. Delivery
```

### 4. Guidelines anpassen

Die Guidelines in `context/guidelines/` koennen projekt-spezifisch sein.
Generische Guidelines kommen aus dem Framework, spezifische bleiben im Projekt.

## Plan-Workflow

Plans folgen der Konvention aus dem Framework:

```
PLAN-NNN-<beschreibung>.md       ← Offen
finished/PLAN-FNNN-<beschreibung>.md  ← Abgeschlossen
```

Commit-Convention fuer Plan-Umsetzung:

```
plan(NNN): <kurze Beschreibung>
```