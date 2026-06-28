# Talk-Konzept: Architecting Agentic Workflows

> Strukturvorschlag für eine 45-minütige **Software-Architecture-Session**
> (PowerPoint + Live-Demos) für **Software-Architekten**.
>
> **Was diese Session *ist*:** ein Architektur-Workshop über die Frage, wie man
> nicht-deterministische Agenten-Systeme baut, kontrolliert und absichert.
>
> **Was diese Session *nicht* ist:** ein Walkthrough durch ein Framework. Das
> `chevp-ai-framework` ist **eine Fallstudie unter vielen möglichen** — es liefert
> sichtbare, anfassbare Belege für jede Architekturentscheidung. Es ist nie das Thema,
> immer nur die Illustration.
>
> **Roter Faden — die Leitfrage des ganzen Vortrags:**
> ## *Wer kontrolliert den Agenten?*
> Jede Folie beantwortet genau **einen Teil** dieser Frage.

---

## Titel & Positionierung

**Architecting Agentic Workflows**
*Wer kontrolliert den Agenten?*

> **Jeder baut gerade Agenten. Kaum jemand architektiert sie.**
>
> **Agenten sind keine Bibliotheken.** Sie sind laufende Systeme mit eigenem Kontrollfluss.
> Deshalb verschiebt sich Architektur vom *Entwurf des Programms* zum Entwurf des
> *Handlungsspielraums* — und der Kernfrage, **wer diesen Spielraum kontrolliert**.

**Abstract.** LLM-Agenten sind keine Werkzeuge mehr, sondern eigenständige
Ausführungseinheiten mit eigenem Kontrollfluss, Zustand und Fehlermodellen. Architektur
bedeutet daher nicht mehr nur, Software zu entwerfen, sondern den **Handlungsspielraum
eines nicht-deterministischen Executors** zu definieren und zu kontrollieren. Diese
Session arbeitet die wiederkehrenden Architekturentscheidungen heraus, die jedes robuste
Agenten-System treffen muss — von Enforcement über Zustandsmodelle bis zur bewussten
Balance zwischen Determinismus und Autonomie. Jede Entscheidung wird mit ihren
**Trade-offs und verworfenen Alternativen** gezeigt. Ein konkretes Framework dient als
durchgehende **Fallstudie**, an der die Entscheidungen sichtbar werden — die
Erkenntnisse gelten für **jedes** Agenten-System.

- **Zielgruppe:** Software-Architekten & Tech Leads. Kein Tiefwissen über LLM-Internals nötig.
- **Format:** 45 Min, praktisch — 3 Live-Demos, jede mit einer Architekturfrage als Titel.
- **Mitnehmen:** Eine Architekten-Checkliste, anwendbar auf das eigene System — unabhängig vom Tool.

---

## Dramaturgie

Der spannendste Moment — *der Agent wird mechanisch gestoppt* — kommt bewusst **früh**
(Akt 2). Der Bogen folgt einer Eskalation von Kontroll-Problemen:

```
Hook & Leitfrage
   →  PROBLEM: niemand kontrolliert
   →  PROBLEM: der Agent darf nicht, tut es trotzdem      → Demo 1 (Enforcement)
   →  PROBLEM: der Agent verliert den Faden / Endlosschleife → Zustandsmodell
   →  PROBLEM: wer entscheidet den nächsten Schritt?      → Control Surface + Demo 2
   →  PROBLEM: Verifikation ist Freitext                  → Demo 3 (strukturiertes Verdict)
   →  PROBLEM: niemand kann es nachvollziehen             → Governance quer
   →  PROBLEM: Agenten überschreiben sich                 → Isolation
   →  Failure Modes  →  Checkliste  →  eine Botschaft
```

Jeder Pfeil ist ein **Failure Mode**, der das Publikum abholt, *bevor* eine Lösung kommt.

---

## Agenda (45 Min)

| Akt | Zeit | Architekturproblem | Teil-Antwort auf „Wer kontrolliert?" |
|-----|------|--------|-----------------|
| 0 · Hook & These | 4 min | Wer hat *diese* Änderung entschieden? | Niemand hat es bewusst entschieden |
| 1 · Kein Controller | 4 min | Prompt-Ketten haben keinen Kontrollpunkt | Aktuell: niemand |
| 2 · Enforcement | 7 min | Wie erzwingt man Regeln in einem nicht-det. System? **(Demo 1)** | Das System, nicht das Modell |
| 3 · Zustand & Ablauf | 9 min | Wer hält den Zustand? Wie verhindert man Endlosschleifen? | Eine explizite State Machine |
| 4 · Die Kernentscheidung | 8 min | Wer entscheidet den nächsten Schritt? **(Demo 2 + Demo 3)** | Bewusst gezogene Control Surface |
| 5 · Governance quer | 5 min | Wie macht man Entscheidungen nachvollziehbar? | Eine Spur in jeder Schicht |
| 6 · Failure Modes | 4 min | Wo bricht Kontrolle weg? | Die Lücken benennen |
| 7 · Takeaways | 4 min | Wende es auf dein System an | Du — als Architekt |

> Hinweis zur Zeit: Akt 3 von 10→9 min gestrafft (Intent+State zu einer Station), die
> gewonnene Minute liegt in Akt 4, wo die *eigentliche* Architekturentscheidung sitzt.

---

## Slide-Outline

