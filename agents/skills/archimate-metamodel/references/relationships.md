# ArchiMate 3.2 relationship matrix

Every permitted relationship between the 53 element types of the Motivation, Strategy, Business, Application, and Technology layers. 2809 pairs.

Look up one element with grep rather than reading this file:

    grep "^ApplicationComponent ->" references/relationships.md

A pair absent from this file is not a permitted relationship.

Source: Archi 3.2 `relationships.xml`, which encodes Appendix B of the ArchiMate 3.2 Specification using the same letter scheme the specification defines in B.5.

Excluded: Implementation & Migration elements, Grouping, Location, Junction. No MVP subagent produces them.

## Contents

- ApplicationCollaboration
- ApplicationComponent
- ApplicationEvent
- ApplicationFunction
- ApplicationInteraction
- ApplicationInterface
- ApplicationProcess
- ApplicationService
- Artifact
- Assessment
- BusinessActor
- BusinessCollaboration
- BusinessEvent
- BusinessFunction
- BusinessInteraction
- BusinessInterface
- BusinessObject
- BusinessProcess
- BusinessRole
- BusinessService
- Capability
- CommunicationNetwork
- Constraint
- Contract
- CourseOfAction
- DataObject
- Device
- DistributionNetwork
- Driver
- Equipment
- Facility
- Goal
- Material
- Meaning
- Node
- Outcome
- Path
- Principle
- Product
- Representation
- Requirement
- Resource
- Stakeholder
- SystemSoftware
- TechnologyCollaboration
- TechnologyEvent
- TechnologyFunction
- TechnologyInteraction
- TechnologyInterface
- TechnologyProcess
- TechnologyService
- Value
- ValueStream

## ApplicationCollaboration

ApplicationCollaboration -> ApplicationCollaboration: Composition, Flow, Aggregation, Association, Specialization, Triggering, Serving
ApplicationCollaboration -> ApplicationComponent: Flow, Aggregation, Association, Realization, Triggering, Serving
ApplicationCollaboration -> ApplicationEvent: Flow, Assignment, Association, Realization, Triggering, Serving
ApplicationCollaboration -> ApplicationFunction: Flow, Assignment, Association, Realization, Triggering, Serving
ApplicationCollaboration -> ApplicationInteraction: Flow, Assignment, Association, Realization, Triggering, Serving
ApplicationCollaboration -> ApplicationInterface: Composition, Flow, Aggregation, Association, Realization, Triggering, Serving
ApplicationCollaboration -> ApplicationProcess: Flow, Assignment, Association, Realization, Triggering, Serving
ApplicationCollaboration -> ApplicationService: Flow, Assignment, Association, Realization, Triggering, Serving
ApplicationCollaboration -> Artifact: Access, Association
ApplicationCollaboration -> Assessment: Influence, Association
ApplicationCollaboration -> BusinessActor: Flow, Association, Triggering, Serving
ApplicationCollaboration -> BusinessCollaboration: Flow, Association, Triggering, Serving
ApplicationCollaboration -> BusinessEvent: Flow, Association, Realization, Triggering, Serving
ApplicationCollaboration -> BusinessFunction: Flow, Association, Realization, Triggering, Serving
ApplicationCollaboration -> BusinessInteraction: Flow, Association, Realization, Triggering, Serving
ApplicationCollaboration -> BusinessInterface: Flow, Association, Realization, Triggering, Serving
ApplicationCollaboration -> BusinessObject: Access, Association
ApplicationCollaboration -> BusinessProcess: Flow, Association, Realization, Triggering, Serving
ApplicationCollaboration -> BusinessRole: Flow, Association, Triggering, Serving
ApplicationCollaboration -> BusinessService: Flow, Association, Realization, Triggering, Serving
ApplicationCollaboration -> Capability: Association, Realization
ApplicationCollaboration -> CommunicationNetwork: Flow, Association, Triggering, Serving
ApplicationCollaboration -> Constraint: Influence, Association, Realization
ApplicationCollaboration -> Contract: Access, Association
ApplicationCollaboration -> CourseOfAction: Association, Realization
ApplicationCollaboration -> DataObject: Access, Association
ApplicationCollaboration -> Device: Flow, Association, Triggering, Serving
ApplicationCollaboration -> DistributionNetwork: Flow, Association, Triggering, Serving
ApplicationCollaboration -> Driver: Influence, Association
ApplicationCollaboration -> Equipment: Flow, Association, Triggering, Serving
ApplicationCollaboration -> Facility: Flow, Association, Triggering, Serving
ApplicationCollaboration -> Goal: Influence, Association, Realization
ApplicationCollaboration -> Material: Access, Association
ApplicationCollaboration -> Meaning: Influence, Association
ApplicationCollaboration -> Node: Flow, Association, Triggering, Serving
ApplicationCollaboration -> Outcome: Influence, Association, Realization
ApplicationCollaboration -> Path: Flow, Association, Triggering, Serving
ApplicationCollaboration -> Principle: Influence, Association, Realization
ApplicationCollaboration -> Product: Flow, Association, Triggering, Serving
ApplicationCollaboration -> Representation: Access, Association
ApplicationCollaboration -> Requirement: Influence, Association, Realization
ApplicationCollaboration -> Resource: Association, Realization
ApplicationCollaboration -> Stakeholder: Influence, Association
ApplicationCollaboration -> SystemSoftware: Flow, Association, Triggering, Serving
ApplicationCollaboration -> TechnologyCollaboration: Flow, Association, Triggering, Serving
ApplicationCollaboration -> TechnologyEvent: Flow, Association, Triggering, Serving
ApplicationCollaboration -> TechnologyFunction: Flow, Association, Triggering, Serving
ApplicationCollaboration -> TechnologyInteraction: Flow, Association, Triggering, Serving
ApplicationCollaboration -> TechnologyInterface: Flow, Association, Triggering, Serving
ApplicationCollaboration -> TechnologyProcess: Flow, Association, Triggering, Serving
ApplicationCollaboration -> TechnologyService: Flow, Association, Triggering, Serving
ApplicationCollaboration -> Value: Influence, Association
ApplicationCollaboration -> ValueStream: Association, Realization

## ApplicationComponent

ApplicationComponent -> ApplicationCollaboration: Flow, Association, Triggering, Serving
ApplicationComponent -> ApplicationComponent: Composition, Flow, Aggregation, Association, Realization, Specialization, Triggering, Serving
ApplicationComponent -> ApplicationEvent: Flow, Assignment, Association, Realization, Triggering, Serving
ApplicationComponent -> ApplicationFunction: Flow, Assignment, Association, Realization, Triggering, Serving
ApplicationComponent -> ApplicationInteraction: Flow, Assignment, Association, Realization, Triggering, Serving
ApplicationComponent -> ApplicationInterface: Composition, Flow, Aggregation, Association, Realization, Triggering, Serving
ApplicationComponent -> ApplicationProcess: Flow, Assignment, Association, Realization, Triggering, Serving
ApplicationComponent -> ApplicationService: Flow, Assignment, Association, Realization, Triggering, Serving
ApplicationComponent -> Artifact: Access, Association
ApplicationComponent -> Assessment: Influence, Association
ApplicationComponent -> BusinessActor: Flow, Association, Triggering, Serving
ApplicationComponent -> BusinessCollaboration: Flow, Association, Triggering, Serving
ApplicationComponent -> BusinessEvent: Flow, Association, Realization, Triggering, Serving
ApplicationComponent -> BusinessFunction: Flow, Association, Realization, Triggering, Serving
ApplicationComponent -> BusinessInteraction: Flow, Association, Realization, Triggering, Serving
ApplicationComponent -> BusinessInterface: Flow, Association, Realization, Triggering, Serving
ApplicationComponent -> BusinessObject: Access, Association
ApplicationComponent -> BusinessProcess: Flow, Association, Realization, Triggering, Serving
ApplicationComponent -> BusinessRole: Flow, Association, Triggering, Serving
ApplicationComponent -> BusinessService: Flow, Association, Realization, Triggering, Serving
ApplicationComponent -> Capability: Association, Realization
ApplicationComponent -> CommunicationNetwork: Flow, Association, Triggering, Serving
ApplicationComponent -> Constraint: Influence, Association, Realization
ApplicationComponent -> Contract: Access, Association
ApplicationComponent -> CourseOfAction: Association, Realization
ApplicationComponent -> DataObject: Access, Association
ApplicationComponent -> Device: Flow, Association, Triggering, Serving
ApplicationComponent -> DistributionNetwork: Flow, Association, Triggering, Serving
ApplicationComponent -> Driver: Influence, Association
ApplicationComponent -> Equipment: Flow, Association, Triggering, Serving
ApplicationComponent -> Facility: Flow, Association, Triggering, Serving
ApplicationComponent -> Goal: Influence, Association, Realization
ApplicationComponent -> Material: Access, Association
ApplicationComponent -> Meaning: Influence, Association
ApplicationComponent -> Node: Flow, Association, Triggering, Serving
ApplicationComponent -> Outcome: Influence, Association, Realization
ApplicationComponent -> Path: Flow, Association, Triggering, Serving
ApplicationComponent -> Principle: Influence, Association, Realization
ApplicationComponent -> Product: Flow, Association, Triggering, Serving
ApplicationComponent -> Representation: Access, Association
ApplicationComponent -> Requirement: Influence, Association, Realization
ApplicationComponent -> Resource: Association, Realization
ApplicationComponent -> Stakeholder: Influence, Association
ApplicationComponent -> SystemSoftware: Flow, Association, Triggering, Serving
ApplicationComponent -> TechnologyCollaboration: Flow, Association, Triggering, Serving
ApplicationComponent -> TechnologyEvent: Flow, Association, Triggering, Serving
ApplicationComponent -> TechnologyFunction: Flow, Association, Triggering, Serving
ApplicationComponent -> TechnologyInteraction: Flow, Association, Triggering, Serving
ApplicationComponent -> TechnologyInterface: Flow, Association, Triggering, Serving
ApplicationComponent -> TechnologyProcess: Flow, Association, Triggering, Serving
ApplicationComponent -> TechnologyService: Flow, Association, Triggering, Serving
ApplicationComponent -> Value: Influence, Association
ApplicationComponent -> ValueStream: Association, Realization

## ApplicationEvent

ApplicationEvent -> ApplicationCollaboration: Flow, Association, Triggering, Serving
ApplicationEvent -> ApplicationComponent: Flow, Association, Triggering, Serving
ApplicationEvent -> ApplicationEvent: Composition, Flow, Aggregation, Association, Specialization, Triggering, Serving
ApplicationEvent -> ApplicationFunction: Flow, Association, Triggering, Serving
ApplicationEvent -> ApplicationInteraction: Flow, Association, Triggering, Serving
ApplicationEvent -> ApplicationInterface: Flow, Association, Triggering, Serving
ApplicationEvent -> ApplicationProcess: Flow, Association, Triggering, Serving
ApplicationEvent -> ApplicationService: Flow, Association, Triggering, Serving
ApplicationEvent -> Artifact: Access, Association
ApplicationEvent -> Assessment: Influence, Association
ApplicationEvent -> BusinessActor: Flow, Association, Triggering, Serving
ApplicationEvent -> BusinessCollaboration: Flow, Association, Triggering, Serving
ApplicationEvent -> BusinessEvent: Flow, Association, Realization, Triggering, Serving
ApplicationEvent -> BusinessFunction: Flow, Association, Triggering, Serving
ApplicationEvent -> BusinessInteraction: Flow, Association, Triggering, Serving
ApplicationEvent -> BusinessInterface: Flow, Association, Triggering, Serving
ApplicationEvent -> BusinessObject: Access, Association
ApplicationEvent -> BusinessProcess: Flow, Association, Triggering, Serving
ApplicationEvent -> BusinessRole: Flow, Association, Triggering, Serving
ApplicationEvent -> BusinessService: Flow, Association, Triggering, Serving
ApplicationEvent -> Capability: Association
ApplicationEvent -> CommunicationNetwork: Flow, Association, Triggering, Serving
ApplicationEvent -> Constraint: Influence, Association, Realization
ApplicationEvent -> Contract: Access, Association
ApplicationEvent -> CourseOfAction: Association
ApplicationEvent -> DataObject: Access, Association
ApplicationEvent -> Device: Flow, Association, Triggering, Serving
ApplicationEvent -> DistributionNetwork: Flow, Association, Triggering, Serving
ApplicationEvent -> Driver: Influence, Association
ApplicationEvent -> Equipment: Flow, Association, Triggering, Serving
ApplicationEvent -> Facility: Flow, Association, Triggering, Serving
ApplicationEvent -> Goal: Influence, Association, Realization
ApplicationEvent -> Material: Access, Association
ApplicationEvent -> Meaning: Influence, Association
ApplicationEvent -> Node: Flow, Association, Triggering, Serving
ApplicationEvent -> Outcome: Influence, Association, Realization
ApplicationEvent -> Path: Flow, Association, Triggering, Serving
ApplicationEvent -> Principle: Influence, Association, Realization
ApplicationEvent -> Product: Flow, Association, Triggering, Serving
ApplicationEvent -> Representation: Access, Association
ApplicationEvent -> Requirement: Influence, Association, Realization
ApplicationEvent -> Resource: Association
ApplicationEvent -> Stakeholder: Influence, Association
ApplicationEvent -> SystemSoftware: Flow, Association, Triggering, Serving
ApplicationEvent -> TechnologyCollaboration: Flow, Association, Triggering, Serving
ApplicationEvent -> TechnologyEvent: Flow, Association, Triggering, Serving
ApplicationEvent -> TechnologyFunction: Flow, Association, Triggering, Serving
ApplicationEvent -> TechnologyInteraction: Flow, Association, Triggering, Serving
ApplicationEvent -> TechnologyInterface: Flow, Association, Triggering, Serving
ApplicationEvent -> TechnologyProcess: Flow, Association, Triggering, Serving
ApplicationEvent -> TechnologyService: Flow, Association, Triggering, Serving
ApplicationEvent -> Value: Influence, Association
ApplicationEvent -> ValueStream: Association

## ApplicationFunction

ApplicationFunction -> ApplicationCollaboration: Flow, Association, Triggering, Serving
ApplicationFunction -> ApplicationComponent: Flow, Association, Triggering, Serving
ApplicationFunction -> ApplicationEvent: Flow, Association, Triggering, Serving
ApplicationFunction -> ApplicationFunction: Composition, Flow, Aggregation, Association, Specialization, Triggering, Serving
ApplicationFunction -> ApplicationInteraction: Composition, Flow, Aggregation, Association, Triggering, Serving
ApplicationFunction -> ApplicationInterface: Flow, Association, Triggering, Serving
ApplicationFunction -> ApplicationProcess: Composition, Flow, Aggregation, Association, Triggering, Serving
ApplicationFunction -> ApplicationService: Flow, Association, Realization, Triggering, Serving
ApplicationFunction -> Artifact: Access, Association
ApplicationFunction -> Assessment: Influence, Association
ApplicationFunction -> BusinessActor: Flow, Association, Triggering, Serving
ApplicationFunction -> BusinessCollaboration: Flow, Association, Triggering, Serving
ApplicationFunction -> BusinessEvent: Flow, Association, Triggering, Serving
ApplicationFunction -> BusinessFunction: Flow, Association, Realization, Triggering, Serving
ApplicationFunction -> BusinessInteraction: Flow, Association, Realization, Triggering, Serving
ApplicationFunction -> BusinessInterface: Flow, Association, Triggering, Serving
ApplicationFunction -> BusinessObject: Access, Association
ApplicationFunction -> BusinessProcess: Flow, Association, Realization, Triggering, Serving
ApplicationFunction -> BusinessRole: Flow, Association, Triggering, Serving
ApplicationFunction -> BusinessService: Flow, Association, Realization, Triggering, Serving
ApplicationFunction -> Capability: Association, Realization
ApplicationFunction -> CommunicationNetwork: Flow, Association, Triggering, Serving
ApplicationFunction -> Constraint: Influence, Association, Realization
ApplicationFunction -> Contract: Access, Association
ApplicationFunction -> CourseOfAction: Association, Realization
ApplicationFunction -> DataObject: Access, Association
ApplicationFunction -> Device: Flow, Association, Triggering, Serving
ApplicationFunction -> DistributionNetwork: Flow, Association, Triggering, Serving
ApplicationFunction -> Driver: Influence, Association
ApplicationFunction -> Equipment: Flow, Association, Triggering, Serving
ApplicationFunction -> Facility: Flow, Association, Triggering, Serving
ApplicationFunction -> Goal: Influence, Association, Realization
ApplicationFunction -> Material: Access, Association
ApplicationFunction -> Meaning: Influence, Association
ApplicationFunction -> Node: Flow, Association, Triggering, Serving
ApplicationFunction -> Outcome: Influence, Association, Realization
ApplicationFunction -> Path: Flow, Association, Triggering, Serving
ApplicationFunction -> Principle: Influence, Association, Realization
ApplicationFunction -> Product: Flow, Association, Triggering, Serving
ApplicationFunction -> Representation: Access, Association
ApplicationFunction -> Requirement: Influence, Association, Realization
ApplicationFunction -> Resource: Association
ApplicationFunction -> Stakeholder: Influence, Association
ApplicationFunction -> SystemSoftware: Flow, Association, Triggering, Serving
ApplicationFunction -> TechnologyCollaboration: Flow, Association, Triggering, Serving
ApplicationFunction -> TechnologyEvent: Flow, Association, Triggering, Serving
ApplicationFunction -> TechnologyFunction: Flow, Association, Triggering, Serving
ApplicationFunction -> TechnologyInteraction: Flow, Association, Triggering, Serving
ApplicationFunction -> TechnologyInterface: Flow, Association, Triggering, Serving
ApplicationFunction -> TechnologyProcess: Flow, Association, Triggering, Serving
ApplicationFunction -> TechnologyService: Flow, Association, Triggering, Serving
ApplicationFunction -> Value: Influence, Association
ApplicationFunction -> ValueStream: Association, Realization

## ApplicationInteraction

ApplicationInteraction -> ApplicationCollaboration: Flow, Association, Triggering, Serving
ApplicationInteraction -> ApplicationComponent: Flow, Association, Triggering, Serving
ApplicationInteraction -> ApplicationEvent: Flow, Association, Triggering, Serving
ApplicationInteraction -> ApplicationFunction: Composition, Flow, Aggregation, Association, Triggering, Serving
ApplicationInteraction -> ApplicationInteraction: Composition, Flow, Aggregation, Association, Specialization, Triggering, Serving
ApplicationInteraction -> ApplicationInterface: Flow, Association, Triggering, Serving
ApplicationInteraction -> ApplicationProcess: Composition, Flow, Aggregation, Association, Triggering, Serving
ApplicationInteraction -> ApplicationService: Flow, Association, Realization, Triggering, Serving
ApplicationInteraction -> Artifact: Access, Association
ApplicationInteraction -> Assessment: Influence, Association
ApplicationInteraction -> BusinessActor: Flow, Association, Triggering, Serving
ApplicationInteraction -> BusinessCollaboration: Flow, Association, Triggering, Serving
ApplicationInteraction -> BusinessEvent: Flow, Association, Triggering, Serving
ApplicationInteraction -> BusinessFunction: Flow, Association, Realization, Triggering, Serving
ApplicationInteraction -> BusinessInteraction: Flow, Association, Realization, Triggering, Serving
ApplicationInteraction -> BusinessInterface: Flow, Association, Triggering, Serving
ApplicationInteraction -> BusinessObject: Access, Association
ApplicationInteraction -> BusinessProcess: Flow, Association, Realization, Triggering, Serving
ApplicationInteraction -> BusinessRole: Flow, Association, Triggering, Serving
ApplicationInteraction -> BusinessService: Flow, Association, Realization, Triggering, Serving
ApplicationInteraction -> Capability: Association, Realization
ApplicationInteraction -> CommunicationNetwork: Flow, Association, Triggering, Serving
ApplicationInteraction -> Constraint: Influence, Association, Realization
ApplicationInteraction -> Contract: Access, Association
ApplicationInteraction -> CourseOfAction: Association, Realization
ApplicationInteraction -> DataObject: Access, Association
ApplicationInteraction -> Device: Flow, Association, Triggering, Serving
ApplicationInteraction -> DistributionNetwork: Flow, Association, Triggering, Serving
ApplicationInteraction -> Driver: Influence, Association
ApplicationInteraction -> Equipment: Flow, Association, Triggering, Serving
ApplicationInteraction -> Facility: Flow, Association, Triggering, Serving
ApplicationInteraction -> Goal: Influence, Association, Realization
ApplicationInteraction -> Material: Access, Association
ApplicationInteraction -> Meaning: Influence, Association
ApplicationInteraction -> Node: Flow, Association, Triggering, Serving
ApplicationInteraction -> Outcome: Influence, Association, Realization
ApplicationInteraction -> Path: Flow, Association, Triggering, Serving
ApplicationInteraction -> Principle: Influence, Association, Realization
ApplicationInteraction -> Product: Flow, Association, Triggering, Serving
ApplicationInteraction -> Representation: Access, Association
ApplicationInteraction -> Requirement: Influence, Association, Realization
ApplicationInteraction -> Resource: Association
ApplicationInteraction -> Stakeholder: Influence, Association
ApplicationInteraction -> SystemSoftware: Flow, Association, Triggering, Serving
ApplicationInteraction -> TechnologyCollaboration: Flow, Association, Triggering, Serving
ApplicationInteraction -> TechnologyEvent: Flow, Association, Triggering, Serving
ApplicationInteraction -> TechnologyFunction: Flow, Association, Triggering, Serving
ApplicationInteraction -> TechnologyInteraction: Flow, Association, Triggering, Serving
ApplicationInteraction -> TechnologyInterface: Flow, Association, Triggering, Serving
ApplicationInteraction -> TechnologyProcess: Flow, Association, Triggering, Serving
ApplicationInteraction -> TechnologyService: Flow, Association, Triggering, Serving
ApplicationInteraction -> Value: Influence, Association
ApplicationInteraction -> ValueStream: Association, Realization

