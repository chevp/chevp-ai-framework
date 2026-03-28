# Phase 6: Delivery

> Sauber abschliessen.

## Wann

Nachdem Validation bestanden und Mensch abgenommen hat.

## Aktivitaeten

### 1. Commit

```bash
git add <geaenderte-dateien>    # Nur spezifische Dateien, NICHT git add .
git commit -m "<typ>(<scope>): <beschreibung>

<was und warum>"
```

**Commit-Regeln:**
- Direkt auf main (keine Feature-Branches fuer Plans, ausser explizit gewuenscht)
- Aussagekraeftige Messages (was UND warum)
- Nur geaenderte Dateien stagen
- Build muss erfolgreich sein

### 2. Plan abschliessen (falls Plan-basiert)

```bash
mv context/plans/PLAN-NNN-<name>.md context/plans/finished/PLAN-FNNN-<name>.md
```

### 3. Dokumentation nachziehen

- CLAUDE.md aktualisieren falls sich Projekt-Kontext geaendert hat
- ADR schreiben falls Architektur-Entscheidung getroffen wurde

## AI-Verhalten

### MUSS
- Auf explizite Commit-Aufforderung warten
- Spezifische Dateien stagen (nicht `git add .`)
- Aussagekraeftige Commit-Message schreiben

### DARF NICHT
- Ohne Aufforderung committen
- Ohne Aufforderung pushen
- Force-Push ausfuehren
- Git Hooks ueberspringen (--no-verify)

## Quality Gate

- [ ] Commit ist auf main
- [ ] Plan-Status aktualisiert (falls Plan-basiert)
- [ ] Dokumentation aktuell
- [ ] Keine offenen TODOs