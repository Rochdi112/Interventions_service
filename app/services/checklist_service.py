# app/services/checklist_service.py

from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.checklist_model import Checklist
from app.schemas.checklist_schema import ChecklistCreate


async def create_checklist(db: AsyncSession, checklist_data: ChecklistCreate) -> Checklist:
    new_checklist = Checklist(**checklist_data.dict())
    db.add(new_checklist)
    await db.commit()
    await db.refresh(new_checklist)
    return new_checklist


async def get_checklists_by_intervention_id(db: AsyncSession, intervention_id: int) -> list[Checklist]:
    result = await db.execute(
        select(Checklist).where(Checklist.intervention_id == intervention_id)
    )
    return result.scalars().all()
