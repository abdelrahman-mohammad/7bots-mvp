STUB_PROMPT = "Respond with the literal text 'stub-ok' and nothing else."

SUBAGENTS = [
    {
        "name": "strategy-analyst",
        "description": "Extracts Motivation and Strategy layer elements from strategic plans, policy and compliance documents, and business case documents.",
        "system_prompt": STUB_PROMPT,
    },
    {
        "name": "business-analyst",
        "description": "Extracts Business layer elements from documents, wikis, and interview transcripts.",
        "system_prompt": STUB_PROMPT,
    },
    {
        "name": "code-analyzer",
        "description": "Extracts Application layer elements from source code repositories and database schema files.",
        "system_prompt": STUB_PROMPT,
    },
    {
        "name": "infra-analyzer",
        "description": "Extracts Technology layer elements from infrastructure as code files and CMDB exports.",
        "system_prompt": STUB_PROMPT,
    },
    {
        "name": "integration-mapper",
        "description": "Extracts cross-layer relationships from API specifications and integration documentation.",
        "system_prompt": STUB_PROMPT,
    },
]
