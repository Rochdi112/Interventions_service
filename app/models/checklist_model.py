from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class Checklist(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    contenu: str
    valide: bool = False
    intervention_id: int = Field(foreign_key="intervention.id")

    intervention: "Intervention" = Relationship(back_populates="checklists")
