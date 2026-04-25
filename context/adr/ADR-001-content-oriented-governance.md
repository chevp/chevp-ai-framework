---
id: ADR-001
type: ADR
status: accepted
proposed-by: ai
decided-by: human
approved-by: chevp
approved-at: 2026-04-25
supersedes: —
date: 2026-04-25
---

# ADR-001: Content-oriented Architecture Governance via executable invariants and code-base drift detection

## Status

Accepted

(Status mirrors frontmatter. Frontmatter is source of truth — see [guidelines/architecture-governance.md](../../guidelines/architecture-governance.md).)

## Context

Der bestehende Governance-Stack des Frameworks (Provenance-Frontmatter, `evidence:`-Block, `governance-log.md`, Gatekeeper-Subagents, `provenance-check.py`) prüft fast ausschliesslich das **Verfahren**: Wer hat vorgeschlagen, wer entschieden, lag Evidenz vor, ist die Statussequenz korrekt. Das ist notwendig, aber nicht hinreichend.

Was fehlt, ist die Prüfung der **Substanz** über Zeit:

1. **ADR↔Code-Drift**: Eine ADR kann `accepted` sein und der Code sie trotzdem verletzen (z. B. ADR "Postgres als Primärspeicher" — aber `sqlite3`-Imports tauchen wieder auf).
2. **Undokumentierte Architektur**: Im Code entstehen wiederkehrende Patterns, ohne dass eine ADR sie deckt — implizite Entscheidungen, die nie ein Gate passiert haben.
3. **Tote ADRs**: Eine ADR referenziert eine Library / einen Pfad, der längst entfernt wurde, bleibt aber `accepted` und verzerrt die Governance-Sicht.
4. **Plan↔Implementation-Divergenz**: Ein EXP-Plan wurde mit Scope X approved, gemergt wurde Y. Das Provenance-Log meldet nichts, weil das Verfahren formal eingehalten wurde.

[agents/architecture-reviewer.md](../../agents/architecture-reviewer.md) verweist bereits auf `context/guidelines/architecture-invariants.md`, aber dieses Dokument existiert weder als Template noch als ausführbare Spezifikation. Damit bleibt die Invariantenbasis konzeptuell — ohne maschinell prüfbare Regeln kann auch ein Reviewer-Agent nur freitexten.

### Spannung: process-driven vs. spec-driven

Das Framework definiert sich explizit als *process-driven, not spec-driven* (CLAUDE.md): "der Spec emerges as an artifact within the Context step." Ein verpflichtendes ausführbares `architecture-invariants.md` zieht das Pendel sichtbar in Richtung spec-driven — die Codebasis muss gegen ein vorab geschriebenes Dokument validieren. Das ist eine bewusste Verschiebung: Governance über Zeit verlangt eine Behauptungsbasis, gegen die Drift überhaupt messbar wird. Die Auflösung dieses Konflikts ist, dass das Invarianten-Dokument selbst *aus dem Prozess heraus* entsteht (jede Invariante referenziert eine ADR, die ein Gate passiert hat) — nicht ein Top-down-Spec, sondern ein indizierter Aggregat-Snapshot über approvte Entscheidungen. Wir tauschen kein Prinzip, wir verschieben die Granularität: vom *was wollen wir bauen* (spec, vorab) zum *was haben wir entschieden, das gelten muss* (assertion, kontinuierlich).

## Decision

Drei gekoppelte Bausteine erweitern die Architecture-Governance um eine Content-Schicht:

### 1. Template `templates/architecture-invariants-template.md`

Strukturierte, ausführbare Invarianten mit klaren Kategorien:

```yaml
forbidden-imports:
  - module: sqlite3
    reason: ADR binds primary storage to Postgres
    binding-adr: ADR-NNN

layer-rules:
  - from: domain/
    must-not-import-from: [infrastructure/, ui/]
    binding-adr: ADR-NNN

library-whitelist:
  http-client:
    allowed: [httpx, requests]
    binding-adr: ADR-NNN

adr-bindings:
  - adr: ADR-NNN
    asserts:
      - "no module imports sqlite3"
      - "config key 'db.engine' equals 'postgres' in all envs"
    locator:
      type: ast-import      # ast-import | grep | config-query
      scope:
        include: ["src/**"]
        exclude: ["tests/**", "**/*.md", "vendor/**"]
      loose: false           # true erlaubt Volltext-grep; default false
```

