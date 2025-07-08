from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List

from app.models.intervention_model import Intervention
from app.schemas.intervention_schema import (
    InterventionCreate,
    InterventionRead,
    InterventionUpdate
)
from app.services import intervention_service
from app.database import get_session
from app.security import get_current_user, admin_required, technicien_required

router = APIRouter(prefix="/interventions", tags=["interventions"])


@router.post("/", response_model=InterventionRead, dependencies=[Depends(admin_required)])
async def create_intervention(
    intervention: InterventionCreate,
    session: Session = Depends(get_session)
):
    return await intervention_service.create_intervention(session, intervention)


@router.get("/", response_model=List[InterventionRead], dependencies=[Depends(admin_required)])
async def get_all_interventions(session: Session = Depends(get_session)):
    return await intervention_service.get_all_interventions(session)


@router.get("/technicien/me", response_model=List[InterventionRead], dependencies=[Depends(technicien_required)])
async def get_my_interventions(
    current_user=Depends(get_current_user),
    session: Session = Depends(get_session)
):
    return await intervention_service.get_interventions_by_technicien(session, current_user.id)


@router.get("/{intervention_id}", response_model=InterventionRead)
async def get_intervention(intervention_id: int, session: Session = Depends(get_session)):
    return await intervention_service.get_intervention(session, intervention_id)


@router.put("/{intervention_id}", response_model=InterventionRead, dependencies=[Depends(admin_required)])
async def update_intervention(
    intervention_id: int,
    intervention_data: InterventionUpdate,
    session: Session = Depends(get_session)
):
    return await intervention_service.update_intervention(session, intervention_id, intervention_data)


@router.delete("/{intervention_id}", dependencies=[Depends(admin_required)])
async def delete_intervention(intervention_id: int, session: Session = Depends(get_session)):
    return await intervention_service.delete_intervention(session, intervention_id)
