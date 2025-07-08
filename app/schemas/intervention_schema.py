from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class InterventionBase(BaseModel):
    titre: str
    description: str
    statut: Optional[str] = "en_attente"
    site_id: int
    technicien_id: int
    materiel_id: int


class InterventionCreate(InterventionBase):
    pass


class InterventionUpdate(BaseModel):
    titre: Optional[str] = None
    description: Optional[str] = None
    statut: Optional[str] = None
    site_id: Optional[int] = None
    technicien_id: Optional[int] = None
    materiel_id: Optional[int] = None


class InterventionRead(InterventionBase):
    id: int
    date_creation: datetime

    model_config = {
        "from_attributes": True
    }
