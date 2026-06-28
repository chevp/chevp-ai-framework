# Folientexte — Architecting Agentic Workflows

> Kopierfertige Texte für den Foliensatz. Pro Folie: **Titel** + Stichpunkte zum direkten
> Einfügen. Keine Tabellen (schlecht einfügbar) — Kontraste und Trade-offs sind in
> Stichpunkte aufgelöst.
>
> *Kursive Zeilen* (Layout / 🗣 Notiz) sind **nicht** für die Folie — nur Hilfestellung.
> Volle Begründung, Trade-off-Logik und Scorecard stehen im Konzept:
> [architecting-agentic-workflows.md](architecting-agentic-workflows.md).

---

## S1 · Titel
*Layout: Titelfolie (R1 rechts)*

**Architecting Agentic Workflows**

Wer kontrolliert den Agenten?

---

## S2 · Der Bruch
*Layout: Nur Titel (R3 links) — Vollbild-Diff-Screenshot*

**Wer hat diese Architektur-Entscheidung getroffen?**

*🗣 Bild: Ein Agent hat 14 Dateien geändert und committed. Antwort: niemand hat es freigegeben — das Modell hat gehandelt, kein Mensch, kein Mechanismus.*

---

## S3 · Die Kernthese
*Layout: Zentrierter Text (R3 rechts)*

Agenten sind keine Bibliotheken.

Sie sind laufende Systeme mit eigenem Kontrollfluss.

Architektur verschiebt sich vom Entwurf des Programms zum Entwurf des Handlungsspielraums.

---

## S4 · Die Leitfrage
*Layout: Titel + Inhalt (R2 links) — Roadmap des Vortrags*

**Wer kontrolliert den Agenten?**

Eine Frage. Sieben Teil-Antworten — jede Folie beantwortet eine:

- Wer darf den Agenten stoppen? → Enforcement
- Wer hält den Zustand? → State
- Wer entscheidet den nächsten Schritt? → Control Surface
- Wer überprüft das Ergebnis? → Verification
- Wer kann Entscheidungen nachvollziehen? → Governance
- Wie bleiben parallele Agenten getrennt? → Isolation
- Wo bricht Kontrolle weg? → Failure Modes

---

## S5 · Kein Controller
*Layout: Titel + Inhalt (R2 links)*

**Die Prompt-Kette hat keinen Kontrollpunkt**

- Prompt → Output → Prompt → Output
- Kein Zustand
- Kein Gate
- Kein Audit
- Vor allem: kein Controller
- Niemand kann eingreifen — es gibt keine Stelle, an der man eingreift

---

## S6 · Bibliothek vs. Agent
*Layout: Titel + 2 Inhalte (R2 rechts) — linke Spalte / rechte Spalte*

**Bibliothek oder Agent?**

Bibliothek
- Du rufst auf
- Deterministisch
- Kontrolle beim Aufrufer

Agent
- Er handelt selbst
- Nicht-deterministisch
- Kontrolle offen — genau das Problem

- Beim Agenten ist „Kontrolle" eine Architekturentscheidung, kein Default
- Triffst du sie nicht, hast du sie trotzdem getroffen — zugunsten des Modells

---

## S7 · Enforcement — das Problem
*Layout: Titel + Inhalt (R2 links)*

**Der Agent tut, was er nicht darf**

- Der Prompt sagt: „kein Code ohne freigegebenen Plan"
- Der Agent schreibt trotzdem
- Ein Prompt ist eine Bitte — kein Vertrag

---

## S8 · Enforcement — die Entscheidung
*Layout: Titel + Inhalt (R2 links)*

**Regeln gehören außerhalb des Modells**

- Eine Regel, die das Modell brechen kann, ist keine Regel
- Der Mechanismus, der „nein" sagt, darf nicht im selben nicht-deterministischen Layer leben
- Enforcement liegt außerhalb der Prompt-Schicht

---

## S9 · Enforcement — Trade-offs
*Layout: Titel + Inhalt (R2 links)*

**Was kostet das?**

