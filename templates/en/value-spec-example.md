---
# Fictional, illustrative example. Company, names and numbers are invented.
id: VS-014
title: "Customers download their own invoices"
status: ready
version: 1.1.0
owners:
  product: "Marina (Product Manager)"
  tech: "Rafael (Tech Lead)"
created: 2026-09-01
updated: 2026-09-12
links:
  prototype: "<link to clickable prototype>"
  issue: "BILL-231"
  design: "specs/014-invoice-download/plan.md"
  agent_context: "AGENTS.md"
  dashboard: "<link to support dashboard>"
---

# Customers download their own invoices

## 1. Problem
B2B customers can't get past invoices from the portal. They open support tickets, and "send me invoice X" is the top ticket category in our helpdesk (internal report, Aug 2026). Support spends time on a task with no judgement involved, and customers wait.

## 2. Who & context
- **Primary users:** finance contacts at customer accounts (role `billing_admin`).
- **Context / trigger:** month-end closing, audits.
- **Systems touched:** customer portal (web), billing service (invoice PDFs already stored).

## 3. Expected value
| Outcome | Metric | Baseline | Target | By when | Measurement method |
|---|---|---|---|---|---|
| Customers self-serve invoices | Weekly "invoice request" tickets | ~120/week (helpdesk tag, Aug 2026, illustrative) | ≤ 40/week | 6 weeks after release | Helpdesk tag report, reviewed weekly by Marina |

## 4. Success criteria
- **SC-1** (EARS): When a `billing_admin` opens *Billing › Invoices*, the portal shall list that account's invoices from the last 24 months, newest first.
- **SC-2** (EARS): When the user selects *Download* on an invoice, the portal shall deliver the stored PDF unchanged.
- **SC-3** (EARS): If a user without `billing_admin` requests an invoice URL, then the portal shall return 403 and log the attempt.
- **SC-4** (threshold): The invoice list loads in under 1 s at p95 for accounts with up to 500 invoices.

## 5. Scope, non-goals and flexibility
- **In scope:** list + download of existing PDFs.
- **Non-goals:** editing invoices, payment, CSV export, invoices older than 24 months.
- **Fixed:** the outcome (fewer invoice tickets); account-scoped access; no direct bucket access.
- **Flexible:** list layout; the 24-month window (could shrink if SC-4 is at risk); release date within September.
- **Revisit this spec if:** tickets don't drop by week 3, or the billing API can't meet SC-4.

## 6. Constraints
- **Technical:** read PDFs through the billing service API. No direct bucket access from the portal.
- **Security & privacy:** signed download URLs expire in 5 min. Invoices are scoped by account ID server-side.
- **Compliance:** download events are retained per the audit policy (see AGENTS.md › Audit).

## 7. Assumptions & risks
| ID | Assumption or risk | Impact if wrong | How we validate | Status |
|---|---|---|---|---|
| A-1 | Finance contacts would use the portal instead of emailing support | High: value not realized | Prototype shown to 6 customers | validated (5/6) |
| A-2 | Billing API can serve 500-item lists fast enough | Med: SC-4 at risk | 1-day spike | validated |

## 8. Open questions
- *(none open; Q-1 on date filters resolved, see decisions)*

## 9. Validation plan
- **Riskiest assumption:** A-1.
- **Prototype:** AI-generated clickable flow with fake data, 1-day timebox.
- **Evidence to proceed:** ≥ 4 of 6 customers say they would stop emailing support.
- **Result:** 5/6 yes. Two asked for date filtering (deferred, see D-2).

## 10. Decisions log
| Date | Decision | Why | Decided by | Affects |
|---|---|---|---|---|
| 2026-09-08 | Use signed URLs, 5 min expiry | Avoid exposing bucket; matches security baseline | Rafael + security | SC-2, constraints |
| 2026-09-12 | Date filter deferred to VS-015 | Not needed for the ticket reduction; keeps slice small | Marina + Rafael | Scope |

## 11. Change log
| Version | Date | Change | Reason | Approved by |
|---|---|---|---|---|
| 1.0.0 | 2026-09-08 | Ready for build | Prototype validated A-1 | Marina, Rafael |
| 1.1.0 | 2026-09-12 | Added SC-3 (403 + log); date filter → non-goal | Security review; prototype feedback | Marina, Rafael |

## 12. Value check
- *(Scheduled 6 weeks after release. Not filled yet.)*

## 13. Agent instructions
> Follow the standard Value Spec agent instructions (template section 13). Feature-specific: never call the storage bucket directly. Every PR cites `Spec: VS-014@1.1.0` and the SC IDs it covers.
