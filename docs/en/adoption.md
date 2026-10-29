# Adopting Value-First

How to start, how to tell whether you're practicing it, and how to grow.

## You're Value-First if…

A team practices Value-First when you can **see** these things. These are signals in the work, not statements of intent:

- [ ] Every relevant item in progress (see [when not to use it](#when-not-to-use-it)) points to a Value Spec with at least **one measurable success criterion**.
- [ ] Every Value Spec has **two named owners**: Product and Tech Lead.
- [ ] Specs are **versioned in the repository** and your agent instructions (AGENTS.md, CLAUDE.md, rules) **point to them**.
- [ ] High-uncertainty items have a **prototype or spike recorded before** the commitment.
- [ ] Changes in scope or date show up as **a change in the spec, with a reason**, not as a "delay" discovered in a status meeting.
- [ ] **Value checks happen** and are recorded. The team can name deliveries that **did not** create the expected value.
- [ ] **All AI-generated code is reviewed by a person**, and stability is tracked alongside speed (for example, DORA's change failure rate, [dora.dev](https://dora.dev/guides/dora-metrics-four-keys/)).

If you tick all seven, you're practicing Value-First, whatever your board or cadence looks like.

### Warning signs

- A spec longer than two pages that nobody updates.
- "Value" written as "improve the experience", with no metric.
- The Tech Lead writing the spec alone, again.
- The Value Spec has turned into one more approval form.
- Agents producing code from a ticket title because "the spec is in someone's head".

---

## Maturity model

Three levels. Find yourself on each line separately: most teams are at different levels on different lines. The aim isn't to reach level 3 everywhere. It's to know where the next step is.

| Dimension | 1. Starting | 2. Practicing | 3. Embedded |
|---|---|---|---|
| **Value** | Items describe features. Value is implied. | Most items state expected value and a metric. | Every relevant item has a baseline, a target and a date to check. Priorities change based on value checks. |
| **Spec** | Tickets and conversations. Context lives in people's heads. | Value Specs exist for larger items, written by the pair. | Value Specs are the input for people and agents. They're versioned, cited in PRs and kept up to date. |
| **Validation** | Build first, find out later. | Spikes or prototypes for the riskiest items. | Prototypes answer one value question before every high-uncertainty commitment, and decisions go into the spec. |
| **Pair** | Product writes and the Tech Lead translates alone. | Product and Tech Lead write specs together for big items. | The pair is the default. The team challenges specs before building. |
| **Change** | Changes show up as delays. | Changes are discussed but not recorded. | Changes go into the spec with a reason and are visible to stakeholders. |
| **Closing the loop** | No look back after release. | Occasional reviews of results. | Value checks are scheduled and recorded, and they feed the backlog. |
| **AI** | Ad hoc use. No shared context. | Agent context file exists. Code review covers AI output. | Agents read the Value Spec, ask about open questions, and trace work to criterion IDs. Stability is tracked. |

### Spec maturity in detail

Specs deserve their own scale, because they are now the input agents act on:

| Level | What the spec looks like | What an agent can do with it |
|---|---|---|
| **0. Implicit** | A ticket title. The rest is in someone's head. | Guess. |
| **1. Described** | A user story with some acceptance criteria. | Build something plausible that may miss constraints and edge cases. |
| **2. Value-scoped** | A Value Spec: problem, value metric, testable criteria, constraints, non-goals. | Plan tasks traced to criteria and stop at non-goals. |
| **3. Anchored** | Level 2, plus versioned next to the code, cited in PRs, updated by decisions and value checks. | Work from current intent, flag conflicts with the code and propose spec changes. |

Level 3 matches what Birgitta Böckeler calls *spec-anchored* development ([martinfowler.com, 2025](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)). Value-First doesn't aim at *spec-as-source*, where people edit only specs and never code.

### Quick self-assessment

Score each dimension 1–3 with your team, in 15 minutes. Don't average the scores. Pick the **lowest** line and improve it next. A shared conversation about the scores is worth more than the numbers.

---

## Start in one week

1. **Pick one upcoming item** with real business value and some uncertainty.
2. **Write the Value Spec as a pair** with the [template](../../templates/en/value-spec.md). Keep it to a page.
3. **Run the readiness check.** Unanswered questions go to "Open questions".
4. **Validate the riskiest assumption** with the cheapest prototype or spike that answers it.
5. **Add the [agent snippet](../../templates/en/agents-snippet.md)** to your AGENTS.md or CLAUDE.md, if you use coding agents.
6. **Build**, citing the spec ID and criterion IDs in PRs.
7. **Book the value check** on the date in the spec. Then run a 15-minute retro: what did the spec lack?

After a few items, decide together whether to make the readiness check a team policy.

## When not to use it

- **Very small or obvious changes.** Bug fixes, typos and routine maintenance don't need a Value Spec.
- **Pure exploration or research spikes.** Their output is learning, so they don't need success metrics up front. Record what you learned in the spec they feed.
- **When nobody can measure value at all.** Start by agreeing on one observable signal. Until then, Value-First will feel like a form to fill in.
