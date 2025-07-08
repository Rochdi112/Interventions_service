from pydantic import BaseModel
from typing import Optional


class ChecklistBase(BaseModel):
    contenu: str
    valide: bool = False
    intervention_id: int


class ChecklistCreate(ChecklistBase):
    pass


class ChecklistRead(ChecklistBase):
    id: int

    model_config = {
        "from_attributes": True
    }
