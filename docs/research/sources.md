# Sources: Value-First Development rebuild (annotated bibliography)

Researcher notes, compiled 2026-10-28/29. Each URL below was opened (or the PDF downloaded and text-extracted) unless it is marked **UNVERIFIED** or "(secondary)". Quotes are exact where shown in quotation marks.

**Thesis-point legend** (from BRIEF.md):
- **MERIT**: acknowledge what came before (Waterfall clarity, Agile feedback, Scrum cadence)
- **GAP**: Scrum-as-practiced became ritual, and a gap opened between product spec and development
- **TL**: the Tech Lead fills that gap informally, so make it explicit
- **S1**: the spec became executable input
- **S2**: the gap got more expensive with AI
- **S3**: TL as "specification engineer", shared with product
- **S4**: spec as a living value contract (problem, value, measurable success criteria, constraints)
- **S5**: shorter idea→validation cycle, prototype as spec
- **LAYER**: Value-First sits as a value/alignment layer above SDD tools
- **RISK**: acknowledge AI limits (quality, review, debt, security)
- **VALUE**: value and outcomes over output

---

## 1. Agile and Scrum: origins and merit

**Manifesto for Agile Software Development**, Beck et al., 2001. https://agilemanifesto.org/
- "Individuals and interactions over processes and tools / Working software over comprehensive documentation / Customer collaboration over contract negotiation / Responding to change over following a plan." Followed by: "That is, while there is value in the items on the right, we value the items on the left more."
- Supports: MERIT. The "value in the items on the right" sentence is a good non-adversarial hook: specs/documentation were never declared worthless.

**Principles behind the Agile Manifesto**, 2001. https://agilemanifesto.org/principles.html
- "Our highest priority is to satisfy the customer through early and continuous delivery of valuable software."
- "Business people and developers must work together daily throughout the project."
- "Working software is the primary measure of progress."
- "Simplicity--the art of maximizing the amount of work not done--is essential."
- Supports: VALUE, MERIT. Value-First can be framed as a *return* to principle #1, not a break from Agile.

**The Scrum Guide**, Ken Schwaber & Jeff Sutherland, November 2020. https://scrumguides.org/scrum-guide.html
- "Scrum is a lightweight framework that helps people, teams and organizations generate value through adaptive solutions for complex problems." Pillars: "transparency, inspection, and adaptation". "The Product Goal describes a future state of the product which can serve as a target for the Scrum Team to plan against."
- Supports: MERIT, GAP. The Guide itself is value-centered, so the gap is in *practice*, not in the Guide. This is the correct citation for the README's "Schwaber and Sutherland (2020)".

**"Managing the Development of Large Software Systems"**, Winston W. Royce, Proc. IEEE WESCON, Aug 1970.
- Scanned copy: https://faculty.washington.edu/hazeline/misc/reserve/royce_waterfall.pdf (image-only PDF, text not machine-readable).
- Context: https://en.wikipedia.org/wiki/Winston_W._Royce
- Per Wikipedia, Royce called the single-pass model "risky and invites failure", never used the word "waterfall", and urged passing through the cycle at least twice. Widely reported paper quote: "I believe in this concept, but the implementation described above is risky and invites failure." That exact sentence is **UNVERIFIED** from the primary text (scan not OCR-able here). The "Do it twice" and "Involve the customer" steps are well known but also **UNVERIFIED** against the scan.
- Supports: MERIT. The current README says Waterfall was "formalized by Winston Royce in 1970", which needs this nuance (see Section 7).

**"The State of Agile Software in 2018"**, Martin Fowler (talk transcript), 25 Aug 2018. https://martinfowler.com/articles/agile-aus-2018.html
- "The Agile Industrial Complex imposing methods on people is an absolute travesty." "the team doing work decides how to do it. That is a fundamental agile principle." His three challenges: get rid of imposing process, "Raise the importance of technical excellence", "organize around products."
- Supports: GAP (process imposed instead of chosen), VALUE ("organize around products"). This is a constructive critique by an Agile Manifesto signatory, so it's tone-safe.

