# Kontrollfluss A — der WORKFLOW entscheidet

Deklarative Definition. Die Reihenfolge der Schritte ist **fixiert**; das Modell füllt nur
den Inhalt jedes Schritts, bestimmt aber **nicht**, was als Nächstes kommt.

```
owner:  workflow
stages: [ explore → plan → verify → apply ]    # feste Reihenfolge, im Ablauf verankert
model:  füllt nur den Inhalt je Stage          # entscheidet NICHT den nächsten Schritt
```

## Vorbereitetes Ergebnis (zwei Läufe)

```
Lauf 1:  explore → plan → verify → apply
Lauf 2:  explore → plan → verify → apply
─────────────────────────────────────────────
verify enthalten?   ja  (in jedem Lauf)
reproduzierbar?     ja  — Reihenfolge ist deklariert, nicht gewählt
```

> Der Trace ist bei **jedem** Lauf identisch → reproduzierbar und auditierbar. Das ist der
> Preis und der Gewinn von Determinismus: keine Überraschung, aber auch keine Anpassung.
