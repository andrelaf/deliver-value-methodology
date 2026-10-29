# Agent context snippet

Paste the block below into your `AGENTS.md`, `CLAUDE.md`, `.cursor/rules/*.mdc` or Kiro steering file. Adjust the path to where your Value Specs live.

Context files are guidance, not enforcement. Agents can still ignore them, so human review stays in place ([Claude Code docs](https://code.claude.com/docs/en/memory); [Böckeler, 2026](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html)).

```markdown
## Value Specs (Value-First Development)

This project uses Value Specs as the source of intent: `specs/VS-*.md`.

Before you plan or change code for a feature:
1. Find the Value Spec for it (ask if there isn't one). Read sections 1–9.
2. Implement only what the success criteria (SC-n) require, within scope.
   Non-goals are hard boundaries.
3. If something is ambiguous, contradicts the code, or touches an Open
   question, stop and ask. Don't pick an interpretation silently.
4. Map every task and test to one or more SC IDs. Work with no SC is out of scope.
5. In PR descriptions, include `Spec: <id>@<version>`, the SC IDs covered,
   the SC IDs not yet covered, and the assumptions you made.
6. Don't edit the spec's problem, value, criteria, scope or constraints
   yourself. Propose the change for the owners (Product + Tech Lead).
7. Never weaken authentication, authorization, input validation or secret
   handling to make a criterion pass. Flag it instead.
```
