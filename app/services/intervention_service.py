# app/services/intervention_service.py
from sqlmodel import Session, select
from fastapi import HTTPException
from app.models.intervention_model import Intervention
from app.schemas.intervention_schema import InterventionCreate, InterventionUpdate


async def create_intervention(session: Session, intervention: InterventionCreate):
    new_intervention = Intervention.model_validate(intervention)
    session.add(new_intervention)
    await session.commit()
    await session.refresh(new_intervention)
    return new_intervention


async def get_all_interventions(session: Session):
    result = await session.exec(select(Intervention))
    return result.all()


async def get_intervention(session: Session, intervention_id: int):
    intervention = await session.get(Intervention, intervention_id)
    if not intervention:
        raise HTTPException(status_code=404, detail="Intervention not found")
    return intervention


async def update_intervention(session: Session, intervention_id: int, intervention_data: InterventionUpdate):
    db_intervention = await session.get(Intervention, intervention_id)
    if not db_intervention:
        raise HTTPException(status_code=404, detail="Intervention not found")

    for field, value in intervention_data.model_dump(exclude_unset=True).items():
        setattr(db_intervention, field, value)

    session.add(db_intervention)
    await session.commit()
    await session.refresh(db_intervention)
    return db_intervention


async def delete_intervention(session: Session, intervention_id: int):
    intervention = await session.get(Intervention, intervention_id)
    if not intervention:
        raise HTTPException(status_code=404, detail="Intervention not found")

    await session.delete(intervention)
    await session.commit()
    return {"ok": True}


async def get_interventions_by_technicien(session: Session, technicien_id: int):
    result = await session.exec(select(Intervention).where(Intervention.technicien_id == technicien_id))
    return result.all()
