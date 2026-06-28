# Talk-Konzept: Architecting Agentic Workflows

> Strukturvorschlag für eine 45-minütige praktische Session (PowerPoint + Live-Demos)
> für **Software-Architekten**.
>
> **Wichtig — der Winkel:** Diese Session ist *kein* Walkthrough durch den 3-Step-Lifecycle
> des `chevp-ai-framework`. Sie ist ein **Meta-Talk**: *Wie konstruiert man so ein
> Agenten-Workflow-System — aus Architektursicht?* Das `chevp-ai-framework` dient als
> **Fallbeispiel**, an dem die Architektur-Entscheidungen sichtbar gemacht werden.
>
> **Roter Faden — die Leitfrage des ganzen Vortrags:**
> ## *Wer kontrolliert den Agenten?*
> Jede Folie ordnet sich dieser Frage unter. Aus einer Sammlung guter Architekturthemen
> wird so eine stringente Erzählung mit klarem Spannungsbogen.
>
> Vorbild für den Repo-/README-Aufbau:
> [patbaumgartner/talk-stop-prompting-start-planning-with-embabel](https://github.com/patbaumgartner/talk-stop-prompting-start-planning-with-embabel).

---

## Repo-Struktur (Embabel-Stil)

```
talk-architecting-agentic-workflows/
├── demos/
│   ├── 01-enforcement-contract/        # Regeln außerhalb des Modells erzwingen
│   ├── 02-verification-capsule/        # Verifikation als gekapselte Einheit (Markdown-Subagent)
│   └── 03-who-decides/                 # Orchestrierte Pipeline vs. model-driven
├── slides/
│   └── architecting-agentic-workflows.pdf
└── README.md
```

---

## Titel & Positionierung

**Architecting Agentic Workflows**
*Wer kontrolliert den Agenten?*

> **Jeder baut gerade Agenten. Kaum jemand architektiert sie.**
>
> **Agenten sind keine Bibliotheken.** Sie sind laufende Systeme mit eigenem Kontrollfluss.
> Deshalb verschiebt sich Architektur vom *Entwurf des Programms* zum *Entwurf des
> Handlungsspielraums*.

**Abstract (gekürzt).** LLM-Agenten sind keine Werkzeuge mehr, sondern eigenständige
Ausführungseinheiten mit eigenem Kontrollfluss, Zustand und Fehlermodellen. Architektur
bedeutet daher nicht mehr nur, Software zu entwerfen, sondern den Handlungsspielraum eines
nicht-deterministischen Executors zu definieren. Anhand des `chevp-ai-framework` zeigen wir,
welche Architekturentscheidungen robuste Agentensysteme ermöglichen — von Zustandsmodellen
über Enforcement bis zur bewussten Balance zwischen Determinismus und Autonomie.

- **Zielgruppe:** Software-Architekten & Tech Leads. Kein Tiefwissen über LLM-Internals nötig.
- **Format:** 45 Min, praktisch — 3 Live-Demos, jede mit einer Architekturfrage als Titel.

---

## Dramaturgie

Der spannendste Teil — *der Agent wird mechanisch gestoppt* — kommt bewusst **früh**
(Akt 2), nicht erst nach 25 Minuten. Der Bogen:

```
Hook & Leitfrage  →  Problem  →  Enforcement-Demo  →  Warum braucht man das?
        →  Die Architektur dahinter (Anatomie als Ablauf)  →  Die Kernentscheidung
        →  Governance als Querschnitt  →  Failure Modes  →  Checkliste
```

---

## Agenda (45 Min)

| Akt | Zeit | Inhalt | Leitfrage-Bezug |
|-----|------|--------|-----------------|
| 0 · Hook & These | 4 min | „Agenten sind keine Bibliotheken" + Leitfrage | Wer kontrolliert? |
| 1 · Das Problem | 4 min | Prompt-Ketten haben keinen Controller | Niemand kontrolliert |
| 2 · Der Moment der Kontrolle | 7 min | **Demo 1** zuerst — Agent wird geblockt | Wer darf stoppen? |
| 3 · Anatomie als Ablauf | 10 min | Intent → State → Orchestration → Execution → Verification (+ **Demo 2**) | Wer kontrolliert *was*? |
| 4 · Die Kernentscheidung | 7 min | Spektrum + **Control Surface** (+ **Demo 3**) | Wer entscheidet? |
| 5 · Governance als Querschnitt | 5 min | Schichtenmodell, Audit, Multi-Agent-Isolation | Wer kann es nachvollziehen? |
| 6 · Failure Modes | 4 min | Fehler → Folge | Wo bricht Kontrolle weg? |
| 7 · Takeaways | 4 min | Checkliste + eine Botschaft + Q&A | Wende es selbst an |

---

## Slide-Outline

### Akt 0 — Hook & These (4 min)
- **S1 · Titel** — „Architecting Agentic Workflows / Wer kontrolliert den Agenten?"
- **S2 · Der Bruch** — Diff-Screenshot: Agent hat 14 Dateien geändert und committed.
  Frage an den Raum: *„Wer hat diese Architektur-Entscheidung getroffen?"*
- **S3 · Die Kernthese (früh & aggressiv)** —
  > **Agenten sind keine Bibliotheken. Sie sind laufende Systeme mit eigenem Kontrollfluss.**
  > Architektur verschiebt sich vom Entwurf des *Programms* zum Entwurf des *Handlungsspielraums*.
- **S4 · Die Leitfrage** — Eine einzige Frage trägt den ganzen Vortrag:
  **„Wer kontrolliert den Agenten?"** — und jede folgende Folie beantwortet einen Teil davon.

### Akt 1 — Das Problem: niemand hält die Kontrolle (4 min)
- **S5 · Das Anti-Pattern** — „Prompt → Output → Prompt → Output". Kein Zustand, keine Gates,
  kein Audit — und vor allem: *kein Controller*. (Embabel-Parallele: *Stop Prompting*.)
- **S6 · Kontrast: Bibliothek vs. Agent** —

  | | Bibliothek | Agent |
  |---|---|---|
  | Aufruf | du rufst auf | er handelt selbst |
  | Verhalten | deterministisch | nicht-deterministisch |
  | Kontrolle | der Aufrufer | **offen — genau das Problem** |

### Akt 2 — Der Moment der Kontrolle (7 min) — *Enforcement zuerst*
- **S7 · Setup** — Wir springen sofort an die spannendste Stelle: Was passiert, wenn der
  Agent etwas tun *will*, das er nicht *darf*?
- **🖥️ Demo 1 — „Wie erzwingt man Regeln außerhalb des Modells?"** (3 min) —
  Ein deklarativer Kontrollpunkt blockt einen `Write`, solange kein freigegebener Plan
  existiert. Live: Agent will Code schreiben → Kontrollpunkt returnt *block* → Agent wird
  umgeleitet. *Fokus auf den Vertrag (Auslöser, Bedingung, Verdict) — die Implementierungs-
  sprache ist nebensächlich und austauschbar.*
- **S8 · Warum braucht man das?** — Prompt-Disziplin allein ist eine *Bitte*, kein *Vertrag*.

  | Ohne | Mit |
  |---|---|
  | Prompt | Contract |
  | Vertrauen | Erzwingen |
  | Empfehlung | Mechanik |

- **S9 · Die Architektur dahinter** — Enforcement liegt **außerhalb der Prompt-Schicht**.
  Das ist eine *Architektur*-Eigenschaft, kein Implementierungs-Detail — und die erste
  konkrete Antwort auf „Wer darf stoppen?": *das System, nicht das Modell*.

### Akt 3 — Anatomie als Ablauf (10 min)
> Keine „sechs Säulen", sondern **ein Ablauf**. Jede Station beantwortet eine Teil-Leitfrage.

- **S10 · Der Ablauf (ein Bild)** —
  ```
  Intent → State → Orchestration → Execution → Verification → Governance
    ↓        ↓          ↓              ↓             ↓             ↓
  erkennt  hält den  entscheidet   darf handeln  überprüft   macht nachvoll-
  Absicht  Ablauf    nächsten       / stoppen     Ergebnisse  ziehbar
                     Schritt
  ```
- **S11 · Intent** — *Wer erkennt, was zu tun ist?* Intent-Klassifikation als Eingang ins System.
- **S12 · State** — *Wer kontrolliert den Ablauf?* Modes als State Machine; wer den Zustand hält.
- **S13 · Orchestration** — *Wer entscheidet den nächsten Schritt?* — **kündigt die Kern-
  entscheidung aus Akt 4 an** (Workflow vs. Modell).
- **S14 · Execution** — *Wer darf handeln — und wer darf stoppen?* Gates + Human-in-the-Loop
  als typisierte Schnittstelle (chevp: nur 2 Interaktions-Primitive). Rückbezug auf Demo 1.
- **S15 · Verification** — *Wer überprüft Ergebnisse?* → direkt in die Demo.
- **🖥️ Demo 2 — „Wie kapselt man Verifikation?"** (3 min) — Ein in **Markdown** definierter
  Gatekeeper-Subagent prüft ein Artefakt und gibt ein **strukturiertes Verdict**
  (`pass | conditional | block` nach festem Schema) zurück statt Fließtext. Zeigt:
  Verifikation als komponierbare, testbare Einheit — *deklariert, nicht programmiert*.
  *(Governance — die sechste Station — bekommt in Akt 5 einen eigenen Querschnitt.)*

### Akt 4 — Die Kernentscheidung: Wer entscheidet? (7 min) — *der eigentliche Kern*
- **S16 · Die eine Frage** — Jede Architekturentscheidung im Agenten-System lässt sich
  zurückführen auf: **Wer entscheidet?**
  > der **Entwickler**? · der **Workflow**? · das **Modell**?
- **S17 · Das Spektrum** — Determinismus ↔ Autonomie. Links: skriptgesteuerte Pipeline
  (vorhersagbar, starr). Rechts: modellgetriebene Autonomie (flexibel, unvorhersehbar).
  Architektur = *bewusst* positionieren — **pro Teilschritt**, nicht global.
- **S18 · Die Control Surface — die zentrale Architekturentscheidung** —
  Auf dem Spektrum wird *eine Linie* gezogen: oberhalb entscheidet das Modell,
  unterhalb entscheidet die Mechanik. **Diese Linie *ist* die Architektur.**
  ```
                    Modell
                darf entscheiden
  ═════════════ Architekturgrenze ═════════════
                    Runtime
                    Policies
                    Contracts
                    Human
  ```
  > **Architektur besteht darin, die Grenze zwischen modellgetriebenen und
  > mechanisch kontrollierten Entscheidungen bewusst zu ziehen.**
  Rückbezug: Demo 1 (Enforcement) liegt *unter* der Linie — Demo 3 zeigt beide Seiten
  am selben Task.
- **S19 · Kontrast: Wer trifft welche Entscheidung?** —

  | Modell entscheidet | Workflow entscheidet |
  |---|---|
  | Exploration | Deployment |
  | Brainstorming | Merge |
  | Klassifikation | Delete |

- **🖥️ Demo 3 — „Wer trifft Entscheidungen?"** (3 min) — Derselbe Task zweimal: einmal als
  *orchestrierte* Stage-Pipeline (Workflow entscheidet), einmal *model-driven* (Modell
  entscheidet). Live: die deterministische Variante ist reproduzierbar, die andere driftet.

### Akt 5 — Governance als Querschnitt (5 min)
> Governance ist **kein Feature**, das man anhängt — sie liegt **quer über allem**.

- **S20 · Das Schichtenmodell** — Governance/Evidence/Audit ziehen sich durch jede Schicht:
  ```
  ┌──────────────────────────────────────────────┐
  │  Runtime                                       │
  │  Workflow                                      │  ◄─┐
  │  Execution                                     │    │ Governance
  ├──────────────────────────────────────────────┤    │ liegt quer:
  │  Evidence  ·  Audit  ·  Signed Decisions      │  ◄─┘ Spur in jeder Schicht
  └──────────────────────────────────────────────┘
  ```
  Architektur erzeugt die *Spur* (Evidence-Blöcke, signierte Entscheidungen, Out-of-scope →
  Proposal), nicht das Gewissen des Entwicklers. Leitfrage: *Wer kann Entscheidungen später
  nachvollziehen?*
- **S21 · Komposition & Layering** — `workflow → framework → domain → project`;
  Regel *tighten, never loosen*. Wie man Governance vererbbar macht.
- **S22 · Multi-Agent-Isolation** — *Ein Agent = ein Branch = ein Working Dir*.
  Nebenläufigkeitsmodell, Worktrees, Merge-Punkt als einziger Konfliktort.

### Akt 6 — Failure Modes (4 min)
- **S23 · Architekturfehler → Konsequenz** —

  | Fehler | Folge |
  |---|---|
  | Gates nur im Prompt | Agent schreibt trotzdem |
  | Kein Zustand | Endlosschleifen |
  | Kein Audit | nicht nachvollziehbar |
  | Gemeinsamer Workspace | Race Conditions |
  | Freitext-Verdicts | nicht automatisierbar |
  | Kein Kill-Kriterium | Sunk Cost, kein Ausstieg |

### Akt 7 — Takeaways & Q&A (4 min)
- **S24 · Die Architekten-Checkliste** — sechs Fragen, sofort auf die eigene Architektur anwendbar:
  1. **Welche Komponente besitzt den Zustand?**
  2. **Welche Entscheidungen sind explizit delegiert?**
  3. **Welche Regeln sind mechanisch erzwingbar?**
  4. **Welche Entscheidungen bleiben modellgetrieben?**
  5. **Wo entstehen Audit-Artefakte?**
  6. **Wie werden Agenten voneinander isoliert?**
- **S25 · Eine Botschaft** — Zurück zur Leitfrage:
  > „Architektur für Agenten heißt: **den Handlungsspielraum entwerfen — und Kontrolle
  > mechanisch erzwingen.** Wer das nicht entscheidet, hat es trotzdem entschieden — implizit."
- **S26 · Links / Repo / Kontakt** — `chevp-ai-framework`, Demos, Speaker-Bio (Embabel-Stil).

---

## Demos — jede mit einer Architekturfrage statt einer Nummer

| Demo | Architekturfrage | Zeigt | Dauer |
|---|---|---|---|
| 1 | **Wie erzwingt man Regeln außerhalb des Modells?** | Mechanisches Enforcement vs. Prompt-Bitte | 3 min |
| 2 | **Wie kapselt man Verifikation?** | Verifikation als komponierbare Einheit mit strukturiertem Verdict | 3 min |
| 3 | **Wer trifft Entscheidungen?** | Determinismus ↔ Autonomie, reproduzierbar | 3 min |

> Die Leute sollen sich an die *Fragestellung* erinnern, nicht an den Code.

---

## Key Takeaways

1. **Entwirf den Handlungsspielraum, nicht den Pfad** — ein Agent ist ein laufendes System mit eigenem Kontrollfluss; Architektur definiert seine Runtime und ihren Controller.
2. **Kontrolle ist die Leitfrage** — bei jeder Schicht: *wer kontrolliert hier?*
3. **Enforcement außerhalb des Modells** — Prompt-Disziplin ist eine Bitte, Mechanik ein Vertrag.
4. **Zieh die Control Surface bewusst** — die Grenze zwischen modellgetriebenen und
   mechanisch kontrollierten Entscheidungen *ist* die Architektur; positioniere jeden
   Teilschritt einzeln auf dem Determinismus ↔ Autonomie-Spektrum.
5. **Governance liegt quer** — Audit & Evidence sind Querschnitt, kein Add-on.

---

## Offene Punkte (vor Foliensatz zu klären)

1. **Demo-Tiefe** — Die 3 Demos sind bewusst *konzeptionell* (Gate-Vertrag, Markdown-Subagent,
   Orchestrierungs-Vergleich), nicht code-zentriert. Für 45 Min trotzdem ambitioniert;
   Alternative: vorbereitete Screencasts. Implementierungssprache nicht in den Vordergrund.
2. **Anatomie-Tempo** — fünf Stationen (Intent → Verification) in 10 Min ist dicht; ggf.
   Intent + State zu einer Folie zusammenziehen.
3. **Mapping zum chevp-ai-framework** — pro Station eine konkrete Mechanik aus dem Repo als
   Beleg, ohne Code-Abstieg (z. B. Modes in `LIFECYCLE.md`, `agents/gatekeeper-g1.md`,
   `guidelines/ask-user-question.md`).
