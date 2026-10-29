---
# Value Spec — Value-First Development
# Readable by humans and coding agents. Keep it short: if it doesn't fit on a few screens, split it.
id: VS-000                     # stable ID; tasks, commits and PRs reference it
title: "<short outcome-oriented title>"
status: draft                  # draft | validating | ready | in-build | delivered | measured | retired
version: 0.1.0                 # bump minor on scope/criteria change, patch on wording
owners:
  product: "<name>"            # owns problem, value, metric
  tech: "<name>"               # Tech Lead: owns constraints, criteria testability, agent context
created: YYYY-MM-DD
updated: YYYY-MM-DD
links:
  prototype: ""                # URL of the validation prototype, if any
  issue: ""                    # tracker epic/issue
  design: ""                   # downstream design/plan (e.g. Spec Kit plan.md, Kiro design.md)
  agent_context: "AGENTS.md"   # or CLAUDE.md / .cursor/rules / .kiro/steering
  dashboard: ""                # where the value metric is observed
---

# <title>

<!-- How to use: product and Tech Lead fill this together in one working session.
     Write what is known; put the unknowns under Open questions instead of guessing.
     This spec is the value contract. Plans, tasks and code are produced downstream from it. -->

## 1. Problem
<!-- 2–4 sentences. What hurts today, for whom, and the evidence (data, tickets, interviews). No solution here. -->

## 2. Who & context
<!-- Primary users/personas, the situation they are in, and the systems or processes involved. -->
- **Primary users:**
- **Context / trigger:**
- **Systems touched:**

## 3. Expected value
<!-- One outcome. If you have three outcomes, you probably have three specs. -->
| Outcome | Metric | Baseline | Target | By when | Measurement method |
|---|---|---|---|---|---|
| <behavior or business change we want> | <metric name> | <current value + source> | <target value> | <date / N weeks after release> | <query, event, survey; who checks> |

## 4. Success criteria
<!-- Measurable and testable. Each one gets an ID that tasks, tests and PRs cite.
     Behavioral criteria: EARS ("When <trigger>, the <system> shall <response>";
       also While <state> / If <unwanted condition>, then ... / Where <feature>)
     or Given / When / Then. Non-behavioral criteria: a threshold that can be checked. -->
- **SC-1** (EARS): When <trigger>, the <system> shall <response>.
- **SC-2** (Given/When/Then): Given <context>, when <action>, then <observable result>.
- **SC-3** (threshold): <e.g. p95 latency of X < 300 ms under N rps>.

## 5. Scope, non-goals and flexibility
- **In scope:**
- **Non-goals (explicitly not doing now):**
<!-- Non-goals matter most for agents: they stop the agent from "helpfully" adding things. -->
- **Fixed (won't change without both owners):** <!-- e.g. the outcome, a legal date, a security constraint -->
- **Flexible (can change to protect the outcome):** <!-- e.g. scope details, UI, delivery date within a window -->
- **Revisit this spec if:** <!-- triggers, e.g. a prototype invalidates A-1, an estimate doubles, a dependency slips -->

## Readiness check
<!-- Don't start building (people or agents) until all five have an answer. -->
- [ ] What problem are we solving? (§1)
- [ ] For whom? (§2)
- [ ] What value do we expect? (§3)
- [ ] How will we measure it? (§3–4)
- [ ] What is fixed and what is flexible? (§5)

## 6. Constraints
<!-- Tech Lead leads this section. Durable, cross-feature rules go in AGENTS.md / steering; list only what's specific here and link the rest. -->
- **Technical / architecture:**
- **Non-functional (performance, availability, accessibility):**
- **Security & privacy:** <!-- data classes, authN/Z, secrets, OWASP concerns -->
- **Compliance / legal:**
- **Dependencies:**

## 7. Assumptions & risks
| ID | Assumption or risk | Impact if wrong | How we validate | Status |
|---|---|---|---|---|
| A-1 | <we believe that...> | <high/med/low + what happens> | <prototype, data query, spike, interview> | open / validated / invalidated |

## 8. Open questions
<!-- Agents: if your work touches one of these, stop and ask. -->
- **Q-1:** <question> — owner: <name> — needed by: <date>

## 9. Validation plan (prototype → evidence)
<!-- Validate value before investing in construction. Prototypes are evidence, not deliverables. -->
- **Riskiest assumption:** A-x
- **Prototype / experiment:** <what, built how (e.g. AI-generated clickable flow), timebox>
- **Who sees it:** <users, stakeholders>
- **Evidence that we proceed:** <signal + threshold>
- **Evidence that we stop or pivot:** <signal>
- **Result:** <filled after validation; link>

## 10. Decisions log
| Date | Decision | Why | Decided by | Affects |
|---|---|---|---|---|
| YYYY-MM-DD | <decision> | <rationale / alternatives considered> | <names> | <SC/A/scope IDs> |

## 11. Change log
<!-- Living spec: every change to value, criteria, scope or constraints gets a line. Scope or criteria changes are a formal renegotiation and need both owners. -->
| Version | Date | Change | Reason (feedback, code, data) | Approved by |
|---|---|---|---|---|
| 0.1.0 | YYYY-MM-DD | Initial draft | — | product + tech |

## 12. Value check
<!-- Filled after delivery, on the date in §3. Compare the result with the target. -->
- **Date checked:**
- **Result vs. target:** <metric: baseline → actual (target)>
- **Verdict:** value delivered / partly / not delivered
- **What we learned & next step:** <update spec, new spec, stop>

## 13. Agent instructions
<!-- Keep this block. It tells coding agents how to use this spec. Durable repo rules live in AGENTS.md / CLAUDE.md. -->
> **For AI coding agents working from this spec:**
> 1. **This spec is the source of intent.** Implement only what is needed to satisfy the success criteria (section 4) within scope (section 5). Do not invent requirements, features or "nice-to-haves". Non-goals are hard boundaries.
> 2. **Ask, don't guess.** If something is ambiguous, contradicts the code, or touches an Open question (section 8), stop and ask the owners. Don't pick an interpretation silently.
> 3. **Respect constraints.** Section 6 and the repo's agent context file (`links.agent_context`) are mandatory. If a constraint seems to block a criterion, report the conflict. Don't work around it.
> 4. **Trace everything.** Each task you plan must map to one or more criterion IDs (SC-n). Each test should name the SC it verifies. Work with no criterion is out of scope.
> 5. **Cite the spec in PRs.** PR descriptions include `Spec: <id>@<version>`, the SC IDs covered, any SC not yet covered, and the assumptions you made.
> 6. **Propose, don't edit, intent.** If implementation shows the spec is wrong or incomplete, propose a change (decision + change-log entry) for the owners. Don't change sections 3–6 yourself.
> 7. **Security first.** Never weaken authentication, authorization, input validation or secret handling to make a criterion pass. Flag it instead.
