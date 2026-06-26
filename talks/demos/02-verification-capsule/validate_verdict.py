#!/usr/bin/env python3
"""Mini-Validator fuer ein Gatekeeper-Verdict (Demo 2).

Prueft ein Verdict-JSON gegen verdict.schema.json. Bewusst dependency-frei:
ein kleiner Validator fuer den JSON-Schema-Subset, den das Schema nutzt
(type / required / enum / additionalProperties / properties / items).
In echt nimmt man die 'jsonschema'-Lib — fuer die Demo zaehlt das Prinzip:
ein strukturiertes Verdict ist *maschinell pruefbar*, ein Freitext nicht.

Aufruf:  python validate_verdict.py <verdict.json>
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

_TYPES = {
    "object": dict, "array": list, "string": str,
    "number": (int, float), "boolean": bool,
}


def validate(node, schema: dict, path: str = "$") -> list[str]:
    errs: list[str] = []
    expected = schema.get("type")
    if expected and not isinstance(node, _TYPES[expected]):
        return [f"{path}: erwartet {expected}, ist {type(node).__name__}"]

    if expected == "object":
        for key in schema.get("required", []):
            if key not in node:
                errs.append(f"{path}: Pflichtfeld '{key}' fehlt")
        props = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for key in node:
                if key not in props:
                    errs.append(f"{path}: unerlaubtes Feld '{key}'")
        for key, sub in props.items():
            if key in node:
                errs += validate(node[key], sub, f"{path}.{key}")

    elif expected == "array":
        item_schema = schema.get("items")
        if item_schema:
            for i, item in enumerate(node):
                errs += validate(item, item_schema, f"{path}[{i}]")

    if "enum" in schema and node not in schema["enum"]:
        errs.append(f"{path}: '{node}' nicht in {schema['enum']}")
    return errs


def main() -> int:
    if len(sys.argv) != 2:
        print("Aufruf: python validate_verdict.py <verdict.json>", file=sys.stderr)
        return 2
    schema = json.loads((HERE / "verdict.schema.json").read_text(encoding="utf-8"))
    verdict = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    errs = validate(verdict, schema)
    if errs:
        print("FEHLER: Verdict entspricht NICHT dem Schema:")
        for e in errs:
            print(f"  - {e}")
        return 1
    print(f"OK: Verdict entspricht dem Schema "
          f"(verdict={verdict['verdict']}, {len(verdict['findings'])} Findings)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
