from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.database import get_session
from app.schemas.attachment_schema import AttachmentCreate, AttachmentRead
from app.services import attachment_service
from app.security import technicien_required

router = APIRouter(prefix="/interventions/attachment", tags=["attachments"])


@router.post("/", response_model=AttachmentRead, dependencies=[Depends(technicien_required)])
async def add_attachment(
    attachment: AttachmentCreate,
    session: Session = Depends(get_session)
):
    return await attachment_service.add_attachment(session, attachment)
