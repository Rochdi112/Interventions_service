from pydantic import BaseModel
from typing import Optional


class AttachmentBase(BaseModel):
    nom_fichier: str
    url: str
    type: str
    intervention_id: int


class AttachmentCreate(AttachmentBase):
    pass


class AttachmentRead(AttachmentBase):
    id: int

    model_config = {
        "from_attributes": True
    }
