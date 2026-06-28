# Kontrollfluss B — das MODELL entscheidet

Deklarative Definition. Pro Iteration wählt das **Modell** selbst die nächste Aktion aus dem
Aktionsraum — der Workflow gibt die Reihenfolge **nicht** vor.

```
owner:   model
actions: { explore, plan, verify, rethink, apply }   # Modell wählt frei je Schritt
stop:    wenn das Modell 'apply' wählt               # es erklärt sich selbst für fertig
```

## Vorbereitetes Ergebnis (zwei Läufe)

```
Lauf 1:  explore → plan → verify → apply
Lauf 2:  explore → rethink → plan → apply          ← 'verify' übersprungen
─────────────────────────────────────────────
verify enthalten?   nicht garantiert  (Lauf 2: NEIN — Garantie verloren)
reproduzierbar?     nein  — anderer Trace bei jedem Lauf
```

> Der Trace **driftet** zwischen Läufen und kann `verify` überspringen. Genau das ist
> Autonomie ohne Leitplanken: flexibel, aber ohne reproduzierbare Garantie — fatal überall,
> wo das Ergebnis irreversibel ist (Deploy, Merge, Delete).
