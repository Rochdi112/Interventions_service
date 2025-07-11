from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from app.database import get_session

DBSession = Annotated[AsyncSession, Depends(get_session)]
