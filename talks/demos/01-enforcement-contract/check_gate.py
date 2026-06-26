#!/usr/bin/env python3
"""Referenz-Runner fuer den Gate-Vertrag (Demo 1).

Bewusst minimal und nebensaechlich: die Architektur steckt in contract.yaml,
nicht hier. Dieser Runner liest Vertrag + Zustand und gibt ein Verdict aus.
Nur Python-3.10-stdlib, kein YAML-Paket noetig (winziger Subset-Parser unten).

Aufruf:  python check_gate.py <ToolName>
Beispiel: python check_gate.py Write
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load_contract(path: Path) -> dict:
    """Winziger YAML-Subset-Parser fuer genau diese Vertragsstruktur.

    Unterstuetzt verschachtelte Maps per Einrueckung und gefaltete '>'-Bloecke.
    In echt wuerde man PyYAML nehmen — fuer die Demo bleibt es dependency-frei.
    """
    root: dict = {}
    stack: list[tuple[int, dict]] = [(-1, root)]
    fold_key = None
    fold_indent = 0
    fold_parts: list[str] = []

    def flush_fold():
        nonlocal fold_key
        if fold_key is not None:
            parent = stack[-1][1]
            parent[fold_key] = " ".join(p.strip() for p in fold_parts).strip()
            fold_key = None
            fold_parts.clear()

    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip())
        if fold_key is not None and indent > fold_indent:
            fold_parts.append(raw)
            continue
        flush_fold()
        while stack and indent <= stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]
        key, _, value = raw.strip().partition(":")
        value = value.split(" #", 1)[0].strip()   # Inline-Kommentare entfernen
        if value == ">":                       # gefalteter Mehrzeilen-Block
            fold_key, fold_indent = key, indent
        elif value == "":                       # neue verschachtelte Map
            child: dict = {}
            parent[key] = child
            stack.append((indent, child))
        else:
            parent[key] = value
    flush_fold()
    return root


def evaluate(contract: dict, state: dict, tool: str) -> tuple[str, str]:
    """Gibt (verdict, message) zurueck. 'allow', wenn der Ausloeser nicht greift."""
    trigger = contract.get("on", {}).get("tool")
    if tool != trigger:                         # kein Ausloeser -> nie blockieren
        return "allow", f"Tool '{tool}' ist kein Ausloeser des Vertrags."

    when = contract.get("when", {})
    condition_met = False
    if "not" in when:                           # when.not.state == false  -> Bedingung erfuellt
        flag = when["not"].get("state")
        condition_met = not state.get(flag, False)

    if condition_met:
        return contract.get("verdict", "block"), contract.get("message", "Blockiert.")
    return "allow", "Bedingung nicht erfuellt — Zugriff erlaubt."


def main() -> int:
    if len(sys.argv) != 2:
        print("Aufruf: python check_gate.py <ToolName>", file=sys.stderr)
        return 2
    tool = sys.argv[1]
    contract = load_contract(HERE / "contract.yaml")
    state = json.loads((HERE / "state.json").read_text(encoding="utf-8"))
    verdict, message = evaluate(contract, state, tool)
    print(f"{verdict.upper()}: {message}")
    return 1 if verdict == "block" else 0


if __name__ == "__main__":
    raise SystemExit(main())
