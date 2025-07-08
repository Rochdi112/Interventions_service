from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class Attachment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nom_fichier: str
    url: str
    type: str
    intervention_id: int = Field(foreign_key="intervention.id")

    intervention: "Intervention" = Relationship(back_populates="attachments")