> Jede Akt-Einleitung startet mit einem **Problem-Statement in einer Zeile** (rot/fett auf
> der Folie). Die Framework-Mechanik kommt erst, wenn die Entscheidung und ihre Trade-offs
> stehen.

### Akt 0 — Hook & These (4 min)

- **S1 · Titel** — „Architecting Agentic Workflows / Wer kontrolliert den Agenten?"
- **S2 · Der Bruch (Problem)** — Diff-Screenshot: ein Agent hat 14 Dateien geändert und
  committed. Frage an den Raum: *„Wer hat diese Architektur-Entscheidung getroffen?"*
  → Niemand. Das Modell hat es getan, kein Mensch und kein Mechanismus hat es freigegeben.
- **S3 · Die Kernthese** —
  > **Agenten sind keine Bibliotheken. Sie sind laufende Systeme mit eigenem Kontrollfluss.**
  > Architektur verschiebt sich vom Entwurf des *Programms* zum Entwurf des
  > *Handlungsspielraums* — und zur Frage, **wer ihn kontrolliert.**
- **S4 · Die Leitfrage** — **„Wer kontrolliert den Agenten?"** Eine Frage, sieben
  Teil-Antworten — die Gliederung des ganzen Vortrags ist diese eine Frage, zerlegt.

### Akt 1 — Kein Controller (4 min)

- **S5 · Problem: Die Prompt-Kette hat keinen Kontrollpunkt** —
  „Prompt → Output → Prompt → Output". Kein Zustand, kein Gate, kein Audit — vor allem:
  *kein Controller*. Niemand kann eingreifen, weil es keine Stelle gibt, an der man eingreift.
- **S6 · Architekturentscheidung: Bibliothek vs. Agent unterscheiden** —

  | | Bibliothek | Agent |
  |---|---|---|
  | Aufruf | du rufst auf | er handelt selbst |
  | Verhalten | deterministisch | nicht-deterministisch |
  | Kontrolle | beim Aufrufer | **offen — genau das Problem** |

  > *Auch ohne dieses Repo gilt:* Sobald ein System selbst handelt, ist „Kontrolle" eine
  > **Architekturentscheidung**, kein Default. Triffst du sie nicht, hast du sie trotzdem
  > getroffen — zugunsten des Modells.

### Akt 2 — Enforcement: Regeln außerhalb des Modells (7 min)

- **S7 · Problem (Failure Mode):** *Der Agent verändert Dateien, obwohl er es nicht darf.*
  Prompt sagt „schreibe keinen Code ohne freigegebenen Plan" — der Agent tut es trotzdem.
  Warum? Weil ein Prompt eine **Bitte** ist, kein **Vertrag**.
- **S8 · Architekturentscheidung:** Enforcement liegt **außerhalb der Prompt-Schicht**.
  Eine Regel, die das Modell *brechen kann*, ist keine Regel. Der Mechanismus, der „nein"
  sagt, darf nicht im selben nicht-deterministischen Layer leben wie die Entscheidung,
  gegen die er schützt.
- **S9 · Trade-offs** —

  | Alternative | Warum verworfen | Preis unserer Lösung |
  |---|---|---|
  | Regeln nur im System-Prompt | Modell kann sie ignorieren | – |
  | Fine-Tuning auf Regeltreue | teuer, nie 100 %, nicht auditierbar | – |
  | Harter Mechanismus (Hook/Guard) | — gewählt — | weniger Flexibilität, mehr Reibung; man muss Ausnahmen *explizit* modellieren |

  > **Wann würde man anders entscheiden?** Bei reinen Read-/Explore-Agenten ohne
  > Seiteneffekte ist harter Enforcement Overkill — dann reicht Prompt-Disziplin.
- **🖥️ Demo 1 — „Wie erzwingt man Regeln außerhalb des Modells?"** (3 min) —
  Ein deklarativer Kontrollpunkt blockt einen `Write`, solange kein freigegebener Plan
  existiert. Live: Agent will Code schreiben → Kontrollpunkt returnt *block* → Agent wird
  umgeleitet. *Fokus auf den Vertrag — Auslöser, Bedingung, Verdict. Die
  Implementierungssprache ist nebensächlich und austauschbar.*
  > *Im Repo:* ein Pre-Tool-Hook + Gate-Contract. *Austauschbar mit:* LangGraph-Edge-Guard,
  > OpenAI-Tool-Gating, eigenem Middleware-Layer. **Die Architektur ist identisch.**

### Akt 3 — Zustand & Ablauf: Wer hält den Faden? (9 min)

> Keine „sechs Säulen", sondern **ein Kontrollfluss**. Jede Station beantwortet eine
> Teil-Leitfrage — und jede beginnt mit einem Failure Mode.

- **S10 · Der Ablauf (ein Bild)** —
  ```
  Intent → State → Orchestration → Execution → Verification → Governance
    ↓        ↓          ↓              ↓             ↓             ↓
  erkennt  hält den  entscheidet   darf handeln  überprüft   macht nachvoll-
  Absicht  Ablauf    nächsten       / stoppen     Ergebnisse  ziehbar
                     Schritt
  ```
  *Diese sechs Verantwortlichkeiten existieren in **jedem** Agenten-System — bewusst oder
  implizit. Architektur heißt, sie explizit zu machen und zuzuordnen.*

**Sektion STATE** — folgt dem Sechs-Schritt-Skelett:

