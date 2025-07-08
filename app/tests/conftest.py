# tests/conftest.py

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import SQLModel
from app.main import app
from app.database import engine, SessionLocal
from app.security import create_access_token


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="function", autouse=True)
async def prepare_database():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)


@pytest.fixture
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.fixture
def admin_token():
    return create_access_token({"sub": "admin@example.com", "id": 1, "role": "admin"})


@pytest.fixture
def technicien_token():
    return create_access_token({"sub": "tech@example.com", "id": 2, "role": "technicien"})
