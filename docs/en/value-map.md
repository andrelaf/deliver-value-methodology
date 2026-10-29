# Value Map

The Value Map is how Value-First draws an initiative on one page. It borrows the idea that made the [C4 model](https://c4model.com/) popular for software architecture: a few levels of zoom, a tiny notation, and drawings anyone can make on a whiteboard without special tools (Simon Brown, c4model.com).

Use it when an initiative is too big for a single Value Spec. For a single item, go straight to the [Value Spec](../../templates/en/value-spec.md).

## Three levels of zoom

| Level | Shows | Answers | Main readers |
|---|---|---|---|
| **1. Outcome** | The initiative: problem, for whom, one metric, what's out | Why are we doing this, and how will we know? | Everyone, including leadership |
| **2. Slices** | The Value Specs that move the outcome, in order | What do we deliver first, and what are we betting on? | Value Pair, team, stakeholders |
| **3. Criteria** | The success criteria (SC-n) of one slice and what verifies each one | How do we know this slice works? | Team and coding agents |

There's a fourth level, **code**, that you don't draw. Tests and pull requests cite the SC IDs, and tools and agents produce it. Like the code level in C4, it's optional on paper.

## Notation: four rules

1. **Every box has a type, a name and one sentence.**
2. **Every Outcome and Slice box has a metric or a signal.** If you can't name one, it isn't ready.
3. **Every arrow has a verb**, such as "contributes to" or "is verified by".
4. **One drawing per level.** Zoom in only where you need to.

Box types:

- **Outcome:** problem · for whom · metric (baseline → target, by when) · out of scope.
- **Slice (VS-xxx):** what it delivers · how it moves the metric · riskiest bet, of value or technical · status.
- **Criterion (SC-n):** the statement in EARS or Given/When/Then · what verifies it (test, dashboard, review).

## Example

*Fictional and illustrative. It extends the [VS-014 example](../../templates/en/value-spec-example.md).*

- **Level 1, Outcome:** *Customers get their invoices on their own.* Billing contacts ask support for invoices. Metric: invoice tickets from ~120 to ≤ 40 per week, 6 weeks after launch. Out of scope: payments, invoice editing.
- **Level 2, Slices:**
  - **VS-014** Download invoices in the portal. Bet: customers would use the portal instead of emailing support (validated, 5 of 6). *In build.*
  - **VS-015** Filter invoices by date. Bet: audits need date ranges (2 of 6 asked). *Next.*
  - **VS-016** Monthly invoice by email. Bet: receiving beats searching (not validated). *Maybe.*
- **Level 3, Criteria of VS-014:** SC-1 list 24 months → end-to-end test · SC-2 unchanged PDF → integration test · SC-3 403 without `billing_admin` → security test · SC-4 p95 < 1 s → load test.

The landing page draws this example. There's also a [blank map to print](https://andrelaf.github.io/deliver-value-methodology/map.html).

## Running it (about 60 minutes)

1. **Level 1 together (15 min).** Product and the Tech Lead, plus one or two stakeholders. If you can't agree on one metric, stop: you probably have two initiatives.
2. **Level 2 (30 min).** List the slices. Each one should be able to move the metric on its own. Write the riskiest bet of each, then order them by what you'll learn first, not by size.
3. **Each slice becomes a Value Spec.** Level 3 is written in the spec, not in the workshop.
4. **Keep it alive.** After each value check, mark the slice as delivered, not delivered or retired, and redraw the order.

## Keeping it in the repository

A whiteboard photo is fine. If you want people and agents to read it, keep it as Markdown next to the specs, for example `specs/README.md`. Use the [Value Map template](../../templates/en/value-map.md).

---

**From v1.** The Value Map replaces the Value-Technology Alignment Canvas. Most of the canvas's 12 blocks now live in the Value Spec, so the map only keeps what the spec doesn't: the outcome above the specs and the order between them. The original canvas is in [docs/archive/v1/en/canvas](../archive/v1/en/canvas/value-technology-alignment-canvas.svg).