## ApplicationInterface

ApplicationInterface -> ApplicationCollaboration: Flow, Association, Triggering, Serving
ApplicationInterface -> ApplicationComponent: Flow, Association, Triggering, Serving
ApplicationInterface -> ApplicationEvent: Flow, Association, Triggering, Serving
ApplicationInterface -> ApplicationFunction: Flow, Association, Triggering, Serving
ApplicationInterface -> ApplicationInteraction: Flow, Association, Triggering, Serving
ApplicationInterface -> ApplicationInterface: Composition, Flow, Aggregation, Association, Specialization, Triggering, Serving
ApplicationInterface -> ApplicationProcess: Flow, Association, Triggering, Serving
ApplicationInterface -> ApplicationService: Flow, Assignment, Association, Triggering, Serving
ApplicationInterface -> Artifact: Access, Association
ApplicationInterface -> Assessment: Influence, Association
ApplicationInterface -> BusinessActor: Flow, Association, Triggering, Serving
ApplicationInterface -> BusinessCollaboration: Flow, Association, Triggering, Serving
ApplicationInterface -> BusinessEvent: Flow, Association, Triggering, Serving
ApplicationInterface -> BusinessFunction: Flow, Association, Triggering, Serving
ApplicationInterface -> BusinessInteraction: Flow, Association, Triggering, Serving
ApplicationInterface -> BusinessInterface: Flow, Association, Realization, Triggering, Serving
ApplicationInterface -> BusinessObject: Access, Association
ApplicationInterface -> BusinessProcess: Flow, Association, Triggering, Serving
ApplicationInterface -> BusinessRole: Flow, Association, Triggering, Serving
ApplicationInterface -> BusinessService: Flow, Association, Realization, Triggering, Serving
ApplicationInterface -> Capability: Association, Realization
ApplicationInterface -> CommunicationNetwork: Flow, Association, Triggering, Serving
ApplicationInterface -> Constraint: Influence, Association, Realization
ApplicationInterface -> Contract: Access, Association
ApplicationInterface -> CourseOfAction: Association, Realization
ApplicationInterface -> DataObject: Access, Association
ApplicationInterface -> Device: Flow, Association, Triggering, Serving
ApplicationInterface -> DistributionNetwork: Flow, Association, Triggering, Serving
ApplicationInterface -> Driver: Influence, Association
ApplicationInterface -> Equipment: Flow, Association, Triggering, Serving
ApplicationInterface -> Facility: Flow, Association, Triggering, Serving
ApplicationInterface -> Goal: Influence, Association, Realization
ApplicationInterface -> Material: Access, Association
ApplicationInterface -> Meaning: Influence, Association
ApplicationInterface -> Node: Flow, Association, Triggering, Serving
ApplicationInterface -> Outcome: Influence, Association, Realization
ApplicationInterface -> Path: Flow, Association, Triggering, Serving
ApplicationInterface -> Principle: Influence, Association, Realization
ApplicationInterface -> Product: Flow, Association, Triggering, Serving
ApplicationInterface -> Representation: Access, Association
ApplicationInterface -> Requirement: Influence, Association, Realization
ApplicationInterface -> Resource: Association, Realization
ApplicationInterface -> Stakeholder: Influence, Association
ApplicationInterface -> SystemSoftware: Flow, Association, Triggering, Serving
ApplicationInterface -> TechnologyCollaboration: Flow, Association, Triggering, Serving
ApplicationInterface -> TechnologyEvent: Flow, Association, Triggering, Serving
ApplicationInterface -> TechnologyFunction: Flow, Association, Triggering, Serving
ApplicationInterface -> TechnologyInteraction: Flow, Association, Triggering, Serving
ApplicationInterface -> TechnologyInterface: Flow, Association, Triggering, Serving
ApplicationInterface -> TechnologyProcess: Flow, Association, Triggering, Serving
ApplicationInterface -> TechnologyService: Flow, Association, Triggering, Serving
ApplicationInterface -> Value: Influence, Association
ApplicationInterface -> ValueStream: Association, Realization

## ApplicationProcess

ApplicationProcess -> ApplicationCollaboration: Flow, Association, Triggering, Serving
ApplicationProcess -> ApplicationComponent: Flow, Association, Triggering, Serving
ApplicationProcess -> ApplicationEvent: Flow, Association, Triggering, Serving
ApplicationProcess -> ApplicationFunction: Composition, Flow, Aggregation, Association, Triggering, Serving
ApplicationProcess -> ApplicationInteraction: Composition, Flow, Aggregation, Association, Triggering, Serving
ApplicationProcess -> ApplicationInterface: Flow, Association, Triggering, Serving
ApplicationProcess -> ApplicationProcess: Composition, Flow, Aggregation, Association, Specialization, Triggering, Serving
ApplicationProcess -> ApplicationService: Flow, Association, Realization, Triggering, Serving
ApplicationProcess -> Artifact: Access, Association
ApplicationProcess -> Assessment: Influence, Association
ApplicationProcess -> BusinessActor: Flow, Association, Triggering, Serving
ApplicationProcess -> BusinessCollaboration: Flow, Association, Triggering, Serving
ApplicationProcess -> BusinessEvent: Flow, Association, Triggering, Serving
ApplicationProcess -> BusinessFunction: Flow, Association, Realization, Triggering, Serving
ApplicationProcess -> BusinessInteraction: Flow, Association, Realization, Triggering, Serving
ApplicationProcess -> BusinessInterface: Flow, Association, Triggering, Serving
ApplicationProcess -> BusinessObject: Access, Association
ApplicationProcess -> BusinessProcess: Flow, Association, Realization, Triggering, Serving
ApplicationProcess -> BusinessRole: Flow, Association, Triggering, Serving
ApplicationProcess -> BusinessService: Flow, Association, Realization, Triggering, Serving
ApplicationProcess -> Capability: Association, Realization
ApplicationProcess -> CommunicationNetwork: Flow, Association, Triggering, Serving
ApplicationProcess -> Constraint: Influence, Association, Realization
ApplicationProcess -> Contract: Access, Association
ApplicationProcess -> CourseOfAction: Association, Realization
ApplicationProcess -> DataObject: Access, Association
ApplicationProcess -> Device: Flow, Association, Triggering, Serving
ApplicationProcess -> DistributionNetwork: Flow, Association, Triggering, Serving
ApplicationProcess -> Driver: Influence, Association
ApplicationProcess -> Equipment: Flow, Association, Triggering, Serving
ApplicationProcess -> Facility: Flow, Association, Triggering, Serving
ApplicationProcess -> Goal: Influence, Association, Realization
ApplicationProcess -> Material: Access, Association
ApplicationProcess -> Meaning: Influence, Association
ApplicationProcess -> Node: Flow, Association, Triggering, Serving
ApplicationProcess -> Outcome: Influence, Association, Realization
ApplicationProcess -> Path: Flow, Association, Triggering, Serving
ApplicationProcess -> Principle: Influence, Association, Realization
ApplicationProcess -> Product: Flow, Association, Triggering, Serving
ApplicationProcess -> Representation: Access, Association
ApplicationProcess -> Requirement: Influence, Association, Realization
ApplicationProcess -> Resource: Association
ApplicationProcess -> Stakeholder: Influence, Association
ApplicationProcess -> SystemSoftware: Flow, Association, Triggering, Serving
ApplicationProcess -> TechnologyCollaboration: Flow, Association, Triggering, Serving
ApplicationProcess -> TechnologyEvent: Flow, Association, Triggering, Serving
ApplicationProcess -> TechnologyFunction: Flow, Association, Triggering, Serving
ApplicationProcess -> TechnologyInteraction: Flow, Association, Triggering, Serving
ApplicationProcess -> TechnologyInterface: Flow, Association, Triggering, Serving
ApplicationProcess -> TechnologyProcess: Flow, Association, Triggering, Serving
ApplicationProcess -> TechnologyService: Flow, Association, Triggering, Serving
ApplicationProcess -> Value: Influence, Association
ApplicationProcess -> ValueStream: Association, Realization

## ApplicationService

ApplicationService -> ApplicationCollaboration: Flow, Association, Triggering, Serving
ApplicationService -> ApplicationComponent: Flow, Association, Triggering, Serving
ApplicationService -> ApplicationEvent: Flow, Association, Triggering, Serving
ApplicationService -> ApplicationFunction: Flow, Association, Triggering, Serving
ApplicationService -> ApplicationInteraction: Flow, Association, Triggering, Serving
ApplicationService -> ApplicationInterface: Flow, Association, Triggering, Serving
ApplicationService -> ApplicationProcess: Flow, Association, Triggering, Serving
ApplicationService -> ApplicationService: Composition, Flow, Aggregation, Association, Specialization, Triggering, Serving
ApplicationService -> Artifact: Access, Association
ApplicationService -> Assessment: Influence, Association
ApplicationService -> BusinessActor: Flow, Association, Triggering, Serving
ApplicationService -> BusinessCollaboration: Flow, Association, Triggering, Serving
ApplicationService -> BusinessEvent: Flow, Association, Triggering, Serving
ApplicationService -> BusinessFunction: Flow, Association, Triggering, Serving
ApplicationService -> BusinessInteraction: Flow, Association, Triggering, Serving
ApplicationService -> BusinessInterface: Flow, Association, Triggering, Serving
ApplicationService -> BusinessObject: Access, Association
ApplicationService -> BusinessProcess: Flow, Association, Triggering, Serving
ApplicationService -> BusinessRole: Flow, Association, Triggering, Serving
ApplicationService -> BusinessService: Flow, Association, Realization, Triggering, Serving
ApplicationService -> Capability: Association, Realization
ApplicationService -> CommunicationNetwork: Flow, Association, Triggering, Serving
ApplicationService -> Constraint: Influence, Association, Realization
ApplicationService -> Contract: Access, Association
ApplicationService -> CourseOfAction: Association, Realization
ApplicationService -> DataObject: Access, Association
ApplicationService -> Device: Flow, Association, Triggering, Serving
ApplicationService -> DistributionNetwork: Flow, Association, Triggering, Serving
ApplicationService -> Driver: Influence, Association
ApplicationService -> Equipment: Flow, Association, Triggering, Serving
ApplicationService -> Facility: Flow, Association, Triggering, Serving
ApplicationService -> Goal: Influence, Association, Realization
ApplicationService -> Material: Access, Association
ApplicationService -> Meaning: Influence, Association
ApplicationService -> Node: Flow, Association, Triggering, Serving
ApplicationService -> Outcome: Influence, Association, Realization
ApplicationService -> Path: Flow, Association, Triggering, Serving
ApplicationService -> Principle: Influence, Association, Realization
ApplicationService -> Product: Flow, Association, Triggering, Serving
ApplicationService -> Representation: Access, Association
ApplicationService -> Requirement: Influence, Association, Realization
ApplicationService -> Resource: Association
ApplicationService -> Stakeholder: Influence, Association
ApplicationService -> SystemSoftware: Flow, Association, Triggering, Serving
ApplicationService -> TechnologyCollaboration: Flow, Association, Triggering, Serving
ApplicationService -> TechnologyEvent: Flow, Association, Triggering, Serving
ApplicationService -> TechnologyFunction: Flow, Association, Triggering, Serving
ApplicationService -> TechnologyInteraction: Flow, Association, Triggering, Serving
ApplicationService -> TechnologyInterface: Flow, Association, Triggering, Serving
ApplicationService -> TechnologyProcess: Flow, Association, Triggering, Serving
ApplicationService -> TechnologyService: Flow, Association, Triggering, Serving
ApplicationService -> Value: Influence, Association
ApplicationService -> ValueStream: Association, Realization

## Artifact

Artifact -> ApplicationCollaboration: Association, Realization
Artifact -> ApplicationComponent: Association, Realization
Artifact -> ApplicationEvent: Association, Realization
Artifact -> ApplicationFunction: Association, Realization
Artifact -> ApplicationInteraction: Association, Realization
Artifact -> ApplicationInterface: Association, Realization
Artifact -> ApplicationProcess: Association, Realization
Artifact -> ApplicationService: Association, Realization
Artifact -> Artifact: Composition, Aggregation, Association, Realization, Specialization
Artifact -> Assessment: Influence, Association
Artifact -> BusinessActor: Association
Artifact -> BusinessCollaboration: Association
Artifact -> BusinessEvent: Association, Realization
Artifact -> BusinessFunction: Association, Realization
Artifact -> BusinessInteraction: Association, Realization
Artifact -> BusinessInterface: Association, Realization
Artifact -> BusinessObject: Association, Realization
Artifact -> BusinessProcess: Association, Realization
Artifact -> BusinessRole: Association
Artifact -> BusinessService: Association, Realization
Artifact -> Capability: Association, Realization
Artifact -> CommunicationNetwork: Association
Artifact -> Constraint: Influence, Association, Realization
Artifact -> Contract: Association, Realization
Artifact -> CourseOfAction: Association, Realization
Artifact -> DataObject: Association, Realization
Artifact -> Device: Association
Artifact -> DistributionNetwork: Association
Artifact -> Driver: Influence, Association
Artifact -> Equipment: Association
Artifact -> Facility: Association
Artifact -> Goal: Influence, Association, Realization
Artifact -> Material: Association
Artifact -> Meaning: Influence, Association
Artifact -> Node: Association
Artifact -> Outcome: Influence, Association, Realization
Artifact -> Path: Association
Artifact -> Principle: Influence, Association, Realization
Artifact -> Product: Association
Artifact -> Representation: Association
Artifact -> Requirement: Influence, Association, Realization
Artifact -> Resource: Association, Realization
Artifact -> Stakeholder: Influence, Association
Artifact -> SystemSoftware: Association, Realization
Artifact -> TechnologyCollaboration: Association
Artifact -> TechnologyEvent: Association, Realization
Artifact -> TechnologyFunction: Association, Realization
Artifact -> TechnologyInteraction: Association, Realization
Artifact -> TechnologyInterface: Association, Realization
Artifact -> TechnologyProcess: Association, Realization
Artifact -> TechnologyService: Association, Realization
Artifact -> Value: Influence, Association
Artifact -> ValueStream: Association, Realization

## Assessment

Assessment -> ApplicationCollaboration: Association
Assessment -> ApplicationComponent: Association
Assessment -> ApplicationEvent: Association
Assessment -> ApplicationFunction: Association
Assessment -> ApplicationInteraction: Association
Assessment -> ApplicationInterface: Association
Assessment -> ApplicationProcess: Association
Assessment -> ApplicationService: Association
Assessment -> Artifact: Association
Assessment -> Assessment: Composition, Aggregation, Influence, Association, Specialization
Assessment -> BusinessActor: Association
Assessment -> BusinessCollaboration: Association
Assessment -> BusinessEvent: Association
Assessment -> BusinessFunction: Association
Assessment -> BusinessInteraction: Association
Assessment -> BusinessInterface: Association
Assessment -> BusinessObject: Association
Assessment -> BusinessProcess: Association
Assessment -> BusinessRole: Association
Assessment -> BusinessService: Association
Assessment -> Capability: Association
Assessment -> CommunicationNetwork: Association
Assessment -> Constraint: Influence, Association
Assessment -> Contract: Association
Assessment -> CourseOfAction: Association
Assessment -> DataObject: Association
Assessment -> Device: Association
Assessment -> DistributionNetwork: Association
Assessment -> Driver: Influence, Association
Assessment -> Equipment: Association
Assessment -> Facility: Association
Assessment -> Goal: Influence, Association
Assessment -> Material: Association
Assessment -> Meaning: Influence, Association
Assessment -> Node: Association
Assessment -> Outcome: Influence, Association
Assessment -> Path: Association
Assessment -> Principle: Influence, Association
Assessment -> Product: Association
Assessment -> Representation: Association
Assessment -> Requirement: Influence, Association
Assessment -> Resource: Association
Assessment -> Stakeholder: Influence, Association
Assessment -> SystemSoftware: Association
Assessment -> TechnologyCollaboration: Association
Assessment -> TechnologyEvent: Association
Assessment -> TechnologyFunction: Association
Assessment -> TechnologyInteraction: Association
Assessment -> TechnologyInterface: Association
Assessment -> TechnologyProcess: Association
Assessment -> TechnologyService: Association
Assessment -> Value: Influence, Association
Assessment -> ValueStream: Association

## BusinessActor

BusinessActor -> ApplicationCollaboration: Flow, Association, Triggering, Serving
BusinessActor -> ApplicationComponent: Flow, Association, Triggering, Serving
BusinessActor -> ApplicationEvent: Flow, Association, Triggering, Serving
BusinessActor -> ApplicationFunction: Flow, Association, Triggering, Serving
BusinessActor -> ApplicationInteraction: Flow, Association, Triggering, Serving
BusinessActor -> ApplicationInterface: Flow, Association, Triggering, Serving
BusinessActor -> ApplicationProcess: Flow, Association, Triggering, Serving
BusinessActor -> ApplicationService: Flow, Association, Triggering, Serving
BusinessActor -> Artifact: Access, Association
BusinessActor -> Assessment: Influence, Association
BusinessActor -> BusinessActor: Composition, Flow, Aggregation, Association, Specialization, Triggering, Serving
BusinessActor -> BusinessCollaboration: Flow, Association, Triggering, Serving
BusinessActor -> BusinessEvent: Flow, Assignment, Association, Triggering, Serving
BusinessActor -> BusinessFunction: Flow, Assignment, Association, Triggering, Serving
BusinessActor -> BusinessInteraction: Flow, Assignment, Association, Triggering, Serving
BusinessActor -> BusinessInterface: Composition, Flow, Aggregation, Assignment, Association, Triggering, Serving
BusinessActor -> BusinessObject: Access, Association
BusinessActor -> BusinessProcess: Flow, Assignment, Association, Triggering, Serving
BusinessActor -> BusinessRole: Flow, Assignment, Association, Triggering, Serving
BusinessActor -> BusinessService: Flow, Assignment, Association, Realization, Triggering, Serving
BusinessActor -> Capability: Association, Realization
BusinessActor -> CommunicationNetwork: Flow, Association, Triggering, Serving
BusinessActor -> Constraint: Influence, Association, Realization
BusinessActor -> Contract: Access, Association
BusinessActor -> CourseOfAction: Association, Realization
BusinessActor -> DataObject: Access, Association
BusinessActor -> Device: Flow, Association, Triggering, Serving
BusinessActor -> DistributionNetwork: Flow, Association, Triggering, Serving
BusinessActor -> Driver: Influence, Association
BusinessActor -> Equipment: Flow, Association, Triggering, Serving
BusinessActor -> Facility: Flow, Association, Triggering, Serving
BusinessActor -> Goal: Influence, Association, Realization
BusinessActor -> Material: Access, Association
BusinessActor -> Meaning: Influence, Association
BusinessActor -> Node: Flow, Association, Triggering, Serving
BusinessActor -> Outcome: Influence, Association, Realization
BusinessActor -> Path: Flow, Association, Triggering, Serving
BusinessActor -> Principle: Influence, Association, Realization
BusinessActor -> Product: Flow, Association, Triggering, Serving
BusinessActor -> Representation: Access, Association
BusinessActor -> Requirement: Influence, Association, Realization
BusinessActor -> Resource: Association, Realization
BusinessActor -> Stakeholder: Assignment, Influence, Association
BusinessActor -> SystemSoftware: Flow, Association, Triggering, Serving
BusinessActor -> TechnologyCollaboration: Flow, Association, Triggering, Serving
BusinessActor -> TechnologyEvent: Flow, Association, Triggering, Serving
BusinessActor -> TechnologyFunction: Flow, Association, Triggering, Serving
BusinessActor -> TechnologyInteraction: Flow, Association, Triggering, Serving
BusinessActor -> TechnologyInterface: Flow, Association, Triggering, Serving
BusinessActor -> TechnologyProcess: Flow, Association, Triggering, Serving
BusinessActor -> TechnologyService: Flow, Association, Triggering, Serving
BusinessActor -> Value: Influence, Association
BusinessActor -> ValueStream: Association, Realization

## BusinessCollaboration

BusinessCollaboration -> ApplicationCollaboration: Flow, Association, Triggering, Serving
BusinessCollaboration -> ApplicationComponent: Flow, Association, Triggering, Serving
BusinessCollaboration -> ApplicationEvent: Flow, Association, Triggering, Serving
BusinessCollaboration -> ApplicationFunction: Flow, Association, Triggering, Serving
BusinessCollaboration -> ApplicationInteraction: Flow, Association, Triggering, Serving
BusinessCollaboration -> ApplicationInterface: Flow, Association, Triggering, Serving
BusinessCollaboration -> ApplicationProcess: Flow, Association, Triggering, Serving
BusinessCollaboration -> ApplicationService: Flow, Association, Triggering, Serving
BusinessCollaboration -> Artifact: Access, Association
BusinessCollaboration -> Assessment: Influence, Association
BusinessCollaboration -> BusinessActor: Flow, Aggregation, Association, Triggering, Serving
BusinessCollaboration -> BusinessCollaboration: Composition, Flow, Aggregation, Association, Specialization, Triggering, Serving
BusinessCollaboration -> BusinessEvent: Flow, Assignment, Association, Triggering, Serving
BusinessCollaboration -> BusinessFunction: Flow, Assignment, Association, Triggering, Serving
BusinessCollaboration -> BusinessInteraction: Flow, Assignment, Association, Triggering, Serving
BusinessCollaboration -> BusinessInterface: Composition, Flow, Aggregation, Assignment, Association, Triggering, Serving
BusinessCollaboration -> BusinessObject: Access, Association
BusinessCollaboration -> BusinessProcess: Flow, Assignment, Association, Triggering, Serving
BusinessCollaboration -> BusinessRole: Flow, Aggregation, Assignment, Association, Triggering, Serving
BusinessCollaboration -> BusinessService: Flow, Assignment, Association, Realization, Triggering, Serving
BusinessCollaboration -> Capability: Association, Realization
BusinessCollaboration -> CommunicationNetwork: Flow, Association, Triggering, Serving
BusinessCollaboration -> Constraint: Influence, Association, Realization
BusinessCollaboration -> Contract: Access, Association
BusinessCollaboration -> CourseOfAction: Association, Realization
BusinessCollaboration -> DataObject: Access, Association
BusinessCollaboration -> Device: Flow, Association, Triggering, Serving
BusinessCollaboration -> DistributionNetwork: Flow, Association, Triggering, Serving
BusinessCollaboration -> Driver: Influence, Association
BusinessCollaboration -> Equipment: Flow, Association, Triggering, Serving
BusinessCollaboration -> Facility: Flow, Association, Triggering, Serving
BusinessCollaboration -> Goal: Influence, Association, Realization
BusinessCollaboration -> Material: Access, Association
BusinessCollaboration -> Meaning: Influence, Association
BusinessCollaboration -> Node: Flow, Association, Triggering, Serving
BusinessCollaboration -> Outcome: Influence, Association, Realization
BusinessCollaboration -> Path: Flow, Association, Triggering, Serving
BusinessCollaboration -> Principle: Influence, Association, Realization
BusinessCollaboration -> Product: Flow, Association, Triggering, Serving
BusinessCollaboration -> Representation: Access, Association
BusinessCollaboration -> Requirement: Influence, Association, Realization
BusinessCollaboration -> Resource: Association, Realization
BusinessCollaboration -> Stakeholder: Assignment, Influence, Association
BusinessCollaboration -> SystemSoftware: Flow, Association, Triggering, Serving
BusinessCollaboration -> TechnologyCollaboration: Flow, Association, Triggering, Serving
BusinessCollaboration -> TechnologyEvent: Flow, Association, Triggering, Serving
BusinessCollaboration -> TechnologyFunction: Flow, Association, Triggering, Serving
BusinessCollaboration -> TechnologyInteraction: Flow, Association, Triggering, Serving
BusinessCollaboration -> TechnologyInterface: Flow, Association, Triggering, Serving
BusinessCollaboration -> TechnologyProcess: Flow, Association, Triggering, Serving
BusinessCollaboration -> TechnologyService: Flow, Association, Triggering, Serving
BusinessCollaboration -> Value: Influence, Association
BusinessCollaboration -> ValueStream: Association, Realization

