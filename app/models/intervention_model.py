from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime


class Intervention(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    titre: str
    description: str
    statut: str = "en_attente"
    date_creation: datetime = Field(default_factory=datetime.utcnow)
    site_id: int
    technicien_id: int
    materiel_id: int

    checklists: List["Checklist"] = Relationship(back_populates="intervention")
    attachments: List["Attachment"] = Relationship(back_populates="intervention")