- Verworfen: Regeln nur im System-Prompt — das Modell kann sie ignorieren
- Verworfen: Fine-Tuning auf Regeltreue — teuer, nie 100 %, nicht auditierbar
- Gewählt: harter Mechanismus (Hook / Guard)
- Preis: weniger Flexibilität, mehr Reibung — Ausnahmen müssen explizit modelliert werden
- Anders entscheiden: reine Read-/Explore-Agenten ohne Seiteneffekte → Prompt-Disziplin reicht

---

## Demo 1 · Enforcement
*Layout: Nur Titel (R3 links) — Live-Screen*

**Demo · Wie erzwingt man Regeln außerhalb des Modells?**

- Agent will schreiben → Kontrollpunkt blockt → Agent wird umgeleitet
- Fokus: der Vertrag — Auslöser · Bedingung · Verdict
- Austauschbar mit: LangGraph-Edge-Guard, OpenAI-Tool-Gating, eigenem Middleware-Layer

---

## S10 · Der Kontrollfluss
*Layout: Titel + Inhalt (R2 links)*

**Ein Agent ist ein Kontrollfluss**

Intent → State → Orchestration → Execution → Verification → Governance

- Intent — erkennt die Absicht
- State — hält den Ablauf
- Orchestration — entscheidet den nächsten Schritt
- Execution — darf handeln / stoppen
- Verification — überprüft Ergebnisse
- Governance — macht nachvollziehbar

*🗣 Diese sechs Verantwortlichkeiten gibt es in jedem Agenten-System — bewusst oder implizit.*

---

## S11a · State — das Problem
*Layout: Titel + 2 Inhalte (R2 rechts)*

**Der Agent verliert den Faden**

Failure Mode
- Er vergisst, wo er steht
- Und dreht sich im Kreis

Warum es bricht
- Der Zustand steckt implizit im Prompt-Verlauf
- Unsichtbar — niemand kann ihn auslesen
- Unzuverlässig — Kontext fällt aus dem Fenster
- Nicht unterbrechbar — kein definierter Pausenpunkt

---

## S11b · State — Entscheidung & Trade-offs
*Layout: Titel, 2 Inhalte über Inhalt (R5 links)*

**Expliziter, externer Zustand**

- Entscheidung: eine State Machine mit wenigen, benannten Modi — außerhalb des Modells
- Verworfen: impliziter Kontext — unsichtbar, flüchtig
- Verworfen: Modell merkt sich den Fortschritt — nicht inspizierbar, nicht reproduzierbar
- Verworfen: volle Workflow-Engine (BPMN) — überschwer für Agenten-Granularität
- Preis: starrer; jeder Modus muss explizit modelliert werden
- Anders entscheiden: einzelner, kurzlebiger Task ohne Wiederaufnahme

---

## S11c · State — Umsetzung
*Layout: Titel + Inhalt (R2 links)*

**Wer den Zustand hält, kontrolliert den Ablauf**

- Wenige benannte Modi mit definierten Übergängen
- Austauschbar mit: LangGraph-State, Enum + Reducer, Status-Feld in der DB
- Auch ohne dieses Repo: hält das Modell den Zustand, kontrolliert es sich selbst

---

## S12 · Brücke
*Layout: Titel + Inhalt (R2 links)*

**Zwei offene Fragen — beantwortet in Akt 4**

- Wer wählt den nächsten Schritt? — der Workflow oder das Modell?
- Wer darf handeln, und wer darf stoppen? — die Mechanik oder der Mensch?

Beide Fragen führen zur selben Architekturentscheidung: der Control Surface.

---

## S15 · Control Surface — das Problem
*Layout: Titel + 2 Inhalte (R2 rechts)*

**Determinismus oder Autonomie — beides hat einen Preis**

Skriptgesteuerte Pipeline
- Vorhersagbar
- Aber blind für Unerwartetes

Modellgetriebene Autonomie
- Flexibel
- Aber driftet, nicht reproduzierbar

Beide Extreme als globaler Default sind falsch.

---

## S16 · Control Surface — die Entscheidung
*Layout: Titel + Inhalt (R2 links)*

**Die Control Surface bewusst ziehen**

