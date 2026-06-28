# Demos — Architecting Agentic Workflows

Drei eigenständige Beispiele zum Talk
[`../architecting-agentic-workflows.md`](../architecting-agentic-workflows.md). Jedes ist ein
in sich geschlossener Ordner und über eine **Architekturfrage** benannt — nicht über eine
Nummer. Die Zuhörer sollen sich an die *Frage* erinnern, nicht an den Code.

| Demo | Architekturfrage | Akt im Talk | Kern-Artefakt |
|------|------------------|-------------|---------------|
| [`01-enforcement-contract/`](01-enforcement-contract/) | **Wie erzwingt man Regeln außerhalb des Modells?** | Akt 2 | `contract.yaml` (deklarativer Gate-Vertrag) |
| [`02-who-decides/`](02-who-decides/) | **Wer trifft Entscheidungen?** | Akt 4 | `orchestrated.py` vs. `model_driven.py` |
| [`03-verification-capsule/`](03-verification-capsule/) | **Wie kapselt man Verifikation?** | Akt 4 | `gatekeeper.md` + `verdict.schema.json` |

## Gemeinsame Prinzipien
- **Deklarativ vor Code.** Das Architektur-Artefakt ist der Vertrag / das Schema / die
  Markdown-Definition — die ausführende Mechanik ist nebensächlich und austauschbar.
- **Dependency-frei.** Wo Code nötig ist, nur Python-3.10-stdlib — kein `pip install`, sofort
  vorführbar.
- **Cross-platform.** Forward-Slashes, ASCII-Ausgaben, keine Drive-Letter — läuft auf Windows,
  macOS, Linux.

## Voraussetzungen
- Python ≥ 3.10 (für die Runner in Demo 1–3). Die Kern-Artefakte (YAML, Markdown, JSON)
  sind auch ohne Python lesbar und zeigbar.

## Schnelltest aller Demos
```bash
# Demo 1
cd 01-enforcement-contract && python check_gate.py Write && cd ..
# Demo 2
cd 02-who-decides && python orchestrated.py && python model_driven.py && cd ..
# Demo 3
cd 03-verification-capsule && python validate_verdict.py sample-verdict.json && cd ..
```
