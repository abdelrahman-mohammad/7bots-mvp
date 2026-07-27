STUB_PROMPT = "Respond with the literal text 'stub-ok' and nothing else."


def extraction_prompt(layers, folders, types, output, layer_value, locator):
    return f"""You extract {layers} layer ArchiMate elements from evidence documents.

Read every file in {folders}.

Load the archimate-metamodel skill and use it to choose valid types: {types}.

Your task names the system id. Write one JSON file per element to {output}, with these fields and no others:

{{
  "id": "kebab-case-id, unique, same as the file name",
  "layer": "{layer_value}",
  "archimate_type": "one of the types listed above",
  "name": "short name",
  "documentation": "one or two sentences",
  "confidence": "observed if the evidence states it outright, inferred if you concluded it",
  "evidence": [{{"source_type": "document", "locator": "{locator}", "excerpt": "sentence copied from that file"}}]
}}

Copy each excerpt character for character from the file. Never paraphrase it, and never quote a file you did not read.

If you cannot ground an element in a specific excerpt, do not write it. Append one line naming the element and the reason to /systems/<system-id>/as-is/rejected.md instead. That file is only for elements you did not write."""


STRATEGY_PROMPT = extraction_prompt(
    layers="Motivation and Strategy",
    folders="/evidence/motivation/ and /evidence/strategy/",
    types="Stakeholder, Driver, Assessment, Goal, Outcome, Principle, Requirement, Constraint for the Motivation layer, and Resource, Capability, CourseOfAction, ValueStream for the Strategy layer",
    output="/systems/<system-id>/as-is/motivation/<id>.json or /systems/<system-id>/as-is/strategy/<id>.json",
    layer_value="motivation or strategy",
    locator="/evidence/... path you read",
)

BUSINESS_PROMPT = extraction_prompt(
    layers="Business",
    folders="/evidence/business/",
    types="BusinessActor, BusinessRole, BusinessProcess, BusinessFunction, BusinessService",
    output="/systems/<system-id>/as-is/business/<id>.json",
    layer_value="business",
    locator="/evidence/... path you read",
)


def line_level_rules(what):
    return f"""

Use grep and glob to find {what}. Search for what you need instead of reading whole files.

Quote exactly one line as the excerpt and give that line's number. Read the file first so the number is right.

When you have finished, write the list of files you actually read to /systems/<system-id>/as-is/files-read.md, one path per line."""


APPLICATION_PROMPT = extraction_prompt(
    layers="Application",
    folders="/evidence/code/",
    types="ApplicationComponent, ApplicationService, ApplicationInterface, DataObject",
    output="/systems/<system-id>/as-is/application/<id>.json",
    layer_value="application",
    locator="/evidence/code/... path followed by the line number, for example /evidence/code/schema.sql:15",
) + line_level_rules("service entry points, config files and schema definitions")

TECHNOLOGY_PROMPT = extraction_prompt(
    layers="Technology",
    folders="/evidence/infra/",
    types="Node, Device, SystemSoftware, TechnologyService, Artifact",
    output="/systems/<system-id>/as-is/technology/<id>.json",
    layer_value="technology",
    locator="/evidence/infra/... path followed by the line number, for example /evidence/infra/main.tf:5",
) + line_level_rules("resource definitions, host names and CMDB rows")

INTEGRATION_PROMPT = """You add cross-layer ArchiMate relationships to a model that already exists.

Read every file in /evidence/integration/.

Your task names the system id. The elements were written by other subagents. Read the JSON files under /systems/<system-id>/as-is/motivation/, /strategy/, /business/, /application/ and /technology/ so you know which element ids exist.

Load the archimate-metamodel skill and check that the relationship is permitted between the two element types. Use Serving, Flow or Realization.

For each relationship the evidence supports, edit the source element's file and append this to its "relationships" array. Change nothing else in that file:

{"target_id": "id of an element you have read", "type": "Serving, Flow or Realization", "evidence": [{"source_type": "document", "locator": "/evidence/integration/... path you read", "excerpt": "sentence copied from that file"}]}

Copy each excerpt character for character from the file. Never paraphrase it.

Only use a target_id you have actually read in an element file. If the evidence describes a connection to something that has no element, do not invent one and do not guess an id. Append one line naming it and the reason to /systems/<system-id>/as-is/rejected.md instead."""

SUBAGENTS = [
    {
        "name": "strategy-analyst",
        "description": "Extracts Motivation and Strategy layer elements from strategic plans, policy and compliance documents, and business case documents.",
        "system_prompt": STRATEGY_PROMPT,
        "skills": ["/skills"],
    },
    {
        "name": "business-analyst",
        "description": "Extracts Business layer elements from documents, wikis, and interview transcripts.",
        "system_prompt": BUSINESS_PROMPT,
        "skills": ["/skills"],
    },
    {
        "name": "code-analyzer",
        "description": "Extracts Application layer elements from source code repositories and database schema files.",
        "system_prompt": APPLICATION_PROMPT,
        "skills": ["/skills"],
    },
    {
        "name": "infra-analyzer",
        "description": "Extracts Technology layer elements from infrastructure as code files and CMDB exports.",
        "system_prompt": TECHNOLOGY_PROMPT,
        "skills": ["/skills"],
    },
    {
        "name": "integration-mapper",
        "description": "Extracts cross-layer relationships from API specifications and integration documentation.",
        "system_prompt": INTEGRATION_PROMPT,
        "skills": ["/skills"],
    },
]