## BusinessEvent

BusinessEvent -> ApplicationCollaboration: Flow, Association, Triggering, Serving
BusinessEvent -> ApplicationComponent: Flow, Association, Triggering, Serving
BusinessEvent -> ApplicationEvent: Flow, Association, Triggering, Serving
BusinessEvent -> ApplicationFunction: Flow, Association, Triggering, Serving
BusinessEvent -> ApplicationInteraction: Flow, Association, Triggering, Serving
BusinessEvent -> ApplicationInterface: Flow, Association, Triggering, Serving
BusinessEvent -> ApplicationProcess: Flow, Association, Triggering, Serving
BusinessEvent -> ApplicationService: Flow, Association, Triggering, Serving
BusinessEvent -> Artifact: Access, Association
BusinessEvent -> Assessment: Influence, Association
BusinessEvent -> BusinessActor: Flow, Association, Triggering, Serving
BusinessEvent -> BusinessCollaboration: Flow, Association, Triggering, Serving
BusinessEvent -> BusinessEvent: Composition, Flow, Aggregation, Association, Specialization, Triggering, Serving
BusinessEvent -> BusinessFunction: Flow, Association, Triggering, Serving
BusinessEvent -> BusinessInteraction: Flow, Association, Triggering, Serving
BusinessEvent -> BusinessInterface: Flow, Association, Triggering, Serving
BusinessEvent -> BusinessObject: Access, Association
BusinessEvent -> BusinessProcess: Flow, Association, Triggering, Serving
BusinessEvent -> BusinessRole: Flow, Association, Triggering, Serving
BusinessEvent -> BusinessService: Flow, Association, Triggering, Serving
BusinessEvent -> Capability: Association
BusinessEvent -> CommunicationNetwork: Flow, Association, Triggering, Serving
BusinessEvent -> Constraint: Influence, Association, Realization
BusinessEvent -> Contract: Access, Association
BusinessEvent -> CourseOfAction: Association
BusinessEvent -> DataObject: Access, Association
BusinessEvent -> Device: Flow, Association, Triggering, Serving
BusinessEvent -> DistributionNetwork: Flow, Association, Triggering, Serving
BusinessEvent -> Driver: Influence, Association
BusinessEvent -> Equipment: Flow, Association, Triggering, Serving
BusinessEvent -> Facility: Flow, Association, Triggering, Serving
BusinessEvent -> Goal: Influence, Association, Realization
BusinessEvent -> Material: Access, Association
BusinessEvent -> Meaning: Influence, Association
BusinessEvent -> Node: Flow, Association, Triggering, Serving
BusinessEvent -> Outcome: Influence, Association, Realization
BusinessEvent -> Path: Flow, Association, Triggering, Serving
BusinessEvent -> Principle: Influence, Association, Realization
BusinessEvent -> Product: Flow, Association, Triggering, Serving
BusinessEvent -> Representation: Access, Association
BusinessEvent -> Requirement: Influence, Association, Realization
BusinessEvent -> Resource: Association
BusinessEvent -> Stakeholder: Influence, Association
BusinessEvent -> SystemSoftware: Flow, Association, Triggering, Serving
BusinessEvent -> TechnologyCollaboration: Flow, Association, Triggering, Serving
BusinessEvent -> TechnologyEvent: Flow, Association, Triggering, Serving
BusinessEvent -> TechnologyFunction: Flow, Association, Triggering, Serving
BusinessEvent -> TechnologyInteraction: Flow, Association, Triggering, Serving
BusinessEvent -> TechnologyInterface: Flow, Association, Triggering, Serving
BusinessEvent -> TechnologyProcess: Flow, Association, Triggering, Serving
BusinessEvent -> TechnologyService: Flow, Association, Triggering, Serving
BusinessEvent -> Value: Influence, Association
BusinessEvent -> ValueStream: Association

## BusinessFunction

BusinessFunction -> ApplicationCollaboration: Flow, Association, Triggering, Serving
BusinessFunction -> ApplicationComponent: Flow, Association, Triggering, Serving
BusinessFunction -> ApplicationEvent: Flow, Association, Triggering, Serving
BusinessFunction -> ApplicationFunction: Flow, Association, Triggering, Serving
BusinessFunction -> ApplicationInteraction: Flow, Association, Triggering, Serving
BusinessFunction -> ApplicationInterface: Flow, Association, Triggering, Serving
BusinessFunction -> ApplicationProcess: Flow, Association, Triggering, Serving
BusinessFunction -> ApplicationService: Flow, Association, Triggering, Serving
BusinessFunction -> Artifact: Access, Association
BusinessFunction -> Assessment: Influence, Association
BusinessFunction -> BusinessActor: Flow, Association, Triggering, Serving
BusinessFunction -> BusinessCollaboration: Flow, Association, Triggering, Serving
BusinessFunction -> BusinessEvent: Flow, Association, Triggering, Serving
BusinessFunction -> BusinessFunction: Composition, Flow, Aggregation, Association, Specialization, Triggering, Serving
BusinessFunction -> BusinessInteraction: Composition, Flow, Aggregation, Association, Triggering, Serving
BusinessFunction -> BusinessInterface: Flow, Association, Triggering, Serving
BusinessFunction -> BusinessObject: Access, Association
BusinessFunction -> BusinessProcess: Composition, Flow, Aggregation, Association, Triggering, Serving
BusinessFunction -> BusinessRole: Flow, Association, Triggering, Serving
BusinessFunction -> BusinessService: Flow, Association, Realization, Triggering, Serving
BusinessFunction -> Capability: Association, Realization
BusinessFunction -> CommunicationNetwork: Flow, Association, Triggering, Serving
BusinessFunction -> Constraint: Influence, Association, Realization
BusinessFunction -> Contract: Access, Association
BusinessFunction -> CourseOfAction: Association, Realization
BusinessFunction -> DataObject: Access, Association
BusinessFunction -> Device: Flow, Association, Triggering, Serving
BusinessFunction -> DistributionNetwork: Flow, Association, Triggering, Serving
BusinessFunction -> Driver: Influence, Association
BusinessFunction -> Equipment: Flow, Association, Triggering, Serving
BusinessFunction -> Facility: Flow, Association, Triggering, Serving
BusinessFunction -> Goal: Influence, Association, Realization
BusinessFunction -> Material: Access, Association
BusinessFunction -> Meaning: Influence, Association
BusinessFunction -> Node: Flow, Association, Triggering, Serving
BusinessFunction -> Outcome: Influence, Association, Realization
BusinessFunction -> Path: Flow, Association, Triggering, Serving
BusinessFunction -> Principle: Influence, Association, Realization
BusinessFunction -> Product: Flow, Association, Triggering, Serving
BusinessFunction -> Representation: Access, Association
BusinessFunction -> Requirement: Influence, Association, Realization
BusinessFunction -> Resource: Association
BusinessFunction -> Stakeholder: Influence, Association
BusinessFunction -> SystemSoftware: Flow, Association, Triggering, Serving
BusinessFunction -> TechnologyCollaboration: Flow, Association, Triggering, Serving
BusinessFunction -> TechnologyEvent: Flow, Association, Triggering, Serving
BusinessFunction -> TechnologyFunction: Flow, Association, Triggering, Serving
BusinessFunction -> TechnologyInteraction: Flow, Association, Triggering, Serving
BusinessFunction -> TechnologyInterface: Flow, Association, Triggering, Serving
BusinessFunction -> TechnologyProcess: Flow, Association, Triggering, Serving
BusinessFunction -> TechnologyService: Flow, Association, Triggering, Serving
BusinessFunction -> Value: Influence, Association
BusinessFunction -> ValueStream: Association, Realization

## BusinessInteraction

BusinessInteraction -> ApplicationCollaboration: Flow, Association, Triggering, Serving
BusinessInteraction -> ApplicationComponent: Flow, Association, Triggering, Serving
BusinessInteraction -> ApplicationEvent: Flow, Association, Triggering, Serving
BusinessInteraction -> ApplicationFunction: Flow, Association, Triggering, Serving
BusinessInteraction -> ApplicationInteraction: Flow, Association, Triggering, Serving
BusinessInteraction -> ApplicationInterface: Flow, Association, Triggering, Serving
BusinessInteraction -> ApplicationProcess: Flow, Association, Triggering, Serving
BusinessInteraction -> ApplicationService: Flow, Association, Triggering, Serving
BusinessInteraction -> Artifact: Access, Association
BusinessInteraction -> Assessment: Influence, Association
BusinessInteraction -> BusinessActor: Flow, Association, Triggering, Serving
BusinessInteraction -> BusinessCollaboration: Flow, Association, Triggering, Serving
BusinessInteraction -> BusinessEvent: Flow, Association, Triggering, Serving
BusinessInteraction -> BusinessFunction: Composition, Flow, Aggregation, Association, Triggering, Serving
BusinessInteraction -> BusinessInteraction: Composition, Flow, Aggregation, Association, Specialization, Triggering, Serving
BusinessInteraction -> BusinessInterface: Flow, Association, Triggering, Serving
BusinessInteraction -> BusinessObject: Access, Association
BusinessInteraction -> BusinessProcess: Composition, Flow, Aggregation, Association, Triggering, Serving
BusinessInteraction -> BusinessRole: Flow, Association, Triggering, Serving
BusinessInteraction -> BusinessService: Flow, Association, Realization, Triggering, Serving
BusinessInteraction -> Capability: Association, Realization
BusinessInteraction -> CommunicationNetwork: Flow, Association, Triggering, Serving
BusinessInteraction -> Constraint: Influence, Association, Realization
BusinessInteraction -> Contract: Access, Association
BusinessInteraction -> CourseOfAction: Association, Realization
BusinessInteraction -> DataObject: Access, Association
BusinessInteraction -> Device: Flow, Association, Triggering, Serving
BusinessInteraction -> DistributionNetwork: Flow, Association, Triggering, Serving
BusinessInteraction -> Driver: Influence, Association
BusinessInteraction -> Equipment: Flow, Association, Triggering, Serving
BusinessInteraction -> Facility: Flow, Association, Triggering, Serving
BusinessInteraction -> Goal: Influence, Association, Realization
BusinessInteraction -> Material: Access, Association
BusinessInteraction -> Meaning: Influence, Association
BusinessInteraction -> Node: Flow, Association, Triggering, Serving
BusinessInteraction -> Outcome: Influence, Association, Realization
BusinessInteraction -> Path: Flow, Association, Triggering, Serving
BusinessInteraction -> Principle: Influence, Association, Realization
BusinessInteraction -> Product: Flow, Association, Triggering, Serving
BusinessInteraction -> Representation: Access, Association
BusinessInteraction -> Requirement: Influence, Association, Realization
BusinessInteraction -> Resource: Association
BusinessInteraction -> Stakeholder: Influence, Association
BusinessInteraction -> SystemSoftware: Flow, Association, Triggering, Serving
BusinessInteraction -> TechnologyCollaboration: Flow, Association, Triggering, Serving
BusinessInteraction -> TechnologyEvent: Flow, Association, Triggering, Serving
BusinessInteraction -> TechnologyFunction: Flow, Association, Triggering, Serving
BusinessInteraction -> TechnologyInteraction: Flow, Association, Triggering, Serving
BusinessInteraction -> TechnologyInterface: Flow, Association, Triggering, Serving
BusinessInteraction -> TechnologyProcess: Flow, Association, Triggering, Serving
BusinessInteraction -> TechnologyService: Flow, Association, Triggering, Serving
BusinessInteraction -> Value: Influence, Association
BusinessInteraction -> ValueStream: Association, Realization

## BusinessInterface

BusinessInterface -> ApplicationCollaboration: Flow, Association, Triggering, Serving
BusinessInterface -> ApplicationComponent: Flow, Association, Triggering, Serving
BusinessInterface -> ApplicationEvent: Flow, Association, Triggering, Serving
BusinessInterface -> ApplicationFunction: Flow, Association, Triggering, Serving
BusinessInterface -> ApplicationInteraction: Flow, Association, Triggering, Serving
BusinessInterface -> ApplicationInterface: Flow, Association, Triggering, Serving
BusinessInterface -> ApplicationProcess: Flow, Association, Triggering, Serving
BusinessInterface -> ApplicationService: Flow, Association, Triggering, Serving
BusinessInterface -> Artifact: Access, Association
BusinessInterface -> Assessment: Influence, Association
BusinessInterface -> BusinessActor: Flow, Association, Triggering, Serving
BusinessInterface -> BusinessCollaboration: Flow, Association, Triggering, Serving
BusinessInterface -> BusinessEvent: Flow, Association, Triggering, Serving
BusinessInterface -> BusinessFunction: Flow, Association, Triggering, Serving
BusinessInterface -> BusinessInteraction: Flow, Association, Triggering, Serving
BusinessInterface -> BusinessInterface: Composition, Flow, Aggregation, Association, Specialization, Triggering, Serving
BusinessInterface -> BusinessObject: Access, Association
BusinessInterface -> BusinessProcess: Flow, Association, Triggering, Serving
BusinessInterface -> BusinessRole: Flow, Association, Triggering, Serving
BusinessInterface -> BusinessService: Flow, Assignment, Association, Triggering, Serving
BusinessInterface -> Capability: Association, Realization
BusinessInterface -> CommunicationNetwork: Flow, Association, Triggering, Serving
BusinessInterface -> Constraint: Influence, Association, Realization
BusinessInterface -> Contract: Access, Association
BusinessInterface -> CourseOfAction: Association, Realization
BusinessInterface -> DataObject: Access, Association
BusinessInterface -> Device: Flow, Association, Triggering, Serving
BusinessInterface -> DistributionNetwork: Flow, Association, Triggering, Serving
BusinessInterface -> Driver: Influence, Association
BusinessInterface -> Equipment: Flow, Association, Triggering, Serving
BusinessInterface -> Facility: Flow, Association, Triggering, Serving
BusinessInterface -> Goal: Influence, Association, Realization
BusinessInterface -> Material: Access, Association
BusinessInterface -> Meaning: Influence, Association
BusinessInterface -> Node: Flow, Association, Triggering, Serving
BusinessInterface -> Outcome: Influence, Association, Realization
BusinessInterface -> Path: Flow, Association, Triggering, Serving
BusinessInterface -> Principle: Influence, Association, Realization
BusinessInterface -> Product: Flow, Association, Triggering, Serving
BusinessInterface -> Representation: Access, Association
BusinessInterface -> Requirement: Influence, Association, Realization
BusinessInterface -> Resource: Association, Realization
BusinessInterface -> Stakeholder: Influence, Association
BusinessInterface -> SystemSoftware: Flow, Association, Triggering, Serving
BusinessInterface -> TechnologyCollaboration: Flow, Association, Triggering, Serving
BusinessInterface -> TechnologyEvent: Flow, Association, Triggering, Serving
BusinessInterface -> TechnologyFunction: Flow, Association, Triggering, Serving
BusinessInterface -> TechnologyInteraction: Flow, Association, Triggering, Serving
BusinessInterface -> TechnologyInterface: Flow, Association, Triggering, Serving
BusinessInterface -> TechnologyProcess: Flow, Association, Triggering, Serving
BusinessInterface -> TechnologyService: Flow, Association, Triggering, Serving
BusinessInterface -> Value: Influence, Association
BusinessInterface -> ValueStream: Association, Realization

## BusinessObject

BusinessObject -> ApplicationCollaboration: Association
BusinessObject -> ApplicationComponent: Association
BusinessObject -> ApplicationEvent: Association
BusinessObject -> ApplicationFunction: Association
BusinessObject -> ApplicationInteraction: Association
BusinessObject -> ApplicationInterface: Association
BusinessObject -> ApplicationProcess: Association
BusinessObject -> ApplicationService: Association
BusinessObject -> Artifact: Association
BusinessObject -> Assessment: Influence, Association
BusinessObject -> BusinessActor: Association
BusinessObject -> BusinessCollaboration: Association
BusinessObject -> BusinessEvent: Association
BusinessObject -> BusinessFunction: Association
BusinessObject -> BusinessInteraction: Association
BusinessObject -> BusinessInterface: Association
BusinessObject -> BusinessObject: Composition, Aggregation, Association, Specialization
BusinessObject -> BusinessProcess: Association
BusinessObject -> BusinessRole: Association
BusinessObject -> BusinessService: Association
BusinessObject -> Capability: Association, Realization
BusinessObject -> CommunicationNetwork: Association
BusinessObject -> Constraint: Influence, Association, Realization
BusinessObject -> Contract: Composition, Aggregation, Association, Specialization
BusinessObject -> CourseOfAction: Association, Realization
BusinessObject -> DataObject: Association
BusinessObject -> Device: Association
BusinessObject -> DistributionNetwork: Association
BusinessObject -> Driver: Influence, Association
BusinessObject -> Equipment: Association
BusinessObject -> Facility: Association
BusinessObject -> Goal: Influence, Association, Realization
BusinessObject -> Material: Association
BusinessObject -> Meaning: Influence, Association
BusinessObject -> Node: Association
BusinessObject -> Outcome: Influence, Association, Realization
BusinessObject -> Path: Association
BusinessObject -> Principle: Influence, Association, Realization
BusinessObject -> Product: Association
BusinessObject -> Representation: Association
BusinessObject -> Requirement: Influence, Association, Realization
BusinessObject -> Resource: Association, Realization
BusinessObject -> Stakeholder: Influence, Association
BusinessObject -> SystemSoftware: Association
BusinessObject -> TechnologyCollaboration: Association
BusinessObject -> TechnologyEvent: Association
BusinessObject -> TechnologyFunction: Association
BusinessObject -> TechnologyInteraction: Association
BusinessObject -> TechnologyInterface: Association
BusinessObject -> TechnologyProcess: Association
BusinessObject -> TechnologyService: Association
BusinessObject -> Value: Influence, Association
BusinessObject -> ValueStream: Association, Realization

## BusinessProcess

BusinessProcess -> ApplicationCollaboration: Flow, Association, Triggering, Serving
BusinessProcess -> ApplicationComponent: Flow, Association, Triggering, Serving
BusinessProcess -> ApplicationEvent: Flow, Association, Triggering, Serving
BusinessProcess -> ApplicationFunction: Flow, Association, Triggering, Serving
BusinessProcess -> ApplicationInteraction: Flow, Association, Triggering, Serving
BusinessProcess -> ApplicationInterface: Flow, Association, Triggering, Serving
BusinessProcess -> ApplicationProcess: Flow, Association, Triggering, Serving
BusinessProcess -> ApplicationService: Flow, Association, Triggering, Serving
BusinessProcess -> Artifact: Access, Association
BusinessProcess -> Assessment: Influence, Association
BusinessProcess -> BusinessActor: Flow, Association, Triggering, Serving
BusinessProcess -> BusinessCollaboration: Flow, Association, Triggering, Serving
BusinessProcess -> BusinessEvent: Flow, Association, Triggering, Serving
BusinessProcess -> BusinessFunction: Composition, Flow, Aggregation, Association, Triggering, Serving
BusinessProcess -> BusinessInteraction: Composition, Flow, Aggregation, Association, Triggering, Serving
BusinessProcess -> BusinessInterface: Flow, Association, Triggering, Serving
BusinessProcess -> BusinessObject: Access, Association
BusinessProcess -> BusinessProcess: Composition, Flow, Aggregation, Association, Specialization, Triggering, Serving
BusinessProcess -> BusinessRole: Flow, Association, Triggering, Serving
BusinessProcess -> BusinessService: Flow, Association, Realization, Triggering, Serving
BusinessProcess -> Capability: Association, Realization
BusinessProcess -> CommunicationNetwork: Flow, Association, Triggering, Serving
BusinessProcess -> Constraint: Influence, Association, Realization
BusinessProcess -> Contract: Access, Association
BusinessProcess -> CourseOfAction: Association, Realization
BusinessProcess -> DataObject: Access, Association
BusinessProcess -> Device: Flow, Association, Triggering, Serving
BusinessProcess -> DistributionNetwork: Flow, Association, Triggering, Serving
BusinessProcess -> Driver: Influence, Association
BusinessProcess -> Equipment: Flow, Association, Triggering, Serving
BusinessProcess -> Facility: Flow, Association, Triggering, Serving
BusinessProcess -> Goal: Influence, Association, Realization
BusinessProcess -> Material: Access, Association
BusinessProcess -> Meaning: Influence, Association
BusinessProcess -> Node: Flow, Association, Triggering, Serving
BusinessProcess -> Outcome: Influence, Association, Realization
BusinessProcess -> Path: Flow, Association, Triggering, Serving
BusinessProcess -> Principle: Influence, Association, Realization
BusinessProcess -> Product: Flow, Association, Triggering, Serving
BusinessProcess -> Representation: Access, Association
BusinessProcess -> Requirement: Influence, Association, Realization
BusinessProcess -> Resource: Association
BusinessProcess -> Stakeholder: Influence, Association
BusinessProcess -> SystemSoftware: Flow, Association, Triggering, Serving
BusinessProcess -> TechnologyCollaboration: Flow, Association, Triggering, Serving
BusinessProcess -> TechnologyEvent: Flow, Association, Triggering, Serving
BusinessProcess -> TechnologyFunction: Flow, Association, Triggering, Serving
BusinessProcess -> TechnologyInteraction: Flow, Association, Triggering, Serving
BusinessProcess -> TechnologyInterface: Flow, Association, Triggering, Serving
BusinessProcess -> TechnologyProcess: Flow, Association, Triggering, Serving
BusinessProcess -> TechnologyService: Flow, Association, Triggering, Serving
BusinessProcess -> Value: Influence, Association
BusinessProcess -> ValueStream: Association, Realization