**"Dark Scrum"**, Ron Jeffries, 8 Sep 2016. https://ronjeffries.com/articles/016-09ff/defense/
- Jeffries (Manifesto signatory) names "Dark Scrum" as Scrum misapplied by those with power. The second half is constructive: working increments, acceptance tests, TDD, refactoring, CI as the way out.
- Supports: GAP. Use with care. Frame it as "even its co-creators observed…", not as "Scrum failed".

**"Agile is Dead (Long Live Agility)"**, Dave Thomas, 4 Mar 2014. https://pragdave.me/thoughts/active/2014-03-04-time-to-kill-agile.html
- "The word 'agile' has been subverted to the point where it is effectively meaningless." "Agile is not a noun, it's an adjective". Proposes "agility" and says "Agility is harder to misappropriate."
- Supports: GAP (ritual vs. the original intent). Manifesto signatory.

**State of Agile (Digital.ai)**: popularity of Scrum. **UNVERIFIED.** Primary pages were not reachable (403). Secondary sources disagree on Scrum's share (63% / 66% / 81%). Use "Scrum is widely reported as the most adopted agile framework" without a figure, or drop the claim.

## 2. Product thinking

**"Product vs. Feature Teams"**, Marty Cagan (SVPG), 29 Aug 2019. https://www.svpg.com/product-vs-feature-teams/
- Empowered product teams are "focused on and measured by outcomes (rather than output)". Their purpose: "to solve problems in ways our customers love, yet work for our business." Feature teams are "all about output", working from "a prioritized list that is called the roadmap."
- Supports: VALUE, GAP, S4.

**Cagan's books** (SVPG). https://www.svpg.com/books/
- *INSPIRED: How to Create Tech Products Customers Love*, 2nd ed. (Wiley, 2017)
- *EMPOWERED: Ordinary People, Extraordinary Products* (with Chris Jones, 2020)
- *TRANSFORMED: Moving to the Product Operating Model* (2024)
- The page lists titles but not years. The years are from my knowledge and are **UNVERIFIED** on that page.
- Supports: VALUE, S3 (product + engineering share discovery).

**User Story Mapping: Discover the Whole Story, Build the Right Product**, Jeff Patton (with Peter Economy), O'Reilly, 2014.
- https://www.oreilly.com/library/view/user-story-mapping/9781491904893/
- https://jpattonassociates.com/story-mapping/
- Publisher blurb: teams "come away with a shared understanding of what you're attempting to build and why." The table of contents includes "Mapping Helps Big Groups Build Shared Understanding" and ch. 14, "Using Discovery to Build Shared Understanding" (seen via search listings, not opened).
- Patton's site: "Talk about the user's journey through your product by building a simple model that tells your user's story as you do."
- Supports: S1/S4. The documents are not the point; shared understanding is. This is a good counterweight: a spec should *carry* shared understanding.

**Shape Up: Stop Running in Circles and Ship Work that Matters**, Ryan Singer, Basecamp/37signals (2019, free online). https://basecamp.com/shapeup/0.3-chapter-01
- Concepts: **shaping** (make a rough idea concrete before betting), **appetite** ("how much time we want to spend" rather than an estimate), **betting table**, **six-week cycles**, **pitch** (the shaped-project document). Year 2019 from my knowledge; the page shows only a copyright range.
- Supports: S4 (pitch ≈ value contract: problem + appetite + solution elements + rabbit holes + no-gos), S5, VALUE.

**Continuous Discovery Habits**, Teresa Torres, Product Talk LLC, 2021.
- Glossary: https://www.producttalk.org/glossary-discovery-continuous-discovery/
- Basics article: https://www.producttalk.org/2021/08/product-discovery/
- Definition: "weekly touch points with customers by the team building the product" conducting "small research activities in pursuit of a desired outcome." Basics article: teams "engage with customers at least weekly"; two key activities are "customer interviewing and assumption testing."
- Supports: S5, S3 (the product trio includes the tech lead/engineer).

