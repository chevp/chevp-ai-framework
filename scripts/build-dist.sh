#!/usr/bin/env bash
# build-dist.sh — Generates dist/chevp-ai-framework.md from source files.
# Usage: bash scripts/build-dist.sh [--check]

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
python3 "$REPO_ROOT/scripts/build_dist.py" "$@"