## BusinessRole

BusinessRole -> ApplicationCollaboration: Flow, Association, Triggering, Serving
BusinessRole -> ApplicationComponent: Flow, Association, Triggering, Serving
BusinessRole -> ApplicationEvent: Flow, Association, Triggering, Serving
BusinessRole -> ApplicationFunction: Flow, Association, Triggering, Serving
BusinessRole -> ApplicationInteraction: Flow, Association, Triggering, Serving
BusinessRole -> ApplicationInterface: Flow, Association, Triggering, Serving
BusinessRole -> ApplicationProcess: Flow, Association, Triggering, Serving
BusinessRole -> ApplicationService: Flow, Association, Triggering, Serving
BusinessRole -> Artifact: Access, Association
BusinessRole -> Assessment: Influence, Association
BusinessRole -> BusinessActor: Flow, Association, Triggering, Serving
BusinessRole -> BusinessCollaboration: Flow, Association, Triggering, Serving
BusinessRole -> BusinessEvent: Flow, Assignment, Association, Triggering, Serving
BusinessRole -> BusinessFunction: Flow, Assignment, Association, Triggering, Serving
BusinessRole -> BusinessInteraction: Flow, Assignment, Association, Triggering, Serving
BusinessRole -> BusinessInterface: Composition, Flow, Aggregation, Association, Triggering, Serving
BusinessRole -> BusinessObject: Access, Association
BusinessRole -> BusinessProcess: Flow, Assignment, Association, Triggering, Serving
BusinessRole -> BusinessRole: Composition, Flow, Aggregation, Association, Specialization, Triggering, Serving
BusinessRole -> BusinessService: Flow, Assignment, Association, Realization, Triggering, Serving
BusinessRole -> Capability: Association, Realization
BusinessRole -> CommunicationNetwork: Flow, Association, Triggering, Serving
BusinessRole -> Constraint: Influence, Association, Realization
BusinessRole -> Contract: Access, Association
BusinessRole -> CourseOfAction: Association, Realization
BusinessRole -> DataObject: Access, Association
BusinessRole -> Device: Flow, Association, Triggering, Serving
BusinessRole -> DistributionNetwork: Flow, Association, Triggering, Serving
BusinessRole -> Driver: Influence, Association
BusinessRole -> Equipment: Flow, Association, Triggering, Serving
BusinessRole -> Facility: Flow, Association, Triggering, Serving
BusinessRole -> Goal: Influence, Association, Realization
BusinessRole -> Material: Access, Association
BusinessRole -> Meaning: Influence, Association
BusinessRole -> Node: Flow, Association, Triggering, Serving
BusinessRole -> Outcome: Influence, Association, Realization
BusinessRole -> Path: Flow, Association, Triggering, Serving
BusinessRole -> Principle: Influence, Association, Realization
BusinessRole -> Product: Flow, Association, Triggering, Serving
BusinessRole -> Representation: Access, Association
BusinessRole -> Requirement: Influence, Association, Realization
BusinessRole -> Resource: Association, Realization
BusinessRole -> Stakeholder: Assignment, Influence, Association
BusinessRole -> SystemSoftware: Flow, Association, Triggering, Serving
BusinessRole -> TechnologyCollaboration: Flow, Association, Triggering, Serving
BusinessRole -> TechnologyEvent: Flow, Association, Triggering, Serving
BusinessRole -> TechnologyFunction: Flow, Association, Triggering, Serving
BusinessRole -> TechnologyInteraction: Flow, Association, Triggering, Serving
BusinessRole -> TechnologyInterface: Flow, Association, Triggering, Serving
BusinessRole -> TechnologyProcess: Flow, Association, Triggering, Serving
BusinessRole -> TechnologyService: Flow, Association, Triggering, Serving
BusinessRole -> Value: Influence, Association
BusinessRole -> ValueStream: Association, Realization

## BusinessService

BusinessService -> ApplicationCollaboration: Flow, Association, Triggering, Serving
BusinessService -> ApplicationComponent: Flow, Association, Triggering, Serving
BusinessService -> ApplicationEvent: Flow, Association, Triggering, Serving
BusinessService -> ApplicationFunction: Flow, Association, Triggering, Serving
BusinessService -> ApplicationInteraction: Flow, Association, Triggering, Serving
BusinessService -> ApplicationInterface: Flow, Association, Triggering, Serving
BusinessService -> ApplicationProcess: Flow, Association, Triggering, Serving
BusinessService -> ApplicationService: Flow, Association, Triggering, Serving
BusinessService -> Artifact: Access, Association
BusinessService -> Assessment: Influence, Association
BusinessService -> BusinessActor: Flow, Association, Triggering, Serving
BusinessService -> BusinessCollaboration: Flow, Association, Triggering, Serving
BusinessService -> BusinessEvent: Flow, Association, Triggering, Serving
BusinessService -> BusinessFunction: Flow, Association, Triggering, Serving
BusinessService -> BusinessInteraction: Flow, Association, Triggering, Serving
BusinessService -> BusinessInterface: Flow, Association, Triggering, Serving
BusinessService -> BusinessObject: Access, Association
BusinessService -> BusinessProcess: Flow, Association, Triggering, Serving
BusinessService -> BusinessRole: Flow, Association, Triggering, Serving
BusinessService -> BusinessService: Composition, Flow, Aggregation, Association, Specialization, Triggering, Serving
BusinessService -> Capability: Association, Realization
BusinessService -> CommunicationNetwork: Flow, Association, Triggering, Serving
BusinessService -> Constraint: Influence, Association, Realization
BusinessService -> Contract: Access, Association
BusinessService -> CourseOfAction: Association, Realization
BusinessService -> DataObject: Access, Association
BusinessService -> Device: Flow, Association, Triggering, Serving
BusinessService -> DistributionNetwork: Flow, Association, Triggering, Serving
BusinessService -> Driver: Influence, Association
BusinessService -> Equipment: Flow, Association, Triggering, Serving
BusinessService -> Facility: Flow, Association, Triggering, Serving
BusinessService -> Goal: Influence, Association, Realization
BusinessService -> Material: Access, Association
BusinessService -> Meaning: Influence, Association
BusinessService -> Node: Flow, Association, Triggering, Serving
BusinessService -> Outcome: Influence, Association, Realization
BusinessService -> Path: Flow, Association, Triggering, Serving
BusinessService -> Principle: Influence, Association, Realization
BusinessService -> Product: Flow, Association, Triggering, Serving
BusinessService -> Representation: Access, Association
BusinessService -> Requirement: Influence, Association, Realization
BusinessService -> Resource: Association
BusinessService -> Stakeholder: Influence, Association
BusinessService -> SystemSoftware: Flow, Association, Triggering, Serving
BusinessService -> TechnologyCollaboration: Flow, Association, Triggering, Serving
BusinessService -> TechnologyEvent: Flow, Association, Triggering, Serving
BusinessService -> TechnologyFunction: Flow, Association, Triggering, Serving
BusinessService -> TechnologyInteraction: Flow, Association, Triggering, Serving
BusinessService -> TechnologyInterface: Flow, Association, Triggering, Serving
BusinessService -> TechnologyProcess: Flow, Association, Triggering, Serving
BusinessService -> TechnologyService: Flow, Association, Triggering, Serving
BusinessService -> Value: Influence, Association
BusinessService -> ValueStream: Association, Realization

## Capability

Capability -> ApplicationCollaboration: Association
Capability -> ApplicationComponent: Association
Capability -> ApplicationEvent: Association
Capability -> ApplicationFunction: Association
Capability -> ApplicationInteraction: Association
Capability -> ApplicationInterface: Association
Capability -> ApplicationProcess: Association
Capability -> ApplicationService: Association
Capability -> Artifact: Association
Capability -> Assessment: Influence, Association
Capability -> BusinessActor: Association
Capability -> BusinessCollaboration: Association
Capability -> BusinessEvent: Association
Capability -> BusinessFunction: Association
Capability -> BusinessInteraction: Association
Capability -> BusinessInterface: Association
Capability -> BusinessObject: Association
Capability -> BusinessProcess: Association
Capability -> BusinessRole: Association
Capability -> BusinessService: Association
Capability -> Capability: Composition, Flow, Aggregation, Association, Specialization, Triggering, Serving
Capability -> CommunicationNetwork: Association
Capability -> Constraint: Influence, Association, Realization
Capability -> Contract: Association
Capability -> CourseOfAction: Flow, Association, Realization, Triggering, Serving
Capability -> DataObject: Association
Capability -> Device: Association
Capability -> DistributionNetwork: Association
Capability -> Driver: Influence, Association
Capability -> Equipment: Association
Capability -> Facility: Association
Capability -> Goal: Influence, Association, Realization
Capability -> Material: Association
Capability -> Meaning: Influence, Association
Capability -> Node: Association
Capability -> Outcome: Influence, Association, Realization
Capability -> Path: Association
Capability -> Principle: Influence, Association, Realization
Capability -> Product: Association
Capability -> Representation: Association
Capability -> Requirement: Influence, Association, Realization
Capability -> Resource: Flow, Association, Triggering, Serving
Capability -> Stakeholder: Influence, Association
Capability -> SystemSoftware: Association
Capability -> TechnologyCollaboration: Association
Capability -> TechnologyEvent: Association
Capability -> TechnologyFunction: Association
Capability -> TechnologyInteraction: Association
Capability -> TechnologyInterface: Association
Capability -> TechnologyProcess: Association
Capability -> TechnologyService: Association
Capability -> Value: Influence, Association
Capability -> ValueStream: Flow, Association, Triggering, Serving

## CommunicationNetwork

CommunicationNetwork -> ApplicationCollaboration: Flow, Association, Realization, Triggering, Serving
CommunicationNetwork -> ApplicationComponent: Flow, Association, Realization, Triggering, Serving
CommunicationNetwork -> ApplicationEvent: Flow, Association, Realization, Triggering, Serving
CommunicationNetwork -> ApplicationFunction: Flow, Association, Realization, Triggering, Serving
CommunicationNetwork -> ApplicationInteraction: Flow, Association, Realization, Triggering, Serving
CommunicationNetwork -> ApplicationInterface: Flow, Association, Realization, Triggering, Serving
CommunicationNetwork -> ApplicationProcess: Flow, Association, Realization, Triggering, Serving
CommunicationNetwork -> ApplicationService: Flow, Association, Realization, Triggering, Serving
CommunicationNetwork -> Artifact: Access, Assignment, Association
CommunicationNetwork -> Assessment: Influence, Association
CommunicationNetwork -> BusinessActor: Flow, Association, Realization, Triggering, Serving
CommunicationNetwork -> BusinessCollaboration: Flow, Association, Realization, Triggering, Serving
CommunicationNetwork -> BusinessEvent: Flow, Association, Realization, Triggering, Serving
CommunicationNetwork -> BusinessFunction: Flow, Association, Realization, Triggering, Serving
CommunicationNetwork -> BusinessInteraction: Flow, Association, Realization, Triggering, Serving
CommunicationNetwork -> BusinessInterface: Flow, Association, Realization, Triggering, Serving
CommunicationNetwork -> BusinessObject: Access, Association
CommunicationNetwork -> BusinessProcess: Flow, Association, Realization, Triggering, Serving
CommunicationNetwork -> BusinessRole: Flow, Association, Realization, Triggering, Serving
CommunicationNetwork -> BusinessService: Flow, Association, Realization, Triggering, Serving
CommunicationNetwork -> Capability: Association, Realization
CommunicationNetwork -> CommunicationNetwork: Composition, Flow, Aggregation, Association, Specialization, Triggering, Serving
CommunicationNetwork -> Constraint: Influence, Association, Realization
CommunicationNetwork -> Contract: Access, Association
CommunicationNetwork -> CourseOfAction: Association, Realization
CommunicationNetwork -> DataObject: Access, Association
CommunicationNetwork -> Device: Flow, Aggregation, Association, Realization, Triggering, Serving
CommunicationNetwork -> DistributionNetwork: Flow, Association, Triggering, Serving
CommunicationNetwork -> Driver: Influence, Association
CommunicationNetwork -> Equipment: Flow, Association, Realization, Triggering, Serving
CommunicationNetwork -> Facility: Flow, Association, Realization, Triggering, Serving
CommunicationNetwork -> Goal: Influence, Association, Realization
CommunicationNetwork -> Material: Access, Association
CommunicationNetwork -> Meaning: Influence, Association
CommunicationNetwork -> Node: Flow, Association, Realization, Triggering, Serving
CommunicationNetwork -> Outcome: Influence, Association, Realization
CommunicationNetwork -> Path: Flow, Association, Realization, Triggering, Serving
CommunicationNetwork -> Principle: Influence, Association, Realization
CommunicationNetwork -> Product: Flow, Association, Triggering, Serving
CommunicationNetwork -> Representation: Access, Association
CommunicationNetwork -> Requirement: Influence, Association, Realization
CommunicationNetwork -> Resource: Association, Realization
CommunicationNetwork -> Stakeholder: Influence, Association, Realization
CommunicationNetwork -> SystemSoftware: Flow, Aggregation, Assignment, Association, Realization, Triggering, Serving
CommunicationNetwork -> TechnologyCollaboration: Flow, Association, Realization, Triggering, Serving
CommunicationNetwork -> TechnologyEvent: Flow, Assignment, Association, Realization, Triggering, Serving
CommunicationNetwork -> TechnologyFunction: Flow, Assignment, Association, Realization, Triggering, Serving
CommunicationNetwork -> TechnologyInteraction: Flow, Assignment, Association, Realization, Triggering, Serving
CommunicationNetwork -> TechnologyInterface: Flow, Aggregation, Assignment, Association, Realization, Triggering, Serving
CommunicationNetwork -> TechnologyProcess: Flow, Assignment, Association, Realization, Triggering, Serving
CommunicationNetwork -> TechnologyService: Flow, Assignment, Association, Realization, Triggering, Serving
CommunicationNetwork -> Value: Influence, Association
CommunicationNetwork -> ValueStream: Association, Realization

## Constraint

Constraint -> ApplicationCollaboration: Association
Constraint -> ApplicationComponent: Association
Constraint -> ApplicationEvent: Association
Constraint -> ApplicationFunction: Association
Constraint -> ApplicationInteraction: Association
Constraint -> ApplicationInterface: Association
Constraint -> ApplicationProcess: Association
Constraint -> ApplicationService: Association
Constraint -> Artifact: Association
Constraint -> Assessment: Influence, Association
Constraint -> BusinessActor: Association
Constraint -> BusinessCollaboration: Association
Constraint -> BusinessEvent: Association
Constraint -> BusinessFunction: Association
Constraint -> BusinessInteraction: Association
Constraint -> BusinessInterface: Association
Constraint -> BusinessObject: Association
Constraint -> BusinessProcess: Association
Constraint -> BusinessRole: Association
Constraint -> BusinessService: Association
Constraint -> Capability: Association
Constraint -> CommunicationNetwork: Association
Constraint -> Constraint: Composition, Aggregation, Influence, Association, Specialization
Constraint -> Contract: Association
Constraint -> CourseOfAction: Association
Constraint -> DataObject: Association
Constraint -> Device: Association
Constraint -> DistributionNetwork: Association
Constraint -> Driver: Influence, Association
Constraint -> Equipment: Association
Constraint -> Facility: Association
Constraint -> Goal: Influence, Association, Realization
Constraint -> Material: Association
Constraint -> Meaning: Influence, Association
Constraint -> Node: Association
Constraint -> Outcome: Influence, Association, Realization
Constraint -> Path: Association
Constraint -> Principle: Influence, Association, Realization
Constraint -> Product: Association
Constraint -> Representation: Association
Constraint -> Requirement: Composition, Aggregation, Influence, Association, Specialization
Constraint -> Resource: Association
Constraint -> Stakeholder: Influence, Association
Constraint -> SystemSoftware: Association
Constraint -> TechnologyCollaboration: Association
Constraint -> TechnologyEvent: Association
Constraint -> TechnologyFunction: Association
Constraint -> TechnologyInteraction: Association
Constraint -> TechnologyInterface: Association
Constraint -> TechnologyProcess: Association
Constraint -> TechnologyService: Association
Constraint -> Value: Influence, Association
Constraint -> ValueStream: Association

## Contract

Contract -> ApplicationCollaboration: Association
Contract -> ApplicationComponent: Association
Contract -> ApplicationEvent: Association
Contract -> ApplicationFunction: Association
Contract -> ApplicationInteraction: Association
Contract -> ApplicationInterface: Association
Contract -> ApplicationProcess: Association
Contract -> ApplicationService: Association
Contract -> Artifact: Association
Contract -> Assessment: Influence, Association
Contract -> BusinessActor: Association
Contract -> BusinessCollaboration: Association
Contract -> BusinessEvent: Association
Contract -> BusinessFunction: Association
Contract -> BusinessInteraction: Association
Contract -> BusinessInterface: Association
Contract -> BusinessObject: Composition, Aggregation, Association, Specialization
Contract -> BusinessProcess: Association
Contract -> BusinessRole: Association
Contract -> BusinessService: Association
Contract -> Capability: Association, Realization
Contract -> CommunicationNetwork: Association
Contract -> Constraint: Influence, Association, Realization
Contract -> Contract: Composition, Aggregation, Association, Specialization
Contract -> CourseOfAction: Association, Realization
Contract -> DataObject: Association
Contract -> Device: Association
Contract -> DistributionNetwork: Association
Contract -> Driver: Influence, Association
Contract -> Equipment: Association
Contract -> Facility: Association
Contract -> Goal: Influence, Association, Realization
Contract -> Material: Association
Contract -> Meaning: Influence, Association
Contract -> Node: Association
Contract -> Outcome: Influence, Association, Realization
Contract -> Path: Association
Contract -> Principle: Influence, Association, Realization
Contract -> Product: Association
Contract -> Representation: Association
Contract -> Requirement: Influence, Association, Realization
Contract -> Resource: Association, Realization
Contract -> Stakeholder: Influence, Association
Contract -> SystemSoftware: Association
Contract -> TechnologyCollaboration: Association
Contract -> TechnologyEvent: Association
Contract -> TechnologyFunction: Association
Contract -> TechnologyInteraction: Association
Contract -> TechnologyInterface: Association
Contract -> TechnologyProcess: Association
Contract -> TechnologyService: Association
Contract -> Value: Influence, Association
Contract -> ValueStream: Association, Realization

## CourseOfAction

CourseOfAction -> ApplicationCollaboration: Association
CourseOfAction -> ApplicationComponent: Association
CourseOfAction -> ApplicationEvent: Association
CourseOfAction -> ApplicationFunction: Association
CourseOfAction -> ApplicationInteraction: Association
CourseOfAction -> ApplicationInterface: Association
CourseOfAction -> ApplicationProcess: Association
CourseOfAction -> ApplicationService: Association
CourseOfAction -> Artifact: Association
CourseOfAction -> Assessment: Influence, Association
CourseOfAction -> BusinessActor: Association
CourseOfAction -> BusinessCollaboration: Association
CourseOfAction -> BusinessEvent: Association
CourseOfAction -> BusinessFunction: Association
CourseOfAction -> BusinessInteraction: Association
CourseOfAction -> BusinessInterface: Association
CourseOfAction -> BusinessObject: Association
CourseOfAction -> BusinessProcess: Association
CourseOfAction -> BusinessRole: Association
CourseOfAction -> BusinessService: Association
CourseOfAction -> Capability: Flow, Association, Triggering, Serving
CourseOfAction -> CommunicationNetwork: Association
CourseOfAction -> Constraint: Influence, Association, Realization
CourseOfAction -> Contract: Association
CourseOfAction -> CourseOfAction: Composition, Flow, Aggregation, Association, Specialization, Triggering, Serving
CourseOfAction -> DataObject: Association
CourseOfAction -> Device: Association
CourseOfAction -> DistributionNetwork: Association
CourseOfAction -> Driver: Influence, Association
CourseOfAction -> Equipment: Association
CourseOfAction -> Facility: Association
CourseOfAction -> Goal: Influence, Association, Realization
CourseOfAction -> Material: Association
CourseOfAction -> Meaning: Influence, Association
CourseOfAction -> Node: Association
CourseOfAction -> Outcome: Influence, Association, Realization
CourseOfAction -> Path: Association
CourseOfAction -> Principle: Influence, Association, Realization
CourseOfAction -> Product: Association
CourseOfAction -> Representation: Association
CourseOfAction -> Requirement: Influence, Association, Realization
CourseOfAction -> Resource: Flow, Association, Triggering, Serving
CourseOfAction -> Stakeholder: Influence, Association
CourseOfAction -> SystemSoftware: Association
CourseOfAction -> TechnologyCollaboration: Association
CourseOfAction -> TechnologyEvent: Association
CourseOfAction -> TechnologyFunction: Association
CourseOfAction -> TechnologyInteraction: Association
CourseOfAction -> TechnologyInterface: Association
CourseOfAction -> TechnologyProcess: Association
CourseOfAction -> TechnologyService: Association
CourseOfAction -> Value: Influence, Association
CourseOfAction -> ValueStream: Flow, Association, Triggering, Serving

