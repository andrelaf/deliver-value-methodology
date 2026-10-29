# Changelog

## v2.0.0: Value-First Development (unreleased, branch `rebuild/v2`)

The framework is repositioned and renamed. The v1 text is preserved verbatim in [docs/archive/v1](docs/archive/v1/). Every decision and its reason are in [DECISIONS.md](DECISIONS.md).

### Changed
- **Name:** *Deliver-Value Framework* (DV / FDCV) → **Value-First Development** (short form **Value-First**). Name-collision research is in [docs/research/name-collision.md](docs/research/name-collision.md).
- **Thesis:** one sentence, with spec quality in the AI era at the center of the argument (not an appendix). See [Why Value-First](docs/en/why.md) and [Specs in the AI era](docs/en/ai-and-specs.md).
- **Principles:** five v1 principles plus the Value Analyst role → six principles ([principles](docs/en/principles.md)).
- **Roles:** the Value Analyst is no longer a job title. A **Value Pair** (Product + Tech Lead) co-owns the spec.
- **Artifacts:** the **Value Spec** is the central artifact and absorbs the Flexibility Contract and the Technical Complexity Map. The Alignment Canvas is replaced by the C4-inspired **Value Map** ([value map](docs/en/value-map.md)); the original is archived.
- **Practices:** 22 v1 practices → 4 signature practices + 1 optional. Well-known techniques are credited as "compatible techniques".
- **Case studies:** v1 "real" cases had unsourced figures that differed between PT and EN. They're replaced by clearly labeled illustrative scenarios.
- **README:** English is primary ([README.md](README.md)), with a full Portuguese mirror ([README.pt-BR.md](README.pt-BR.md)). It reads in about three minutes.
- **Tone:** an invitation to change mindset, crediting Waterfall, Agile, Scrum, Kanban and Shape Up. Every factual claim is linked to a source ([sources](docs/en/sources.md)).

### Added
- [Specs in the AI era](docs/en/ai-and-specs.md): spec-driven development, agent context files, DORA findings, limits and risks.
- [Value Spec template](templates/en/value-spec.md), [filled example](templates/en/value-spec-example.md) and [agent snippet](templates/en/agents-snippet.md) for AGENTS.md / CLAUDE.md, in EN and PT.
- [Adoption](docs/en/adoption.md): "You're Value-First if…" checklist, maturity model (including spec maturity), first-week guide, when not to use it.
- [Comparison](docs/en/comparison.md) with Scrum, Kanban, Shape Up, spec-driven development and SAFe.
- Brand identity: logo variants, palette and tokens ([assets/brand](assets/brand/BRAND.md)).
- Diagrams in SVG, EN/PT, light/dark ([assets/diagrams](assets/diagrams/)): cycle, the gap, before × now, roles, where Value-First sits.
- Landing page in `site/` (EN/PT, responsive, light/dark), with a manual GitHub Pages workflow.
- [Value Map](docs/en/value-map.md) (C4-inspired, with a guided demo and a fillable map on the site).
- Technical additions to the Value Spec: instrumentation criterion, release & rollback, hard-to-reverse decisions, operations, cost, AI inside the feature, and agent rules for dependencies and untrusted content.
- [DECISIONS.md](DECISIONS.md), the [diagnosis](docs/diagnostico.md) and the [annotated research](docs/research/sources.md).

### Removed
- Empty `translations/README.es.md` and `translations/README.pt.md`. `translations/README.en.md` is superseded by `README.md` and archived.
- Placeholder links (`seu-usuario/fdcv`, `your-username`).

## v1: Deliver-Value Framework
The original framework. Archived in [docs/archive/v1](docs/archive/v1/).
