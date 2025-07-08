# app/services/attachment_service.py

from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.attachment_model import Attachment
from app.schemas.attachment_schema import AttachmentCreate


async def create_attachment(db: AsyncSession, attachment_data: AttachmentCreate) -> Attachment:
    new_attachment = Attachment(**attachment_data.dict())
    db.add(new_attachment)
    await db.commit()
    await db.refresh(new_attachment)
    return new_attachment


async def get_attachments_by_intervention_id(db: AsyncSession, intervention_id: int) -> list[Attachment]:
    result = await db.execute(
        select(Attachment).where(Attachment.intervention_id == intervention_id)
    )
    return result.scalars().all()