**Outcomes Over Output**, Joshua Seiden, Sense & Respond Press, 2019. https://www.intercom.com/blog/podcasts/josh-seiden-on-why-product-teams-should-focus-on-outcome-vs-output
- Seiden: "an outcome is a change in human behavior that drives business results." Seen via the Intercom interview search snippet and Goodreads (secondary; book not opened).
- Gothelf & Seiden co-wrote *Lean UX* and *Sense & Respond*. Their joint "outcomes" framing is widely cited, but co-authorship of *Outcomes Over Output* is Seiden alone.
- Supports: S4 (measurable success criteria = behavior change), VALUE.

**Impact Mapping**, Gojko Adzic, Provoking Thoughts, 2012. https://www.impactmapping.org/
- "Impact mapping is a lightweight, collaborative planning technique for teams". Its levels are goal (Why) → actors (Who) → impacts (How behavior changes) → deliverables (What). Year 2012 from my knowledge; the site doesn't state it.
- Supports: S4 (linking deliverables to goals), VALUE.

**Specification by Example**, Gojko Adzic, Manning, 2011. https://gojko.net/books/specification-by-example/
- Teams use "agile acceptance testing and behaviour driven development to bridge the communication gap between stakeholders and implementation teams." Specs as "living documents" (quoted from a Jolt Award review on the page).
- Supports: S1, S4 (executable specs predate AI, which is good for tone continuity: "specs as executable input" is not new, AI extends it).

**Kanban: Successful Evolutionary Change for Your Technology Business**, David J. Anderson, Blue Hole Press, 2010.
- Catalog: https://search.ub.tum.de/vufind/Record/DE-604.BV036572231
- Publisher: https://shop.leankanban.com/products/kanban-successful-evolutionary-change-for-your-technology-business
- Visualize work, limit WIP, manage flow; evolutionary change (start with what you do now). Seen via catalog/search listing only.
- Supports: MERIT, LAYER (Value-First can sit on top of Scrum *or* Kanban).

## 3. Delivery performance (DORA)

**Accelerate: The Science of Lean Software and DevOps**, Nicole Forsgren, Jez Humble, Gene Kim, IT Revolution, 27 Mar 2018. https://itrevolution.com/product/accelerate/
- Uses "rigorous statistical methods" to "measure software delivery performance―and what drives it". It is the origin of the four key (DORA) metrics: deployment frequency, lead time for changes, change failure rate, time to restore. The metric names are from my knowledge; the product page doesn't list them.
- Supports: VALUE (measure outcomes, not activity), MERIT.

**2024 Accelerate State of DevOps Report**, DORA / Google Cloud, Oct 2024 (v. 2024.3).
- PDF: https://services.google.com/fh/files/misc/2024_final_dora_report.pdf (text-extracted)
- Blog: https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report (Nathen Harvey & Derek DeBellis, 22 Oct 2024)
- Throughput and stability: "AI adoption is negatively impacting software delivery performance… an estimated 1.5% reduction [in delivery throughput] for every 25% increase in AI adoption… The negative impact on delivery stability is larger (an estimated 7.2% reduction for every 25% increase in AI adoption)."
- "improving the development process does not automatically improve software delivery--at least not without proper adherence to the basics of successful software delivery, like small batch sizes and robust testing mechanisms." "AI does not appear to be a panacea."
- A 25% increase in AI adoption is also associated with +7.5% documentation quality, +3.4% code quality and +3.1% code review speed, and **−2.6% time spent on valuable work** (report figure).
- "More than 75 percent of respondents… rely on AI for at least one daily professional responsibility". "39% of the respondents reported little to no trust in AI-generated code."
- The report also has a "User-centricity drives performance" finding.
- Supports: S2, RISK, VALUE. These are correlational survey estimates, not causal effects, so phrase them as "associated with".

