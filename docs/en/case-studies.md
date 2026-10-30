# Illustrative scenarios

> Illustrative scenarios: each one shows a common gap between product and technology, and how the practices help close it. Used Value-First in a real team? [Share your experience](../../CONTRIBUTING.md).

---

## 1. A regulatory deadline with uncertain scope

**Situation.** An online store has to support a new tax rule by a fixed legal date. Product's first ticket says "adapt checkout to the new rule".

**With Value-First.**
- The Value Pair writes a Value Spec. **Fixed:** the legal date and compliance. **Flexible:** everything else, including UI polish and the less common payment methods.
- The Tech Lead adds the constraints the ticket left out: which tax service, how to round values and how to keep the audit trail.
- A two-day spike shows that one payment provider can't support the rule in time. That goes into the spec as a risk, with a fallback.
- When the provider's date slips, the change log records the fallback being triggered. Stakeholders see it the same day.

**What the practice made visible:** the difference between what can't move and what can. Without it, everything looks equally urgent.

## 2. Coding agents on a feature with vague intent

**Situation.** A team using coding agents gets a story: "let customers export their data". An agent produces a full CSV export in an afternoon. In review, the team learns that the real need was a monthly report for an auditor, in a specific format.

**With Value-First.**
- The readiness check fails on "What value do we expect?" and "How will we measure it?".
- Product talks to two customers and finds the auditor requirement. The Value Spec now states the format and who receives the report. A non-goal reads: "general-purpose export".
- The agent's next plan maps every task to a success criterion and stops at the non-goal.

**What the practice made visible:** the agent wasn't wrong. It did exactly what the story said. The gap was in the spec, so the fix was in the spec.

## 3. An internal product with many stakeholders

**Situation.** Three departments want different things from an internal approvals tool. Each one sees its own request as the priority.

**With Value-First.**
- An optional Value Map session puts one shared outcome at the top and produces four candidate Value Specs, each with its riskiest bet.
- Each spec states its expected value with a metric that the department itself provides, such as approval lead time or rework requests.
- A simple table ranks the four by expected value and effort. Two get built first.
- Value checks after release show that one delivery didn't change its metric. The team retires the follow-up spec instead of extending it.

**What the practice made visible:** a shared way to compare requests, and permission to stop investing where value didn't appear.

---

**From v1.** v1 presented two "real" case studies with precise percentages and amounts, but without organizations, dates or sources, and the PT and EN versions reported different figures. They were removed under the "every factual claim needs a source" rule ([Decision D6](../../DECISIONS.md)). The original text is in [docs/archive/v1](../archive/v1/en/case-studies.md).