- **S11a · 1 Praxisproblem** — *Failure Mode: der Agent vergisst, wo er steht, wiederholt
  Schritte und dreht sich im Kreis — eine Endlosschleife ohne Abbruch.*
- **S11b · 2 Warum existierende Ansätze scheitern** — der Zustand steckt implizit im
  Prompt-Verlauf / Kontextfenster. Das ist *unsichtbar* (niemand kann ihn auslesen),
  *unzuverlässig* (Kontext fällt aus dem Fenster) und *nicht unterbrechbar* (es gibt keinen
  definierten Punkt, an dem man pausiert).
- **S11c · 3 Architekturentscheidung** — *Wir haben entschieden, dass* der Ablauf einen
  **expliziten, externen Zustand** hält — eine State Machine mit wenigen, benannten Modi —
  der außerhalb des Modells lebt.
- **S11d · 4 Trade-offs** —

  | Alternative | Warum verworfen | |
  |---|---|---|
  | Impliziter Zustand im Kontextfenster | unsichtbar, fällt aus dem Fenster | |
  | Modell „merkt sich" den Fortschritt selbst | nicht inspizierbar, nicht reproduzierbar | |
  | Vollständige Workflow-Engine (BPMN o. ä.) | überschwer für Agenten-Granularität | |
  | **Gewählt: schlanke externe State Machine** | | — |

  **Nachteil der gewählten Lösung:** starrer als freie Modell-Navigation; jeder neue Modus
  muss explizit modelliert werden; das System kann nur Zustände annehmen, die man vorgesehen
  hat. **Wann anders?** Bei einem einzelnen, kurzlebigen Task ohne Wiederaufnahme ist eine
  State Machine Overhead — dann genügt ein linearer Lauf.
- **S11e · 5 Umsetzung im Repo** — wenige benannte Modi mit definierten Übergängen. *Im
  Repo:* eine Mode-State-Machine. *Austauschbar mit:* LangGraph-State, einer eigenen
  Enum + Reducer, einem Status-Feld in der DB.
  > *Auch ohne dieses Repo:* Wer den Zustand hält, kontrolliert den Ablauf. Hält ihn das
  > Modell, kontrolliert es sich selbst. (Diese Sektion hat **keine** Demo — Zustand zeigt
  > man im Diagramm, nicht live.)

- **S12 · Orchestration & Execution (Brücke, 1 Folie)** — zwei kurze Teil-Leitfragen, die
  in Akt 4 beantwortet werden: *Wer wählt den nächsten Schritt* (→ Control Surface) und
  *wer darf handeln / stoppen* (→ typisierte Human-Schnittstelle, Rückbezug auf Demo 1).
  Bewusst knapp — hier nur die Fragen aufmachen, nicht beantworten.

### Akt 4 — Die Kernentscheidung: Wer entscheidet? (8 min) — *der eigentliche Kern*

**Sektion CONTROL SURFACE** — Sechs-Schritt-Skelett:

- **S15 · 1 Praxisproblem + 2 Warum Ansätze scheitern** — *Failure Mode links:* die
  skriptgesteuerte Pipeline ist vorhersagbar, aber **blind** — sie scheitert an allem, was
  nicht vorgesehen war. *Failure Mode rechts:* die voll-autonome Schleife ist flexibel, aber
  **driftet** — derselbe Input, zwei Läufe, zwei Ergebnisse; nicht reproduzierbar, nicht
  freigabefähig. **Beide Extreme als globaler Default sind falsch.**
- **S16 · 3 Architekturentscheidung: Die Control Surface bewusst ziehen** —
  *Wir haben entschieden, dass* auf dem Determinismus↔Autonomie-Spektrum **pro Teilschritt
  eine Linie** gezogen wird: oberhalb entscheidet das Modell, unterhalb die Mechanik.
  **Diese Linie *ist* die Architektur** — nicht global, sondern pro Entscheidung.
  ```
                    Modell
                darf entscheiden
  ═════════════ Architekturgrenze ═════════════
                    Runtime
                    Policies
                    Contracts
                    Human
  ```
- **S17 · 4 Trade-offs & Heuristik** —

  | Alternative | Warum verworfen |
  |---|---|
  | Alles deterministisch skripten | starr, blind für Unerwartetes, tötet den Nutzen des Agenten |
  | Alles dem Modell überlassen | nicht reproduzierbar, nicht auditierbar, nicht freigabefähig |
  | Eine globale Linie für das ganze System | zu grob — derselbe Agent macht reversible *und* irreversible Schritte |
  | **Gewählt: Linie pro Teilschritt** | — |

  **Heuristik:** je *irreversibler* die Folge, desto weiter *unter* die Linie (Deployment,
  Merge, Delete, Geldausgabe → Mechanik; Exploration, Klassifikation, Entwürfe → Modell).
  **Nachteil der gewählten Lösung:** die Linie ist kein Einmal-Akt — sie muss *gepflegt*
  werden; falsch gezogen wird das System entweder gängelnd (zu viel Mechanik) oder
  unkontrollierbar (zu viel Modell). **Wann anders?** Reiner Wegwerf-Prototyp ohne
  irreversible Schritte → Linie ganz oben, alles dem Modell, ist vertretbar.
- **S18 · 5 Umsetzung im Repo** — pro Schritt deklariert, *wer* entscheidet. *Austauschbar
  mit:* jeder Orchestrierung, die deterministische und model-driven Stages mischt.
  > **Architektur besteht darin, die Grenze zwischen modellgetriebenen und mechanisch
  > kontrollierten Entscheidungen bewusst zu ziehen.** *Auch ohne dieses Repo gilt das.*