**2025 State of AI-assisted Software Development (DORA Report)**, DORA / Google Cloud, Sep 2025 (v. 2025.2).
- PDF: https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf (text-extracted)
- Blog: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report (Harvey & DeBellis, 23 Sep 2025)
- Methods: nearly 5,000 respondents, survey from 13 Jun to 21 Jul 2025, plus 100+ hours of qualitative data.
- The amplifier finding: "AI's primary role in software development is that of an amplifier. It magnifies the strengths of high-performing organizations and the dysfunctions of struggling ones." "Without this foundation, AI creates localized pockets of productivity that are often lost to downstream chaos."
- Adoption and trust: 90% use AI at work. More than 80% believe it increased productivity. "30% report little or no trust in the code generated by AI".
- Throughput and stability: "AI adoption now improves software delivery throughput, a key shift from last year. However, it still increases delivery instability."
- The **DORA AI Capabilities Model**, seven capabilities (exact names from the report): **Clear and communicated AI stance; Healthy data ecosystems; AI-accessible internal data; Strong version control practices; Working in small batches; User-centric focus; Quality internal platforms.**
- User-centric focus: "in the absence of a user-centric focus, AI adoption has a negative impact on team performance." "Without a user-centric focus, AI adoption is unlikely to help teams. It may even harm them." It is measured by agreement with "creating value for users is their focus" and two related items.
- Value stream management: "VSM, the practice of visualizing, analyzing, and improving the flow of work from idea to customer, acts as a force multiplier for AI, ensuring that local productivity gains translate into measurable improvements in team and product performance."
- Platforms: 90% of organizations have adopted platform engineering.
- Seven team profiles, from "harmonious high-achievers" to "legacy bottleneck".
- Supports: **core evidence for the whole thesis.** VALUE, S2, S4, LAYER (Value-First ≈ the user-centric + VSM capabilities), RISK. Companion page: https://dora.dev/ai/capabilities-model/report/ (last updated 25 Nov 2025).

## 4. AI and specifications

