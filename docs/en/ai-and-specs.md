# Specs in the AI era

> Sources checked on 2026-10-28. Figures are quoted with their scope; where the evidence is mixed, we say so.

For years, most teams treated the gap between "what product asked for" and "what the code needs to know" as a normal part of the job. A story arrived a little vague, someone (often the Tech Lead) asked three questions in a hallway, filled in the blanks from experience, and the work moved on. That informal translation is one of the quiet strengths of good teams.

Coding agents change the economics of that gap. This page explains how, what the industry is building in response, and where Value-First fits. It's an invitation to update how we think about specs. It isn't a verdict on any earlier way of working: Waterfall gave us the discipline of writing things down, Agile gave us short feedback loops, and Scrum gave us a steady cadence. We want to keep all three.

---

![Before and now: from product to spec to code](../../assets/diagrams/before-after-en.svg)

## 1. The spec has become executable input

When a person reads a spec, they interpret it. When an agent reads a spec, it acts on it, often producing hundreds of lines of plausible code in minutes.

GitHub's introduction to its open-source Spec Kit puts it directly. Language models are "exceptional at pattern completion, but not at mind reading." A request like "add photo sharing to my app" leaves the model guessing at "potentially thousands of unstated requirements" ([GitHub Blog, Sep 2025](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/)). The same post describes specs as "living, executable artifacts" and "the shared source of truth".

The practical consequence: **with an agent in the loop, the quality of what gets delivered is bounded by the quality of what was specified.** A vague spec doesn't slow the work down. It produces the wrong thing faster.

## 2. The gap got more expensive

Humans compensate for incomplete specs with conversation, context and intuition. An agent can ask questions only if it is told to, and it executes what is written. What used to be a nuisance becomes a bottleneck.

The evidence on AI and delivery points the same way. AI magnifies whatever system it lands in:

- The [2024 DORA report](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report) found that higher AI adoption went along with better documentation quality, code quality and review speed. It also found that every 25% increase in AI adoption was associated with an estimated **1.5% drop in delivery throughput and a 7.2% drop in delivery stability** (survey correlations, not causal effects). DORA's reading was that AI doesn't replace "the basics of successful software delivery, like small batch sizes and robust testing."
- The [2025 DORA report](https://blog.google/innovation-and-ai/technology/developers-tools/dora-report-2025/) found adoption at 90% and, this time, a link to *higher* throughput. Its central framing is that AI is "a mirror and a multiplier": it helps cohesive organizations and exposes fragmented ones.
- DORA's [AI Capabilities Model](https://cloud.google.com/blog/products/ai-machine-learning/introducing-doras-inaugural-ai-capabilities-model) names **user-centric focus** as one of seven amplifying capabilities: "when users aren't the focus, AI-assisted development teams may just be moving quickly in the wrong direction." Working in small batches is another.

Speed at the keyboard is no longer the scarce resource. Clarity about *what* to build, and *why*, is.

## 3. The Tech Lead as "specification engineer", shared with product

In many teams the Tech Lead already does this work informally: translating, completing, deciding. Value-First proposes making that role **explicit and central**, without leaving the Tech Lead to carry it alone.

- **Product** owns the problem, the expected value and how success will be measured.
- **The Tech Lead** owns the translation into constraints, risks, testable criteria and the context agents need (architecture rules, conventions, non-functional requirements).
- **Both** sign the spec, and both are accountable when it changes.

This matches what practitioners report about working with agents. GitHub's [Spec Kit post](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/) says it plainly: "your role isn't just to steer. It's to verify." Birgitta Böckeler (Thoughtworks) highlights the same line in her [review of SDD tools](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html). Her [article on context engineering](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html) shows how much judgement goes into deciding which context an agent should get. Someone has to own that judgement. We think it should be a pair, not a hero.

## 4. The spec as a value contract, not a document

A Value-First spec isn't a requirements dump. It's a short agreement on four things:

1. **The problem**, and for whom.
2. **The expected value**: an outcome, a metric, a baseline and a target.
3. **Measurable success criteria**: testable statements an agent can map tasks to and a reviewer can check. Behavioral criteria can use [EARS](https://alistairmavin.com/ears/) ("When <trigger>, the <system> shall <response>"), a notation from Rolls-Royce that [Kiro](https://kiro.dev/docs/specs/feature-specs/) also uses, or Given/When/Then.
4. **Technical constraints**: non-functional requirements, security, compliance, architectural limits.

And it's **living**. Böckeler separates three levels of SDD: *spec-first* (the spec is written for one task), *spec-anchored* (the spec is kept and evolves with the feature) and *spec-as-source* (humans edit only the spec) ([martinfowler.com](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)). Value-First aims at **spec-anchored**. The spec stays next to the code, is versioned with it, and changes when code or user feedback teach us something. A decisions log and a change log make that visible. See the [Value Spec template](../../templates/en/value-spec.md).

## 5. A shorter cycle from idea to validation

Agents make prototypes cheap. That opens up a practice we want to make standard: **use a prototype as a form of spec.** A clickable flow or a throwaway implementation, generated in hours, can show product, users and engineers what the words couldn't. It tests the riskiest assumption *before* we invest in production-grade construction.

This also answers a fair critique of SDD (see "Limits and risks" below). The aim isn't to write more before we build. It's to **learn sooner what's worth building, and then write down exactly that.** Prototypes are evidence, not deliverables. They get thrown away, and the spec keeps what they taught us.

---

## State of the art: who does what

| Layer | What it answers | Examples |
|---|---|---|
| **Value & alignment** | *Is this worth building? How will we know? What are the non-negotiables?* | **Value-First** (Value Spec, validation, value check) |
| **Spec-to-code workflow** | *Given the intent, what's the plan, which tasks, what code?* | [GitHub Spec Kit](https://github.com/github/spec-kit): constitution → specify → plan → tasks → implement. [AWS Kiro](https://kiro.dev/docs/specs/): `requirements.md` (EARS) → `design.md` → `tasks.md`, with a requirements-first or design-first variant. [Tessl](https://tessl.io/): explored *spec-as-source* while in beta in 2025 ([Böckeler](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)) and now presents itself as an "agent enablement platform" for skills and context. |
| **Agent context** | *What should every agent session know about this codebase and team?* | [AGENTS.md](https://agents.md/) (open format stewarded by the Agentic AI Foundation under the Linux Foundation; the site reports use by 60k+ open-source projects). [CLAUDE.md](https://code.claude.com/docs/en/memory) (Claude Code, which can also read AGENTS.md). [Cursor rules](https://cursor.com/docs/context/rules) (`.cursor/rules/*.mdc`, plus AGENTS.md). [Kiro steering](https://kiro.dev/docs/steering/) (`product.md`, `tech.md`, `structure.md`). |
| **Industry assessment** | *How mature is this?* | Thoughtworks Technology Radar (Nov 2025): [spec-driven development in **Assess**](https://www.thoughtworks.com/radar/techniques/spec-driven-development) and [AGENTS.md in **Trial**](https://www.thoughtworks.com/radar/techniques/agents-md). |

**Where Value-First sits.** Value-First is the **value and alignment layer above** these tools, not a competitor to them:

- **Value-First** decides *what is worth building and how we'll know it worked*: problem, expected value, success criteria, constraints, validation plan.
- **SDD tools** (Spec Kit, Kiro and others) turn that into plan, tasks and code.
- **Agent context files** (AGENTS.md, CLAUDE.md, rules, steering) carry the durable constraints and conventions into every session.

In practice, a Value Spec can serve as the input to Spec Kit's `specify` step or to Kiro's requirements phase. Its constraints and non-negotiables can feed a Spec Kit *constitution* or a steering or AGENTS.md file. Value-First doesn't replace any of these. It makes sure what goes into them is worth building.

---

## Limits and risks

We'd rather be honest than persuasive here.

- **Productivity gains aren't guaranteed.** In METR's [2025 randomized controlled trial](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/), 16 experienced open-source developers took **19% longer** with AI tools, while believing AI had sped them up by about 20%. METR's [February 2026 update](https://metr.org/blog/2026-02-24-uplift-update/) with late-2025 tools points toward speedups, but every confidence interval includes zero, and METR itself calls the new data unreliable because of selection effects. The honest summary: perception isn't measurement, and the outcome depends on context.
- **Quality and security.** Veracode's [2025 GenAI Code Security Report](https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/) found that generated code introduced security vulnerabilities in 45% of cases, testing 80 curated coding tasks across 100+ models. It's a vendor benchmark, not a universal rate, but it's a reason to keep security constraints explicit in the spec and to keep scanning.
- **Trust and review burden.** In [Stack Overflow's 2025 survey](https://survey.stackoverflow.co/2025/ai), 46% of developers said they don't trust the accuracy of AI output, and 45% named time-consuming debugging of AI code as a key frustration. SDD tools add their own review load: Böckeler found Spec Kit generating many verbose markdown files she would rather not review, and Kiro turning a small bug into four user stories with 16 acceptance criteria ("a sledgehammer to crack a nut").
- **"Vibe coding".** Andrej Karpathy [coined the term](https://x.com/karpathy/status/1886192184808149383) for a style where you "forget that the code even exists". It's fine for throwaway prototypes and risky for production. Simon Willison's [rule](https://simonwillison.net/2025/Mar/19/vibe-coding/) is a good default: don't commit code you couldn't explain to someone else.
- **Spec drift and ignored specs.** Most tools are *spec-first* in practice, and long-term spec maintenance is often left vague ([Böckeler](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)). Agents also ignore or over-apply instructions, and context files are guidance, not enforcement. Claude Code's docs say they are treated "as context, not enforced configuration" ([docs](https://code.claude.com/docs/en/memory)). Böckeler warns of an "illusion of control" ([context engineering](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html)). Thoughtworks adds that "handcrafting detailed rules for AI ultimately doesn't scale" and that "we may be relearning a bitter lesson" ([Radar](https://www.thoughtworks.com/radar/techniques/spec-driven-development)).
- **The waterfall-revival critique.** François Zaninotto argues that SDD revives heavy upfront documentation and that "coding agents supercharge Agile" when used in small increments ([Marmelab, Nov 2025](https://marmelab.com/blog/2025/11/12/spec-driven-development-waterfall-strikes-back.html)). Marc Brooker (AWS) answers that SDD "isn't about pulling designs *up-front*, it's about pulling designs *up*" ([Apr 2026](https://brooker.co.za/blog/2026/04/09/waterfall-vs-spec)). We take the critique seriously.

**How Value-First avoids rebuilding waterfall:**

1. **Small, value-scoped specs.** One spec per outcome or slice of value, not per project. Aim for one page. Past two, split it. (This is DORA's "small batches" applied to specs.)
2. **Prototype first when the value is uncertain.** Validate the riskiest assumption cheaply, then specify what you learned.
3. **Living, not frozen.** Specs are versioned next to the code, with a decisions log and a change log. Principle 5 ("a changed plan is information, not failure") is how a spec changes: with a reason, visibly, and both owners agree.
4. **Value before volume.** The spec states the problem, the value and the evidence. Plans and tasks are generated downstream, so we don't hand-write them upfront.
5. **Humans verify.** Every agent-produced change is traced to a success-criterion ID and reviewed by a person.

---

## How to start (one feature, one week)

1. **Pick one upcoming feature** with real business value and some uncertainty.
2. **Write a Value Spec together**: product and Tech Lead, in one session, using the [template](../../templates/en/value-spec.md). Keep it short.
3. **Name the riskiest assumption** and validate it with the cheapest prototype or spike (often AI-generated) before committing to build.
4. **Add or tidy an `AGENTS.md`** (or CLAUDE.md, rules or steering) with the durable constraints: build and test commands, architecture rules, security must-haves.
5. **Feed the spec to your SDD tool or agent** and require tasks and PRs to cite success-criterion IDs.
6. **Review against the spec, not just the diff.** Did we meet the criteria? Did the spec need to change? Log it.
7. **Measure the value** you said you'd measure, and run a short retro on what the spec lacked.

---

### Sources

- GitHub Blog — [Spec-driven development with AI](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/) (Den Delimarsky, 2 Sep 2025)
- [GitHub Spec Kit repository](https://github.com/github/spec-kit)
- Kiro — [Specs](https://kiro.dev/docs/specs/), [Feature specs / EARS](https://kiro.dev/docs/specs/feature-specs/), [Steering](https://kiro.dev/docs/steering/)
- [Tessl](https://tessl.io/)
- Birgitta Böckeler — [Understanding Spec-Driven Development: Kiro, spec-kit, and Tessl](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) (15 Oct 2025); [Context Engineering for Coding Agents](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html) (5 Feb 2026)
- Thoughtworks Technology Radar — [Spec-driven development (Assess)](https://www.thoughtworks.com/radar/techniques/spec-driven-development); [AGENTS.md (Trial)](https://www.thoughtworks.com/radar/techniques/agents-md) (Nov 2025)
- [AGENTS.md](https://agents.md/) · [Claude Code memory / CLAUDE.md](https://code.claude.com/docs/en/memory) · [Cursor rules](https://cursor.com/docs/context/rules)
- DORA — [2024 report announcement](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report); [2025 report summary](https://blog.google/innovation-and-ai/technology/developers-tools/dora-report-2025/); [AI Capabilities Model](https://cloud.google.com/blog/products/ai-machine-learning/introducing-doras-inaugural-ai-capabilities-model)
- METR — [Early-2025 RCT](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/); [Feb 2026 design update](https://metr.org/blog/2026-02-24-uplift-update/)
- [Veracode 2025 GenAI Code Security Report (press release)](https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/)
- [Stack Overflow 2025 Developer Survey (press release)](https://stackoverflow.co/company/press/archive/stack-overflow-2025-developer-survey/)
- [EARS — Alistair Mavin](https://alistairmavin.com/ears/)
- Simon Willison — [Not all AI-assisted programming is vibe coding](https://simonwillison.net/2025/Mar/19/vibe-coding/)
- François Zaninotto — [Spec-Driven Development: The Waterfall Strikes Back](https://marmelab.com/blog/2025/11/12/spec-driven-development-waterfall-strikes-back.html); Marc Brooker — [Spec Driven Development isn't Waterfall](https://brooker.co.za/blog/2026/04/09/waterfall-vs-spec)