## DataObject

DataObject -> ApplicationCollaboration: Association
DataObject -> ApplicationComponent: Association
DataObject -> ApplicationEvent: Association
DataObject -> ApplicationFunction: Association
DataObject -> ApplicationInteraction: Association
DataObject -> ApplicationInterface: Association
DataObject -> ApplicationProcess: Association
DataObject -> ApplicationService: Association
DataObject -> Artifact: Association
DataObject -> Assessment: Influence, Association
DataObject -> BusinessActor: Association
DataObject -> BusinessCollaboration: Association
DataObject -> BusinessEvent: Association
DataObject -> BusinessFunction: Association
DataObject -> BusinessInteraction: Association
DataObject -> BusinessInterface: Association
DataObject -> BusinessObject: Association, Realization
DataObject -> BusinessProcess: Association
DataObject -> BusinessRole: Association
DataObject -> BusinessService: Association
DataObject -> Capability: Association, Realization
DataObject -> CommunicationNetwork: Association
DataObject -> Constraint: Influence, Association, Realization
DataObject -> Contract: Association, Realization
DataObject -> CourseOfAction: Association, Realization
DataObject -> DataObject: Composition, Aggregation, Association, Specialization
DataObject -> Device: Association
DataObject -> DistributionNetwork: Association
DataObject -> Driver: Influence, Association
DataObject -> Equipment: Association
DataObject -> Facility: Association
DataObject -> Goal: Influence, Association, Realization
DataObject -> Material: Association
DataObject -> Meaning: Influence, Association
DataObject -> Node: Association
DataObject -> Outcome: Influence, Association, Realization
DataObject -> Path: Association
DataObject -> Principle: Influence, Association, Realization
DataObject -> Product: Association
DataObject -> Representation: Association
DataObject -> Requirement: Influence, Association, Realization
DataObject -> Resource: Association, Realization
DataObject -> Stakeholder: Influence, Association
DataObject -> SystemSoftware: Association
DataObject -> TechnologyCollaboration: Association
DataObject -> TechnologyEvent: Association
DataObject -> TechnologyFunction: Association
DataObject -> TechnologyInteraction: Association
DataObject -> TechnologyInterface: Association
DataObject -> TechnologyProcess: Association
DataObject -> TechnologyService: Association
DataObject -> Value: Influence, Association
DataObject -> ValueStream: Association, Realization

## Device

Device -> ApplicationCollaboration: Flow, Association, Realization, Triggering, Serving
Device -> ApplicationComponent: Flow, Association, Realization, Triggering, Serving
Device -> ApplicationEvent: Flow, Association, Realization, Triggering, Serving
Device -> ApplicationFunction: Flow, Association, Realization, Triggering, Serving
Device -> ApplicationInteraction: Flow, Association, Realization, Triggering, Serving
Device -> ApplicationInterface: Flow, Association, Realization, Triggering, Serving
Device -> ApplicationProcess: Flow, Association, Realization, Triggering, Serving
Device -> ApplicationService: Flow, Association, Realization, Triggering, Serving
Device -> Artifact: Access, Assignment, Association
Device -> Assessment: Influence, Association
Device -> BusinessActor: Flow, Association, Triggering, Serving
Device -> BusinessCollaboration: Flow, Association, Triggering, Serving
Device -> BusinessEvent: Flow, Association, Realization, Triggering, Serving
Device -> BusinessFunction: Flow, Association, Realization, Triggering, Serving
Device -> BusinessInteraction: Flow, Association, Realization, Triggering, Serving
Device -> BusinessInterface: Flow, Association, Realization, Triggering, Serving
Device -> BusinessObject: Access, Association
Device -> BusinessProcess: Flow, Association, Realization, Triggering, Serving
Device -> BusinessRole: Flow, Association, Triggering, Serving
Device -> BusinessService: Flow, Association, Realization, Triggering, Serving
Device -> Capability: Association, Realization
Device -> CommunicationNetwork: Flow, Association, Triggering, Serving
Device -> Constraint: Influence, Association, Realization
Device -> Contract: Access, Association
Device -> CourseOfAction: Association, Realization
Device -> DataObject: Access, Association
Device -> Device: Composition, Flow, Aggregation, Association, Specialization, Triggering, Serving
Device -> DistributionNetwork: Flow, Association, Triggering, Serving
Device -> Driver: Influence, Association
Device -> Equipment: Flow, Association, Triggering, Serving
Device -> Facility: Flow, Association, Triggering, Serving
Device -> Goal: Influence, Association, Realization
Device -> Material: Access, Association
Device -> Meaning: Influence, Association
Device -> Node: Flow, Association, Triggering, Serving
Device -> Outcome: Influence, Association, Realization
Device -> Path: Flow, Association, Triggering, Serving
Device -> Principle: Influence, Association, Realization
Device -> Product: Flow, Association, Triggering, Serving
Device -> Representation: Access, Association
Device -> Requirement: Influence, Association, Realization
Device -> Resource: Association, Realization
Device -> Stakeholder: Influence, Association
Device -> SystemSoftware: Composition, Flow, Aggregation, Assignment, Association, Realization, Triggering, Serving
Device -> TechnologyCollaboration: Flow, Association, Triggering, Serving
Device -> TechnologyEvent: Flow, Assignment, Association, Realization, Triggering, Serving
Device -> TechnologyFunction: Flow, Assignment, Association, Realization, Triggering, Serving
Device -> TechnologyInteraction: Flow, Assignment, Association, Realization, Triggering, Serving
Device -> TechnologyInterface: Composition, Flow, Aggregation, Assignment, Association, Realization, Triggering, Serving
Device -> TechnologyProcess: Flow, Assignment, Association, Realization, Triggering, Serving
Device -> TechnologyService: Flow, Assignment, Association, Realization, Triggering, Serving
Device -> Value: Influence, Association
Device -> ValueStream: Association, Realization

## DistributionNetwork

DistributionNetwork -> ApplicationCollaboration: Flow, Association, Realization, Triggering, Serving
DistributionNetwork -> ApplicationComponent: Flow, Association, Realization, Triggering, Serving
DistributionNetwork -> ApplicationEvent: Flow, Association, Realization, Triggering, Serving
DistributionNetwork -> ApplicationFunction: Flow, Association, Realization, Triggering, Serving
DistributionNetwork -> ApplicationInteraction: Flow, Association, Realization, Triggering, Serving
DistributionNetwork -> ApplicationInterface: Flow, Association, Realization, Triggering, Serving
DistributionNetwork -> ApplicationProcess: Flow, Association, Realization, Triggering, Serving
DistributionNetwork -> ApplicationService: Flow, Association, Realization, Triggering, Serving
DistributionNetwork -> Artifact: Access, Assignment, Association
DistributionNetwork -> Assessment: Influence, Association
DistributionNetwork -> BusinessActor: Flow, Assignment, Association, Realization, Triggering, Serving
DistributionNetwork -> BusinessCollaboration: Flow, Assignment, Association, Realization, Triggering, Serving
DistributionNetwork -> BusinessEvent: Flow, Assignment, Association, Realization, Triggering, Serving
DistributionNetwork -> BusinessFunction: Flow, Assignment, Association, Realization, Triggering, Serving
DistributionNetwork -> BusinessInteraction: Flow, Assignment, Association, Realization, Triggering, Serving
DistributionNetwork -> BusinessInterface: Flow, Assignment, Association, Realization, Triggering, Serving
DistributionNetwork -> BusinessObject: Access, Association
DistributionNetwork -> BusinessProcess: Flow, Assignment, Association, Realization, Triggering, Serving
DistributionNetwork -> BusinessRole: Flow, Assignment, Association, Realization, Triggering, Serving
DistributionNetwork -> BusinessService: Flow, Assignment, Association, Realization, Triggering, Serving
DistributionNetwork -> Capability: Association, Realization
DistributionNetwork -> CommunicationNetwork: Flow, Association, Triggering, Serving
DistributionNetwork -> Constraint: Influence, Association, Realization
DistributionNetwork -> Contract: Access, Association
DistributionNetwork -> CourseOfAction: Association, Realization
DistributionNetwork -> DataObject: Access, Association
DistributionNetwork -> Device: Flow, Aggregation, Assignment, Association, Realization, Triggering, Serving
DistributionNetwork -> DistributionNetwork: Composition, Flow, Aggregation, Association, Specialization, Triggering, Serving
DistributionNetwork -> Driver: Influence, Association
DistributionNetwork -> Equipment: Flow, Aggregation, Assignment, Association, Realization, Triggering, Serving
DistributionNetwork -> Facility: Flow, Aggregation, Assignment, Association, Realization, Triggering, Serving
DistributionNetwork -> Goal: Influence, Association, Realization
DistributionNetwork -> Material: Access, Assignment, Association
DistributionNetwork -> Meaning: Influence, Association
DistributionNetwork -> Node: Flow, Aggregation, Assignment, Association, Realization, Triggering, Serving
DistributionNetwork -> Outcome: Influence, Association, Realization
DistributionNetwork -> Path: Flow, Association, Realization, Triggering, Serving
DistributionNetwork -> Principle: Influence, Association, Realization
DistributionNetwork -> Product: Flow, Association, Triggering, Serving
DistributionNetwork -> Representation: Access, Association
DistributionNetwork -> Requirement: Influence, Association, Realization
DistributionNetwork -> Resource: Association, Realization
DistributionNetwork -> Stakeholder: Assignment, Influence, Association, Realization
DistributionNetwork -> SystemSoftware: Flow, Aggregation, Assignment, Association, Realization, Triggering, Serving
DistributionNetwork -> TechnologyCollaboration: Flow, Association, Realization, Triggering, Serving
DistributionNetwork -> TechnologyEvent: Flow, Assignment, Association, Realization, Triggering, Serving
DistributionNetwork -> TechnologyFunction: Flow, Assignment, Association, Realization, Triggering, Serving
DistributionNetwork -> TechnologyInteraction: Flow, Assignment, Association, Realization, Triggering, Serving
DistributionNetwork -> TechnologyInterface: Flow, Aggregation, Assignment, Association, Realization, Triggering, Serving
DistributionNetwork -> TechnologyProcess: Flow, Assignment, Association, Realization, Triggering, Serving
DistributionNetwork -> TechnologyService: Flow, Assignment, Association, Realization, Triggering, Serving
DistributionNetwork -> Value: Influence, Association
DistributionNetwork -> ValueStream: Association, Realization

## Driver

Driver -> ApplicationCollaboration: Association
Driver -> ApplicationComponent: Association
Driver -> ApplicationEvent: Association
Driver -> ApplicationFunction: Association
Driver -> ApplicationInteraction: Association
Driver -> ApplicationInterface: Association
Driver -> ApplicationProcess: Association
Driver -> ApplicationService: Association
Driver -> Artifact: Association
Driver -> Assessment: Influence, Association
Driver -> BusinessActor: Association
Driver -> BusinessCollaboration: Association
Driver -> BusinessEvent: Association
Driver -> BusinessFunction: Association
Driver -> BusinessInteraction: Association
Driver -> BusinessInterface: Association
Driver -> BusinessObject: Association
Driver -> BusinessProcess: Association
Driver -> BusinessRole: Association
Driver -> BusinessService: Association
Driver -> Capability: Association
Driver -> CommunicationNetwork: Association
Driver -> Constraint: Influence, Association
Driver -> Contract: Association
Driver -> CourseOfAction: Association
Driver -> DataObject: Association
Driver -> Device: Association
Driver -> DistributionNetwork: Association
Driver -> Driver: Composition, Aggregation, Influence, Association, Specialization
Driver -> Equipment: Association
Driver -> Facility: Association
Driver -> Goal: Influence, Association
Driver -> Material: Association
Driver -> Meaning: Influence, Association
Driver -> Node: Association
Driver -> Outcome: Influence, Association
Driver -> Path: Association
Driver -> Principle: Influence, Association
Driver -> Product: Association
Driver -> Representation: Association
Driver -> Requirement: Influence, Association
Driver -> Resource: Association
Driver -> Stakeholder: Influence, Association
Driver -> SystemSoftware: Association
Driver -> TechnologyCollaboration: Association
Driver -> TechnologyEvent: Association
Driver -> TechnologyFunction: Association
Driver -> TechnologyInteraction: Association
Driver -> TechnologyInterface: Association
Driver -> TechnologyProcess: Association
Driver -> TechnologyService: Association
Driver -> Value: Influence, Association
Driver -> ValueStream: Association

## Equipment

Equipment -> ApplicationCollaboration: Flow, Association, Realization, Triggering, Serving
Equipment -> ApplicationComponent: Flow, Association, Realization, Triggering, Serving
Equipment -> ApplicationEvent: Flow, Association, Realization, Triggering, Serving
Equipment -> ApplicationFunction: Flow, Association, Realization, Triggering, Serving
Equipment -> ApplicationInteraction: Flow, Association, Realization, Triggering, Serving
Equipment -> ApplicationInterface: Flow, Association, Realization, Triggering, Serving
Equipment -> ApplicationProcess: Flow, Association, Realization, Triggering, Serving
Equipment -> ApplicationService: Flow, Association, Realization, Triggering, Serving
Equipment -> Artifact: Access, Assignment, Association
Equipment -> Assessment: Influence, Association
Equipment -> BusinessActor: Flow, Association, Triggering, Serving
Equipment -> BusinessCollaboration: Flow, Association, Triggering, Serving
Equipment -> BusinessEvent: Flow, Association, Realization, Triggering, Serving
Equipment -> BusinessFunction: Flow, Association, Realization, Triggering, Serving
Equipment -> BusinessInteraction: Flow, Association, Realization, Triggering, Serving
Equipment -> BusinessInterface: Flow, Association, Realization, Triggering, Serving
Equipment -> BusinessObject: Access, Association
Equipment -> BusinessProcess: Flow, Association, Realization, Triggering, Serving
Equipment -> BusinessRole: Flow, Association, Triggering, Serving
Equipment -> BusinessService: Flow, Association, Realization, Triggering, Serving
Equipment -> Capability: Association, Realization
Equipment -> CommunicationNetwork: Flow, Association, Triggering, Serving
Equipment -> Constraint: Influence, Association, Realization
Equipment -> Contract: Access, Association
Equipment -> CourseOfAction: Association, Realization
Equipment -> DataObject: Access, Association
Equipment -> Device: Composition, Flow, Aggregation, Association, Realization, Triggering, Serving
Equipment -> DistributionNetwork: Flow, Association, Triggering, Serving
Equipment -> Driver: Influence, Association
Equipment -> Equipment: Composition, Flow, Aggregation, Association, Realization, Specialization, Triggering, Serving
Equipment -> Facility: Flow, Association, Triggering, Serving
Equipment -> Goal: Influence, Association, Realization
Equipment -> Material: Access, Assignment, Association
Equipment -> Meaning: Influence, Association
Equipment -> Node: Flow, Association, Triggering, Serving
Equipment -> Outcome: Influence, Association, Realization
Equipment -> Path: Flow, Association, Triggering, Serving
Equipment -> Principle: Influence, Association, Realization
Equipment -> Product: Flow, Association, Triggering, Serving
Equipment -> Representation: Access, Association
Equipment -> Requirement: Influence, Association, Realization
Equipment -> Resource: Association, Realization
Equipment -> Stakeholder: Influence, Association
Equipment -> SystemSoftware: Composition, Flow, Aggregation, Assignment, Association, Realization, Triggering, Serving
Equipment -> TechnologyCollaboration: Flow, Association, Triggering, Serving
Equipment -> TechnologyEvent: Flow, Assignment, Association, Realization, Triggering, Serving
Equipment -> TechnologyFunction: Flow, Assignment, Association, Realization, Triggering, Serving
Equipment -> TechnologyInteraction: Flow, Assignment, Association, Realization, Triggering, Serving
Equipment -> TechnologyInterface: Composition, Flow, Aggregation, Assignment, Association, Realization, Triggering, Serving
Equipment -> TechnologyProcess: Flow, Assignment, Association, Realization, Triggering, Serving
Equipment -> TechnologyService: Flow, Assignment, Association, Realization, Triggering, Serving
Equipment -> Value: Influence, Association
Equipment -> ValueStream: Association, Realization

## Facility

Facility -> ApplicationCollaboration: Flow, Association, Realization, Triggering, Serving
Facility -> ApplicationComponent: Flow, Association, Realization, Triggering, Serving
Facility -> ApplicationEvent: Flow, Association, Realization, Triggering, Serving
Facility -> ApplicationFunction: Flow, Association, Realization, Triggering, Serving
Facility -> ApplicationInteraction: Flow, Association, Realization, Triggering, Serving
Facility -> ApplicationInterface: Flow, Association, Realization, Triggering, Serving
Facility -> ApplicationProcess: Flow, Association, Realization, Triggering, Serving
Facility -> ApplicationService: Flow, Association, Realization, Triggering, Serving
Facility -> Artifact: Access, Assignment, Association
Facility -> Assessment: Influence, Association
Facility -> BusinessActor: Flow, Assignment, Association, Triggering, Serving
Facility -> BusinessCollaboration: Flow, Assignment, Association, Triggering, Serving
Facility -> BusinessEvent: Flow, Assignment, Association, Realization, Triggering, Serving
Facility -> BusinessFunction: Flow, Assignment, Association, Realization, Triggering, Serving
Facility -> BusinessInteraction: Flow, Assignment, Association, Realization, Triggering, Serving
Facility -> BusinessInterface: Flow, Assignment, Association, Realization, Triggering, Serving
Facility -> BusinessObject: Access, Association
Facility -> BusinessProcess: Flow, Assignment, Association, Realization, Triggering, Serving
Facility -> BusinessRole: Flow, Assignment, Association, Triggering, Serving
Facility -> BusinessService: Flow, Assignment, Association, Realization, Triggering, Serving
Facility -> Capability: Association, Realization
Facility -> CommunicationNetwork: Flow, Association, Triggering, Serving
Facility -> Constraint: Influence, Association, Realization
Facility -> Contract: Access, Association
Facility -> CourseOfAction: Association, Realization
Facility -> DataObject: Access, Association
Facility -> Device: Composition, Flow, Aggregation, Assignment, Association, Realization, Triggering, Serving
Facility -> DistributionNetwork: Flow, Association, Triggering, Serving
Facility -> Driver: Influence, Association
Facility -> Equipment: Composition, Flow, Aggregation, Assignment, Association, Realization, Triggering, Serving
Facility -> Facility: Composition, Flow, Aggregation, Assignment, Association, Specialization, Triggering, Serving
Facility -> Goal: Influence, Association, Realization
Facility -> Material: Access, Assignment, Association
Facility -> Meaning: Influence, Association
Facility -> Node: Composition, Flow, Aggregation, Assignment, Association, Triggering, Serving
Facility -> Outcome: Influence, Association, Realization
Facility -> Path: Flow, Association, Triggering, Serving
Facility -> Principle: Influence, Association, Realization
Facility -> Product: Flow, Association, Triggering, Serving
Facility -> Representation: Access, Association
Facility -> Requirement: Influence, Association, Realization
Facility -> Resource: Association, Realization
Facility -> Stakeholder: Assignment, Influence, Association
Facility -> SystemSoftware: Composition, Flow, Aggregation, Assignment, Association, Realization, Triggering, Serving
Facility -> TechnologyCollaboration: Flow, Association, Triggering, Serving
Facility -> TechnologyEvent: Flow, Assignment, Association, Realization, Triggering, Serving
Facility -> TechnologyFunction: Flow, Assignment, Association, Realization, Triggering, Serving
Facility -> TechnologyInteraction: Flow, Assignment, Association, Realization, Triggering, Serving
Facility -> TechnologyInterface: Composition, Flow, Aggregation, Assignment, Association, Realization, Triggering, Serving
Facility -> TechnologyProcess: Flow, Assignment, Association, Realization, Triggering, Serving
Facility -> TechnologyService: Flow, Assignment, Association, Realization, Triggering, Serving
Facility -> Value: Influence, Association
Facility -> ValueStream: Association, Realization

## Goal

Goal -> ApplicationCollaboration: Association
Goal -> ApplicationComponent: Association
Goal -> ApplicationEvent: Association
Goal -> ApplicationFunction: Association
Goal -> ApplicationInteraction: Association
Goal -> ApplicationInterface: Association
Goal -> ApplicationProcess: Association
Goal -> ApplicationService: Association
Goal -> Artifact: Association
Goal -> Assessment: Influence, Association
Goal -> BusinessActor: Association
Goal -> BusinessCollaboration: Association
Goal -> BusinessEvent: Association
Goal -> BusinessFunction: Association
Goal -> BusinessInteraction: Association
Goal -> BusinessInterface: Association
Goal -> BusinessObject: Association
Goal -> BusinessProcess: Association
Goal -> BusinessRole: Association
Goal -> BusinessService: Association
Goal -> Capability: Association
Goal -> CommunicationNetwork: Association
Goal -> Constraint: Influence, Association
Goal -> Contract: Association
Goal -> CourseOfAction: Association
Goal -> DataObject: Association
Goal -> Device: Association
Goal -> DistributionNetwork: Association
Goal -> Driver: Influence, Association
Goal -> Equipment: Association
Goal -> Facility: Association
Goal -> Goal: Composition, Aggregation, Influence, Association, Specialization
Goal -> Material: Association
Goal -> Meaning: Influence, Association
Goal -> Node: Association
Goal -> Outcome: Influence, Association
Goal -> Path: Association
Goal -> Principle: Influence, Association
Goal -> Product: Association
Goal -> Representation: Association
Goal -> Requirement: Influence, Association
Goal -> Resource: Association
Goal -> Stakeholder: Influence, Association
Goal -> SystemSoftware: Association
Goal -> TechnologyCollaboration: Association
Goal -> TechnologyEvent: Association
Goal -> TechnologyFunction: Association
Goal -> TechnologyInteraction: Association
Goal -> TechnologyInterface: Association
Goal -> TechnologyProcess: Association
Goal -> TechnologyService: Association
Goal -> Value: Influence, Association
Goal -> ValueStream: Association