- **🖥️ 6 Demo 2 — „Wer trifft Entscheidungen?"** (3 min) — Derselbe Task zweimal: einmal als
  *orchestrierte* Stage-Pipeline (Workflow entscheidet), einmal *model-driven* (Modell
  entscheidet). Live: die deterministische Variante ist reproduzierbar, die andere driftet.
  Demo 1 lag *unter* der Linie — hier sieht man beide Seiten am selben Task.
  *(Diese Demo erscheint im Ablauf vor der Verifikations-Demo — daher Demo 2.)*

**Sektion VERIFICATION** — Sechs-Schritt-Skelett (kompakt, eine Folie + Demo):

- **S19 · 1–4 Problem → Entscheidung → Trade-offs** — *Failure Mode: der Verifier sagt
  „sieht gut aus" — eine Maschine kann damit nichts tun, kein Gate kann darauf schalten.*
  **Warum Ansätze scheitern:** Freitext-Reviews sind nicht maschinell verzweigbar.
  **Entscheidung:** Verifikation liefert ein **strukturiertes Verdict** nach festem Schema
  (`pass | conditional | block`), nicht Prosa — und wird so zur komponierbaren, testbaren
  Einheit.

  | Alternative | Warum verworfen |
  |---|---|
  | Freitext-Review | nicht maschinell auswertbar, nicht gate-fähig |
  | Reiner Boolean (pass/fail) | verliert die Zwischenstufe „mit Auflagen" |
  | **Gewählt: kleines Verdict-Schema** | — |

  **Nachteil der gewählten Lösung:** ein Schema verliert Nuance gegenüber Freitext und muss
  gepflegt werden. **Wann anders?** Reines Human-Review ohne nachgelagerte Automatik braucht
  kein Schema.
- **🖥️ S20 · 6 Demo 3 — „Wie kapselt man Verifikation?"** (2 min) — Ein **deklarierter**
  Gatekeeper-Subagent prüft ein Artefakt und gibt ein strukturiertes Verdict zurück statt
  Fließtext: Verifikation *deklariert, nicht programmiert*.
  > *Im Repo:* ein Markdown-Subagent. *Austauschbar mit:* jeder Funktion/jedem Tool, das ein
  > typisiertes Ergebnis liefert (JSON-Schema-Output, Pydantic-Modell, Enum). Das Prinzip —
  > *Verdict als Datenstruktur, nicht als Text* — bleibt.

### Akt 5 — Governance & Isolation als Querschnitt (5 min)

**Sektion GOVERNANCE** — Sechs-Schritt-Skelett:

- **S21 · 1 Praxisproblem + 2 Warum Ansätze scheitern** — *Failure Mode: drei Wochen
  später fragt jemand „warum hat der Agent das getan?" — und niemand kann es
  rekonstruieren.* Audit-Logging *nachträglich* anzuhängen scheitert, weil die
  Begründung (welche Evidenz, wer hat freigegeben) zum Zeitpunkt der Entscheidung schon
  verloren ist. Governance ist **kein Feature, das man anhängt**.
- **S22 · 3 Architekturentscheidung: Eine Spur in jeder Schicht** —
  ```
  ┌──────────────────────────────────────────────┐
  │  Runtime                                       │
  │  Workflow                                      │  ◄─┐
  │  Execution                                     │    │ Governance
  ├──────────────────────────────────────────────┤    │ liegt quer:
  │  Evidence  ·  Audit  ·  Signed Decisions      │  ◄─┘ Spur in jeder Schicht
  └──────────────────────────────────────────────┘
  ```
  *Wir haben entschieden, dass* jede Schicht ihre eigene *Spur* erzeugt (Evidenz, signierte
  Entscheidungen, Out-of-scope → Proposal) — die Architektur erzwingt die Spur, nicht das
  Gewissen des Entwicklers.
- **S23 · 4 Trade-offs** —

  | Alternative | Warum verworfen |
  |---|---|
  | Audit nachträglich aus Logs rekonstruieren | Begründung & Freigabe-Kontext sind dann weg |
  | Governance als separates Tool/Schicht obendrauf | umgehbar — Kernpfad kennt es nicht |
  | **Gewählt: Spur in jede Schicht eingebaut** | — |

  **Nachteil der gewählten Lösung:** durchgängige Spur = mehr Pflicht-Artefakte, mehr
  Reibung pro Schritt, höhere Einstiegshürde. **Wann anders?** Wegwerf-Prototypen und
  Spikes brauchen das nicht — dort ist die Reibung reiner Verlust.
- **S24 · 5 Umsetzung im Repo: Komposition & Layering** — `workflow → framework → domain →
  project`, Regel *tighten, never loosen*: Governance ist *vererbbar* und nur
  *verschärfbar*, nie aufweichbar. *Austauschbar mit:* jeder Policy-Vererbung (OPA-Layer,
  Config-Overlays). Diese Sektion hat **keine** Demo — Spuren zeigt man am Artefakt.
  > *Auch ohne dieses Repo:* Auditierbarkeit ist eine Eigenschaft der Architektur, nicht
  > der Disziplin. Was nicht eingebaut ist, entsteht nicht.

**Sektion ISOLATION** — Sechs-Schritt-Skelett (kompakt):

