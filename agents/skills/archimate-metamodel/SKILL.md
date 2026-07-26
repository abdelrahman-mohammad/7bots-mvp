---
name: archimate-metamodel
description: Defines the valid ArchiMate 3.2 element types for the Motivation, Strategy, Business, Application, and Technology layers, and the permitted relationships between them. Use when creating, classifying, or validating any ArchiMate element or relationship, when choosing an archimate_type for an extracted element, or when checking whether a relationship between two elements is legal.
---

# ArchiMate 3.2 metamodel

Reference data. Look values up here; do not rely on recall.

## Rules

1. `archimate_type` must be one of the 53 element types listed below, spelled exactly as written.
2. `layer` must be the layer that element type belongs to.
3. Every relationship must appear in `references/relationships.md`. A pair that is absent is invalid.
4. If no listed element type fits the evidence, report the gap. Never invent a type.

## Checking a relationship

Grep the reference file rather than reading it; it is 3,000 lines.

    grep "^BusinessActor -> Node:" references/relationships.md

Returns `BusinessActor -> Node: Flow, Association, Triggering, Serving`, so Realization between those two is invalid. No output means no relationship of any kind is permitted.

Relationships are directional. `A -> B` says nothing about `B -> A`; look up both.

## Relationship types

The 11 types used throughout the matrix. Association is the fallback when no other type fits, so prefer a more specific type when the evidence supports one.

### Structural

| Type        | Definition                                                                                                                          |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Composition | Represents that an element consists of one or more other concepts.                                                                  |
| Aggregation | Represents that an element combines one or more other concepts.                                                                     |
| Assignment  | Represents the allocation of responsibility, performance of behavior, storage, or execution.                                        |
| Realization | Represents that an element plays a critical role in the creation, achievement, sustenance, or operation of a more abstract element. |

### Dependency

| Type        | Definition                                                                                                          |
| ----------- | ------------------------------------------------------------------------------------------------------------------- |
| Serving     | Represents that an element provides its functionality to another element.                                           |
| Access      | Represents the ability of behavior and active structure elements to observe or act upon passive structure elements. |
| Influence   | Represents that an element affects the implementation or achievement of some motivation element.                    |
| Association | Represents an unspecified relationship, or one that is not represented by another ArchiMate relationship.           |

### Dynamic

| Type       | Definition                                                     |
| ---------- | -------------------------------------------------------------- |
| Triggering | Represents a temporal or causal relationship between elements. |
| Flow       | Represents transfer from one element to another.               |

### Other

| Type           | Definition                                                          |
| -------------- | ------------------------------------------------------------------- |
| Specialization | Represents that an element is a particular kind of another element. |

## Element types

### Motivation (10)

| Element     | Definition                                                                                                                                           |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Stakeholder | Represents the role of an individual, team, or organization (or classes thereof) that represents their interests in the effects of the architecture. |
| Driver      | Represents an external or internal condition that motivates an organization to define its goals and implement the changes necessary to achieve them. |
| Assessment  | Represents the result of an analysis of the state of affairs of the enterprise with respect to some driver.                                          |
| Goal        | Represents a high-level statement of intent, direction, or desired end state for an organization and its stakeholders.                               |
| Outcome     | Represents an end result, effect, or consequence of a certain state of affairs.                                                                      |
| Principle   | Represents a statement of intent defining a general property that applies to any system in a certain context in the architecture.                    |
| Requirement | Represents a statement of need defining a property that applies to a specific system as described by the architecture.                               |
| Constraint  | Represents a limitation on aspects of the architecture, its implementation process, or its realization.                                              |
| Meaning     | Represents the knowledge or expertise present in, or the interpretation given to, a concept in a particular context.                                 |
| Value       | Represents the relative worth, utility, or importance of a concept.                                                                                  |

### Strategy (4)

| Element        | Definition                                                                                                                      |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Resource       | Represents an asset owned or controlled by an individual or organization.                                                       |
| Capability     | Represents an ability that an active structure element, such as an organization, person, or system, possesses.                  |
| ValueStream    | Represents a sequence of activities that create an overall result for a customer, stakeholder, or end user.                     |
| CourseOfAction | Represents an approach or plan for configuring some capabilities and resources of the enterprise, undertaken to achieve a goal. |

### Business (13)

