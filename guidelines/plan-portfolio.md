# Plan Portfolio Heatmap

Visualize all active and backlog plans on an **effort × value** quadrant chart.
Helps a solo developer see at a glance where energy is going (Quick Wins, Big
Bets, Fill-ins, Time Sinks) and spot drift before it becomes a problem.

## Prerequisites

The framework must be **cloned locally** — the renderer is a Python script, not
inlined into this guideline. Single-file `@url` consumers will not have access
to it. This is intentional: executable code should live in the repo, not be
fetched from a URL.

Local script path: [`scripts/plan_portfolio.py`](../scripts/plan_portfolio.py)

Dependencies:

```bash
pip install pyyaml matplotlib
```

## Frontmatter Fields

Three optional fields on any plan (flat or §-numbered):

```yaml
effort: 3      # 1-5 — XS/S/M/L/XL implementation cost
value:  4      # 1-5 — nice-to-have -> game-changer
risk:   2      # 1-5 — optional, controls bubble size (default 2)
```

All three are optional. Plans missing `effort` or `value` land in a grey
"unscored" strip at the right edge of the chart — no gate enforcement, no
bookkeeping pressure. Score when it helps you; skip when it doesn't.

## Usage

From the project root:

```bash
python3 scripts/plan_portfolio.py
```

Or via slash command (if the plugin is installed):

```
/portfolio
```

Optional arguments:

```bash
python3 scripts/plan_portfolio.py <plans_dir> <output_png>
# defaults: context/plans  ->  context/plan-portfolio.png
```

## Encoding

| Dimension     | Meaning                                               |
|---------------|-------------------------------------------------------|
| X-axis        | `effort` (1-5)                                        |
| Y-axis        | `value` (1-5)                                         |
| Bubble size   | `risk` (1-5)                                          |
| Bubble color  | `type` — CTX (purple), EXP (blue), PRD (green)        |
| Label         | `id` or `§<n>`                                        |
| Quadrant tint | Quick Wins (green), Big Bets (blue), Fill-ins (yellow), Time Sinks (red) |

## Filter

Only plans with `status ∈ {active, backlog, draft, proposed, approved}` are
rendered. Finished, archived, and deprecated plans are filtered out — the
point is to reason about *what's on the plate right now*, not celebrate past
work.

## When to run

- Before picking the next plan to work on (Quick Wins first)
- When the backlog feels unclear or bloated
- Before committing to a Big Bet — is the slot free?
- Periodically as a sanity check — is too much in Time Sinks?

The generated PNG can be committed to `context/` to track portfolio drift
over time via git diffs.