## Material

Material -> ApplicationCollaboration: Association, Realization
Material -> ApplicationComponent: Association, Realization
Material -> ApplicationEvent: Association, Realization
Material -> ApplicationFunction: Association, Realization
Material -> ApplicationInteraction: Association, Realization
Material -> ApplicationInterface: Association, Realization
Material -> ApplicationProcess: Association, Realization
Material -> ApplicationService: Association, Realization
Material -> Artifact: Association, Realization
Material -> Assessment: Influence, Association
Material -> BusinessActor: Association
Material -> BusinessCollaboration: Association
Material -> BusinessEvent: Association, Realization
Material -> BusinessFunction: Association, Realization
Material -> BusinessInteraction: Association, Realization
Material -> BusinessInterface: Association, Realization
Material -> BusinessObject: Association, Realization
Material -> BusinessProcess: Association, Realization
Material -> BusinessRole: Association
Material -> BusinessService: Association, Realization
Material -> Capability: Association, Realization
Material -> CommunicationNetwork: Association
Material -> Constraint: Influence, Association, Realization
Material -> Contract: Association, Realization
Material -> CourseOfAction: Association, Realization
Material -> DataObject: Association, Realization
Material -> Device: Association, Realization
Material -> DistributionNetwork: Association
Material -> Driver: Influence, Association
Material -> Equipment: Association, Realization
Material -> Facility: Association
Material -> Goal: Influence, Association, Realization
Material -> Material: Composition, Aggregation, Association, Realization, Specialization
Material -> Meaning: Influence, Association
Material -> Node: Association
Material -> Outcome: Influence, Association, Realization
Material -> Path: Association
Material -> Principle: Influence, Association, Realization
Material -> Product: Association
Material -> Representation: Association
Material -> Requirement: Influence, Association, Realization
Material -> Resource: Association, Realization
Material -> Stakeholder: Influence, Association
Material -> SystemSoftware: Association, Realization
Material -> TechnologyCollaboration: Association
Material -> TechnologyEvent: Association, Realization
Material -> TechnologyFunction: Association, Realization
Material -> TechnologyInteraction: Association, Realization
Material -> TechnologyInterface: Association, Realization
Material -> TechnologyProcess: Association, Realization
Material -> TechnologyService: Association, Realization
Material -> Value: Influence, Association
Material -> ValueStream: Association, Realization

## Meaning

Meaning -> ApplicationCollaboration: Association
Meaning -> ApplicationComponent: Association
Meaning -> ApplicationEvent: Association
Meaning -> ApplicationFunction: Association
Meaning -> ApplicationInteraction: Association
Meaning -> ApplicationInterface: Association
Meaning -> ApplicationProcess: Association
Meaning -> ApplicationService: Association
Meaning -> Artifact: Association
Meaning -> Assessment: Influence, Association
Meaning -> BusinessActor: Association
Meaning -> BusinessCollaboration: Association
Meaning -> BusinessEvent: Association
Meaning -> BusinessFunction: Association
Meaning -> BusinessInteraction: Association
Meaning -> BusinessInterface: Association
Meaning -> BusinessObject: Association
Meaning -> BusinessProcess: Association
Meaning -> BusinessRole: Association
Meaning -> BusinessService: Association
Meaning -> Capability: Association
Meaning -> CommunicationNetwork: Association
Meaning -> Constraint: Influence, Association
Meaning -> Contract: Association
Meaning -> CourseOfAction: Association
Meaning -> DataObject: Association
Meaning -> Device: Association
Meaning -> DistributionNetwork: Association
Meaning -> Driver: Influence, Association
Meaning -> Equipment: Association
Meaning -> Facility: Association
Meaning -> Goal: Influence, Association
Meaning -> Material: Association
Meaning -> Meaning: Composition, Aggregation, Influence, Association, Specialization
Meaning -> Node: Association
Meaning -> Outcome: Influence, Association
Meaning -> Path: Association
Meaning -> Principle: Influence, Association
Meaning -> Product: Association
Meaning -> Representation: Association
Meaning -> Requirement: Influence, Association
Meaning -> Resource: Association
Meaning -> Stakeholder: Influence, Association
Meaning -> SystemSoftware: Association
Meaning -> TechnologyCollaboration: Association
Meaning -> TechnologyEvent: Association
Meaning -> TechnologyFunction: Association
Meaning -> TechnologyInteraction: Association
Meaning -> TechnologyInterface: Association
Meaning -> TechnologyProcess: Association
Meaning -> TechnologyService: Association
Meaning -> Value: Influence, Association
Meaning -> ValueStream: Association

## Node

Node -> ApplicationCollaboration: Flow, Association, Realization, Triggering, Serving
Node -> ApplicationComponent: Flow, Association, Realization, Triggering, Serving
Node -> ApplicationEvent: Flow, Association, Realization, Triggering, Serving
Node -> ApplicationFunction: Flow, Association, Realization, Triggering, Serving
Node -> ApplicationInteraction: Flow, Association, Realization, Triggering, Serving
Node -> ApplicationInterface: Flow, Association, Realization, Triggering, Serving
Node -> ApplicationProcess: Flow, Association, Realization, Triggering, Serving
Node -> ApplicationService: Flow, Association, Realization, Triggering, Serving
Node -> Artifact: Access, Assignment, Association
Node -> Assessment: Influence, Association
Node -> BusinessActor: Flow, Assignment, Association, Triggering, Serving
Node -> BusinessCollaboration: Flow, Assignment, Association, Triggering, Serving
Node -> BusinessEvent: Flow, Assignment, Association, Realization, Triggering, Serving
Node -> BusinessFunction: Flow, Assignment, Association, Realization, Triggering, Serving
Node -> BusinessInteraction: Flow, Assignment, Association, Realization, Triggering, Serving
Node -> BusinessInterface: Flow, Assignment, Association, Realization, Triggering, Serving
Node -> BusinessObject: Access, Association
Node -> BusinessProcess: Flow, Assignment, Association, Realization, Triggering, Serving
Node -> BusinessRole: Flow, Assignment, Association, Triggering, Serving
Node -> BusinessService: Flow, Assignment, Association, Realization, Triggering, Serving
Node -> Capability: Association, Realization
Node -> CommunicationNetwork: Flow, Association, Triggering, Serving
Node -> Constraint: Influence, Association, Realization
Node -> Contract: Access, Association
Node -> CourseOfAction: Association, Realization
Node -> DataObject: Access, Association
Node -> Device: Composition, Flow, Aggregation, Assignment, Association, Realization, Triggering, Serving
Node -> DistributionNetwork: Flow, Association, Triggering, Serving
Node -> Driver: Influence, Association
Node -> Equipment: Composition, Flow, Aggregation, Assignment, Association, Realization, Triggering, Serving
Node -> Facility: Composition, Flow, Aggregation, Assignment, Association, Triggering, Serving
Node -> Goal: Influence, Association, Realization
Node -> Material: Access, Assignment, Association
Node -> Meaning: Influence, Association
Node -> Node: Composition, Flow, Aggregation, Assignment, Association, Specialization, Triggering, Serving
Node -> Outcome: Influence, Association, Realization
Node -> Path: Flow, Association, Triggering, Serving
Node -> Principle: Influence, Association, Realization
Node -> Product: Flow, Association, Triggering, Serving
Node -> Representation: Access, Association
Node -> Requirement: Influence, Association, Realization
Node -> Resource: Association, Realization
Node -> Stakeholder: Assignment, Influence, Association
Node -> SystemSoftware: Composition, Flow, Aggregation, Assignment, Association, Realization, Triggering, Serving
Node -> TechnologyCollaboration: Flow, Association, Triggering, Serving
Node -> TechnologyEvent: Flow, Assignment, Association, Realization, Triggering, Serving
Node -> TechnologyFunction: Flow, Assignment, Association, Realization, Triggering, Serving
Node -> TechnologyInteraction: Flow, Assignment, Association, Realization, Triggering, Serving
Node -> TechnologyInterface: Composition, Flow, Aggregation, Assignment, Association, Realization, Triggering, Serving
Node -> TechnologyProcess: Flow, Assignment, Association, Realization, Triggering, Serving
Node -> TechnologyService: Flow, Assignment, Association, Realization, Triggering, Serving
Node -> Value: Influence, Association
Node -> ValueStream: Association, Realization

## Outcome

Outcome -> ApplicationCollaboration: Association
Outcome -> ApplicationComponent: Association
Outcome -> ApplicationEvent: Association
Outcome -> ApplicationFunction: Association
Outcome -> ApplicationInteraction: Association
Outcome -> ApplicationInterface: Association
Outcome -> ApplicationProcess: Association
Outcome -> ApplicationService: Association
Outcome -> Artifact: Association
Outcome -> Assessment: Influence, Association
Outcome -> BusinessActor: Association
Outcome -> BusinessCollaboration: Association
Outcome -> BusinessEvent: Association
Outcome -> BusinessFunction: Association
Outcome -> BusinessInteraction: Association
Outcome -> BusinessInterface: Association
Outcome -> BusinessObject: Association
Outcome -> BusinessProcess: Association
Outcome -> BusinessRole: Association
Outcome -> BusinessService: Association
Outcome -> Capability: Association
Outcome -> CommunicationNetwork: Association
Outcome -> Constraint: Influence, Association
Outcome -> Contract: Association
Outcome -> CourseOfAction: Association
Outcome -> DataObject: Association
Outcome -> Device: Association
Outcome -> DistributionNetwork: Association
Outcome -> Driver: Influence, Association
Outcome -> Equipment: Association
Outcome -> Facility: Association
Outcome -> Goal: Influence, Association, Realization
Outcome -> Material: Association
Outcome -> Meaning: Influence, Association
Outcome -> Node: Association
Outcome -> Outcome: Composition, Aggregation, Influence, Association, Specialization
Outcome -> Path: Association
Outcome -> Principle: Influence, Association
Outcome -> Product: Association
Outcome -> Representation: Association
Outcome -> Requirement: Influence, Association
Outcome -> Resource: Association
Outcome -> Stakeholder: Influence, Association
Outcome -> SystemSoftware: Association
Outcome -> TechnologyCollaboration: Association
Outcome -> TechnologyEvent: Association
Outcome -> TechnologyFunction: Association
Outcome -> TechnologyInteraction: Association
Outcome -> TechnologyInterface: Association
Outcome -> TechnologyProcess: Association
Outcome -> TechnologyService: Association
Outcome -> Value: Influence, Association
Outcome -> ValueStream: Association

## Path

Path -> ApplicationCollaboration: Flow, Association, Realization, Triggering, Serving
Path -> ApplicationComponent: Flow, Association, Realization, Triggering, Serving
Path -> ApplicationEvent: Flow, Association, Realization, Triggering, Serving
Path -> ApplicationFunction: Flow, Association, Realization, Triggering, Serving
Path -> ApplicationInteraction: Flow, Association, Realization, Triggering, Serving
Path -> ApplicationInterface: Flow, Association, Realization, Triggering, Serving
Path -> ApplicationProcess: Flow, Association, Realization, Triggering, Serving
Path -> ApplicationService: Flow, Association, Realization, Triggering, Serving
Path -> Artifact: Access, Assignment, Association
Path -> Assessment: Influence, Association
Path -> BusinessActor: Flow, Assignment, Association, Triggering, Serving
Path -> BusinessCollaboration: Flow, Assignment, Association, Triggering, Serving
Path -> BusinessEvent: Flow, Assignment, Association, Realization, Triggering, Serving
Path -> BusinessFunction: Flow, Assignment, Association, Realization, Triggering, Serving
Path -> BusinessInteraction: Flow, Assignment, Association, Realization, Triggering, Serving
Path -> BusinessInterface: Flow, Assignment, Association, Realization, Triggering, Serving
Path -> BusinessObject: Access, Association
Path -> BusinessProcess: Flow, Assignment, Association, Realization, Triggering, Serving
Path -> BusinessRole: Flow, Assignment, Association, Triggering, Serving
Path -> BusinessService: Flow, Assignment, Association, Realization, Triggering, Serving
Path -> Capability: Association, Realization
Path -> CommunicationNetwork: Flow, Association, Triggering, Serving
Path -> Constraint: Influence, Association, Realization
Path -> Contract: Access, Association
Path -> CourseOfAction: Association, Realization
Path -> DataObject: Access, Association
Path -> Device: Flow, Aggregation, Assignment, Association, Realization, Triggering, Serving
Path -> DistributionNetwork: Flow, Association, Triggering, Serving
Path -> Driver: Influence, Association
Path -> Equipment: Flow, Aggregation, Assignment, Association, Realization, Triggering, Serving
Path -> Facility: Flow, Aggregation, Assignment, Association, Triggering, Serving
Path -> Goal: Influence, Association, Realization
Path -> Material: Access, Assignment, Association
Path -> Meaning: Influence, Association
Path -> Node: Flow, Aggregation, Assignment, Association, Triggering, Serving
Path -> Outcome: Influence, Association, Realization
Path -> Path: Composition, Flow, Aggregation, Association, Specialization, Triggering, Serving
Path -> Principle: Influence, Association, Realization
Path -> Product: Flow, Association, Triggering, Serving
Path -> Representation: Access, Association
Path -> Requirement: Influence, Association, Realization
Path -> Resource: Association, Realization
Path -> Stakeholder: Assignment, Influence, Association
Path -> SystemSoftware: Flow, Aggregation, Assignment, Association, Realization, Triggering, Serving
Path -> TechnologyCollaboration: Flow, Aggregation, Association, Triggering, Serving
Path -> TechnologyEvent: Flow, Assignment, Association, Realization, Triggering, Serving
Path -> TechnologyFunction: Flow, Assignment, Association, Realization, Triggering, Serving
Path -> TechnologyInteraction: Flow, Assignment, Association, Realization, Triggering, Serving
Path -> TechnologyInterface: Flow, Aggregation, Assignment, Association, Realization, Triggering, Serving
Path -> TechnologyProcess: Flow, Assignment, Association, Realization, Triggering, Serving
Path -> TechnologyService: Flow, Assignment, Association, Realization, Triggering, Serving
Path -> Value: Influence, Association
Path -> ValueStream: Association, Realization

## Principle

Principle -> ApplicationCollaboration: Association
Principle -> ApplicationComponent: Association
Principle -> ApplicationEvent: Association
Principle -> ApplicationFunction: Association
Principle -> ApplicationInteraction: Association
Principle -> ApplicationInterface: Association
Principle -> ApplicationProcess: Association
Principle -> ApplicationService: Association
Principle -> Artifact: Association
Principle -> Assessment: Influence, Association
Principle -> BusinessActor: Association
Principle -> BusinessCollaboration: Association
Principle -> BusinessEvent: Association
Principle -> BusinessFunction: Association
Principle -> BusinessInteraction: Association
Principle -> BusinessInterface: Association
Principle -> BusinessObject: Association
Principle -> BusinessProcess: Association
Principle -> BusinessRole: Association
Principle -> BusinessService: Association
Principle -> Capability: Association
Principle -> CommunicationNetwork: Association
Principle -> Constraint: Influence, Association
Principle -> Contract: Association
Principle -> CourseOfAction: Association
Principle -> DataObject: Association
Principle -> Device: Association
Principle -> DistributionNetwork: Association
Principle -> Driver: Influence, Association
Principle -> Equipment: Association
Principle -> Facility: Association
Principle -> Goal: Influence, Association, Realization
Principle -> Material: Association
Principle -> Meaning: Influence, Association
Principle -> Node: Association
Principle -> Outcome: Influence, Association, Realization
Principle -> Path: Association
Principle -> Principle: Composition, Aggregation, Influence, Association, Specialization
Principle -> Product: Association
Principle -> Representation: Association
Principle -> Requirement: Influence, Association
Principle -> Resource: Association
Principle -> Stakeholder: Influence, Association
Principle -> SystemSoftware: Association
Principle -> TechnologyCollaboration: Association
Principle -> TechnologyEvent: Association
Principle -> TechnologyFunction: Association
Principle -> TechnologyInteraction: Association
Principle -> TechnologyInterface: Association
Principle -> TechnologyProcess: Association
Principle -> TechnologyService: Association
Principle -> Value: Influence, Association
Principle -> ValueStream: Association

## Product

Product -> ApplicationCollaboration: Flow, Association, Realization, Triggering, Serving
Product -> ApplicationComponent: Flow, Association, Realization, Triggering, Serving
Product -> ApplicationEvent: Flow, Association, Realization, Triggering, Serving
Product -> ApplicationFunction: Flow, Association, Realization, Triggering, Serving
Product -> ApplicationInteraction: Flow, Association, Realization, Triggering, Serving
Product -> ApplicationInterface: Flow, Association, Realization, Triggering, Serving
Product -> ApplicationProcess: Flow, Association, Realization, Triggering, Serving
Product -> ApplicationService: Composition, Flow, Aggregation, Association, Realization, Triggering, Serving
Product -> Artifact: Access, Composition, Aggregation, Association
Product -> Assessment: Influence, Association
Product -> BusinessActor: Flow, Association, Triggering, Serving
Product -> BusinessCollaboration: Flow, Association, Triggering, Serving
Product -> BusinessEvent: Flow, Association, Realization, Triggering, Serving
Product -> BusinessFunction: Flow, Association, Realization, Triggering, Serving
Product -> BusinessInteraction: Flow, Association, Realization, Triggering, Serving
Product -> BusinessInterface: Flow, Association, Realization, Triggering, Serving
Product -> BusinessObject: Access, Composition, Aggregation, Association
Product -> BusinessProcess: Flow, Association, Realization, Triggering, Serving
Product -> BusinessRole: Flow, Association, Triggering, Serving
Product -> BusinessService: Composition, Flow, Aggregation, Association, Realization, Triggering, Serving
Product -> Capability: Association, Realization
Product -> CommunicationNetwork: Flow, Association, Triggering, Serving
Product -> Constraint: Influence, Association, Realization
Product -> Contract: Access, Composition, Aggregation, Association
Product -> CourseOfAction: Association, Realization
Product -> DataObject: Access, Composition, Aggregation, Association
Product -> Device: Flow, Association, Realization, Triggering, Serving
Product -> DistributionNetwork: Flow, Association, Triggering, Serving
Product -> Driver: Influence, Association
Product -> Equipment: Flow, Association, Realization, Triggering, Serving
Product -> Facility: Flow, Association, Triggering, Serving
Product -> Goal: Influence, Association, Realization
Product -> Material: Access, Composition, Aggregation, Association
Product -> Meaning: Influence, Association
Product -> Node: Flow, Association, Triggering, Serving
Product -> Outcome: Influence, Association, Realization
Product -> Path: Flow, Association, Triggering, Serving
Product -> Principle: Influence, Association, Realization
Product -> Product: Composition, Flow, Aggregation, Association, Specialization, Triggering, Serving
Product -> Representation: Access, Composition, Aggregation, Association
Product -> Requirement: Influence, Association, Realization
Product -> Resource: Association, Realization
Product -> Stakeholder: Influence, Association
Product -> SystemSoftware: Flow, Association, Realization, Triggering, Serving
Product -> TechnologyCollaboration: Flow, Association, Triggering, Serving
Product -> TechnologyEvent: Flow, Association, Realization, Triggering, Serving
Product -> TechnologyFunction: Flow, Association, Realization, Triggering, Serving
Product -> TechnologyInteraction: Flow, Association, Realization, Triggering, Serving
Product -> TechnologyInterface: Flow, Association, Realization, Triggering, Serving
Product -> TechnologyProcess: Flow, Association, Realization, Triggering, Serving
Product -> TechnologyService: Composition, Flow, Aggregation, Association, Realization, Triggering, Serving
Product -> Value: Influence, Association
Product -> ValueStream: Association, Realization

## Representation

Representation -> ApplicationCollaboration: Association
Representation -> ApplicationComponent: Association
Representation -> ApplicationEvent: Association
Representation -> ApplicationFunction: Association
Representation -> ApplicationInteraction: Association
Representation -> ApplicationInterface: Association
Representation -> ApplicationProcess: Association
Representation -> ApplicationService: Association
Representation -> Artifact: Association
Representation -> Assessment: Influence, Association
Representation -> BusinessActor: Association
Representation -> BusinessCollaboration: Association
Representation -> BusinessEvent: Association
Representation -> BusinessFunction: Association
Representation -> BusinessInteraction: Association
Representation -> BusinessInterface: Association
Representation -> BusinessObject: Association, Realization
Representation -> BusinessProcess: Association
Representation -> BusinessRole: Association
Representation -> BusinessService: Association
Representation -> Capability: Association, Realization
Representation -> CommunicationNetwork: Association
Representation -> Constraint: Influence, Association, Realization
Representation -> Contract: Association, Realization
Representation -> CourseOfAction: Association, Realization
Representation -> DataObject: Association
Representation -> Device: Association
Representation -> DistributionNetwork: Association
Representation -> Driver: Influence, Association
Representation -> Equipment: Association
Representation -> Facility: Association
Representation -> Goal: Influence, Association, Realization
Representation -> Material: Association
Representation -> Meaning: Influence, Association
Representation -> Node: Association
Representation -> Outcome: Influence, Association, Realization
Representation -> Path: Association
Representation -> Principle: Influence, Association, Realization
Representation -> Product: Association
Representation -> Representation: Composition, Aggregation, Association, Specialization
Representation -> Requirement: Influence, Association, Realization
Representation -> Resource: Association, Realization
Representation -> Stakeholder: Influence, Association
Representation -> SystemSoftware: Association
Representation -> TechnologyCollaboration: Association
Representation -> TechnologyEvent: Association
Representation -> TechnologyFunction: Association
Representation -> TechnologyInteraction: Association
Representation -> TechnologyInterface: Association
Representation -> TechnologyProcess: Association
Representation -> TechnologyService: Association
Representation -> Value: Influence, Association
Representation -> ValueStream: Association, Realization