- **S25 · 1–4 Problem → Entscheidung → Trade-offs** — *Failure Mode: mehrere Agenten,
  ein Working Dir → sie überschreiben sich, Race Conditions.* **Warum Ansätze scheitern:**
  Locking/Mutex im gemeinsamen Verzeichnis serialisiert die Arbeit und tötet die
  Parallelität. **Entscheidung:** *Ein Agent = ein Branch = ein Working Dir* — Isolation
  als Nebenläufigkeitsmodell, der Merge-Punkt ist der **einzige** Konfliktort.

  | Alternative | Warum verworfen |
  |---|---|
  | Gemeinsames Working Dir + Locking | serialisiert, tötet Parallelität |
  | Optimistisch schreiben, Konflikte später lösen | korrupter Zwischenzustand, schwer testbar |
  | **Gewählt: Isolation pro Agent, Merge als einziger Treffpunkt** | — |

  **Nachteil der gewählten Lösung:** Setup-Kosten (Worktrees/Branches pro Agent),
  verzögerte Integration, der Merge kann groß werden. **Wann anders?** Einzelner Agent oder
  rein lesende Agenten brauchen keine Isolation.
- **S26 · 5 Umsetzung im Repo** — Worktree/Branch je Agent. *Austauschbar mit:* Containern,
  Sandboxes, getrennten Arbeitskopien. **Keine** Demo. *Prinzip:* Parallelität wird durch
  Isolation + einen definierten Merge-Punkt beherrschbar, nicht durch Sperren.

### Akt 6 — Failure Modes (4 min)

- **S27 · Architekturfehler → Konsequenz** — *jede Zeile = eine nicht getroffene Entscheidung* —

  | Fehler (Entscheidung ausgelassen) | Folge |
  |---|---|
  | Gates nur im Prompt | Agent schreibt trotzdem |
  | Kein expliziter Zustand | Endlosschleifen / Drift |
  | Kein Audit | nicht nachvollziehbar |
  | Gemeinsamer Workspace | Race Conditions |
  | Freitext-Verdicts | nicht automatisierbar |
  | Kein Kill-Kriterium | Sunk Cost, kein Ausstieg |
  | Control Surface nie gezogen | Modell entscheidet alles — implizit |

### Akt 7 — Takeaways & Q&A (4 min)

- **S28 · Die Architekten-Checkliste** — sieben Fragen, sofort auf das **eigene** System
  anwendbar (unabhängig vom Tool):
  1. **Welche Komponente besitzt den Zustand?**
  2. **Welche Entscheidungen sind explizit ans Modell delegiert — welche an die Mechanik?**
  3. **Welche Regeln sind mechanisch erzwingbar — und liegen sie außerhalb des Modells?**
  4. **Wo verläuft deine Control Surface — pro Teilschritt?**
  5. **Liefert deine Verifikation ein Verdict, das eine Maschine weiterverarbeiten kann?**
  6. **Wo entstehen Audit-Artefakte — automatisch oder gar nicht?**
  7. **Wie werden parallele Agenten voneinander isoliert?**
- **S29 · Eine Botschaft** —
  > „Architektur für Agenten heißt: **den Handlungsspielraum entwerfen — und Kontrolle
  > mechanisch erzwingen.** Wer die Control Surface nicht zieht, hat sie trotzdem gezogen —
  > zugunsten des Modells."
- **S30 · Links / Fallstudie / Kontakt** — die Fallstudie (`chevp-ai-framework`), Demos,
  Speaker-Bio. *Bewusst als letzte Folie* — das Repo ist Beleg, nicht Botschaft.

---

## Demos — jede mit einer Architekturfrage statt einer Nummer

| Demo | Architekturfrage | Architekturprinzip (frameworkunabhängig) | Im Repo | Dauer |
|---|---|---|---|---|
| 1 | **Wie erzwingt man Regeln außerhalb des Modells?** | Enforcement lebt nicht im nicht-det. Layer | Pre-Tool-Hook + Gate-Contract | 3 min |
| 2 | **Wer trifft Entscheidungen?** | Control Surface pro Teilschritt | Orchestrierte vs. model-driven Pipeline | 3 min |
| 3 | **Wie kapselt man Verifikation?** | Verdict als Datenstruktur, nicht als Text | Markdown-Gatekeeper-Subagent | 2 min |

> Die Leute sollen sich an die **Fragestellung** und das **Prinzip** erinnern, nicht an den
> Code oder den Framework-Namen. Jede Demo nennt explizit, womit die Repo-Mechanik
> *austauschbar* ist.

---

## Key Takeaways

1. **Entwirf den Handlungsspielraum, nicht den Pfad** — ein Agent ist ein laufendes System
   mit eigenem Kontrollfluss; Architektur definiert seine Runtime und ihren Controller.
2. **Kontrolle ist die Leitfrage** — bei jeder Schicht: *wer kontrolliert hier?*
3. **Enforcement außerhalb des Modells** — Prompt-Disziplin ist eine Bitte, Mechanik ein Vertrag.
4. **Zieh die Control Surface bewusst** — die Grenze zwischen modellgetriebenen und
   mechanisch kontrollierten Entscheidungen *ist* die Architektur; positioniere jeden
   Teilschritt einzeln auf dem Determinismus ↔ Autonomie-Spektrum.
5. **Verdict als Datenstruktur** — Verifikation muss maschinell weiterverarbeitbar sein.
6. **Governance liegt quer** — Audit & Evidence sind Querschnitt, kein Add-on.
7. **Jede Entscheidung hat einen Trade-off** — und das Auslassen einer Entscheidung *ist*
   eine Entscheidung.

