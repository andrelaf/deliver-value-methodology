# Name collision research: "Value-First Development" / "Value-First"

Researcher notes, checked 2026-10-28/29. Every item below was opened or queried directly unless it is marked **UNVERIFIED**.

## Verdict

- **Risk: LOW-MEDIUM.** "Value-First Development", the full name, is **low** risk: I found no methodology, book, product or GitHub project under that exact name. "Value-First", the short form on its own, is **medium** risk: "ValueFirst" is an established commercial brand in software-adjacent markets, and the phrase is a generic marketing term.
- **Recommendation: keep the name, but always use the qualified form.** Use "Value-First Development" as the canonical name. Use "Value-First" only after the full name has appeared, and never as "ValueFirst" (one word, which is the Tanla brand spelling). Don't build a logo or wordmark on "ValueFirst" alone. Use a GitHub repo or org name with "development", or keep the existing repo.
- A formal trademark search was **not done** (see the Limits section). Before any commercial use, such as paid training or certification, the owner should run a USPTO, EUIPO and INPI (Brazil) search.

## Findings

### 1. Exact name "Value-First Development"
- **Web search**: there's no established methodology, book or framework with this name. Search returned only loosely related work:
  - Boehm's Value-Based Software Engineering (VBSE)
  - The "Speedplay" values-first process (arXiv 2108.05624, https://arxiv.org/pdf/2108.05624, about *human* values, not business value)
  - Blog posts on "value-driven development" (e.g. https://sep.com/blog/value-driven-development/)
- **GitHub**: a repo search for `"value first development"` returned `total_count: 0` (GitHub API, 2026-10-29).
- **Domains** (RDAP):
  - `valuefirstdevelopment.com`: RDAP 404 at Verisign (appears **unregistered**).
  - `value-first.dev`: RDAP 404 at Google Registry (appears **unregistered**).
  - `value-first-development.dev` and `valuefirstdev.com`: RDAP 404 (appear unregistered).
  - `valuefirst.dev`: **registered 2026-08-23** through Name.com, expires 2027-08-23. It doesn't resolve in DNS (no site). The owner is unknown, so check whether the project owner registered it.

### 2. "ValueFirst" (one word): the main commercial collision
- **ValueFirst Digital Media (India)** is a CPaaS company offering SMS, WhatsApp Business, RCS, email and voice APIs, conversational AI and marketing automation. Its site https://www.vfirst.com/ states it is "part of Tanla Platforms Limited". It still exists and is active as of Oct 2026.
- **Ownership history:** Twilio acquired it, then Tanla bought "ValueFirst India" from Twilio in 2023. Tanla newsroom: https://tanla.com/newsroom/tanla-acquires-valuefirst-india-from-twilio. I didn't open that page. The date and price (all-cash, about $42M, closed July 2023) come from search snippets and are **UNVERIFIED** in detail.
- **ValueFirst Management Consulting Ltd.** (Uetikon am See, Switzerland) owns `valuefirst.com`, registered 1997-09-04. I opened the site to confirm this.
- `value-first.com` was registered 2014-03-17 and is still registered. I didn't identify the owner or the content.
- Why this matters: the Tanla brand sits in B2B software and APIs, so customers and SEO overlap partly. Its spelling and domain are different, though, and it's a messaging product, not a methodology. The risk of confusion is moderate for the short form and low for the full name.

### 3. "Value-First" as a phrase in software and consulting
- **Value-Driven Solutions** (South Africa) is a software process consultancy that markets a "Value-First Engineering Approach". The only source is a beBee profile (https://bebee.com/za/companies/value-driven-solutions), seen in a search snippet. It's a small firm and the phrase is descriptive. Risk is low.
- **One Network Enterprises** (now part of Blue Yonder) has a white paper titled "Putting Value First: An Innovative Approach to Enterprise Software Implementations". Search snippets describe a "Value First" methodology for enterprise software implementations. **UNVERIFIED**: the page returned HTTP 403 (https://www.supplychain247.com/paper/putting_value_first_an_innovative_approach_to_enterprise_software/One_Network_Enterprises). It looks like an older vendor white paper. If it's still active, it's the closest "methodology" use of the name. Risk is low-medium.
- Thoughtworks publishes "Value-Oriented Incremental Delivery" (VOID): https://www.thoughtworks.com/insights/blog/exploring-value-oriented-incremental-delivery. The name is different but the concept is adjacent, so it's worth citing as a peer idea rather than treating as a collision. Seen in search only, not opened.
- The phrase "value-first" is used generically in many marketing and blog contexts. That makes the phrase hard to protect as a trademark, but also unlikely to be blocked.

### 4. GitHub
- User `ValueFirst` was created 2024-04-23 and has 0 public repos. User `Value-first` was created 2022-04-28 and has 0 public repos. **Both org/user handles are taken**, though dormant.
- Repos named value-first or ValueFirst are mostly empty personal repos or SMS-API clients for the Tanla service, e.g. `saud978/ValueFirst`, "Swift 5 library to send messages and get credit for ValueFirst SMS". There's one unrelated JS library, `MaximeRivest/lapipe`, a "value-first pipe operator".

### 5. Trademarks
- **Not verified.** Search turned up no USPTO, EUIPO or INPI record, but web search isn't a trademark search. The USPTO (tmsearch.uspto.gov), EUIPO eSearch and INPI Brazil (busca.inpi.gov.br) databases are interactive and couldn't be queried from here. The Tanla/ValueFirst brand very likely has an Indian registration (**UNVERIFIED**).

## Fallback name ideas (brief check)

| Candidate | Collision check | Notes |
|---|---|---|
| **Spec-to-Value** | Web search found no framework by this name. Results are only about "spec-to-code" and SDD. GitHub repo name search: 2 results. `spectovalue.dev` and `spec-to-value.dev` returned RDAP 404 (appear free). | Pairs naturally with the "from spec to software" tagline and the AI-era thesis. Risk: low. |
| **ValueSpec** | No company or product with this exact name. Near-misses: "Valspec" (a validation/compliance software vendor) and the UML term "ValueSpecification". `valuespec.dev` returned RDAP 404. GitHub repo name search: 12 results. | Short, but could read like a UML or tech term. Risk: low-medium. |
| **Value Loop** | `valueloop.dev` is registered. GitHub repo name search: 8 results. Not searched further. | Generic. Risk: medium (not checked deeply). |

## Limits of this check
- No paid or official trademark database query.
- Domain availability comes from RDAP 404 responses, which strongly suggest a name is unregistered but don't prove a registrar would sell it (it could be reserved or premium).
- Social handles (X, LinkedIn, Instagram) weren't checked.