Jede Invariante referenziert die ADR, die sie codiert. Damit wird `accepted` zu einer laufenden Behauptung über die Codebasis, nicht ein historisches Datum.

**Default-Locator-Disziplin** (Mitigation für False-Positive-Flut): Locator-Typen sind enumeriert (`ast-import`, `grep`, `config-query`); jeder Locator MUSS einen `scope.include` führen; Volltext-grep ist nur per `loose: true` opt-in erreichbar. Ohne diese Disziplin produziert der Auditor in den ersten Läufen mehr Lärm als Signal und Kill Criterion löst zwangsläufig aus.

**Starter-Pack im Template** (Mitigation gegen leere Schablonen): Das Template wird mit 3–5 sofort einsatzfähigen Default-Invarianten ausgeliefert (z. B. "keine `print()` ausserhalb von `cli/`-Modulen", "keine direkten DB-Imports in UI-Layer", "keine TODO-Kommentare ohne Issue-Referenz"). Diese sind opt-out, nicht opt-in — ein Projekt, das sie nicht will, kommentiert sie aus, statt sie schreiben zu müssen. Der Auditor schlägt zusätzlich beim ersten Lauf Erst-Invarianten aus den existierenden ADRs des Projekts vor.

### 2. Agent `agents/governance-auditor.md`

Content-orientierter Auditor mit drei Pflicht-Checks:

- **ADR-Drift**: Für jede `accepted` ADR mit `adr-bindings`-Locator: prüfen, ob die Behauptung im aktuellen Code hält. Verstösse → `BLOCK`-Finding.
- **Undokumentierte Patterns**: Cluster ähnlicher Code-Strukturen identifizieren, denen keine ADR zugeordnet ist → `CONCERN`-Finding mit Vorschlag, eine ADR zu öffnen.
- **Obsolete ADRs**: ADRs, deren `binding-adr`-referenzierte Symbole/Pfade nicht mehr existieren → `CONCERN`-Finding mit Vorschlag `deprecated` oder `superseded`.

Nicht im Scope: Stilistische Code-Reviews, Performance, Security — diese liegen bei `architecture-reviewer` bzw. spezialisierten Agents.

### 3. Slash-Command `/governance-audit`

Triggert den Auditor on-demand und appended das Ergebnis (Finding-Liste, kein Verdict) in `governance-log.md` als eigenen Event-Typ:

```
2026-04-25  AUDIT  —  proposed:ai  decided:—  "3 drift findings, 1 obsolete ADR"
```

Der Mensch entscheidet Folgemassnahmen via `/approve`, `/reject`, oder ADR-Supersession — das Verfahren bleibt unverändert.

### 4. Erweiterung `guidelines/architecture-governance.md`

Neue Sektion **"Content Governance"** unterhalb der Provenance-Sektion:
> Approval ist eine Behauptung an einem Zeitpunkt. Content-Governance prüft, ob die Behauptung über Zeit hält. ADRs ohne Code-Bindung haben kein Drift-Signal — das ist erlaubt, aber dokumentiert.

## Alternatives

### Alternative A: Status quo (nur Plan-Governance)
- Pros: Minimaler Aufwand, mechanisch über Hooks abdeckbar
- Cons: Blind gegenüber Substanz-Drift; das Hauptproblem bleibt ungelöst

### Alternative B: Harter Linter / CI-Check
- Pros: Deterministisch, billig, reproduzierbar
- Cons: Kann "undokumentiertes Pattern" nicht erkennen (semantische Mustererkennung nötig); Invarianten-Sprache wird mit Edge-Cases überfrachtet

### Alternative C: Kombiniert — deklarative Invarianten + LLM-Auditor (gewählt)
- Pros: Harte Checks (forbidden-imports, layer-rules) bleiben mechanisch und billig; semantische Drift (undokumentierte Patterns) nutzt LLM-Stärken
- Cons: Zwei Mechanismen statt einem; Projekt muss Invarianten pflegen

## Consequences

### Positive
- ADRs werden zu lebendigen Constraints, nicht historischer Paperwork
- "Approval requires evidence" bekommt eine Zeit-Dimension: Evidenz muss auch nach Approval gelten
- Die Invariantenbasis wird zur durchsuchbaren Architektur-Spezifikation

