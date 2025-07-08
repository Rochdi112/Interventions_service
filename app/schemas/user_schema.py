# app/schemas/user_schema.py

from pydantic import BaseModel

class TokenData(BaseModel):
    id: int
    role: str

class User(BaseModel):
    id: int
    role: str
