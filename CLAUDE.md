# CLAUDE.md — chevp-ai-framework

Dies ist ein Prozess-Framework fuer AI-gestuetzte Softwareentwicklung.
Es definiert den uebergeordneten Lifecycle, den Claude in allen Projekten einhalten muss.

## Kernregeln

1. **Phasen sind sequentiell** — Keine Phase darf uebersprungen werden
2. **Mensch entscheidet** — Bei jedem Phase-Uebergang muss der Mensch explizit bestaetigen
3. **Kontext vor Code** — AI schreibt keinen Production Code ohne vorherige Spec
4. **Prototyp vor Production** — UX-Prototypen validieren bevor implementiert wird (wo anwendbar)
5. **Ownership bleibt beim Menschen** — AI liefert Vorschlaege, Entwickler tragen Verantwortung

## Lifecycle-Phasen

```
1. Discovery → 2. Specification → 3. UX-Prototype → 4. Implementation → 5. Validation → 6. Delivery
```

Details: [process/LIFECYCLE.md](process/LIFECYCLE.md)

## Dokumentation

| Ordner | Inhalt |
|--------|--------|
| [process/](process/) | Lifecycle-Phasen und Uebergaenge |
| [artifacts/](artifacts/) | Templates fuer Plans, Specs, ADRs, CLAUDE.md |
| [guidelines/](guidelines/) | Qualitaetsregeln fuer AI-Zusammenarbeit |
| [integration/](integration/) | Wie man das Framework in Projekte einbindet |