---

# Anhang — Design-Notizen für den Foliensatz (nicht Teil des Vortrags)

> Alles ab hier ist **Bauanleitung für die Folien**, nicht Vortragsinhalt. Es gehört nicht
> auf eine Folie und wird nicht vorgetragen — es ist das Qualitätsgate, gegen das der
> Foliensatz oben geprüft wird.

## Regel 1 — Das Sektions-Skelett (jede Hauptsektion, identisch)

Jede der **sechs Architektur-Sektionen** (Enforcement · State · Control Surface ·
Verification · Governance · Isolation) folgt **exakt demselben** Sechs-Schritt-Muster.
Nach zehn Minuten weiß das Publikum intuitiv: *jetzt kommt wieder Problem → Entscheidung →
Demo.* Dieser Rhythmus macht den Vortrag ruhig und vorhersehbar.

```
  1 · PRAXISPROBLEM            ein realistischer Failure Mode, kein Feature
        ↓
  2 · WARUM ANSÄTZE SCHEITERN  was man naheliegend versucht — und warum es bricht
        ↓
  3 · ARCHITEKTURENTSCHEIDUNG  "Wir haben entschieden, dass …" (nicht "Wir haben X gebaut")
        ↓
  4 · TRADE-OFFS              Alternativen · warum verworfen · Nachteil · wann anders
        ↓
  5 · UMSETZUNG IM REPO       wie die Fallstudie das löst — eine Mechanik, kein Code-Abstieg
        ↓
  6 · DEMO                    nur bei den drei Kern-Sektionen — letzter Schritt, nie der erste
```

> Wenn die Antwort auf „Welche Architekturentscheidung wird hier getroffen?" lautet
> **„Wir haben X gebaut"** → Folie ist noch nicht architekturzentriert.
> Lautet sie **„Wir haben entschieden, dass …"** → Folie ist richtig.

Der **Trade-off-Block (Schritt 4)** ist auf jeder Sektion gleich aufgebaut — das ist der
Teil, der den Architekten vom Framework-Autor unterscheidet:

| Feld | Inhalt |
|---|---|
| **Alternativen** | 2–3 ernsthaft erwogene andere Ansätze |
| **Warum verworfen** | der konkrete Grund je Alternative |
| **Nachteil der gewählten Lösung** | was *unsere* Wahl kostet — ehrlich |
| **Wann anders entscheiden?** | die Bedingung, unter der die Alternative gewinnt |

## Regel 2 — Der Austauschbarkeitstest (die harte Nebenbedingung)

> **Stell dir vor, das Repository hieße anders oder wäre durch ein beliebiges anderes
> Agenten-Framework ersetzt. Verliert die Folie dann ihren Wert, ist sie zu
> framework-zentriert.**

Jede Aussage muss **frameworkunabhängig** formuliert sein, *bevor* die Fallstudie
genannt wird:

| ❌ framework-zentriert | ✅ architekturzentriert |
|---|---|
| „chevp besitzt Gate Contracts." | „Agentensysteme brauchen einen Mechanismus, der Regeln **außerhalb des Modells** erzwingt. — Im `chevp-ai-framework` heißt diese Mechanik *Gate Contract*; in LangGraph wäre es ein Edge-Guard, bei dir vielleicht ein Pre-Tool-Hook." |
| „Das Framework hat 3 Modes." | „Ein Agent braucht einen **expliziten Zustand**, sonst kann niemand seinen Ablauf kontrollieren. — Eine mögliche Umsetzung: eine State Machine mit wenigen Modi." |

Auf jeder Kern-Folie steht unten eine kleine **„Auch ohne dieses Repo gilt:"**-Zeile.
Das ist der sichtbare Beweis, dass die Architektur die Aussage trägt, nicht das Tool.

## Layout-Empfehlung je Folie (LibreOffice Impress)

**Legende — die 12 Auto-Layouts im Eigenschaften-Panel** (Position = Reihe/Spalte, vgl. Screenshot):

| Kürzel | Layout | Panel-Position |
|---|---|---|
| **Leer** | leere Folie | R1 · links |
| **Titelfolie** | Titel + Untertitel, zentriert | R1 · rechts |
| **Titel+Inhalt** | Titel + ein Inhaltsbereich | R2 · links |
| **Titel+2** | Titel + zwei Inhalte nebeneinander | R2 · rechts |
| **Nur Titel** | Titelzeile, Rest frei (für Vollbild/Screencast) | R3 · links |
| **Zentriert** | zentrierter Text, kein Inhaltsrahmen | R3 · rechts |
| **2-über-1** | Titel + zwei Inhalte oben, ein breiter unten | R5 · links |
| **1-über-1** | Titel + Inhalt oben, Inhalt unten | R5 · rechts |
| **4 Inhalte** | Titel + 2×2-Raster | R6 · links |
| **6 Inhalte** | Titel + 2×3-Raster | R6 · rechts |

**Pro-Folie-Empfehlung** (folgt der Inhaltsform, nicht umgekehrt):