| Element               | Definition                                                                                                                                                                                                                                    |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BusinessActor         | Represents a business entity that is capable of performing behavior.                                                                                                                                                                          |
| BusinessRole          | Represents the responsibility for performing specific behavior, to which an actor can be assigned, or the part an actor plays in a particular action or event.                                                                                |
| BusinessCollaboration | Represents an aggregate of two or more business internal active structure elements that work together to perform collective behavior.                                                                                                         |
| BusinessInterface     | Represents a point of access where business services are made available to the environment.                                                                                                                                                   |
| BusinessProcess       | Represents a sequence of business behaviors that achieves a specific result such as a defined set of products or business services.                                                                                                           |
| BusinessFunction      | Represents a collection of business behavior based on a chosen set of criteria such as required business resources and/or competencies, and is managed or performed as a whole.                                                               |
| BusinessInteraction   | Represents a unit of collective business behavior performed by (a collaboration of) two or more business actors, business roles, or business collaborations.                                                                                  |
| BusinessEvent         | Represents a business-related state change.                                                                                                                                                                                                   |
| BusinessService       | Represents explicitly defined behavior that a business role, business actor, or business collaboration exposes to its environment.                                                                                                            |
| BusinessObject        | Represents a concept used within a particular business domain.                                                                                                                                                                                |
| Contract              | Represents a formal or informal specification of an agreement between a provider and a consumer that specifies the rights and obligations associated with a product and establishes functional and non-functional parameters for interaction. |
| Representation        | Represents a perceptible form of the information carried by a business object.                                                                                                                                                                |
| Product               | Represents a coherent collection of services and/or passive structure elements, accompanied by a contract, which is offered as a whole to (internal or external) customers.                                                                   |

### Application (9)

| Element                  | Definition                                                                                                                                           |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| ApplicationComponent     | Represents an encapsulation of application functionality aligned to implementation structure, which is modular and replaceable.                      |
| ApplicationCollaboration | Represents an aggregate of two or more application internal active structure elements that work together to perform collective application behavior. |
| ApplicationInterface     | Represents a point of access where application services are made available to a user, another application component, or a node.                      |
| ApplicationFunction      | Represents automated behavior that can be performed by an application component.                                                                     |
| ApplicationInteraction   | Represents a unit of collective application behavior performed by (a collaboration of) two or more application components.                           |
| ApplicationProcess       | Represents a sequence of application behaviors that achieves a specific result.                                                                      |
| ApplicationEvent         | Represents an application state change.                                                                                                              |
| ApplicationService       | Represents an explicitly defined exposed application behavior.                                                                                       |
| DataObject               | Represents data structured for automated processing.                                                                                                 |

### Technology (17)

| Element                 | Definition                                                                                                                                                |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Node                    | Represents a computational or physical resource that hosts, manipulates, or interacts with other computational or physical resources.                     |
| Device                  | Represents a physical IT resource upon which system software and artifacts may be stored or deployed for execution.                                       |
| SystemSoftware          | Represents software that provides or contributes to an environment for storing, executing, and using software or data deployed within it.                 |
| TechnologyCollaboration | Represents an aggregate of two or more technology internal active structure elements that work together to perform collective technology behavior.        |
| TechnologyInterface     | Represents a point of access where technology services offered by a technology internal active structure can be accessed.                                 |
| Path                    | Represents a link between two or more technology internal active structure elements, through which these elements can exchange data, energy, or material. |
| CommunicationNetwork    | Represents a set of structures that connects devices or system software for transmission, routing, and reception of data.                                 |
| TechnologyFunction      | Represents a collection of technology behavior that can be performed by a technology internal active structure element.                                   |
| TechnologyProcess       | Represents a sequence of technology behaviors that achieves a specific result.                                                                            |
| TechnologyInteraction   | Represents a unit of collective technology behavior performed by (a collaboration of) two or more technology internal active structure elements.          |
| TechnologyEvent         | Represents a technology state change.                                                                                                                     |
| TechnologyService       | Represents an explicitly defined exposed technology behavior.                                                                                             |
| Artifact                | Represents a piece of data that is used or produced in a software development process, or by deployment and operation of an IT system.                    |
| Equipment               | Represents one or more physical machines, tools, or instruments that can create, use, store, move, or transform materials.                                |
| Facility                | Represents a physical structure or environment.                                                                                                           |
| DistributionNetwork     | Represents a physical network used to transport materials or energy.                                                                                      |
| Material                | Represents tangible physical matter or energy.                                                                                                            |

## Sources

Element definitions are quoted verbatim from the ArchiMate 3.2 Specification, Tables 4 to 8.

The relationship matrix in `references/relationships.md` comes from Archi 3.2 `relationships.xml`, which encodes Appendix B of the specification. Appendix B publishes its tables as images, so this is the machine-readable form of the same data; both use the letter scheme defined in Appendix B.5.
