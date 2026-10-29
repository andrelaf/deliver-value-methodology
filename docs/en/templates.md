# Templates

All templates are plain Markdown, so they can be copied into your repository and read by people and coding agents alike.

| Template | What it's for |
|---|---|
| [Value Spec](../../templates/en/value-spec.md) | The central artifact. One per relevant item: problem, value, success criteria, constraints, validation, decisions, value check and agent instructions. |
| [Value Spec: filled example](../../templates/en/value-spec-example.md) | A fictional, illustrative example to show the level of detail. |
| [Agent context snippet](../../templates/en/agents-snippet.md) | A block for AGENTS.md / CLAUDE.md / rules that points agents to the Value Spec. |
| [Value Map](../../templates/en/value-map.md) | Optional, for initiatives bigger than one spec: the outcome and the ordered Value Specs that move it. Keep it in `specs/README.md`. |

## Where to keep Value Specs

A common layout is a `specs/` folder at the repository root, one file per spec: `specs/VS-014-invoice-download.md`. If you use Spec Kit or Kiro, keep the Value Spec next to the files those tools generate, and link them through `links.design`.

## Using the Value Map

See [Value Map](./value-map.md) for the three levels, the four rules and a 60-minute session. There's also a [blank map to print](https://andrelaf.github.io/deliver-value-methodology/map.html). The v1 canvas is in [docs/archive/v1](../archive/v1/en/canvas/value-technology-alignment-canvas.svg).

The v1 templates (Value Matrix, Flexibility Contract) are now part of the Value Spec. The originals are in [docs/archive/v1](../archive/v1/en/templates.md).