Modell darf entscheiden
═══════ Architekturgrenze ═══════
Runtime · Policies · Contracts · Human

- Oberhalb der Linie entscheidet das Modell, unterhalb die Mechanik
- Die Linie wird pro Teilschritt gezogen, nicht global
- Diese Linie ist die Architektur

---

## S17 · Control Surface — Trade-offs
*Layout: Titel, 2 Inhalte über Inhalt (R5 links)*

**Wo zieht man die Linie?**

- Verworfen: alles deterministisch skripten — starr, tötet den Nutzen des Agenten
- Verworfen: alles dem Modell überlassen — nicht reproduzierbar, nicht freigabefähig
- Verworfen: eine globale Linie — zu grob
- Gewählt: Linie pro Teilschritt
- Heuristik: je irreversibler die Folge, desto weiter unter die Linie
- Modell entscheidet: Exploration, Klassifikation, Entwürfe
- Mechanik entscheidet: Deployment, Merge, Delete, Geldausgabe
- Preis: die Linie muss gepflegt werden — falsch gezogen = gängelnd oder unkontrollierbar

---

## S18 · Control Surface — Umsetzung
*Layout: Titel + Inhalt (R2 links)*

**Architektur ist, wo du die Grenze ziehst**

- Pro Schritt deklariert, wer entscheidet
- Austauschbar mit: jeder Orchestrierung, die deterministische und model-driven Stages mischt
- Auch ohne dieses Repo: wer die Grenze nicht zieht, hat sie zugunsten des Modells gezogen

---

## Demo 2 · Wer entscheidet
*Layout: Nur Titel (R3 links) — Live-Screen*

**Demo · Wer trifft Entscheidungen?**

- Derselbe Task zweimal: orchestriert (Workflow) vs. model-driven (Modell)
- Die deterministische Variante ist reproduzierbar — die andere driftet

---

## S19 · Verification
*Layout: Titel, 2 Inhalte über Inhalt (R5 links)*

**„Sieht gut aus" ist nicht automatisierbar**

- Failure Mode: der Verifier antwortet in Freitext — eine Maschine kann damit nichts tun
- Warum es bricht: Freitext ist nicht maschinell verzweigbar
- Entscheidung: strukturiertes Verdict nach festem Schema — pass / conditional / block
- Verworfen: Freitext-Review — nicht gate-fähig
- Verworfen: reiner Boolean (pass/fail) — verliert die Stufe „mit Auflagen"
- Preis: ein Schema verliert Nuance und muss gepflegt werden
- Anders entscheiden: reines Human-Review ohne nachgelagerte Automatik

---

## Demo 3 · Verifikation
*Layout: Nur Titel (R3 links) — Live-Screen*

**Demo · Wie kapselt man Verifikation?**

- Ein deklarierter Gatekeeper prüft ein Artefakt
- Ergebnis: strukturiertes Verdict statt Fließtext — deklariert, nicht programmiert
- Austauschbar mit: jedem Tool mit typisiertem Output (JSON-Schema, Pydantic, Enum)
- Prinzip: Verdict als Datenstruktur, nicht als Text

---

## S21 · Governance — das Problem
*Layout: Titel + Inhalt (R2 links)*

**„Warum hat der Agent das getan?"**

- Drei Wochen später fragt jemand — und niemand kann es rekonstruieren
- Audit nachträglich anhängen scheitert: die Begründung ist zum Entscheidungszeitpunkt schon verloren
- Governance ist kein Feature, das man anhängt

---

## S22 · Governance — die Entscheidung
*Layout: Titel + Inhalt (R2 links)*

**Eine Spur in jeder Schicht**

Runtime · Workflow · Execution
—— quer dazu ——
Evidence · Audit · Signed Decisions

- Jede Schicht erzeugt ihre eigene Spur: Evidenz, signierte Entscheidungen, Out-of-scope → Proposal
- Die Architektur erzwingt die Spur — nicht das Gewissen des Entwicklers

---

## S23 · Governance — Trade-offs
*Layout: Titel + Inhalt (R2 links)*

**Was kostet die Spur?**

