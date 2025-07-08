from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.database import get_session
from app.schemas.checklist_schema import ChecklistCreate, ChecklistRead
from app.services import checklist_service
from app.security import technicien_required

router = APIRouter(prefix="/interventions/checklist", tags=["checklist"])


@router.post("/", response_model=ChecklistRead, dependencies=[Depends(technicien_required)])
async def add_checklist(
    checklist: ChecklistCreate,
    session: Session = Depends(get_session)
):
    return await checklist_service.add_checklist(session, checklist)
