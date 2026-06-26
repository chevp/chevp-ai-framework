# Talk-Konzept: Architecting Agentic Workflows

> Strukturvorschlag für eine 45-minütige praktische Session (PowerPoint + Live-Demos)
> für **Software-Architekten**.
>
> **Wichtig — der Winkel:** Diese Session ist *kein* Walkthrough durch den 3-Step-Lifecycle
> des `chevp-ai-framework`. Sie ist ein **Meta-Talk**: *Wie konstruiert man so ein
> Agenten-Workflow-System — aus Architektursicht?* Das `chevp-ai-framework` dient als
> **Fallbeispiel**, an dem die Architektur-Entscheidungen sichtbar gemacht werden.
>
> Vorbild für den Repo-/README-Aufbau:
> [patbaumgartner/talk-stop-prompting-start-planning-with-embabel](https://github.com/patbaumgartner/talk-stop-prompting-start-planning-with-embabel)
> (Titel mit Antithese → Abstract → Kernkonzept → Value Prop → `demos/`-Ordner → Speaker-Bio).

---

## Repo-Struktur (Embabel-Stil)

```
talk-architecting-agentic-workflows/
├── demos/
│   ├── 01-hook-as-gate/                # Python-Hook, der einen Write blockt
│   ├── 02-gatekeeper-subagent/         # Subagent mit strukturiertem Verdict
│   └── 03-deterministic-orchestration/ # Script-Pipeline vs. model-driven
├── slides/
│   └── architecting-agentic-workflows.pdf
└── README.md
```

---

## Titel & Positionierung

**Architecting Agentic Workflows**
*Nicht* was *der Agent tut — sondern* worin *er es tut.*

> **Jeder baut gerade Agenten. Kaum jemand architektiert sie.**
> Diese Session zeigt an einem realen Framework, welche Architektur-Entscheidungen
> ein Agenten-System tragen — und welche es zum Einsturz bringen.

**Abstract.** Ein LLM-Agent, der schreiben, löschen und committen darf, ist kein Feature —
er ist ein neues Architektur-Subjekt mit eigenem Kontrollfluss, Zustand und Fehlermodellen.
Software-Architekten entwerfen nicht mehr nur das System, sondern die *Leitplanken*, in denen
ein nicht-deterministischer Executor arbeitet. Anhand des `chevp-ai-framework` zerlegen wir
ein laufendes Agenten-Workflow-System in seine Bausteine: Zustandsmaschine,
Enforcement-Schichten, spezialisierte Subagenten, Human-in-the-Loop als typisierte
Schnittstelle — und die zentrale Entscheidung jedes Agenten-Systems: *deterministische
Orchestrierung vs. modellgetriebene Autonomie*.

- **Zielgruppe:** Software-Architekten & Tech Leads. Kein Tiefwissen über LLM-Internals nötig.
- **Format:** 45 Min, praktisch — 3 Live-Demos, baubar nachzuvollziehen.

---

## Agenda (45 Min)

| Akt | Zeit | Inhalt | Modus |
|-----|------|--------|-------|
| 0 · Hook | 3 min | „Der Agent ist ein Architektur-Subjekt" | Slides |
| 1 · Das Problem | 5 min | Warum Prompt-Ketten als Architektur scheitern | Slides |
| 2 · Anatomie | 8 min | Die 6 Bausteine eines Agenten-Workflows | Slides + Diagramm |
| 3 · Die Kernentscheidung | 6 min | Determinismus ↔ Autonomie als Spektrum | Slides + **Demo 3** |
| 4 · Enforcement | 7 min | Zwei Schichten: AI-Disziplin + mechanisch | **Demo 1 + Demo 2** |
| 5 · Querschnitt | 7 min | Governance, Komposition, Multi-Agent-Isolation | Slides |
| 6 · Failure Modes | 5 min | Der „Challenger" auf die eigene Architektur angewandt | Slides |
| 7 · Takeaways | 4 min | Architekten-Checkliste + Q&A | Slides |

---

## Slide-Outline

### Akt 0 — Hook (3 min)
- **S1 · Titel** — „Architecting Agentic Workflows / Nicht *was*, sondern *worin*".
- **S2 · Der Bruch** — Diff-Screenshot: Agent hat 14 Dateien geändert und committed.
  Frage an den Raum: *„Wer hat diese Architektur-Entscheidung getroffen?"*
- **S3 · These** — Der Agent ist kein Tool mehr, sondern ein **nicht-deterministischer
  Executor mit Schreibrechten**. Architektur heißt jetzt: den Möglichkeitsraum entwerfen,
  nicht den Pfad.

### Akt 1 — Warum Prompt-Ketten keine Architektur sind (5 min)
- **S4 · Das Anti-Pattern** — „Prompt → Output → Prompt → Output". Kein Zustand,
  keine Gates, kein Audit. (Embabel-Parallele: *Stop Prompting*.)
- **S5 · Die 4 fehlenden Eigenschaften** — Determinismus an den richtigen Stellen ·
  Erzwingbarkeit · Auditierbarkeit · Komponierbarkeit.
- **S6 · Reframe** — Von „besseren Prompts" zu **System-Design**: Kontrollfluss, Zustand,
  Schnittstellen, Fehlermodelle. Das ist Architektenarbeit.

### Akt 2 — Anatomie eines Agenten-Workflows (8 min)
- **S7 · Das Schichtenbild** — *Source of Truth* (deklarativ, portabel) **vs.**
  *Execution Layer* (callable, erzwingend). Die wichtigste Entscheidung des ganzen Systems.
  → am `chevp`-Beispiel: Markdown = Wahrheit, Plugin (commands/agents/skills/hooks) = additive Oberfläche.
- **S8 · Baustein 1 — Zustand & Kontrollfluss** — Modes als State Machine;
  Intent-Klassifikation als Transitionsfunktion; *wer* hält den Zustand.
- **S9 · Baustein 2 — Gates / Kontrollpunkte** — Enforcement-Punkte im Fluss,
  nicht am Ende. Forward only.
- **S10 · Baustein 3 — Spezialisierte Subagenten** — isolierter Kontext,
  *single responsibility*, **strukturierte Verdicts** statt Prosa (`pass | conditional | block`).
- **S11 · Baustein 4 — Callable Surface** — Commands / Skills / Tools als typisierte
  Eingänge ins System.
- **S12 · Baustein 5 — Human-in-the-Loop als typisierte Schnittstelle** —
  Interaktionsfläche *bewusst verengen* (chevp: nur 2 Primitive — Clickable Question + Draft-Confirm).
- **S13 · Baustein 6 — Enforcement-Schichten** — AI-Disziplin (Prompt/Markdown) **+**
  mechanisch (Hooks). Defense in depth.
- **S14 · Das Gesamtdiagramm** — die 6 Bausteine als ein Bild (Karte, auf die wir den
  Rest referenzieren).

### Akt 3 — Die Kernentscheidung: Determinismus ↔ Autonomie (6 min)
- **S15 · Das Spektrum** — Links: skriptgesteuerte Pipeline (vorhersagbar, starr).
  Rechts: modellgetriebene Autonomie (flexibel, unvorhersehbar). Architektur = *bewusst*
  auf diesem Spektrum positionieren — pro Teilschritt.
- **S16 · Heuristik** — Deterministisch orchestrieren bei: Fan-out, Schleifen, Verifikation,
  irreversiblen Schritten. Modell entscheiden lassen bei: Exploration, Klassifikation, Synthese.
- **🖥️ Demo 3 (3 min)** — Derselbe Task, zwei Mal: einmal als *script-orchestrierte*
  Stage-Pipeline, einmal *model-driven*. Live zeigen, wie die deterministische Variante
  reproduzierbar ist und die andere driftet.

### Akt 4 — Enforcement live (7 min) — *praktischer Kern*
- **S17 · Warum zwei Schichten** — Prompt-Disziplin allein ist eine Bitte, kein Vertrag.
  Mechanisches Enforcement macht die Regel unausweichlich.
- **🖥️ Demo 1 (3 min) — Der Gate-Hook** — Ein ~20-Zeilen-Python-Hook (`gate-check.py`-Stil),
  der einen `Write` blockt, solange kein freigegebener Plan existiert. Live: Agent will Code
  schreiben → Hook returnt *block* → Agent wird umgeleitet.
- **🖥️ Demo 2 (4 min) — Der Gatekeeper-Subagent** — Ein Subagent, der ein Artefakt prüft
  und ein **strukturiertes Verdict** (JSON-Schema) zurückgibt statt Fließtext.
  Zeigt: Verifikation als komponierbare, testbare Einheit.
- **S18 · Lektion** — Erzwingbarkeit ist eine *Architektur*-Eigenschaft, kein Prompt-Detail.

### Akt 5 — Querschnittsbelange (7 min)
- **S19 · Governance & Auditierbarkeit by design** — Evidence-Blöcke, signierte
  Entscheidungen, Out-of-scope → Proposal (nichts verschwindet in Prosa). Architektur erzeugt
  die Spur, nicht das Gewissen des Entwicklers.
- **S20 · Komposition & Layering** — `workflow → framework → domain → project`;
  Regel *tighten, never loosen*; Extension Points. Wie man ein Agenten-System vererbbar macht.
- **S21 · Multi-Agent-Isolation** — *Ein Agent = ein Branch = ein Working Dir*.
  Nebenläufigkeitsmodell, Worktrees, Merge-Punkt als einziger Konfliktort.
- **S22 · Kontext als knappe Ressource** — Subagenten als Kontext-Isolation;
  warum „alles in einen Prompt" ein Architektur-Smell ist.

### Akt 6 — Failure Modes (5 min)
- **S23 · Der Challenger auf die Architektur** — Top-Fehlermodi solcher Systeme:
  *Enforcement nur im Prompt* · *kein Kill-Kriterium (sunk cost)* · *Gates als Rubber-Stamp* ·
  *stiller Mode-Wechsel* · *ungetestete Subagenten-Verdicts*.
- **S24 · Smell-Test** — 5 Fragen, an denen man ein nicht-architektiertes Agenten-System erkennt.

### Akt 7 — Takeaways & Q&A (4 min)
- **S25 · Architekten-Checkliste** — 6 Fragen, die du an *jedes* Agenten-Workflow-Design
  stellst (eine pro Baustein).
- **S26 · Eine Botschaft** — „Architektur für Agenten heißt: den Möglichkeitsraum
  entwerfen — und ihn mechanisch erzwingen."
- **S27 · Links / Repo / Kontakt** — `chevp-ai-framework`, Demos, Speaker-Bio (Embabel-Stil).

---

## Demos (im `demos/`-Ordner, lauffähig)

| # | Titel | Zeigt architektonisch | Dauer |
|---|-------|------------------------|-------|
| 1 | Hook-as-Gate | Mechanisches Enforcement vs. Prompt-Bitte | 3 min |
| 2 | Gatekeeper-Subagent | Verifikation als komponierbare Einheit mit strukturiertem Output | 4 min |
| 3 | Deterministic Orchestration | Determinismus↔Autonomie-Spektrum, reproduzierbar | 3 min |

---

## Key Takeaways

1. Der Agent ist ein **Architektur-Subjekt**, kein Tool — entwirf seinen Möglichkeitsraum.
2. Trenne **Source of Truth** (deklarativ) von **Execution Layer** (erzwingend).
3. Enforcement braucht **zwei Schichten** — Prompt-Disziplin *und* Mechanik.
4. Positioniere jeden Teilschritt **bewusst** auf dem Determinismus↔Autonomie-Spektrum.
5. **Governance & Isolation** sind Querschnittsbelange, keine Add-ons.

---

## Offene Punkte (vor Foliensatz zu klären)

1. **Demo-Tiefe** — Live-Coding der 3 Mini-Artefakte (Python-Hook, Subagent-Schema,
   Pipeline-Script) ist für 45 Min ambitioniert. Alternative: vorbereitete Screencasts.
2. **Bausteine-Anzahl** — 6 Bausteine in 8 Min ist dicht; ggf. auf 4 Kern-Bausteine
   reduzieren und 2 als „weitere Belange" streifen.
3. **Mapping zum chevp-ai-framework** — pro Baustein eine konkrete Datei/Mechanik aus dem
   Repo als Beleg zeigen (z. B. `hooks/gate-check.py`, `agents/gatekeeper-g1.md`,
   `LIFECYCLE.md`-Modes, `guidelines/ask-user-question.md`).