**"Spec-driven development with AI: Get started with a new open source toolkit"**, Den Delimarsky (GitHub), 2 Sep 2025. https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/
- Specs as "living, executable artifacts that evolve with the project". The shift from "code is the source of truth" to "intent is the source of truth". Agents are "more like literal-minded pair programmers". Four phases: Specify → Plan → Tasks → Implement, with checkpoints. "your role isn't just to steer. It's to verify."
- Supports: **S1, S2** ("literal-minded" = AI executes what's written), RISK (human verification), LAYER.

**GitHub Spec Kit** (repo), GitHub, MIT license. https://github.com/github/spec-kit
- SDD: "Define what to build and why, then turn the specification into a plan, tasks, and working code."
- Commands at the time of checking: `/speckit-constitution`, `-specify`, `-plan`, `-tasks`, `-implement`, `-converge`. Older docs use the dotted form `/speckit.specify`.
- Extensions include "idea assessment" (intake → research → define → shape → decide: go / needs-clarification / kill).
- About 144k stars on 2026-10-29. Supports 30+ agents (per search; **UNVERIFIED** exact count).
- Supports: LAYER. Note that Spec Kit now includes an idea-assessment/go-kill step, which overlaps with value framing. Position Value-First as the *why/value* upstream that feeds `/specify`.

**Kiro: Specs**, AWS (Kiro IDE). https://kiro.dev/docs/specs/
- Specs are "structured artifacts that formalize the development process for features and bug fixes". Three files: `requirements.md` (user stories + acceptance criteria; `bugfix.md` for bugs), `design.md` (architecture, sequence diagrams), `tasks.md` (trackable implementation plan).
- EARS notation: https://kiro.dev/docs/specs/concepts says requirements are written as "user stories with acceptance criteria in EARS notation" (via search snippet, not opened). The pattern is `WHEN [condition/event] THE SYSTEM SHALL [expected behavior]`. EARS background: https://en.wikipedia.org/wiki/Easy_Approach_to_Requirements_Syntax (Mavin et al., Rolls-Royce, 2009).
- Supports: S1, S4 (testable acceptance criteria), LAYER.

**Thoughtworks Technology Radar: "Spec-driven development"**, Techniques, **Assess**, Nov 2025 (Vol. 33). https://www.thoughtworks.com/radar/techniques/spec-driven-development
- Starts "with a structured functional specification", then breaks it down into pieces, solutions and tasks. Names Kiro, spec-kit and Tessl.
- Cautions: workflows are "elaborate and opinionated". Some tools produce "lengthy spec files that are hard to review". It's unclear who the intended user of generated PRDs/user stories is. There is a possible "bitter lesson": handcrafting detailed rules for AI doesn't scale.
- "Vol. 33" is from secondary sources. The page only shows "Nov 2025" and that the blip is no longer on the current edition.
- Supports: LAYER, RISK. SDD is promising but immature, so Value-First should not over-claim.

**Thoughtworks Technology Radar: "AGENTS.md"**, Techniques, **Trial**, Nov 2025. https://www.thoughtworks.com/radar/techniques/agents-md
- "AGENTS.md is a common format for providing instructions to AI coding agents working on a project." "Essentially a README file for agents".
- Supports: S1, LAYER.

**Thoughtworks Technology Radar: "Context engineering"**: **Adopt** in Vol. 34 (Apr 2026), Assess in Nov 2025. https://www.thoughtworks.com/radar/techniques/context-engineering
- "Context engineering has evolved from an optimization tactic into a foundational architectural concern".
- **Vol. 34 themes** (https://www.thoughtworks.com/radar, current volume as of 2026-10-29): "Putting coding agents on a leash". Feedforward controls (Agent Skills, spec-driven development) guide agents before they act; feedback controls (linters, tests, mutation testing) catch failures. The volume also warns of "codebase cognitive debt".
- SDD's ring in Vol. 34 is **UNVERIFIED** (a secondary source says still Assess).
- Supports: S1, LAYER, RISK. Note that Vol. 35 may publish around Nov 2026, so re-check before release.

**"Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl"**, Birgitta Böckeler (Thoughtworks), martinfowler.com, 15 Oct 2025. https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
- Three levels:
  - **spec-first**: "A well thought-out spec is written first, and then used in the AI-assisted development workflow"
  - **spec-anchored**: "The spec is kept even after the task is complete"
  - **spec-as-source**: "only the spec is edited by the human, the human never touches the code"
- Observations: Kiro produced 4 user stories / 16 acceptance criteria for a small bug ("overkill"). Spec-kit's markdown is "repetitive and tedious to review". Tessl output varied between runs (non-determinism). She is skeptical of heavy up-front spec design and prefers reviewing code over markdown. Parallel drawn with MDD.
- Supports: **S4** (Value-First's "living spec" = spec-anchored), RISK, and tone: Value-First should advocate *right-sized* specs, not big up-front design.

**AGENTS.md**. https://agents.md/
- "A simple, open format for guiding coding agents". "used by over 60k open-source projects". "AGENTS.md is now stewarded by the Agentic AI Foundation under the Linux Foundation."
- Supports: S1, LAYER.

**Claude Code docs: "How Claude remembers your project" (CLAUDE.md)**, Anthropic. https://code.claude.com/docs/en/memory
- CLAUDE.md files are "markdown files that give Claude persistent instructions for a project". Claude "can also read a repository's AGENTS.md files". Claude treats them "as context, not enforced configuration". "The more specific and concise your instructions, the more consistently Claude follows them." "target under 200 lines per CLAUDE.md file."
- Supports: S1, S4 (concise and specific beats long), RISK (instructions aren't guarantees).

**"Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity"**, METR, 10 Jul 2025. https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- RCT with 16 experienced OSS developers and 246 real issues in their own repos: with AI tools they "take 19% longer". They forecast a 24% speedup and afterwards still believed in a 20% speedup.
- Caveats from METR: small sample; a snapshot of early-2025 tools. The page now labels these results out of date.
- Supports: RISK (perception vs. measured), S2.

**"We are Changing our Developer Productivity Experiment Design"**, METR, 24 Feb 2026. https://metr.org/blog/2026-02-24-uplift-update/
- The follow-up experiment (from Aug 2025) gives "an unreliable signal" because developers increasingly refuse to work without AI (selection effects). Raw estimates: returning developers −18% time change (CI −38% to +9%), new recruits −4% (CI −15% to +9%). METR believes developers are likely more sped up in early 2026 but calls its data "only very weak evidence".
- Supports: tone. **Do not cite the 19% figure without this update.** Recommended framing: "evidence on individual productivity is mixed and evolving."

**"How much does AI impact development speed? An enterprise-based randomized controlled trial"**, Paradis et al. (Google), arXiv:2410.12944, Oct 2024 (rev. Nov 2024). https://arxiv.org/abs/2410.12944
- An RCT with 96 Google engineers found AI shortened task time by "about 21%, although our confidence interval is large." Internal tooling, summer 2024.
- Supports: balance (AI helps in some settings).

**"The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers"**, Cui, Demirer, Jaffe, Musolff, Peng, Salz, *Management Science* (2025). https://pubsonline.informs.org/doi/fpi/10.1287/mnsc.2025.00535 and SSRN https://papers.ssrn.com/abstract=4945566
- Microsoft, Accenture and a Fortune 100 company; 4,867 developers; +26.08% (SE 10.3%) completed tasks with Copilot. Gains are larger for junior and short-tenure developers. Code quality was not measured.
- From search snippets/abstract; I did not open the full text (**secondary**).
- Supports: balance. Notice it measures output (tasks), not value.

**Stack Overflow Developer Survey 2025: AI section**, Stack Overflow, 2025. https://survey.stackoverflow.co/2025/ai
- 84% "are using or planning to use AI tools" (n = 33,662).
- Trust in AI accuracy (n = 33,244): highly trust 3.1%, somewhat trust 29.6%, somewhat distrust 26.1%, highly distrust 19.6%. That's about 33% trust vs. 46% distrust.
- Top frustration: "AI solutions that are almost right, but not quite" 66%. "Debugging AI-generated code is more time-consuming" 45.2% (n = 31,476).
- Supports: **S2** ("almost right" = what a vague spec produces), RISK.

**"AI Copilot Code Quality: 2025 Look Back at 12 Months of Data"**, GitClear, 2025. https://www.gitclear.com/ai_assistant_code_quality_2025_research
- 211M changed lines (2020–2024). Copy/pasted (cloned) lines rose from 8.3% of changed lines (2021) to 12.3% (2024). Moved/refactored lines fell from about 25% to under 10%. "copy/paste exceeds moved code for first time in history." Short-term churn rising.
- The "8x duplicated blocks" figure appears in press coverage, not on this page, so use 4x / 8.3%→12.3%.
- Caveat: these are correlational trends, not line-level attribution to AI.
- Also exists: GitClear 2026 "Write-Only Mode: AI Code Quality in 2026" https://www.gitclear.com/write_only_mode_ai_research (**not opened**).
- Supports: RISK (technical debt).

**2025 GenAI Code Security Report**, Veracode, press release 30 Jul 2025. https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/
- AI-generated code "introduces security vulnerabilities in 45 percent of cases" across 80 curated tasks and 100+ LLMs. Java failure rate "over 70 percent". "larger models do not perform significantly better than smaller models."
- Vendor research; an October 2025 update exists at https://www.veracode.com/resources/2025-genai-code-security-report/ (not opened).
- Supports: RISK (security, human review).

## 5. The Tech Lead role

**"The Definition of a Tech Lead"**, Patrick Kua, patkua.com, 2020. https://www.patkua.com/blog/the-definition-of-a-tech-lead/
- "A Tech Lead is a software engineer responsible for leading a team and alignment of the technical direction." The Product Manager focuses on the "What", the Tech Lead on the "How". Describes meetings with product people to confirm the architecture supports future work.
- Supports: TL, S3.

**Talking with Tech Leads: From Novices to Practitioners**, Patrick Kua, Leanpub (2015; year **UNVERIFIED** on the page). https://leanpub.com/talking-with-tech-leads
- "Discover how more than 35 Tech Leads find the delicate balance between the technical and non-technical worlds."
- Supports: TL (bridging technical and non-technical worlds).

**Staff Engineer: Leadership Beyond the Management Track**, Will Larson, 2021: "Staff archetypes". https://staffeng.com/guides/staff-archetypes/
- "The Tech Lead guides the approach and execution of a particular team." "Tech Leads are the most common Staff archetype". The other archetypes are Architect, Solver and Right Hand.
- Supports: TL.

**The Manager's Path: A Guide for Tech Leaders Navigating Growth and Change**, Camille Fournier, O'Reilly, 2017.
- O'Reilly page returned 403. Secondary: https://www.welcometothejungle.com/en/articles/btc-manager-path-camille-fournier
- Ch. 3 "Tech Lead": the role combines "systems architect, business analyst, project planner, software developer, and team leader" (secondary quote; book not opened).
- Supports: **TL**. "Business analyst" inside the TL role is direct support for "the TL informally absorbed the systems analyst's translation job".

## 6. Cost of rework and requirements: contested evidence (handle carefully)

**"Software Defect Reduction Top 10 List"**, Barry Boehm & Victor Basili, *IEEE Computer* 34(1):135–137, Jan 2001. DOI 10.1109/2.962984. Copy: https://condor.depaul.edu/dmumaugh/readings/handouts/SE425/J81.pdf (text-extracted)
- Item 1: "Finding and fixing a software problem after delivery is often 100 times more expensive than finding and fixing it during the requirements and design phase." The same item qualifies that for "small, noncritical software systems" the ratio may "be more like 5:1 than 100:1".
- Supports: S2, if it's used at all, and **only with the 5:1 qualifier**.

**The Leprechauns of Software Engineering**, Laurent Bossavit, Leanpub (2012–2015). https://leanpub.com/leprechauns
- Examines "the cost-of-change curve" and the "defect-cost-increase curve" (ch. 10, "The cost of defects: an illustrated history"; Appendix B), and assesses "the *real* weight of the evidence". It argues such "cornerstone truths" are largely folklore built on weak or misquoted data. His exact verdict wording is in the book. The interview/TechWell pages returned 403, so detailed quotes are **UNVERIFIED**.
- Supports: tone/accuracy. **Do not state "cost increases exponentially" as fact.**

**"The Cost of Change Curve Is Outdated"**, Mountain Goat Software (Mike Cohn), last updated 3 Mar 2026. https://www.mountaingoatsoftware.com/blog/the-cost-of-change-curve-is-outdated
- "The curve hasn't disappeared, but it's far flatter than most people assume." Agile, CI and modularity flattened it. With AI, "the primary cost of change increasingly becomes feedback delay, not development effort."
- Supports: **S2/S5.** It directly backs the Value-First angle: the expensive part is now misunderstanding value, not typing code.

**"A spiral model of software development and enhancement"**, Barry Boehm, *IEEE Computer* 21(5):61–72, May 1988. DOI 10.1109/2.59 (verified via Crossref)
- This is what "Boehm (1988)" refers to. It's the risk-driven, iterative spiral model, **not** a cost-of-defects study.
- Supports: MERIT (iterative, risk-driven thinking predates Agile).

**"The rise and fall of the Chaos report figures"**, J. Laurenz Eveleens & Chris Verhoef, *IEEE Software* 27(1):30–36, Jan 2010. DOI 10.1109/MS.2009.154 (verified via Crossref)
- The paper argues the Standish figures are meaningless because they average estimates with unknown bias, and that they didn't match the authors' case data (abstract via search snippet).
- See also Robert L. Glass, "The Standish report: does it really describe a software crisis?", *CACM* 49(8):15–16, Aug 2006. DOI 10.1145/1145287.1145301 (verified via Crossref).
- Supports: tone/accuracy. **Avoid citing CHAOS success/failure percentages.**

## 7. Unsourced or incorrect claims in the CURRENT repo docs

| Location | Current claim | Problem | Suggested sourced version |
|---|---|---|---|
| `README.md:47` and `translations/README.en.md:47` | "As highlighted by Boehm (1988), the cost of correcting a defect increases exponentially as the project progresses." | Boehm 1988 is the **spiral model** paper (IEEE Computer 21(5)), not a cost-of-defects study. "Exponentially" overstates the evidence. The defect-cost data trace to Boehm's *Software Engineering Economics* (1981) and are contested (Bossavit). | "Boehm and Basili (2001) reported that fixing a problem after delivery is *often* 100 times more expensive than during requirements and design — but closer to 5:1 for small, non-critical systems. Others have since argued the curve has flattened with modern practices (Cohn, 2026) and that the original evidence is weaker than its popularity suggests (Bossavit)." Or soften to opinion: "Misunderstandings discovered late tend to cost more than those caught early." |
| Same line | "Pressman (2014) also observed that projects that rigidly follow the Waterfall model frequently fail to meet end-user expectations." | No page or quote. Pressman & Maxim, *Software Engineering: A Practitioner's Approach*, 8th ed. (McGraw-Hill, 2014) exists, but the specific claim is unverified. The latest edition is the 9th (2019 international / 2020 US). | Cite Royce himself, who warned that the single-pass model "invites failure" (via Wikipedia; verify against the primary text), or drop it. If Pressman is kept, the owner must supply the page number from the 8th or 9th edition. |
| `README.md` / `README.en.md:29` | "Waterfall model … formalized by Winston Royce in 1970" | Royce described the sequential model in order to *warn against* the single-pass version, and never used the term "waterfall". | "Royce (1970) described a sequential model — and warned that doing it in a single pass was 'risky and invites failure', recommending iteration." |
| `README.en.md:51` | Scrum "stood out as one of the most adopted" | No source. | Cite Digital.ai *State of Agile* only after verifying the exact figure (**UNVERIFIED** here), or rephrase without the ranking. |
| `README.en.md:67` | "the agile model, by distributing responsibilities, created a gap in the interface between business and technology" | Presented as fact; no source. It's the thesis. | Frame it as the authors' observation/hypothesis. Support with Fournier (TL includes the "business analyst" role), Fowler 2018 (imposed process), Jeffries "Dark Scrum", Cagan's feature teams, and DORA 2025 (user-centric focus as the AI prerequisite). |
| `docs/{pt,en}/case-studies.md` (lines ~66–69, 115–117, 161, 201–203, 242, 285) | "Real case studies" with precise metrics: 40%, 65%, 28%, "$300,000", 70%, 45%, 30%, 60%, 25%, 35% | No organizations, dates or sources. These can't be verified. | Relabel as "illustrative scenarios (fictional)" and remove the precise numbers, or replace them with sourced public cases. Flag for owner approval before deleting. |
| `docs/{pt,en}/templates.md:70–72` | "50% reduction… 70% decrease… 30% increase" | Template example values. Fine if clearly marked as an example. | Mark as "example placeholder values". |
| `docs/en/principles.md:23` / `docs/pt/principles.md:16` | Quote: "It's better to deliver 80% of the value with high quality than 100%…" | Presented as a quote with no author. | Present it as a principle statement (not a quotation), or attribute it to the framework itself. |
| `README.md` badge links | `seu-usuario/fdcv`, `your-username/(DV)` | Placeholders. | `github.com/andrelaf/deliver-value-methodology`. |

## 8. Quick "safe claims" list for writers

1. AI use is near-universal among developers. DORA 2025: 90%. Stack Overflow 2025: 84% use or plan to use.
2. Trust is low. DORA 2025: 30% report little or no trust in AI code. Stack Overflow 2025: about 46% distrust vs. about 33% trust accuracy, and 66% are frustrated by "almost right" answers.
3. DORA 2025: AI is an amplifier. A user-centric focus is one of the seven capabilities, and without it AI adoption hurts team performance. VSM acts as a force multiplier.
4. DORA 2024: AI adoption was associated with lower delivery throughput (−1.5%) and stability (−7.2%) per 25% adoption increase. DORA 2025: throughput turned positive, instability persists.
5. Individual-productivity evidence is mixed. Google RCT about −21% time; field experiments +26% tasks; METR 2025 +19% time, with METR's own 2026 caveat that this is outdated.
6. SDD is real but immature. Thoughtworks put it in Assess (Nov 2025) and Böckeler raises review-burden and non-determinism concerns. AGENTS.md is in Trial and is now under the Linux Foundation's Agentic AI Foundation.
7. Security and quality risks are measurable: Veracode found flaws in 45% of cases; GitClear shows cloning up and refactoring down.
