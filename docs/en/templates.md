# Templates

All templates are plain Markdown, so they can be copied into your repository and read by people and coding agents alike.

| Template | What it's for |
|---|---|
| [Value Spec](../../templates/en/value-spec.md) | The central artifact. One per relevant item: problem, value, success criteria, constraints, validation, decisions, value check and agent instructions. |
| [Value Spec: filled example](../../templates/en/value-spec-example.md) | A fictional, illustrative example to show the level of detail. |
| [Agent context snippet](../../templates/en/agents-snippet.md) | A block for AGENTS.md / CLAUDE.md / rules that points agents to the Value Spec. |
| [Value-Technology Alignment Canvas](./canvas/value-technology-alignment-canvas.svg) | Optional workshop tool for larger initiatives ([PNG](./canvas/value-technology-alignment-canvas.png), [filled example](./canvas/value-technology-alignment-canvas-example.png)). |

## Where to keep Value Specs

A common layout is a `specs/` folder at the repository root, one file per spec: `specs/VS-014-invoice-download.md`. If you use Spec Kit or Kiro, keep the Value Spec next to the files those tools generate, and link them through `links.design`.

## Using the Canvas

1. **Prepare.** Invite Product, the Tech Lead and one or two key stakeholders. 60–90 minutes.
2. **Fill it in together**, business blocks first, then technical blocks, then risks.
3. **Turn it into Value Specs.** Each distinct outcome becomes one candidate spec.
4. **Come back to it** when an initiative changes direction.

The v1 templates (Value Matrix, Flexibility Contract) are now part of the Value Spec. The originals are in [docs/archive/v1](../archive/v1/en/templates.md).
