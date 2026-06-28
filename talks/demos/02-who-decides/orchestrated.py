#!/usr/bin/env python3
"""Orchestriert: der WORKFLOW entscheidet den Kontrollfluss (Demo 2).

Die Reihenfolge der Schritte ist im Code festgelegt. Das 'Modell' fuellt nur den
Inhalt jedes Schritts — es bestimmt NICHT, was als Naechstes kommt. Folge:
der Ablauf ist bei jedem Lauf identisch, also reproduzierbar und auditierbar.
"""
from __future__ import annotations

# Der Workflow besitzt den Kontrollfluss. Feste Stages, feste Reihenfolge.
STAGES = ["explore", "plan", "verify", "apply"]


def run_stage(name: str) -> str:
    # In echt: hier ruft der Workflow einen (Sub-)Agenten fuer genau diesen Schritt.
    # Gemockt: der Schritt liefert immer dasselbe deterministische Ergebnis.
    return f"{name}:ok"


def main() -> None:
    trace = [run_stage(stage) for stage in STAGES]
    print("WORKFLOW entscheidet  ->  Trace:", " -> ".join(trace))
    print("verify enthalten? ", "ja" if any(s.startswith("verify") for s in trace) else "NEIN")
    print("reproduzierbar?   ", "ja - Reihenfolge ist im Code fixiert")


if __name__ == "__main__":
    main()
