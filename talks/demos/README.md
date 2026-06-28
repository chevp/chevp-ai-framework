# Demos — Architecting Agentic Workflows

Drei eigenständige Beispiele zum Talk
[`../architecting-agentic-workflows.md`](../architecting-agentic-workflows.md). Jedes ist ein
in sich geschlossener Ordner und über eine **Architekturfrage** benannt — nicht über eine
Nummer. Die Zuhörer sollen sich an die *Frage* erinnern, nicht an den Code.

| Demo | Architekturfrage | Akt im Talk | Kern-Artefakt |
|------|------------------|-------------|---------------|
| [`01-enforcement-contract/`](01-enforcement-contract/) | **Wie erzwingt man Regeln außerhalb des Modells?** | Akt 2 | `contract.yaml` (deklarativer Gate-Vertrag) |
| [`02-who-decides/`](02-who-decides/) | **Wer trifft Entscheidungen?** | Akt 4 | `orchestrated.flow.md` vs. `model-driven.flow.md` |
| [`03-verification-capsule/`](03-verification-capsule/) | **Wie kapselt man Verifikation?** | Akt 4 | `gatekeeper.md` + `verdict.schema.json` |

## Gemeinsame Prinzipien
- **Deklarativ statt Code.** Jede Demo ist ein deklaratives Artefakt (Vertrag / Flow-Definition
  / Schema + Markdown-Subagent) plus ein **vorbereitetes Ergebnis** zum Zeigen. Bewusst
  *ohne* ausführbare Skripte — die Botschaft des Talks ist „schaut auf den Vertrag, nicht auf
  die Sprache", und das gilt auch für die Demos selbst.
- **Vorführ-fertig.** Das erwartete Ergebnis liegt jeweils als Datei bei (`expected-output.md`,
  Traces in den `*.flow.md`, `sample-verdict.json`) — kopierbar, zeigbar, als Screencast-Vorlage.
- **Cross-platform.** Forward-Slashes, ASCII-Ausgaben, keine Drive-Letter — auf Windows,
  macOS, Linux gleich zeigbar.

## So führst du die Demos vor (kein Code nötig)
- **Demo 1** — [`contract.yaml`](01-enforcement-contract/contract.yaml) +
  [`state.json`](01-enforcement-contract/state.json) zeigen, dann
  [`expected-output.md`](01-enforcement-contract/expected-output.md) (BLOCK → ALLOW → Read frei).
- **Demo 2** — [`orchestrated.flow.md`](02-who-decides/orchestrated.flow.md) (identischer Trace)
  gegen [`model-driven.flow.md`](02-who-decides/model-driven.flow.md) (driftender Trace) stellen.
- **Demo 3** — [`sample-plan.md`](03-verification-capsule/sample-plan.md) →
  [`gatekeeper.md`](03-verification-capsule/gatekeeper.md) →
  [`sample-verdict.json`](03-verification-capsule/sample-verdict.json) neben
  [`verdict.schema.json`](03-verification-capsule/verdict.schema.json) legen.

> Wer eine Demo dennoch live ausführen will, kann jedes Artefakt von einer beliebigen Runtime
> auswerten lassen (Hook, Proxy, CI-Step, JSON-Schema-Validator). Das Ergebnis ändert sich
> nicht — es folgt allein aus dem deklarativen Artefakt.
