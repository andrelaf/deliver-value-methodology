# Decisions log — Value-First Development v2

Decisions taken autonomously during the v2 rebuild (branch `rebuild/v2`), with the reason. Items marked **[owner]** need the owner's confirmation.

| # | Date | Decision | Reason |
|---|------|----------|--------|
| D1 | 2026-10-28 | Name: **Value-First Development**; short form **Value-First** (with hyphen). Never "ValueFirst" (one word). | Exact name has no collision found; "ValueFirst" is an active company (Tanla, vfirst.com). See [docs/research/name-collision.md](docs/research/name-collision.md). Trademark search (USPTO/EUIPO/INPI) not done — **[owner]** before any commercial use. |
| D2 | 2026-10-28 | Strategy: **reposition** (not patch, not rewrite from zero). | Core ideas still hold (TL filling the spec gap, alignment canvas, fixed vs. flexible, feasibility before commitment); AI makes the gap costlier. See [docs/diagnostico.md](docs/diagnostico.md). |
| D3 | 2026-10-28 | "Value Analyst" stops being a job title; value + spec become a shared responsibility of a **Product + Tech Lead pair** ("a hat, not a role"). | A new role adds a handoff layer — the very gap the framework addresses. |
| D4 | 2026-10-28 | **Value Spec** becomes the central artifact, absorbing the Flexibility Contract and Technical Complexity Map. The Alignment Canvas stays as an optional workshop tool. | Fewer artifacts; one living document usable by humans and agents. |
| D5 | 2026-10-28 | v1 docs are preserved verbatim in `docs/archive/v1/` before being rewritten; nothing is deleted from history. | Owner asked not to delete content without approval; archive keeps it reachable. |
| D6 | 2026-10-28 | v1 "real" case studies (unsourced figures, PT/EN mismatch: R$ 1,2 mi vs US$ 300k) are rewritten as clearly labeled **illustrative scenarios** without precise numbers. **[owner]** if any case is real and publishable, provide a source and it will be restored as a case study. | "Every factual claim needs a source." |
| D7 | 2026-10-28 | `README.md` in **English**, `README.pt-BR.md` in Portuguese, same content. Empty `translations/README.{es,pt}.md` removed (pre-approved in the brief); `translations/README.en.md` superseded by `README.md` (archived). Spanish dropped until a native reviewer contributes. | Reach on GitHub; owner's brief allows removing empty translations. |
| D8 | 2026-10-28 | Use the word **"framework"** consistently. | Continuity with v1 and the owner's own wording. |
| D9 | 2026-10-28 | License stays **MIT**. Suggestion: CC BY 4.0 for docs — **[owner]**. | License change is the owner's call. |
| D10 | 2026-10-28 | Brand: teal `#0B6E63` + amber value dot, IBM Plex Sans/Mono. See [assets/brand/BRAND.md](assets/brand/BRAND.md). | Calm, editorial, no AI-hype visuals; works light/dark and at 16px. |
| D11 | 2026-10-28 | Token economy: review loop runs in batches (one red-team pass per content bundle, max 2 rounds) instead of per file. | Owner asked to keep token consumption in check. |
| D12 | 2026-10-28 | METR 2025 "19% slower" is only cited together with METR's Feb 2026 caveat; Boehm cost-of-change is cited as Boehm & Basili 2001 (100:1 for large systems, ~5:1 small), not "exponential". | Accuracy of sources (see docs/research/sources.md). |