- Verworfen: Audit nachträglich aus Logs — Begründung & Freigabe-Kontext sind dann weg
- Verworfen: Governance als separate Schicht obendrauf — umgehbar, der Kernpfad kennt es nicht
- Gewählt: Spur in jede Schicht eingebaut
- Preis: mehr Pflicht-Artefakte, mehr Reibung pro Schritt
- Anders entscheiden: Wegwerf-Prototypen und Spikes

---

## S24 · Layering
*Layout: Titel + Inhalt (R2 links)*

**Governance vererben — nur verschärfen**

Schichten: workflow → framework → domain → project

- Regel: tighten, never loosen
- Governance ist vererbbar und nur verschärfbar, nie aufweichbar
- Austauschbar mit: jeder Policy-Vererbung (OPA-Layer, Config-Overlays)
- Auch ohne dieses Repo: was nicht eingebaut ist, entsteht nicht

---

## S25 · Isolation
*Layout: Titel, 2 Inhalte über Inhalt (R5 links)*

**Zwei Agenten, ein Verzeichnis → Chaos**

- Failure Mode: mehrere Agenten teilen ein Working Dir — sie überschreiben sich, Race Conditions
- Warum es bricht: Locking serialisiert die Arbeit und tötet die Parallelität
- Entscheidung: ein Agent = ein Branch = ein Working Dir; der Merge-Punkt ist der einzige Konfliktort
- Verworfen: shared Dir + Locking — serialisiert
- Verworfen: optimistisch schreiben — korrupter Zwischenzustand
- Preis: Setup-Kosten, verzögerte Integration, großer Merge
- Anders entscheiden: einzelner oder rein lesender Agent

---

## S26 · Isolation — Umsetzung
*Layout: Titel + Inhalt (R2 links)*

**Parallelität durch Isolation, nicht durch Sperren**

- Worktree / Branch je Agent
- Austauschbar mit: Containern, Sandboxes, getrennten Arbeitskopien
- Beherrschbar wird Parallelität durch Isolation + einen definierten Merge-Punkt

---

## S27 · Failure Modes
*Layout: Titel + Inhalt (R2 links)*

**Wo Kontrolle wegbricht**

- Gates nur im Prompt → der Agent schreibt trotzdem
- Kein expliziter Zustand → Endlosschleifen / Drift
- Kein Audit → nicht nachvollziehbar
- Gemeinsamer Workspace → Race Conditions
- Freitext-Verdicts → nicht automatisierbar
- Kein Kill-Kriterium → Sunk Cost, kein Ausstieg
- Control Surface nie gezogen → das Modell entscheidet alles, implizit

*🗣 Jede Zeile = eine nicht getroffene Entscheidung.*

---

## S28 · Die Architekten-Checkliste
*Layout: Titel + 2 Inhalte (R2 rechts)*

**Sieben Fragen an deine Architektur**

1. Welche Komponente besitzt den Zustand?
2. Welche Entscheidungen sind ans Modell delegiert — welche an die Mechanik?
3. Welche Regeln sind mechanisch erzwingbar — und liegen sie außerhalb des Modells?
4. Wo verläuft deine Control Surface — pro Teilschritt?
5. Liefert deine Verifikation ein maschinenlesbares Verdict?
6. Wo entstehen Audit-Artefakte — automatisch oder gar nicht?
7. Wie werden parallele Agenten isoliert?

---

## S29 · Eine Botschaft
*Layout: Zentrierter Text (R3 rechts)*

Architektur für Agenten heißt: den Handlungsspielraum entwerfen — und Kontrolle mechanisch erzwingen.

Wer die Control Surface nicht zieht, hat sie trotzdem gezogen — zugunsten des Modells.

---

## S30 · Fallstudie & Kontakt
*Layout: Titel + 2 Inhalte (R2 rechts)*

**Fallstudie & Kontakt**

Fallstudie
- chevp-ai-framework
- Demos: 01-enforcement-contract · 02-who-decides · 03-verification-capsule

Kontakt
- [Name / Speaker-Bio]
- [Repo-Link · E-Mail]