### Negative
- Pro Projekt entsteht initiale Pflege-Last (`architecture-invariants.md` schreiben)
- LLM-Audit bringt nicht-deterministische Findings; Mensch muss filtern
- Erweitert die Agent-Landschaft (Risiko von Rollenüberlappung mit `architecture-reviewer`)

### Risks
- **R-ADR-001-1**: Invarianten selbst werden stale. *Mitigation*: jede `binding-adr`-Behauptung hat einen Locator, der mechanisch fehlschlägt, wenn das Symbol verschwindet.
- **R-ADR-001-2**: False Positives durch Auditor-Halluzination. *Mitigation*: harte Regeln (forbidden-imports, layer-rules) deterministisch prüfen; LLM nur für semantische Cluster.
- **R-ADR-001-3**: Scope-Creep mit `architecture-reviewer`. *Mitigation*: klare Trennung — Reviewer prüft *einzelne Änderungen* gegen Invarianten, Auditor prüft *Repo-Zustand* gegen ADR-Bindings.

## Kill Criteria

Nach 3 Audit-Läufen ohne actionable Findings ODER >70% False-Positive-Rate: Auditor-Agent retiren, Invarianten-Template behalten (es ist Doku-Wert auch ohne Agent).

## Cross-references

- Erweitert: [guidelines/architecture-governance.md](../../guidelines/architecture-governance.md)
- Komplementär zu: [agents/architecture-reviewer.md](../../agents/architecture-reviewer.md)
- Hook-Layer: [hooks/provenance-check.py](../../hooks/provenance-check.py) (unverändert)

## Challenger

### 1. Top-3 ways this approach could fail

**Failure 1 — Invarianten-Template wird nie gefüllt.**
*What breaks*: Drei Monate nach Einführung existiert in keinem Konsumprojekt ein nicht-leeres `architecture-invariants.md`; der Auditor läuft gegen eine Schablone und produziert null Findings. Content Governance wird Shelfware, das Verfahren ist um eine Layer reicher, der Code-Bezug bleibt aus.
*Cheapest signal*: Zähle nach 90 Tagen, wieviele Projekte ein nicht-leeres `architecture-invariants.md` mit ≥3 echten Bindings haben (nicht Platzhalter-Beispielen). Wenn <50%: Failure manifest.
*What we would do*: Mit dem Template 3–5 sofort einsatzfähige Standard-Invarianten ausliefern (keine `print()` in Production, übliche Layer-Regeln für Standard-Stacks); zusätzlich den Auditor so erweitern, dass er aus existierenden ADRs Erst-Vorschläge für Invarianten generiert.

**Failure 2 — Locator-Sprache produziert False-Positive-Flut.**
*What breaks*: Ein `grep`-basierter Locator für `sqlite3` matcht Kommentare, Doku, Tests und schiesst beim ersten Audit-Lauf 30+ "Violations" raus, von denen 25 unecht sind. Nach drei solchen Läufen ignorieren Menschen den Auditor und das Kill Criterion (>70% FP) löst aus.
*Cheapest signal*: Findings→Action-Ratio im ersten Audit-Lauf. <30% bedeutet zu unscharf.
*What we would do*: Locator-Sprache strikt definieren (default scope = `src/**`, exclude `tests/**`, `**/*.md`); harte Regeln nur über AST-Imports, nicht Volltext-grep; Volltext-grep nur als opt-in `loose: true`.

**Failure 3 — Rollenüberlappung mit `architecture-reviewer` bleibt nominell.**
*What breaks*: Beide Agents lesen `architecture-invariants.md`, ihre Definitionen driften über Zeit auseinander, Nutzer wissen nicht, wann welcher zu rufen ist. Im schlimmsten Fall werden beide auf jede Änderung angewendet, was Token-Kosten verdoppelt; im häufigsten Fall keiner.
*Cheapest signal*: Nach drei Monaten messen, wie oft beide Agents auf demselben Artefakt liefen, und wie oft keiner trotz vorhandenem `architecture-invariants.md`.
*What we would do*: Beide Agent-Definitionen müssen eine "Wann wen?"-Matrix tragen, die per CI-Check auf Konsistenz validiert wird. Bei materialisierter Verwirrung: zu *einem* Agent mit zwei Modi (`--mode=change|repo`) mergen.

### 2. Two alternative approaches

