from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field, field_validator

SKILL = Path(__file__).parent / "skills" / "archimate-metamodel" / "SKILL.md"

Layer = Literal["motivation", "strategy", "business", "application", "technology"]


def first_column(block):
    names = []
    for line in block.splitlines():
        if line.startswith("|") and "---" not in line:
            name = line.strip("|").split("|")[0].strip()
            if name and name not in ("Element", "Type"):
                names.append(name)
    return names


SKILL_TEXT = SKILL.read_text(encoding="utf-8")
RELATIONSHIP_TYPES = first_column(
    SKILL_TEXT.split("## Relationship types")[1].split("## Element types")[0]
)
ELEMENT_TYPES = first_column(SKILL_TEXT.split("## Element types")[1])


class Evidence(BaseModel):
    source_type: str
    locator: str
    excerpt: str


class Relationship(BaseModel):
    target_id: str
    type: str

    @field_validator("type")
    @classmethod
    def known_type(cls, value):
        if value not in RELATIONSHIP_TYPES:
            raise ValueError(f"unknown relationship type: {value}")
        return value


class ModelElement(BaseModel):
    id: str
    layer: Layer
    archimate_type: str
    name: str
    documentation: str
    confidence: Literal["observed", "inferred"]
    evidence: list[Evidence] = Field(min_length=1)
    relationships: list[Relationship] = []

    @field_validator("archimate_type")
    @classmethod
    def known_type(cls, value):
        if value not in ELEMENT_TYPES:
            raise ValueError(f"unknown archimate_type: {value}")
        return value
