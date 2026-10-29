
# Recommended Practices for the Deliver-Value Framework (DV)

This document details the recommended practices for effective implementation of the Deliver-Value Framework (DV). These practices have been compiled from real experiences and are adaptable to different organizational contexts.

## Summary

- [General Practices](#general-practices)
- [Discovery Practices](#discovery-practices)
- [Planning Practices](#planning-practices)
- [Execution Practices](#execution-practices)
- [Validation Practices](#validation-practices)
- [Conflict Resolution Practices](#conflict-resolution-practices)
- [Practices for Scaling the Framework](#practices-for-scaling-the-framework)

## General Practices

### 1. Establish a Common Vocabulary

**What**: Create and maintain a shared glossary between business and technology areas.

**How to implement**:
- Conduct workshops to align terminology between areas
- Maintain a living document with clear definitions of domain-specific terms
- Review periodically to ensure new terminology is included

**Benefits**:
- Reduces misunderstandings caused by different interpretations of the same terms
- Accelerates meetings and discussions by eliminating the need for repetitive explanations
- Facilitates the integration of new team members

### 2. Culture of Technical Transparency

**What**: Promote a culture where technical limitations can be openly discussed, without judgment.

**How to implement**:
- Conduct regular "Tech Shares" where technical challenges are presented to the business area
- Encourage the technical team to explain "why" something is complex, not just state that it is
- Create a safe environment where no one is penalized for bringing problems to light

**Benefits**:
- Anticipates risks before they become problems
- Creates empathy between areas with different perspectives
- Allows for more realistic expectations adjustments

### 3. Minimum Viable Documentation

**What**: Define and implement a minimum set of documentation that balances agility and traceability.

**How to implement**:
- For each type of project, identify which documents add real value
- Automate technical documentation generation whenever possible
- Focus on documenting decisions ("decision records") rather than detailed specifications

**Benefits**:
- Reduces administrative overhead without losing essential information
- Maintains traceability of important decisions
- Allows new members to understand the project history

### 4. Standardized Diagram Models

**What**: Use standardized diagram notations to facilitate communication between teams and document system aspects.

**How to implement**:
- **C4 Model**: For architecture documentation at different levels of abstraction (Context, Containers, Components, and Code)
- **BPMN (Business Process Model and Notation)**: For business process representation
- **UML**: For detailed documentation of components and interactions when necessary
- **Entity-Relationship Diagrams (ERD)**: For data modeling
- **Sequence Diagrams**: For complex interaction flows
- **Mermaid or PlantUML**: For diagrams maintained as code alongside documentation

**Benefits**:
- Establishes a common visual standard across the organization
- Facilitates quick understanding of complex structures
- Allows different levels of abstraction for different audiences
- Integrates with documentation-as-code practices

**Usage recommendations**:
- Use C4 Model for architectural views with technical stakeholders
- Use BPMN for process discussions with the business area
- Keep diagrams simple and focused on a specific aspect
- Consider tools that allow versioning diagrams along with code

## Discovery Practices

### 1. Product Value Workshop

**What**: Collaborative session to identify and quantify the core value that the product/project should deliver.

**How to implement**:
- Gather representatives from business, technology, and UX
- Use techniques such as Impact Mapping or Value Proposition Canvas
- Clearly document the value in terms of outcomes (results), not outputs (deliverables)
- Utilize the [Value-Technology Alignment Canvas](/docs/en/templates.md) as a visual guide during the workshop
  
**Benefits**:
- Aligns all areas around the true purpose of the project
- Provides a clear direction for future decisions
- Allows prioritization based on real value

### 2. Domain Storytelling

**What**: Collaborative technique where domain experts narrate stories about their business processes, while a facilitator documents them visually.

**How to implement**:
- Invite domain experts who deeply understand the process
- Use a simple visual notation (actors, work objects, activities)
- Capture real stories, not idealized processes
- Document domain-specific vocabulary during sessions

**Benefits**:
- Creates a shared language between business and technology
- Reveals subtle details of processes that don't appear in formal documentation
- Identifies pain points and improvement opportunities in the current flow
- Facilitates the creation of a more accurate domain model

### 3. Event Storming

**What**: Collaborative workshop to model complex business processes using domain events on a timeline.

**How to implement**:
- Use a large space (wall or board) with colored sticky notes
- Start with domain events (usually in orange)
- Add commands, actors, aggregates, and policies in successive iterations
- Identify bounded contexts and possible domain subdivisions

**Benefits**:
- Creates a shared understanding of the business event flow
- Reveals complexities and bottlenecks in the current process
- Helps identify natural boundaries for system division
- Facilitates the transition to an event-driven architecture or microservices

### 4. Exploratory Technical Assessment

**What**: Period dedicated to exploring technical feasibility before formal commitment to estimates.

**How to implement**:
- Allow the Technical Specialist to form a small group for exploration
- Clearly document assumptions and uncertainties
- Build concept prototypes for higher-risk aspects

**Benefits**:
- Reduces risks of unrealistic estimates
- Identifies technical challenges early
- Allows scope adjustment before the formal start of the project

### 5. Dependency Mapping

**What**: Systematic identification of all internal and external dependencies that may impact the project.

**How to implement**:
- Create a visual dependency diagram
- Classify dependencies by criticality and control (within or outside team control)
- Define strategies to mitigate risks in critical dependencies

**Benefits**:
- Prevents unpleasant surprises during execution
- Allows contingency planning for high-risk dependencies
- Identifies potential bottlenecks early

## Planning Practices

### 1. Collaborative Creation of the Value Matrix

**What**: Joint development of the Value Matrix that relates features to business value.

**How to implement**:
- Conduct sessions with active participation from business and technology
- Use prioritization techniques such as RICE (Reach, Impact, Confidence, Effort)
- Clearly document acceptance criteria focused on value

**Benefits**:
- Creates a shared understanding of priorities
- Enables objective decisions when tradeoffs are necessary
- Keeps focus on what really matters for project success

### 2. Flexibility Contracts

**What**: Formal establishment of fixed and flexible parameters for the project.

**How to implement**:
- Clearly identify what is non-negotiable (e.g., regulatory requirements)
- Formally establish what can be flexible (scope, deadline, resources)
- Define triggers and processes for renegotiation

**Benefits**:
- Creates clear expectations about what can be adjusted
- Allows adaptation without unnecessary conflicts
- Formalizes a process for dealing with inevitable changes

### 3. Wave Planning

**What**: Planning approach that details the short term and keeps the long term more flexible.

**How to implement**:
- Plan in detail only the next 2-3 sprints
- Maintain medium-term plans with intermediate granularity
- Use thematic roadmaps for long term, without detailing specific features

**Benefits**:
- Balances predictability with adaptability
- Reduces excessive replanning
- Allows adjustments based on learnings without losing direction

## Execution Practices

### 1. Tech Alignment Sessions

**What**: Regular meetings to align technical vision and resolve technical impediments.

**How to implement**:
- Conduct short meetings (30-45 min) involving technical specialists
- Focus on architectural decisions and impediment removal
- Document important decisions and share with the team

**Benefits**:
- Maintains technical consistency in the project
- Quickly resolves technical blocks
- Disseminates knowledge among different specialists

### 2. Value Checkpoints

**What**: Regular checks to ensure that the planned value is being created.

**How to implement**:
- Conduct checkpoints every 2-3 sprints
- Involve representatives from business and technology
- Evaluate progress in terms of value, not just delivered features

**Benefits**:
- Allows quick course corrections
- Keeps focus on the real value being created
- Identifies when planned value is not being achieved

### 3. Value-Oriented Showcases

**What**: Progress demonstrations focused on delivered value, not just features.

**How to implement**:
- Structure demonstrations around user journeys or business cases
- Explicitly highlight the value generated by each increment
- Invite diverse stakeholders to get varied feedback

**Benefits**:
- Keeps stakeholders connected to real progress
- Facilitates meaningful and contextualized feedback
- Reinforces the culture of value focus

## Validation Practices

### 1. Continuous Validation in Short Cycles

**What**: Frequent verification with real users or business representatives about the value being delivered.

**How to implement**:
- Establish short feedback cycles (1-2 weeks)
- Use techniques such as usability testing, interviews, or A/B testing
- Document insights and implement improvements quickly

**Benefits**:
- Avoids prolonged development in the wrong direction
- Keeps the product aligned with users' real needs
- Allows rapid iterations based on concrete feedback

### 2. Objective Validation Metrics

**What**: Set of specific metrics to verify if the planned value is being realized.

**How to implement**:
- Establish clear KPIs linked to value objectives
- Implement instrumentation to collect data automatically
- Review metrics regularly with the team and stakeholders

**Benefits**:
- Provides objective evidence of delivered value
- Enables data-driven decisions, not opinion-based
- Quickly identifies when objectives are not being met

### 3. Value-Centered Retrospectives

**What**: Retrospectives that focus not only on processes but on delivered and perceived value.

**How to implement**:
- Add specific questions about value in retrospectives
- Occasionally invite business representatives to participate
- Document learnings related to value delivery

**Benefits**:
- Keeps the team focused on the broader purpose of the project
- Identifies opportunities to improve value delivery
- Creates continuous alignment between execution and objectives

## Conflict Resolution Practices

### 1. Data-Based Escalation

**What**: Structured process for conflict resolution using objective data.

**How to implement**:
- Establish a clear framework for decisions (e.g., impact/effort matrix)
- Require that conflicting positions be supported by data or evidence
- Document assumptions behind each position

**Benefits**:
- Depersonalizes conflicts, focusing on data rather than opinions
- Facilitates more objective and less emotional decisions
- Creates useful precedents for future situations

### 2. Prioritization Committee

**What**: Multidisciplinary group responsible for resolving prioritization conflicts.

**How to implement**:
- Form a committee with representatives from different areas
- Establish clear criteria for prioritization
- Hold regular or on-demand meetings to resolve conflicts

**Benefits**:
- Provides a formal mechanism to resolve deadlocks
- Balances different perspectives in decisions
- Increases transparency in the decision-making process

### 3. Commitment Agreements

**What**: Formal documents that record commitments when adjustments are necessary.

**How to implement**:
- Create a simple template to record agreements
- Clearly document what each party is committing to
- Establish deadlines and criteria for review

**Benefits**:
- Avoids misunderstandings about what was agreed
- Provides clear reference for follow-up
- Creates accountability for all parties involved

## Practices for Scaling the Framework

### 1. Communities of Practice

**What**: Informal groups that promote knowledge sharing and standardization of practices.

**How to implement**:
- Create communities for specific roles (e.g., Value Analysts, Technical Specialists)
- Promote regular meetings for experience exchange
- Encourage documentation of patterns and best practices

**Benefits**:
- Disseminates knowledge between teams
- Standardizes practices while maintaining space for adaptation
- Creates peer support for common challenges

### 2. Contextual Adaptation Framework

**What**: Clear guidelines on how to adapt the DV for different contexts.

**How to implement**:
- Create an adaptation matrix based on variables such as project size, criticality, etc.
- Document examples of successful adaptations
- Allow teams to customize with clear justification

**Benefits**:
- Avoids rigid application of the framework in inappropriate contexts
- Provides guidance for adaptations without losing essential principles
- Allows organic evolution of practices based on learnings

### 3. Adoption and Maturity Metrics

**What**: System to assess the level of adoption and maturity in DV implementation.

**How to implement**:
- Develop a maturity model with clear levels
- Create self-assessment tools for teams
- Conduct periodic reviews to identify improvement areas

**Benefits**:
- Provides visibility on the actual adoption of the framework
- Identifies areas that need more support or training
- Allows celebrating advances in implementation

---

## Adapting Practices to Your Context

It is essential to emphasize that these practices are recommendations, not rigid rules. Each organization should adapt these practices to its specific context, considering:

- Existing organizational culture
- Team maturity
- Nature of projects
- Specific domain constraints

The success of the DV does not lie in the literal application of all these practices, but in the incorporation of its fundamental principles in a way that makes sense for your reality.

We recommend starting with a subset of these practices, evaluating the results, and gradually incorporating more elements as the team gains experience with the framework.