**Alternative D — `architecture-reviewer` mit Repo-Modus erweitern, kein neuer Agent.**
*Sketch*: Statt einen `governance-auditor` einzuführen, dem Reviewer ein Flag `--mode=repo` geben. Er liest dieselben `architecture-invariants.md`, prüft aber den ganzen Tree statt eines Diffs. Eine Slash-Command-Variante (`/architecture-review --repo`) genügt.
*Why rejected*: Im ADR aus Klarheits- und Trennbarkeitsgründen abgelehnt — Reviewer ist per-change und auf Architektur-Invarianten gegen Änderung optimiert; Auditor ist per-repo mit Drift-/Obsoleszenz-Logik. Eigene Datei macht das auffindbar.
*Re-open if*: Failure 3 materialisiert sich. Wenn die Rollenüberlappung nach drei Monaten Praxis Probleme macht statt Klarheit zu schaffen, ist Merge richtig.

**Alternative E — Invarianten zur Audit-Zeit aus ADRs ableiten, kein Template.**
*Sketch*: Auditor liest alle `accepted` ADRs, extrahiert per LLM imperative Behauptungen ("muss Postgres", "kein SQLite") und prüft sie. Kein separates Invarianten-Dokument nötig.
*Why rejected*: Nicht-deterministisch. Menschen können nicht pre-approven, was der AI später aus ADRs herausliest; Debug-Pfad bei "warum hat der Auditor das geflaggt?" wird zur Archäologie. Verstösst gegen das Provenance-Prinzip — die Behauptung muss dort prüfbar sein, wo sie codiert wurde.
*Re-open if*: NLP-Extraktion imperativer Aussagen aus Freitext erreicht reproduzierbare Genauigkeit (>95% gleicher Output bei zwei Läufen) und ADRs erhalten ein striktes "Decision"-Subschema, das die Extraktion deterministisch macht.

### 3. Strongest counter-argument

Das stärkste Argument gegen diesen ADR ist, dass wir ein Problem lösen, das wir noch nicht beobachtet haben. Das Framework ist jung, kein Konsumprojekt hat bisher gemeldet "wir haben eine ADR approved und der Code ist gedriftet." Wir bauen die Antikörper vor der Infektion. Die Kosten sind real (Template, Agent, Slash-Command, Doku-Updates, laufende Pflege einer zweiten Governance-Schicht, die selbst mit der ersten synchron gehalten werden muss); der Nutzen ist hypothetisch. Der ehrliche Zug wäre, auf mindestens einen konkreten Drift-Vorfall in einem realen Projekt zu warten und das Design aus diesem Vorfall heraus zu entwickeln — nicht aus vorgestellten. Vorzeitige Governance hat eine Tendenz, selbst zur Bürokratie zu werden, die sie verhindern sollte; das Framework predigt "uncertainty before code", aber dieser ADR codifiziert eine Antwort auf ungemessene Unsicherheit.

### 4. Product-coherence check

**Vision fit**: Die Kernformel des Frameworks ist *uncertainty before code* (CLAUDE.md), und Post-Approval-Drift ist genau die Klasse Unsicherheit, die das Verfahren noch nicht erfasst. Insofern Anschluss. *Aber*: das Framework definiert sich explizit als "process-driven, not spec-driven" und sagt, "der Spec emerges as an artifact" — `architecture-invariants.md` als verpflichtendes ausführbares Artefakt zieht das Pendel sichtbar Richtung spec-driven. Die Spannung ist real und sollte im ADR-Text benannt werden, nicht überspielt.

**Decision continuity**: Baut auf [guidelines/architecture-governance.md](../../guidelines/architecture-governance.md) auf, ergänzt [agents/architecture-reviewer.md](../../agents/architecture-reviewer.md), widerspricht keiner akzeptierten Entscheidung. Der ADR-Template-Hinweis "During drift detection: AI must flag it for review" macht Drift-Detection schon abstrakt zur AI-Pflicht; dieser ADR konkretisiert diese Klausel. Kontinuierlich.

**Problem validation**: Hypothetisch. Es gibt keinen gemessenen Drift-Vorfall, keine Support-Tickets, keine empirisch belegte Lücke. Die stärkste Begründung ist *strukturell* (Provenance ohne Substanz-Check ist verfahrensorientiert) — diese Beobachtung ist plausibel, aber theoretisch. Konsequenz für G2 (falls dieser ADR später in einer EXP umgesetzt wird): die EXP MUSS in `Hypotheses` festhalten, dass Content-Drift erwartet wird, und in `Kill Criteria` definieren, ab wann Ausbleiben von Findings den Auditor retiret.