| Folie | Inhaltsform | Layout | Panel |
|---|---|---|---|
| S1 · Titel | Titel + Untertitel | **Titelfolie** | R1 · rechts |
| S2 · Der Bruch | Diff-Screenshot groß + Frage | **Nur Titel** | R3 · links |
| S3 · Kernthese | großes Zitat | **Zentriert** | R3 · rechts |
| S4 · Leitfrage | eine Frage, formatfüllend | **Zentriert** | R3 · rechts |
| S5 · Anti-Pattern | ein Ketten-Diagramm | **Titel+Inhalt** | R2 · links |
| S6 · Bibliothek vs. Agent | Kontrast-Tabelle | **Titel+2** | R2 · rechts |
| S7 · Enforcement-Problem | Failure Mode + Text | **Titel+Inhalt** | R2 · links |
| S8 · Enforcement-Entscheidung | These + Begründung | **Titel+Inhalt** | R2 · links |
| S9 · Enforcement-Trade-offs | eine Tabelle | **Titel+Inhalt** | R2 · links |
| 🖥️ Demo 1 | Live-Screen | **Nur Titel** | R3 · links |
| S10 · Kontrollfluss-Bild | ein Diagramm | **Titel+Inhalt** | R2 · links |
| S11a–b · State Problem/Warum | Problem ‖ Warum scheitert | **Titel+2** | R2 · rechts |
| S11c–d · State Entscheidung/Trade-offs | Entscheidung oben, Tabelle | **2-über-1** | R5 · links |
| S11e · State Umsetzung | Mechanik + „auch ohne Repo" | **Titel+Inhalt** | R2 · links |
| S12 · Orchestration/Execution-Brücke | zwei kurze Fragen | **Zentriert** | R3 · rechts |
| S15 · Spektrum-Problem | links/rechts Gegenüberstellung | **Titel+2** | R2 · rechts |
| S16 · Control Surface | Linien-Diagramm | **Titel+Inhalt** | R2 · links |
| S17 · CS Trade-offs | Tabelle oben, Heuristik unten | **2-über-1** | R5 · links |
| S18 · CS Umsetzung | Mechanik + „auch ohne Repo" | **Titel+Inhalt** | R2 · links |
| 🖥️ Demo 2 | zwei Läufe nebeneinander | **Titel+2** | R2 · rechts |
| S19 · Verification | Problem/Warum oben, Trade-offs | **2-über-1** | R5 · links |
| 🖥️ Demo 3 | Live, strukturiertes Verdict | **Nur Titel** | R3 · links |
| S21 · Governance-Problem | Failure Mode + Text | **Titel+Inhalt** | R2 · links |
| S22 · Governance-Schichten | Schichten-Diagramm | **Titel+Inhalt** | R2 · links |
| S23 · Governance-Trade-offs | eine Tabelle | **Titel+Inhalt** | R2 · links |
| S24 · Layering | Kette + Regel | **Titel+Inhalt** | R2 · links |
| S25 · Isolation Problem/Trade-offs | Problem oben, Tabelle | **2-über-1** | R5 · links |
| S26 · Isolation Umsetzung | Mechanik + Prinzip | **Titel+Inhalt** | R2 · links |
| S27 · Failure Modes | große 2-Spalten-Tabelle | **Titel+Inhalt** | R2 · links |
| S28 · Checkliste | 7 nummerierte Fragen | **Titel+2** (2 Spalten) | R2 · rechts |
| S29 · Eine Botschaft | Schluss-Zitat | **Zentriert** | R3 · rechts |
| S30 · Links/Repo/Bio | Repo links, Kontakt rechts | **Titel+2** | R2 · rechts |

**Konsistenz-Hinweis (verbindet Layout mit Regel 1):** Die sechs Kern-Sektionen sind
bewusst auf **wenige** Layouts gelegt — `Titel+Inhalt` für Diagramm-/Tabellen-Folien,
`2-über-1` für den vollen Problem→Trade-off-Block, `Nur Titel` für jede Live-Demo. So
erkennt das Publikum das **Sektions-Skelett** auch *visuell* wieder: gleiche Form = gleicher
Schritt im immer gleichen Muster. *Variante für maximale Strenge:* alle sechs Kern-Sektionen
durchgängig auf **2-über-1** — dann ist jede Sektion physisch identisch aufgebaut.

## Wie die Fallstudie genutzt wird, ohne zum Mittelpunkt zu werden

Leitprinzip: **Prinzip zuerst, Repo als Beleg.** Konkret:

1. **Reihenfolge erzwingen.** Auf jeder Kern-Folie steht das Repo *unter* der
   Architekturentscheidung und ihren Trade-offs — nie darüber. Sprecher-Regel: das Wort
   „chevp" fällt erst, nachdem das Prinzip generisch formuliert wurde.
2. **Immer mit Alternativen nennen.** Jede Repo-Mechanik wird mit „austauschbar mit X, Y, Z"
   eingeführt (LangGraph, eigene Middleware, OpenAI-Tooling). Das Repo ist *ein* Punkt im
   Lösungsraum, nicht *der* Punkt.
3. **Repo nur in Demos zeigen, nie in Konzept-Folien.** Konzept-Folien sind framework-frei
   (Diagramme, Trade-off-Tabellen). Erst in der Live-Demo wird konkreter Code sichtbar —
   und auch dort liegt der Fokus auf dem *Vertrag*, nicht der Sprache.
4. **Die „Auch ohne dieses Repo gilt:"-Zeile.** Sie steht auf jeder Kern-Folie und ist der
   eingebaute Austauschbarkeitstest für das Publikum.
5. **Schluss-Folie, nicht Eröffnung.** Das Repo bekommt genau eine eigene Folie — die
   letzte (S30), als Beleg-Quelle für Interessierte.

