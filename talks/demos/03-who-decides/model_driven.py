#!/usr/bin/env python3
"""Model-driven: das MODELL entscheidet den naechsten Schritt (Demo 3).

Pro Iteration waehlt das (gemockte) Modell selbst die naechste Aktion aus dem
Aktionsraum — der Workflow gibt die Reihenfolge NICHT vor. Folge: der Ablauf
driftet zwischen Laeufen, kann Schritte wiederholen oder 'verify' ueberspringen.
Genau das ist Autonomie ohne Leitplanken.

Hinweis: 'random' steht hier stellvertretend fuer die Nicht-Determiniertheit eines
LLM. Es geht um den Kontrollfluss, nicht um echte Modellqualitaet.
"""
from __future__ import annotations

import random

ACTIONS = ["explore", "plan", "verify", "rethink", "apply"]
MAX_STEPS = 8


def model_decides(history: list[str]) -> str:
    # Gemockte 'Entscheidung': das Modell waehlt frei. Es MUSS 'verify' nicht waehlen.
    return random.choice(ACTIONS)


def main() -> None:
    trace: list[str] = []
    for _ in range(MAX_STEPS):
        action = model_decides(trace)
        trace.append(action)
        if action == "apply":      # das Modell erklaert sich selbst fuer fertig
            break
    print("MODELL entscheidet    ->  Trace:", " -> ".join(trace))
    print("verify enthalten? ", "ja" if "verify" in trace else "NEIN  <- Garantie verloren")
    print("reproduzierbar?   ", "nein - anderer Trace bei jedem Lauf")


if __name__ == "__main__":
    main()
