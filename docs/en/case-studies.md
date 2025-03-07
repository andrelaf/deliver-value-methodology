# Case Studies and Examples of the Deliver-Value Framework (DV)

This document centralizes real case studies and illustrative examples of applying the Deliver-Value Framework (DV) in different organizational contexts and project types.

## Summary

- [Real Case Studies](#real-case-studies)
  - [Case 1: Digital Transformation in a Financial Institution](#case-1-digital-transformation-in-a-financial-institution)
  - [Case 2: Healthcare Management System](#case-2-healthcare-management-system)
- [Illustrative Examples](#illustrative-examples)
  - [Example 1: E-commerce Project with Regulatory Deadline](#example-1-e-commerce-project-with-regulatory-deadline)
  - [Example 2: Legacy System Modernization](#example-2-legacy-system-modernization)
  - [Example 3: Internal Product with Multiple Stakeholders](#example-3-internal-product-with-multiple-stakeholders)
  - [Example 4: Startup with Limited Resources](#example-4-startup-with-limited-resources)
  - [Example 5: Project with External Dependencies](#example-5-project-with-external-dependencies)
- [Contribute Your Case](#contribute-your-case)

## Real Case Studies

> The cases described below are based on real implementations of the DV, with some details modified to preserve confidentiality.

### Case 1: Digital Transformation in a Financial Institution

#### Organization
Mid-sized bank with over 50 years in the market and 3 million customers.

#### Challenge
The bank needed to modernize its digital channels to compete with fintechs, but faced:
- Legacy technology with high coupling
- Organizational culture resistant to change
- Bureaucratic internal processes
- Constant conflicts between IT and business areas

#### DV Implementation

**1. Initial Diagnosis**

The transformation team conducted a series of workshops with representatives from all areas to:
- Map conflicts and misalignments between areas
- Identify friction points in existing processes
- Establish shared value metrics

**2. Work Model Structuring**

The following were implemented:
- Creation of the Value Analyst role, filled by professionals with experience in both business and technology
- Formalization of Technical Specialists as a bridge between architecture and development
- Establishment of collaboration agreements between areas

**3. Pilot Project**

A critical project (new mobile application) was selected as a pilot for the DV:
- Domain Storytelling workshop with financial product experts
- Detailed value mapping, with weights for different functionalities
- Technical complexity matrix developed by Technical Specialists
- Formal flexibility contract between product and technology directorates

**4. Implementation and Results**

- Development cycles with value checkpoints every two weeks
- Value vs. complexity dashboards for decision making
- Formal mechanism for scope renegotiation when necessary

#### Measurable Results

- 40% reduction in launch time compared to similar previous projects
- 65% decrease in conflicts escalated to executive level
- 28% increase in end-user satisfaction scores
- Estimated savings of $300,000 in avoided rework

#### Critical Success Factors

- Explicit support from senior leadership
- Strategic choice of pilot project (visible and important)
- Extensive training in new roles and responsibilities
- Clear metrics shared between business and technology areas

---

### Case 2: Healthcare Management System

#### Organization
Software company that develops systems for hospital management and medical clinics.

#### Challenge
The company faced:
- Long development cycles with low predictability
- Requirements constantly changing during development
- Disconnection between what doctors needed and what was delivered
- High rate of rework after implementation

#### DV Implementation

**1. Discovery Process Reformulation**

- Implementation of Domain Storytelling with medical professionals
- Creation of high-fidelity prototypes before development commitment
- Usability labs with real doctors and nurses

**2. Structuring of Roles and Responsibilities**

- Creation of the "Medical Value Analyst" role (professionals with both healthcare and technology training)
- Technical Specialists dedicated to specific domains (scheduling, medical records, etc.)
- Multidisciplinary squad model by clinical domain

**3. Adoption of Specific Practices**

- Event Storming to map complex clinical flows
- Clinical criticality matrix (impact on patient care) for prioritization
- Regular checkpoints with medical-technical committee
- Implementation of "shadow releases" (controlled release to specific user groups)

#### Measurable Results

- 70% reduction in post-implementation change requests
- 45% increase in adoption rate by doctors and nurses
- 30% faster development cycle
- Significant improvement in user satisfaction indices

#### Lessons Learned

- Adapting the Value Analyst role to the specific context (healthcare) was crucial
- Prioritization based on clinical criticality (not just commercial value) created alignment with users
- Including healthcare professionals in all phases of the process drastically reduced usability problems

---

## Illustrative Examples

> The following examples are composite scenarios, created to illustrate the application of the DV in different contexts.

### Example 1: E-commerce Project with Regulatory Deadline

#### Context
A retail company needed to adapt its e-commerce platform to new data protection regulations, with a fixed deadline set by law. The scope included changes to the entire process of collecting, storing, and processing customer data.

#### Challenge
- Non-negotiable deadline (legal requirement)
- Extensive and complex scope
- Impact on multiple legacy systems

#### DV Application

**Discovery Phase**
- **Regulatory Value Matrix**: Classification of requirements into "mandatory for legal compliance" vs. "desirable improvements"
- **Event Storming for Data Mapping**: Sessions with legal and technical experts to map the complete flow of customer data
- **Technical-Legal Risk Analysis**: Joint assessment of technical risks and legal consequences

**Planning Phase**
- **Layered Scope**: Definition of implementation layers (essential, important, desirable)
- **Roadmap with Regulatory Milestones**: Alignment of technical milestones with regulatory deadlines
- **Flexibility Contract**: Formal agreement on which functionalities could be simplified in case of technical challenges

**Execution Phase**
- **Data Domain Squads**: Teams dedicated to specific areas of the data flow
- **Weekly Compliance Checkpoints**: Regular validation with the legal team
- **Regulatory Value Dashboard**: Clear visualization of progress in terms of legal compliance

#### Results
- Legal compliance achieved within the deadline
- 30% reduction in the scope of "desirable improvements" after technical assessment
- Greater clarity for stakeholders about trade-offs made
- Comprehensive compliance documentation as a by-product of the process

#### Lessons Learned
- The clear separation between legal requirements and desirable improvements allowed focus on what really mattered
- Including the legal team in value checkpoints created trust and allowed adjustments to regulatory interpretation
- Detailed initial mapping saved significant time during implementation

---

### Example 2: Legacy System Modernization

#### Context
A financial institution needed to modernize a core system that was over 15 years old, written in obsolete technologies, and lacking adequate documentation. The system processed more than 70% of the company's financial operations.

#### Challenge
- Highly coupled legacy code
- Domain knowledge concentrated in a few specialists nearing retirement
- Need to maintain operation while modernizing
- Fixed annual budget for the multi-year project

#### DV Application

**Discovery Phase**
- **Extensive Domain Storytelling**: Multiple sessions with domain experts to document tacit knowledge
- **Hidden Dependencies Mapping**: Static and dynamic analysis to identify undocumented couplings
- **Value Matrix by Module**: Identification of the real business value of each system component

**Planning Phase**
- **Strangler Pattern Strategy**: Planning for gradual replacement while keeping the system operational
- **Phased Roadmap by Domain**: Division of work into cohesive business domains
- **Expert-Developer Partnerships**: Formal linking of domain experts to development teams

**Execution Phase**
- **Value Analysis before each Module**: Reassessment of business value before starting each component
- **Temporary Dual Implementation**: Parallel execution of old and new systems with automatic result comparison
- **Documentation as a Product**: Elevation of documentation to a "product" with users and feedback

#### Results
- 60% system modernization in the first year (exceeding the 40% expectation)
- Capture of critical domain knowledge before specialist retirement
- 25% reduction in scope after value analysis (rarely used modules were simplified)
- Zero significant interruptions during transition

#### Lessons Learned
- Quantifying the real value of each module allowed objective decisions for simplification or removal
- The formal partnership between experts and developers created effective knowledge transfer
- The parallel execution approach significantly reduced transition risk

---

### Example 3: Internal Product with Multiple Stakeholders

#### Context
A multinational company needed to develop a new performance management system for global use, meeting requirements from multiple departments (HR, Finance, Operations) in different regions.

#### Challenge
- Stakeholders with conflicting needs
- Unrealistic initial expectations (broad scope, short deadline)
- Complexity of regional requirements (legal and cultural)
- Need for consensus among various directors

#### DV Application

**Discovery Phase**
- **Value Alignment Workshop**: Session with all stakeholders to define shared success criteria
- **Requirements Matrix by Region/Department**: Visual mapping of overlaps and conflicts
- **Technical Compatibility Assessment**: Analysis of the technical feasibility of unifying divergent requirements

**Planning Phase**
- **Multi-phase Scope with Regional MVPs**: Definition of incremental deliveries by region/department
- **Interdepartmental Prioritization Committee**: Creation of a formal forum for conflict resolution
- **Flexibility Contract with Triggers**: Predefined mechanisms to escalate decisions to C-level when necessary

**Execution Phase**
- **Showcases by Stakeholder Group**: Customized demonstrations for different areas
- **Perceived Value Measurement**: Regular surveys with stakeholders about the value of deliveries
- **Quarterly Roadmap Adjustments**: Formal reviews of the plan based on feedback and learnings

#### Results
- 40% reduction in change requests after implementing the prioritization committee
- Greater stakeholder satisfaction compared to previous similar projects
- Global MVP launched 2 months ahead of schedule due to focus on essential value
- Faster adoption by end users due to constant involvement

#### Lessons Learned
- Creating a formal forum for conflict resolution avoided impasses and constant changes in direction
- Joint visualization of conflicting requirements facilitated negotiations and compromises
- Transparency about trade-offs from the beginning avoided later frustrations

---

### Example 4: Startup with Limited Resources

#### Context
A technology startup needed to launch an innovative product with a small team (5 developers) and limited investment, facing pressure from investors to show results quickly.

#### Challenge
- Extremely limited resources (people and budget)
- High uncertainty about requirements and market
- Need to show rapid progress for the next investment round
- Team with knowledge gaps in some necessary technologies

#### DV Application

**Discovery Phase**
- **Value Hypothesis Matrix**: Prioritization of features based on potential market impact
- **Skills Assessment Workshop**: Honest mapping of team skills vs. technical needs
- **Timeboxed Technical Exploration**: 2 weeks to validate the feasibility of the most risky technical approaches

**Planning Phase**
- **Truly Minimal MVP**: Rigorous definition of the minimum scope to validate main hypotheses
- **Adaptive Roadmap**: Detailed planning only until the next investment milestone
- **Technical Agreements Matrix**: Explicit definition of where to invest in quality vs. where to accept technical debt

**Execution Phase**
- **Weekly Value Review Cycles**: Frequent analyses to ensure constant focus on essential value
- **Strategic Pair Programming**: Pairing focused on knowledge gap areas
- **Early Adopter Feedback**: Rapid feedback cycles with selected users after each important feature

#### Results
- Functional MVP launch 3 weeks ahead of schedule
- Positive market feedback enabling new investment round
- Elimination of 35% of initially planned features due to low value validation
- Significant reduction in rework due to constant validation

#### Lessons Learned
- Explicit documentation of where to assume technical debt allowed conscious decisions without compromising future maintainability
- Short validation cycles avoided investment in features that didn't prove valuable
- Transparency about the team's technical limitations allowed better architecture and technology decisions

---

### Example 5: Project with External Dependencies

#### Context
A company needed to integrate its core system with multiple external partners (20+ integrations) as part of an open platform strategy, with an aggressive commercial deadline.

#### Challenge
- Dependencies on external teams and systems outside direct control
- Lack of standardization between different integrations
- Need to maintain security and performance with increased traffic
- Uncertainty about partner implementations

#### DV Application

**Discovery Phase**
- **Critical Dependencies Mapping**: Identification of which integrations were essential vs. optional
- **Risk Assessment by Partner**: Classification of partners by technical maturity and strategic importance
- **Main APIs Prototyping**: Early technical validation of the most critical endpoints

**Planning Phase**
- **Partner Wave Plan**: Grouping of partners by technical similarity and business priority
- **Clear Service Contracts**: Detailed documentation and examples to facilitate partner integration
- **Roadmap with Strategic Buffers**: Deliberate inclusion of slack in points of greater external uncertainty

**Execution Phase**
- **API Gateway with Sandbox**: Creation of a realistic testing environment for partners
- **Technical Checkpoints with Key Partners**: Regular meetings with strategic partners
- **Integration Progress Dashboard**: Visibility on the status of each integration for stakeholders

#### Results
- 15 of 22 integrations completed within the initial deadline
- Additional partners completed integrations in the following 4 weeks
- Effective isolation of individual partner problems without affecting the core system
- Lower average integration time per partner than in previous projects

#### Lessons Learned
- Grouping similar partners allowed knowledge reuse and accelerated integrations
- Creating sandbox and detailed documentation significantly reduced needed support
- Initial risk classification allowed more efficient allocation of support resources

---

## Contribute Your Case

Have you implemented the DV in your organization? Share your experience to help others learn from your successes and challenges.

To contribute your case study:

1. Fork the repository
2. Follow the template below to document your case
3. Follow the guidelines in the [CONTRIBUTING.md](/deliver-value-methodology/CONTRIBUTING.md) file for the complete contribution process
4. Submit a pull request

### Template for New Cases

```markdown
### [Organization Name or Project Type]

#### Context
[Brief description of the organization and situation]

#### Challenge
[Main problems faced]

#### DV Implementation
[How the framework was adapted and implemented]

#### Results
[Measurable benefits obtained]

#### Lessons Learned
[Important insights for other implementers]
```

All submitted cases will be reviewed by the community before inclusion. We encourage the inclusion of quantitative metrics whenever possible.