## Requirement

Requirement -> ApplicationCollaboration: Association
Requirement -> ApplicationComponent: Association
Requirement -> ApplicationEvent: Association
Requirement -> ApplicationFunction: Association
Requirement -> ApplicationInteraction: Association
Requirement -> ApplicationInterface: Association
Requirement -> ApplicationProcess: Association
Requirement -> ApplicationService: Association
Requirement -> Artifact: Association
Requirement -> Assessment: Influence, Association
Requirement -> BusinessActor: Association
Requirement -> BusinessCollaboration: Association
Requirement -> BusinessEvent: Association
Requirement -> BusinessFunction: Association
Requirement -> BusinessInteraction: Association
Requirement -> BusinessInterface: Association
Requirement -> BusinessObject: Association
Requirement -> BusinessProcess: Association
Requirement -> BusinessRole: Association
Requirement -> BusinessService: Association
Requirement -> Capability: Association
Requirement -> CommunicationNetwork: Association
Requirement -> Constraint: Composition, Aggregation, Influence, Association, Specialization
Requirement -> Contract: Association
Requirement -> CourseOfAction: Association
Requirement -> DataObject: Association
Requirement -> Device: Association
Requirement -> DistributionNetwork: Association
Requirement -> Driver: Influence, Association
Requirement -> Equipment: Association
Requirement -> Facility: Association
Requirement -> Goal: Influence, Association, Realization
Requirement -> Material: Association
Requirement -> Meaning: Influence, Association
Requirement -> Node: Association
Requirement -> Outcome: Influence, Association, Realization
Requirement -> Path: Association
Requirement -> Principle: Influence, Association, Realization
Requirement -> Product: Association
Requirement -> Representation: Association
Requirement -> Requirement: Composition, Aggregation, Influence, Association, Specialization
Requirement -> Resource: Association
Requirement -> Stakeholder: Influence, Association
Requirement -> SystemSoftware: Association
Requirement -> TechnologyCollaboration: Association
Requirement -> TechnologyEvent: Association
Requirement -> TechnologyFunction: Association
Requirement -> TechnologyInteraction: Association
Requirement -> TechnologyInterface: Association
Requirement -> TechnologyProcess: Association
Requirement -> TechnologyService: Association
Requirement -> Value: Influence, Association
Requirement -> ValueStream: Association

## Resource

Resource -> ApplicationCollaboration: Association
Resource -> ApplicationComponent: Association
Resource -> ApplicationEvent: Association
Resource -> ApplicationFunction: Association
Resource -> ApplicationInteraction: Association
Resource -> ApplicationInterface: Association
Resource -> ApplicationProcess: Association
Resource -> ApplicationService: Association
Resource -> Artifact: Association
Resource -> Assessment: Influence, Association
Resource -> BusinessActor: Association
Resource -> BusinessCollaboration: Association
Resource -> BusinessEvent: Association
Resource -> BusinessFunction: Association
Resource -> BusinessInteraction: Association
Resource -> BusinessInterface: Association
Resource -> BusinessObject: Association
Resource -> BusinessProcess: Association
Resource -> BusinessRole: Association
Resource -> BusinessService: Association
Resource -> Capability: Flow, Assignment, Association, Triggering, Serving
Resource -> CommunicationNetwork: Association
Resource -> Constraint: Influence, Association, Realization
Resource -> Contract: Association
Resource -> CourseOfAction: Flow, Association, Realization, Triggering, Serving
Resource -> DataObject: Association
Resource -> Device: Association
Resource -> DistributionNetwork: Association
Resource -> Driver: Influence, Association
Resource -> Equipment: Association
Resource -> Facility: Association
Resource -> Goal: Influence, Association, Realization
Resource -> Material: Association
Resource -> Meaning: Influence, Association
Resource -> Node: Association
Resource -> Outcome: Influence, Association, Realization
Resource -> Path: Association
Resource -> Principle: Influence, Association, Realization
Resource -> Product: Association
Resource -> Representation: Association
Resource -> Requirement: Influence, Association, Realization
Resource -> Resource: Composition, Flow, Aggregation, Association, Specialization, Triggering, Serving
Resource -> Stakeholder: Influence, Association
Resource -> SystemSoftware: Association
Resource -> TechnologyCollaboration: Association
Resource -> TechnologyEvent: Association
Resource -> TechnologyFunction: Association
Resource -> TechnologyInteraction: Association
Resource -> TechnologyInterface: Association
Resource -> TechnologyProcess: Association
Resource -> TechnologyService: Association
Resource -> Value: Influence, Association
Resource -> ValueStream: Flow, Assignment, Association, Triggering, Serving

## Stakeholder

Stakeholder -> ApplicationCollaboration: Association
Stakeholder -> ApplicationComponent: Association
Stakeholder -> ApplicationEvent: Association
Stakeholder -> ApplicationFunction: Association
Stakeholder -> ApplicationInteraction: Association
Stakeholder -> ApplicationInterface: Association
Stakeholder -> ApplicationProcess: Association
Stakeholder -> ApplicationService: Association
Stakeholder -> Artifact: Association
Stakeholder -> Assessment: Influence, Association
Stakeholder -> BusinessActor: Association
Stakeholder -> BusinessCollaboration: Association
Stakeholder -> BusinessEvent: Association
Stakeholder -> BusinessFunction: Association
Stakeholder -> BusinessInteraction: Association
Stakeholder -> BusinessInterface: Association
Stakeholder -> BusinessObject: Association
Stakeholder -> BusinessProcess: Association
Stakeholder -> BusinessRole: Association
Stakeholder -> BusinessService: Association
Stakeholder -> Capability: Association
Stakeholder -> CommunicationNetwork: Association
Stakeholder -> Constraint: Influence, Association
Stakeholder -> Contract: Association
Stakeholder -> CourseOfAction: Association
Stakeholder -> DataObject: Association
Stakeholder -> Device: Association
Stakeholder -> DistributionNetwork: Association
Stakeholder -> Driver: Influence, Association
Stakeholder -> Equipment: Association
Stakeholder -> Facility: Association
Stakeholder -> Goal: Influence, Association
Stakeholder -> Material: Association
Stakeholder -> Meaning: Influence, Association
Stakeholder -> Node: Association
Stakeholder -> Outcome: Influence, Association
Stakeholder -> Path: Association
Stakeholder -> Principle: Influence, Association
Stakeholder -> Product: Association
Stakeholder -> Representation: Association
Stakeholder -> Requirement: Influence, Association
Stakeholder -> Resource: Association
Stakeholder -> Stakeholder: Composition, Aggregation, Influence, Association, Specialization
Stakeholder -> SystemSoftware: Association
Stakeholder -> TechnologyCollaboration: Association
Stakeholder -> TechnologyEvent: Association
Stakeholder -> TechnologyFunction: Association
Stakeholder -> TechnologyInteraction: Association
Stakeholder -> TechnologyInterface: Association
Stakeholder -> TechnologyProcess: Association
Stakeholder -> TechnologyService: Association
Stakeholder -> Value: Influence, Association
Stakeholder -> ValueStream: Association

## SystemSoftware

SystemSoftware -> ApplicationCollaboration: Flow, Association, Realization, Triggering, Serving
SystemSoftware -> ApplicationComponent: Flow, Association, Realization, Triggering, Serving
SystemSoftware -> ApplicationEvent: Flow, Association, Realization, Triggering, Serving
SystemSoftware -> ApplicationFunction: Flow, Association, Realization, Triggering, Serving
SystemSoftware -> ApplicationInteraction: Flow, Association, Realization, Triggering, Serving
SystemSoftware -> ApplicationInterface: Flow, Association, Realization, Triggering, Serving
SystemSoftware -> ApplicationProcess: Flow, Association, Realization, Triggering, Serving
SystemSoftware -> ApplicationService: Flow, Association, Realization, Triggering, Serving
SystemSoftware -> Artifact: Access, Assignment, Association
SystemSoftware -> Assessment: Influence, Association
SystemSoftware -> BusinessActor: Flow, Association, Triggering, Serving
SystemSoftware -> BusinessCollaboration: Flow, Association, Triggering, Serving
SystemSoftware -> BusinessEvent: Flow, Association, Realization, Triggering, Serving
SystemSoftware -> BusinessFunction: Flow, Association, Realization, Triggering, Serving
SystemSoftware -> BusinessInteraction: Flow, Association, Realization, Triggering, Serving
SystemSoftware -> BusinessInterface: Flow, Association, Realization, Triggering, Serving
SystemSoftware -> BusinessObject: Access, Association
SystemSoftware -> BusinessProcess: Flow, Association, Realization, Triggering, Serving
SystemSoftware -> BusinessRole: Flow, Association, Triggering, Serving
SystemSoftware -> BusinessService: Flow, Association, Realization, Triggering, Serving
SystemSoftware -> Capability: Association, Realization
SystemSoftware -> CommunicationNetwork: Flow, Association, Triggering, Serving
SystemSoftware -> Constraint: Influence, Association, Realization
SystemSoftware -> Contract: Access, Association
SystemSoftware -> CourseOfAction: Association, Realization
SystemSoftware -> DataObject: Access, Association
SystemSoftware -> Device: Flow, Association, Triggering, Serving
SystemSoftware -> DistributionNetwork: Flow, Association, Triggering, Serving
SystemSoftware -> Driver: Influence, Association
SystemSoftware -> Equipment: Flow, Association, Triggering, Serving
SystemSoftware -> Facility: Flow, Association, Triggering, Serving
SystemSoftware -> Goal: Influence, Association, Realization
SystemSoftware -> Material: Access, Association
SystemSoftware -> Meaning: Influence, Association
SystemSoftware -> Node: Flow, Association, Triggering, Serving
SystemSoftware -> Outcome: Influence, Association, Realization
SystemSoftware -> Path: Flow, Association, Triggering, Serving
SystemSoftware -> Principle: Influence, Association, Realization
SystemSoftware -> Product: Flow, Association, Triggering, Serving
SystemSoftware -> Representation: Access, Association
SystemSoftware -> Requirement: Influence, Association, Realization
SystemSoftware -> Resource: Association, Realization
SystemSoftware -> Stakeholder: Influence, Association
SystemSoftware -> SystemSoftware: Composition, Flow, Aggregation, Assignment, Association, Realization, Specialization, Triggering, Serving
SystemSoftware -> TechnologyCollaboration: Flow, Association, Triggering, Serving
SystemSoftware -> TechnologyEvent: Flow, Assignment, Association, Realization, Triggering, Serving
SystemSoftware -> TechnologyFunction: Flow, Assignment, Association, Realization, Triggering, Serving
SystemSoftware -> TechnologyInteraction: Flow, Assignment, Association, Realization, Triggering, Serving
SystemSoftware -> TechnologyInterface: Composition, Flow, Aggregation, Assignment, Association, Realization, Triggering, Serving
SystemSoftware -> TechnologyProcess: Flow, Assignment, Association, Realization, Triggering, Serving
SystemSoftware -> TechnologyService: Flow, Assignment, Association, Realization, Triggering, Serving
SystemSoftware -> Value: Influence, Association
SystemSoftware -> ValueStream: Association, Realization

## TechnologyCollaboration

TechnologyCollaboration -> ApplicationCollaboration: Flow, Association, Realization, Triggering, Serving
TechnologyCollaboration -> ApplicationComponent: Flow, Association, Realization, Triggering, Serving
TechnologyCollaboration -> ApplicationEvent: Flow, Association, Realization, Triggering, Serving
TechnologyCollaboration -> ApplicationFunction: Flow, Association, Realization, Triggering, Serving
TechnologyCollaboration -> ApplicationInteraction: Flow, Association, Realization, Triggering, Serving
TechnologyCollaboration -> ApplicationInterface: Flow, Association, Realization, Triggering, Serving
TechnologyCollaboration -> ApplicationProcess: Flow, Association, Realization, Triggering, Serving
TechnologyCollaboration -> ApplicationService: Flow, Association, Realization, Triggering, Serving
TechnologyCollaboration -> Artifact: Access, Assignment, Association
TechnologyCollaboration -> Assessment: Influence, Association
TechnologyCollaboration -> BusinessActor: Flow, Assignment, Association, Triggering, Serving
TechnologyCollaboration -> BusinessCollaboration: Flow, Assignment, Association, Triggering, Serving
TechnologyCollaboration -> BusinessEvent: Flow, Assignment, Association, Realization, Triggering, Serving
TechnologyCollaboration -> BusinessFunction: Flow, Assignment, Association, Realization, Triggering, Serving
TechnologyCollaboration -> BusinessInteraction: Flow, Assignment, Association, Realization, Triggering, Serving
TechnologyCollaboration -> BusinessInterface: Flow, Assignment, Association, Realization, Triggering, Serving
TechnologyCollaboration -> BusinessObject: Access, Association
TechnologyCollaboration -> BusinessProcess: Flow, Assignment, Association, Realization, Triggering, Serving
TechnologyCollaboration -> BusinessRole: Flow, Assignment, Association, Triggering, Serving
TechnologyCollaboration -> BusinessService: Flow, Assignment, Association, Realization, Triggering, Serving
TechnologyCollaboration -> Capability: Association, Realization
TechnologyCollaboration -> CommunicationNetwork: Flow, Association, Triggering, Serving
TechnologyCollaboration -> Constraint: Influence, Association, Realization
TechnologyCollaboration -> Contract: Access, Association
TechnologyCollaboration -> CourseOfAction: Association, Realization
TechnologyCollaboration -> DataObject: Access, Association
TechnologyCollaboration -> Device: Flow, Aggregation, Assignment, Association, Realization, Triggering, Serving
TechnologyCollaboration -> DistributionNetwork: Flow, Association, Triggering, Serving
TechnologyCollaboration -> Driver: Influence, Association
TechnologyCollaboration -> Equipment: Flow, Aggregation, Assignment, Association, Realization, Triggering, Serving
TechnologyCollaboration -> Facility: Flow, Aggregation, Assignment, Association, Triggering, Serving
TechnologyCollaboration -> Goal: Influence, Association, Realization
TechnologyCollaboration -> Material: Access, Assignment, Association
TechnologyCollaboration -> Meaning: Influence, Association
TechnologyCollaboration -> Node: Flow, Aggregation, Assignment, Association, Triggering, Serving
TechnologyCollaboration -> Outcome: Influence, Association, Realization
TechnologyCollaboration -> Path: Flow, Association, Triggering, Serving
TechnologyCollaboration -> Principle: Influence, Association, Realization
TechnologyCollaboration -> Product: Flow, Association, Triggering, Serving
TechnologyCollaboration -> Representation: Access, Association
TechnologyCollaboration -> Requirement: Influence, Association, Realization
TechnologyCollaboration -> Resource: Association, Realization
TechnologyCollaboration -> Stakeholder: Assignment, Influence, Association
TechnologyCollaboration -> SystemSoftware: Flow, Aggregation, Assignment, Association, Realization, Triggering, Serving
TechnologyCollaboration -> TechnologyCollaboration: Composition, Flow, Aggregation, Association, Specialization, Triggering, Serving
TechnologyCollaboration -> TechnologyEvent: Flow, Assignment, Association, Realization, Triggering, Serving
TechnologyCollaboration -> TechnologyFunction: Flow, Assignment, Association, Realization, Triggering, Serving
TechnologyCollaboration -> TechnologyInteraction: Flow, Assignment, Association, Realization, Triggering, Serving
TechnologyCollaboration -> TechnologyInterface: Composition, Flow, Aggregation, Assignment, Association, Realization, Triggering, Serving
TechnologyCollaboration -> TechnologyProcess: Flow, Assignment, Association, Realization, Triggering, Serving
TechnologyCollaboration -> TechnologyService: Flow, Assignment, Association, Realization, Triggering, Serving
TechnologyCollaboration -> Value: Influence, Association
TechnologyCollaboration -> ValueStream: Association, Realization

## TechnologyEvent

TechnologyEvent -> ApplicationCollaboration: Flow, Association, Triggering, Serving
TechnologyEvent -> ApplicationComponent: Flow, Association, Triggering, Serving
TechnologyEvent -> ApplicationEvent: Flow, Association, Realization, Triggering, Serving
TechnologyEvent -> ApplicationFunction: Flow, Association, Triggering, Serving
TechnologyEvent -> ApplicationInteraction: Flow, Association, Triggering, Serving
TechnologyEvent -> ApplicationInterface: Flow, Association, Triggering, Serving
TechnologyEvent -> ApplicationProcess: Flow, Association, Triggering, Serving
TechnologyEvent -> ApplicationService: Flow, Association, Triggering, Serving
TechnologyEvent -> Artifact: Access, Association
TechnologyEvent -> Assessment: Influence, Association
TechnologyEvent -> BusinessActor: Flow, Association, Triggering, Serving
TechnologyEvent -> BusinessCollaboration: Flow, Association, Triggering, Serving
TechnologyEvent -> BusinessEvent: Flow, Association, Realization, Triggering, Serving
TechnologyEvent -> BusinessFunction: Flow, Association, Triggering, Serving
TechnologyEvent -> BusinessInteraction: Flow, Association, Triggering, Serving
TechnologyEvent -> BusinessInterface: Flow, Association, Triggering, Serving
TechnologyEvent -> BusinessObject: Access, Association
TechnologyEvent -> BusinessProcess: Flow, Association, Triggering, Serving
TechnologyEvent -> BusinessRole: Flow, Association, Triggering, Serving
TechnologyEvent -> BusinessService: Flow, Association, Triggering, Serving
TechnologyEvent -> Capability: Association
TechnologyEvent -> CommunicationNetwork: Flow, Association, Triggering, Serving
TechnologyEvent -> Constraint: Influence, Association, Realization
TechnologyEvent -> Contract: Access, Association
TechnologyEvent -> CourseOfAction: Association
TechnologyEvent -> DataObject: Access, Association
TechnologyEvent -> Device: Flow, Association, Triggering, Serving
TechnologyEvent -> DistributionNetwork: Flow, Association, Triggering, Serving
TechnologyEvent -> Driver: Influence, Association
TechnologyEvent -> Equipment: Flow, Association, Triggering, Serving
TechnologyEvent -> Facility: Flow, Association, Triggering, Serving
TechnologyEvent -> Goal: Influence, Association, Realization
TechnologyEvent -> Material: Access, Association
TechnologyEvent -> Meaning: Influence, Association
TechnologyEvent -> Node: Flow, Association, Triggering, Serving
TechnologyEvent -> Outcome: Influence, Association, Realization
TechnologyEvent -> Path: Flow, Association, Triggering, Serving
TechnologyEvent -> Principle: Influence, Association, Realization
TechnologyEvent -> Product: Flow, Association, Triggering, Serving
TechnologyEvent -> Representation: Access, Association
TechnologyEvent -> Requirement: Influence, Association, Realization
TechnologyEvent -> Resource: Association
TechnologyEvent -> Stakeholder: Influence, Association
TechnologyEvent -> SystemSoftware: Flow, Association, Triggering, Serving
TechnologyEvent -> TechnologyCollaboration: Flow, Association, Triggering, Serving
TechnologyEvent -> TechnologyEvent: Composition, Flow, Aggregation, Association, Specialization, Triggering, Serving
TechnologyEvent -> TechnologyFunction: Flow, Association, Triggering, Serving
TechnologyEvent -> TechnologyInteraction: Flow, Association, Triggering, Serving
TechnologyEvent -> TechnologyInterface: Flow, Association, Triggering, Serving
TechnologyEvent -> TechnologyProcess: Flow, Association, Triggering, Serving
TechnologyEvent -> TechnologyService: Flow, Association, Triggering, Serving
TechnologyEvent -> Value: Influence, Association
TechnologyEvent -> ValueStream: Association

## TechnologyFunction

TechnologyFunction -> ApplicationCollaboration: Flow, Association, Triggering, Serving
TechnologyFunction -> ApplicationComponent: Flow, Association, Triggering, Serving
TechnologyFunction -> ApplicationEvent: Flow, Association, Triggering, Serving
TechnologyFunction -> ApplicationFunction: Flow, Association, Realization, Triggering, Serving
TechnologyFunction -> ApplicationInteraction: Flow, Association, Realization, Triggering, Serving
TechnologyFunction -> ApplicationInterface: Flow, Association, Triggering, Serving
TechnologyFunction -> ApplicationProcess: Flow, Association, Realization, Triggering, Serving
TechnologyFunction -> ApplicationService: Flow, Association, Realization, Triggering, Serving
TechnologyFunction -> Artifact: Access, Association
TechnologyFunction -> Assessment: Influence, Association
TechnologyFunction -> BusinessActor: Flow, Association, Triggering, Serving
TechnologyFunction -> BusinessCollaboration: Flow, Association, Triggering, Serving
TechnologyFunction -> BusinessEvent: Flow, Association, Triggering, Serving
TechnologyFunction -> BusinessFunction: Flow, Association, Realization, Triggering, Serving
TechnologyFunction -> BusinessInteraction: Flow, Association, Realization, Triggering, Serving
TechnologyFunction -> BusinessInterface: Flow, Association, Triggering, Serving
TechnologyFunction -> BusinessObject: Access, Association
TechnologyFunction -> BusinessProcess: Flow, Association, Realization, Triggering, Serving
TechnologyFunction -> BusinessRole: Flow, Association, Triggering, Serving
TechnologyFunction -> BusinessService: Flow, Association, Realization, Triggering, Serving
TechnologyFunction -> Capability: Association, Realization
TechnologyFunction -> CommunicationNetwork: Flow, Association, Triggering, Serving
TechnologyFunction -> Constraint: Influence, Association, Realization
TechnologyFunction -> Contract: Access, Association
TechnologyFunction -> CourseOfAction: Association, Realization
TechnologyFunction -> DataObject: Access, Association
TechnologyFunction -> Device: Flow, Association, Triggering, Serving
TechnologyFunction -> DistributionNetwork: Flow, Association, Triggering, Serving
TechnologyFunction -> Driver: Influence, Association
TechnologyFunction -> Equipment: Flow, Association, Triggering, Serving
TechnologyFunction -> Facility: Flow, Association, Triggering, Serving
TechnologyFunction -> Goal: Influence, Association, Realization
TechnologyFunction -> Material: Access, Association
TechnologyFunction -> Meaning: Influence, Association
TechnologyFunction -> Node: Flow, Association, Triggering, Serving
TechnologyFunction -> Outcome: Influence, Association, Realization
TechnologyFunction -> Path: Flow, Association, Triggering, Serving
TechnologyFunction -> Principle: Influence, Association, Realization
TechnologyFunction -> Product: Flow, Association, Triggering, Serving
TechnologyFunction -> Representation: Access, Association
TechnologyFunction -> Requirement: Influence, Association, Realization
TechnologyFunction -> Resource: Association
TechnologyFunction -> Stakeholder: Influence, Association
TechnologyFunction -> SystemSoftware: Flow, Association, Triggering, Serving
TechnologyFunction -> TechnologyCollaboration: Flow, Association, Triggering, Serving
TechnologyFunction -> TechnologyEvent: Flow, Association, Triggering, Serving
TechnologyFunction -> TechnologyFunction: Composition, Flow, Aggregation, Association, Specialization, Triggering, Serving
TechnologyFunction -> TechnologyInteraction: Composition, Flow, Aggregation, Association, Triggering, Serving
TechnologyFunction -> TechnologyInterface: Flow, Association, Triggering, Serving
TechnologyFunction -> TechnologyProcess: Composition, Flow, Aggregation, Association, Triggering, Serving
TechnologyFunction -> TechnologyService: Flow, Association, Realization, Triggering, Serving
TechnologyFunction -> Value: Influence, Association
TechnologyFunction -> ValueStream: Association, Realization

