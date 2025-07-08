from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer

from app.config import settings
from app.schemas.user_schema import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: int = payload.get("sub")
        role: str = payload.get("role")
        if user_id is None or role is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    return User(id=user_id, role=role)


def admin_required(current_user: Annotated[User, Depends(get_current_user)]):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin privileges required")


def technicien_required(current_user: Annotated[User, Depends(get_current_user)]):
    if current_user.role != "technicien":
        raise HTTPException(status_code=403, detail="Technicien privileges required")