---

## Wo der Entwurf noch zu framework-lastig wirken kann — und der Gegenzug

| Risiko-Stelle | Symptom | Gegenzug |
|---|---|---|
| S12 „typisierte Primitive" | klingt nach chevp-Feature | generisch formulieren: *„typisierte statt Freitext-Interaktion"*, chevp nur als Beispiel |
| Demo 3 „Markdown-Subagent" | Format wirkt framework-spezifisch | Prinzip betonen: *Verdict als Datenstruktur*; Markdown ist nur *eine* Deklarationsform |
| Mapping-Verweise auf Dateinamen | `LIFECYCLE.md`, `gatekeeper-g1.md` auf Folien | Dateinamen aus den Folien verbannen, nur in Sprecher-Notizen / Repo-README |
| „Control Surface" als Begriff | klingt wie ein Produktname | als *generisches Architekturkonzept* einführen, bevor das Repo es so nennt |
| S24 Layering-Kette | `workflow → framework → domain → project` ist chevp-Topologie | als *Beispiel* einer vererbbaren Governance zeigen, Prinzip = *tighten, never loosen* |

---

## Austauschbarkeitstest — Folien-Scorecard

> **Prüffrage je Folie:** *Ersetze „chevp-ai-framework" durch „LangGraph", „OpenAI Agents
> SDK" oder ein internes Framework — stimmt die Aussage weiterhin?*
>
> - **Ja** — die Aussage beschreibt ein allgemeines Architekturprinzip; das Repo ist nur Beispiel.
> - **Teilweise** — zu viele Implementierungsdetails; generisch umformulieren.
> - **Nein** — die Folie erklärt das Framework und muss neu strukturiert werden.
>
> Ziel: alle Konzept-Folien **Ja**, Demo-Folien dürfen **Teilweise** sein (sie *zeigen* ja
> konkret), aber nie **Nein**.

| Folie | Inhalt | Test | Was zu tun |
|---|---|---|---|
| S1–S4 | Hook, These, Leitfrage | **Ja** | frameworkfrei — so lassen |
| S5–S6 | Kein Controller / Bibliothek vs. Agent | **Ja** | — |
| S7–S8 | Enforcement: Problem + Entscheidung | **Ja** | — |
| S9 | Enforcement: Trade-offs | **Ja** | — |
| Demo 1 | Gate-Contract live | **Teilweise** | ok — „austauschbar mit"-Zeile macht es explizit |
| S10 | Kontrollfluss-Bild | **Ja** | sechs Verantwortlichkeiten gelten generisch |
| S11 | State (volles Skelett) | **Ja** | — |
| S12 | Orchestration/Execution-Brücke | **Ja** | — |
| S15–S17 | Control Surface + Trade-offs | **Ja** | Begriff generisch einführen, *dann* Repo |
| S18 | Control Surface: Umsetzung | **Teilweise** | „austauschbar mit"-Zeile zwingend |
| Demo 2 | orchestriert vs. model-driven | **Teilweise** | ok als Demo |
| S19 | Verification: Problem→Trade-offs | **Ja** | — |
| Demo 3 | strukturiertes Verdict | **Teilweise** → Risiko **Nein** | „Markdown-Subagent" tilgen; *Verdict als Datenstruktur* betonen |
| S21–S23 | Governance: Problem→Trade-offs | **Ja** | — |
| S24 | Layering `workflow→…→project` | **Teilweise** | als *Beispiel* einer Policy-Vererbung rahmen |
| S25–S26 | Isolation | **Ja** | „Worktree" als *eine* Option nennen |
| S27 | Failure Modes | **Ja** | — |
| S28–S29 | Checkliste, Botschaft | **Ja** | — |
| S30 | Repo / Links | **Nein — und das ist ok** | einzige bewusst framework-zentrierte Folie, ganz am Ende |

**Drei Folien mit Nachbesserungsbedarf** (Test = Teilweise mit Abrutsch-Risiko):
Demo 3 (Markdown), S18 (Control-Surface-Umsetzung), S24 (Layering-Topologie). Für alle drei
gilt derselbe Fix: **Prinzip generisch zuerst, Repo-Mechanik mit „austauschbar mit X, Y, Z"
zweitens.**

---

## Offene Punkte (vor Foliensatz zu klären)

1. **Demo-Tiefe.** Die 3 Demos sind bewusst **code-frei**: je ein deklaratives Artefakt
   (Gate-Vertrag, Flow-Definitionen, Schema + Markdown-Gatekeeper) plus ein vorbereitetes
   Ergebnis zum Zeigen/Screencast — keine ausführbaren Skripte. Das hält die Botschaft
   („schaut auf den Vertrag, nicht auf die Sprache") auch in den Demos konsequent.
2. **Anatomie-Tempo.** Akt 3 hält fünf Verantwortlichkeiten in 9 Min — Intent + State sind
   bereits zu einer Folie zusammengezogen. Bei Zeitdruck Orchestration (S12) als reine
   Brücke in 30 Sek. fahren.
3. **Repo als Fallstudie, nicht als Thema.** Pro Station max. *eine* konkrete Mechanik als
   Beleg, ohne Code-Abstieg. Der Austauschbarkeitstest (Regel 2) ist das stehende Gate:
   Wenn eine Folie ohne das Repo zusammenbricht, gehört sie überarbeitet.
```