## TechnologyInteraction

TechnologyInteraction -> ApplicationCollaboration: Flow, Association, Triggering, Serving
TechnologyInteraction -> ApplicationComponent: Flow, Association, Triggering, Serving
TechnologyInteraction -> ApplicationEvent: Flow, Association, Triggering, Serving
TechnologyInteraction -> ApplicationFunction: Flow, Association, Realization, Triggering, Serving
TechnologyInteraction -> ApplicationInteraction: Flow, Association, Realization, Triggering, Serving
TechnologyInteraction -> ApplicationInterface: Flow, Association, Triggering, Serving
TechnologyInteraction -> ApplicationProcess: Flow, Association, Realization, Triggering, Serving
TechnologyInteraction -> ApplicationService: Flow, Association, Realization, Triggering, Serving
TechnologyInteraction -> Artifact: Access, Association
TechnologyInteraction -> Assessment: Influence, Association
TechnologyInteraction -> BusinessActor: Flow, Association, Triggering, Serving
TechnologyInteraction -> BusinessCollaboration: Flow, Association, Triggering, Serving
TechnologyInteraction -> BusinessEvent: Flow, Association, Triggering, Serving
TechnologyInteraction -> BusinessFunction: Flow, Association, Realization, Triggering, Serving
TechnologyInteraction -> BusinessInteraction: Flow, Association, Realization, Triggering, Serving
TechnologyInteraction -> BusinessInterface: Flow, Association, Triggering, Serving
TechnologyInteraction -> BusinessObject: Access, Association
TechnologyInteraction -> BusinessProcess: Flow, Association, Realization, Triggering, Serving
TechnologyInteraction -> BusinessRole: Flow, Association, Triggering, Serving
TechnologyInteraction -> BusinessService: Flow, Association, Realization, Triggering, Serving
TechnologyInteraction -> Capability: Association, Realization
TechnologyInteraction -> CommunicationNetwork: Flow, Association, Triggering, Serving
TechnologyInteraction -> Constraint: Influence, Association, Realization
TechnologyInteraction -> Contract: Access, Association
TechnologyInteraction -> CourseOfAction: Association, Realization
TechnologyInteraction -> DataObject: Access, Association
TechnologyInteraction -> Device: Flow, Association, Triggering, Serving
TechnologyInteraction -> DistributionNetwork: Flow, Association, Triggering, Serving
TechnologyInteraction -> Driver: Influence, Association
TechnologyInteraction -> Equipment: Flow, Association, Triggering, Serving
TechnologyInteraction -> Facility: Flow, Association, Triggering, Serving
TechnologyInteraction -> Goal: Influence, Association, Realization
TechnologyInteraction -> Material: Access, Association
TechnologyInteraction -> Meaning: Influence, Association
TechnologyInteraction -> Node: Flow, Association, Triggering, Serving
TechnologyInteraction -> Outcome: Influence, Association, Realization
TechnologyInteraction -> Path: Flow, Association, Triggering, Serving
TechnologyInteraction -> Principle: Influence, Association, Realization
TechnologyInteraction -> Product: Flow, Association, Triggering, Serving
TechnologyInteraction -> Representation: Access, Association
TechnologyInteraction -> Requirement: Influence, Association, Realization
TechnologyInteraction -> Resource: Association
TechnologyInteraction -> Stakeholder: Influence, Association
TechnologyInteraction -> SystemSoftware: Flow, Association, Triggering, Serving
TechnologyInteraction -> TechnologyCollaboration: Flow, Association, Triggering, Serving
TechnologyInteraction -> TechnologyEvent: Flow, Association, Triggering, Serving
TechnologyInteraction -> TechnologyFunction: Composition, Flow, Aggregation, Association, Triggering, Serving
TechnologyInteraction -> TechnologyInteraction: Composition, Flow, Aggregation, Association, Specialization, Triggering, Serving
TechnologyInteraction -> TechnologyInterface: Flow, Association, Triggering, Serving
TechnologyInteraction -> TechnologyProcess: Composition, Flow, Aggregation, Association, Triggering, Serving
TechnologyInteraction -> TechnologyService: Flow, Association, Realization, Triggering, Serving
TechnologyInteraction -> Value: Influence, Association
TechnologyInteraction -> ValueStream: Association, Realization

## TechnologyInterface

TechnologyInterface -> ApplicationCollaboration: Flow, Association, Triggering, Serving
TechnologyInterface -> ApplicationComponent: Flow, Association, Triggering, Serving
TechnologyInterface -> ApplicationEvent: Flow, Association, Triggering, Serving
TechnologyInterface -> ApplicationFunction: Flow, Association, Triggering, Serving
TechnologyInterface -> ApplicationInteraction: Flow, Association, Triggering, Serving
TechnologyInterface -> ApplicationInterface: Flow, Association, Realization, Triggering, Serving
TechnologyInterface -> ApplicationProcess: Flow, Association, Triggering, Serving
TechnologyInterface -> ApplicationService: Flow, Association, Realization, Triggering, Serving
TechnologyInterface -> Artifact: Access, Association
TechnologyInterface -> Assessment: Influence, Association
TechnologyInterface -> BusinessActor: Flow, Association, Triggering, Serving
TechnologyInterface -> BusinessCollaboration: Flow, Association, Triggering, Serving
TechnologyInterface -> BusinessEvent: Flow, Association, Triggering, Serving
TechnologyInterface -> BusinessFunction: Flow, Association, Triggering, Serving
TechnologyInterface -> BusinessInteraction: Flow, Association, Triggering, Serving
TechnologyInterface -> BusinessInterface: Flow, Association, Realization, Triggering, Serving
TechnologyInterface -> BusinessObject: Access, Association
TechnologyInterface -> BusinessProcess: Flow, Association, Triggering, Serving
TechnologyInterface -> BusinessRole: Flow, Association, Triggering, Serving
TechnologyInterface -> BusinessService: Flow, Association, Realization, Triggering, Serving
TechnologyInterface -> Capability: Association, Realization
TechnologyInterface -> CommunicationNetwork: Flow, Association, Triggering, Serving
TechnologyInterface -> Constraint: Influence, Association, Realization
TechnologyInterface -> Contract: Access, Association
TechnologyInterface -> CourseOfAction: Association, Realization
TechnologyInterface -> DataObject: Access, Association
TechnologyInterface -> Device: Flow, Association, Triggering, Serving
TechnologyInterface -> DistributionNetwork: Flow, Association, Triggering, Serving
TechnologyInterface -> Driver: Influence, Association
TechnologyInterface -> Equipment: Flow, Association, Triggering, Serving
TechnologyInterface -> Facility: Flow, Association, Triggering, Serving
TechnologyInterface -> Goal: Influence, Association, Realization
TechnologyInterface -> Material: Access, Association
TechnologyInterface -> Meaning: Influence, Association
TechnologyInterface -> Node: Flow, Association, Triggering, Serving
TechnologyInterface -> Outcome: Influence, Association, Realization
TechnologyInterface -> Path: Flow, Association, Triggering, Serving
TechnologyInterface -> Principle: Influence, Association, Realization
TechnologyInterface -> Product: Flow, Association, Triggering, Serving
TechnologyInterface -> Representation: Access, Association
TechnologyInterface -> Requirement: Influence, Association, Realization
TechnologyInterface -> Resource: Association, Realization
TechnologyInterface -> Stakeholder: Influence, Association
TechnologyInterface -> SystemSoftware: Flow, Association, Triggering, Serving
TechnologyInterface -> TechnologyCollaboration: Flow, Association, Triggering, Serving
TechnologyInterface -> TechnologyEvent: Flow, Association, Triggering, Serving
TechnologyInterface -> TechnologyFunction: Flow, Association, Triggering, Serving
TechnologyInterface -> TechnologyInteraction: Flow, Association, Triggering, Serving
TechnologyInterface -> TechnologyInterface: Composition, Flow, Aggregation, Association, Specialization, Triggering, Serving
TechnologyInterface -> TechnologyProcess: Flow, Association, Triggering, Serving
TechnologyInterface -> TechnologyService: Flow, Assignment, Association, Triggering, Serving
TechnologyInterface -> Value: Influence, Association
TechnologyInterface -> ValueStream: Association, Realization

## TechnologyProcess

TechnologyProcess -> ApplicationCollaboration: Flow, Association, Triggering, Serving
TechnologyProcess -> ApplicationComponent: Flow, Association, Triggering, Serving
TechnologyProcess -> ApplicationEvent: Flow, Association, Triggering, Serving
TechnologyProcess -> ApplicationFunction: Flow, Association, Realization, Triggering, Serving
TechnologyProcess -> ApplicationInteraction: Flow, Association, Realization, Triggering, Serving
TechnologyProcess -> ApplicationInterface: Flow, Association, Triggering, Serving
TechnologyProcess -> ApplicationProcess: Flow, Association, Realization, Triggering, Serving
TechnologyProcess -> ApplicationService: Flow, Association, Realization, Triggering, Serving
TechnologyProcess -> Artifact: Access, Association
TechnologyProcess -> Assessment: Influence, Association
TechnologyProcess -> BusinessActor: Flow, Association, Triggering, Serving
TechnologyProcess -> BusinessCollaboration: Flow, Association, Triggering, Serving
TechnologyProcess -> BusinessEvent: Flow, Association, Triggering, Serving
TechnologyProcess -> BusinessFunction: Flow, Association, Realization, Triggering, Serving
TechnologyProcess -> BusinessInteraction: Flow, Association, Realization, Triggering, Serving
TechnologyProcess -> BusinessInterface: Flow, Association, Triggering, Serving
TechnologyProcess -> BusinessObject: Access, Association
TechnologyProcess -> BusinessProcess: Flow, Association, Realization, Triggering, Serving
TechnologyProcess -> BusinessRole: Flow, Association, Triggering, Serving
TechnologyProcess -> BusinessService: Flow, Association, Realization, Triggering, Serving
TechnologyProcess -> Capability: Association, Realization
TechnologyProcess -> CommunicationNetwork: Flow, Association, Triggering, Serving
TechnologyProcess -> Constraint: Influence, Association, Realization
TechnologyProcess -> Contract: Access, Association
TechnologyProcess -> CourseOfAction: Association, Realization
TechnologyProcess -> DataObject: Access, Association
TechnologyProcess -> Device: Flow, Association, Triggering, Serving
TechnologyProcess -> DistributionNetwork: Flow, Association, Triggering, Serving
TechnologyProcess -> Driver: Influence, Association
TechnologyProcess -> Equipment: Flow, Association, Triggering, Serving
TechnologyProcess -> Facility: Flow, Association, Triggering, Serving
TechnologyProcess -> Goal: Influence, Association, Realization
TechnologyProcess -> Material: Access, Association
TechnologyProcess -> Meaning: Influence, Association
TechnologyProcess -> Node: Flow, Association, Triggering, Serving
TechnologyProcess -> Outcome: Influence, Association, Realization
TechnologyProcess -> Path: Flow, Association, Triggering, Serving
TechnologyProcess -> Principle: Influence, Association, Realization
TechnologyProcess -> Product: Flow, Association, Triggering, Serving
TechnologyProcess -> Representation: Access, Association
TechnologyProcess -> Requirement: Influence, Association, Realization
TechnologyProcess -> Resource: Association
TechnologyProcess -> Stakeholder: Influence, Association
TechnologyProcess -> SystemSoftware: Flow, Association, Triggering, Serving
TechnologyProcess -> TechnologyCollaboration: Flow, Association, Triggering, Serving
TechnologyProcess -> TechnologyEvent: Flow, Association, Triggering, Serving
TechnologyProcess -> TechnologyFunction: Composition, Flow, Aggregation, Association, Triggering, Serving
TechnologyProcess -> TechnologyInteraction: Composition, Flow, Aggregation, Association, Triggering, Serving
TechnologyProcess -> TechnologyInterface: Flow, Association, Triggering, Serving
TechnologyProcess -> TechnologyProcess: Composition, Flow, Aggregation, Association, Specialization, Triggering, Serving
TechnologyProcess -> TechnologyService: Flow, Association, Realization, Triggering, Serving
TechnologyProcess -> Value: Influence, Association
TechnologyProcess -> ValueStream: Association, Realization

## TechnologyService

TechnologyService -> ApplicationCollaboration: Flow, Association, Triggering, Serving
TechnologyService -> ApplicationComponent: Flow, Association, Triggering, Serving
TechnologyService -> ApplicationEvent: Flow, Association, Triggering, Serving
TechnologyService -> ApplicationFunction: Flow, Association, Triggering, Serving
TechnologyService -> ApplicationInteraction: Flow, Association, Triggering, Serving
TechnologyService -> ApplicationInterface: Flow, Association, Triggering, Serving
TechnologyService -> ApplicationProcess: Flow, Association, Triggering, Serving
TechnologyService -> ApplicationService: Flow, Association, Realization, Triggering, Serving
TechnologyService -> Artifact: Access, Association
TechnologyService -> Assessment: Influence, Association
TechnologyService -> BusinessActor: Flow, Association, Triggering, Serving
TechnologyService -> BusinessCollaboration: Flow, Association, Triggering, Serving
TechnologyService -> BusinessEvent: Flow, Association, Triggering, Serving
TechnologyService -> BusinessFunction: Flow, Association, Triggering, Serving
TechnologyService -> BusinessInteraction: Flow, Association, Triggering, Serving
TechnologyService -> BusinessInterface: Flow, Association, Triggering, Serving
TechnologyService -> BusinessObject: Access, Association
TechnologyService -> BusinessProcess: Flow, Association, Triggering, Serving
TechnologyService -> BusinessRole: Flow, Association, Triggering, Serving
TechnologyService -> BusinessService: Flow, Association, Realization, Triggering, Serving
TechnologyService -> Capability: Association, Realization
TechnologyService -> CommunicationNetwork: Flow, Association, Triggering, Serving
TechnologyService -> Constraint: Influence, Association, Realization
TechnologyService -> Contract: Access, Association
TechnologyService -> CourseOfAction: Association, Realization
TechnologyService -> DataObject: Access, Association
TechnologyService -> Device: Flow, Association, Triggering, Serving
TechnologyService -> DistributionNetwork: Flow, Association, Triggering, Serving
TechnologyService -> Driver: Influence, Association
TechnologyService -> Equipment: Flow, Association, Triggering, Serving
TechnologyService -> Facility: Flow, Association, Triggering, Serving
TechnologyService -> Goal: Influence, Association, Realization
TechnologyService -> Material: Access, Association
TechnologyService -> Meaning: Influence, Association
TechnologyService -> Node: Flow, Association, Triggering, Serving
TechnologyService -> Outcome: Influence, Association, Realization
TechnologyService -> Path: Flow, Association, Triggering, Serving
TechnologyService -> Principle: Influence, Association, Realization
TechnologyService -> Product: Flow, Association, Triggering, Serving
TechnologyService -> Representation: Access, Association
TechnologyService -> Requirement: Influence, Association, Realization
TechnologyService -> Resource: Association
TechnologyService -> Stakeholder: Influence, Association
TechnologyService -> SystemSoftware: Flow, Association, Triggering, Serving
TechnologyService -> TechnologyCollaboration: Flow, Association, Triggering, Serving
TechnologyService -> TechnologyEvent: Flow, Association, Triggering, Serving
TechnologyService -> TechnologyFunction: Flow, Association, Triggering, Serving
TechnologyService -> TechnologyInteraction: Flow, Association, Triggering, Serving
TechnologyService -> TechnologyInterface: Flow, Association, Triggering, Serving
TechnologyService -> TechnologyProcess: Flow, Association, Triggering, Serving
TechnologyService -> TechnologyService: Composition, Flow, Aggregation, Association, Specialization, Triggering, Serving
TechnologyService -> Value: Influence, Association
TechnologyService -> ValueStream: Association, Realization

## Value

Value -> ApplicationCollaboration: Association
Value -> ApplicationComponent: Association
Value -> ApplicationEvent: Association
Value -> ApplicationFunction: Association
Value -> ApplicationInteraction: Association
Value -> ApplicationInterface: Association
Value -> ApplicationProcess: Association
Value -> ApplicationService: Association
Value -> Artifact: Association
Value -> Assessment: Influence, Association
Value -> BusinessActor: Association
Value -> BusinessCollaboration: Association
Value -> BusinessEvent: Association
Value -> BusinessFunction: Association
Value -> BusinessInteraction: Association
Value -> BusinessInterface: Association
Value -> BusinessObject: Association
Value -> BusinessProcess: Association
Value -> BusinessRole: Association
Value -> BusinessService: Association
Value -> Capability: Association
Value -> CommunicationNetwork: Association
Value -> Constraint: Influence, Association
Value -> Contract: Association
Value -> CourseOfAction: Association
Value -> DataObject: Association
Value -> Device: Association
Value -> DistributionNetwork: Association
Value -> Driver: Influence, Association
Value -> Equipment: Association
Value -> Facility: Association
Value -> Goal: Influence, Association
Value -> Material: Association
Value -> Meaning: Influence, Association
Value -> Node: Association
Value -> Outcome: Influence, Association
Value -> Path: Association
Value -> Principle: Influence, Association
Value -> Product: Association
Value -> Representation: Association
Value -> Requirement: Influence, Association
Value -> Resource: Association
Value -> Stakeholder: Influence, Association
Value -> SystemSoftware: Association
Value -> TechnologyCollaboration: Association
Value -> TechnologyEvent: Association
Value -> TechnologyFunction: Association
Value -> TechnologyInteraction: Association
Value -> TechnologyInterface: Association
Value -> TechnologyProcess: Association
Value -> TechnologyService: Association
Value -> Value: Composition, Aggregation, Influence, Association, Specialization
Value -> ValueStream: Association

## ValueStream

ValueStream -> ApplicationCollaboration: Association
ValueStream -> ApplicationComponent: Association
ValueStream -> ApplicationEvent: Association
ValueStream -> ApplicationFunction: Association
ValueStream -> ApplicationInteraction: Association
ValueStream -> ApplicationInterface: Association
ValueStream -> ApplicationProcess: Association
ValueStream -> ApplicationService: Association
ValueStream -> Artifact: Association
ValueStream -> Assessment: Influence, Association
ValueStream -> BusinessActor: Association
ValueStream -> BusinessCollaboration: Association
ValueStream -> BusinessEvent: Association
ValueStream -> BusinessFunction: Association
ValueStream -> BusinessInteraction: Association
ValueStream -> BusinessInterface: Association
ValueStream -> BusinessObject: Association
ValueStream -> BusinessProcess: Association
ValueStream -> BusinessRole: Association
ValueStream -> BusinessService: Association
ValueStream -> Capability: Flow, Association, Triggering, Serving
ValueStream -> CommunicationNetwork: Association
ValueStream -> Constraint: Influence, Association, Realization
ValueStream -> Contract: Association
ValueStream -> CourseOfAction: Flow, Association, Realization, Triggering, Serving
ValueStream -> DataObject: Association
ValueStream -> Device: Association
ValueStream -> DistributionNetwork: Association
ValueStream -> Driver: Influence, Association
ValueStream -> Equipment: Association
ValueStream -> Facility: Association
ValueStream -> Goal: Influence, Association, Realization
ValueStream -> Material: Association
ValueStream -> Meaning: Influence, Association
ValueStream -> Node: Association
ValueStream -> Outcome: Influence, Association, Realization
ValueStream -> Path: Association
ValueStream -> Principle: Influence, Association, Realization
ValueStream -> Product: Association
ValueStream -> Representation: Association
ValueStream -> Requirement: Influence, Association, Realization
ValueStream -> Resource: Flow, Association, Triggering, Serving
ValueStream -> Stakeholder: Influence, Association
ValueStream -> SystemSoftware: Association
ValueStream -> TechnologyCollaboration: Association
ValueStream -> TechnologyEvent: Association
ValueStream -> TechnologyFunction: Association
ValueStream -> TechnologyInteraction: Association
ValueStream -> TechnologyInterface: Association
ValueStream -> TechnologyProcess: Association
ValueStream -> TechnologyService: Association
ValueStream -> Value: Influence, Association
ValueStream -> ValueStream: Composition, Flow, Aggregation, Association, Specialization, Triggering, Serving
