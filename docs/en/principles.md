# Principles

Six principles define Value-First. If a team drops one, it's doing something else. That can be fine, but it isn't Value-First.

## 1. Value is explicit before the work starts

Every relevant piece of work starts by saying which problem it solves, for whom, what value it should create and how we'll know. Deadlines and scope still matter. They serve the value, not the other way around.

*Builds on:* the first Agile principle, "early and continuous delivery of valuable software" ([agilemanifesto.org](https://agilemanifesto.org/principles.html)), and outcome-focused product work ([Cagan](https://www.svpg.com/product-vs-feature-teams/); Seiden, *Outcomes Over Output*, 2019).

## 2. The spec is a value contract, and it lives

A spec isn't a document you hand off and forget. It's a short agreement on problem, value, success criteria and constraints. It's versioned with the code and changes when the code or feedback teaches us something. With coding agents, it's also executable input: what isn't written, the agent guesses.

*Builds on:* Specification by Example's "living documents" ([Adzic, 2011](https://gojko.net/books/specification-by-example/)); "spec-anchored" development ([Böckeler, 2025](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)).

## 3. Validate before you build

Before committing, reduce the biggest uncertainty in the cheapest way: a conversation, a technical spike or a prototype. A prototype can be generated with AI and is disposable by default. What it teaches goes into the spec.

*Builds on:* shaping in Shape Up ([Singer, 2019](https://basecamp.com/shapeup)); assumption testing in continuous discovery ([Torres](https://www.producttalk.org/2021/08/product-discovery/)).

## 4. Product and Tech specify together

The spec has two owners. Product owns the problem and the value. The Tech Lead owns feasibility, constraints and making the spec buildable, by people and by agents. The translation work the Tech Lead already does gets a name and a partner.

*Builds on:* the Agile principle "business people and developers must work together daily" ([agilemanifesto.org](https://agilemanifesto.org/principles.html)); the product trio in continuous discovery.

## 5. A changed plan is information, not failure

What's fixed and what's flexible is agreed at the start. When reality changes, the change goes into the spec, with its reason, and everyone can see it. No contracts, no committees: a short, visible record.

*Builds on:* "responding to change over following a plan" ([Agile Manifesto](https://agilemanifesto.org/)); appetite and variable scope in Shape Up.

## 6. People own the outcome; AI speeds it up

Agents help to specify, prototype and build. Decisions, code review, security and technical debt remain human responsibilities. We measure outcomes, not the amount of code or tickets.

*Builds on:* DORA's finding that AI amplifies the system it lands in, and that stability needs attention as throughput grows ([DORA 2024](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report), [DORA 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)).

---

**From v1.** These six replace the five v1 principles. "Value over deadlines" became #1, "Efficient translation" became #2 and "Preliminary technical assessment" became #3. "Formal renegotiation" and "Continuous transparency" merged into #5. #4 replaces the v1 "Value Analyst" role with a pair (see [roles](./roles-and-artifacts.md)). #6 is new. The v1 text is in [docs/archive/v1](../archive/v1/en/principles.md).
