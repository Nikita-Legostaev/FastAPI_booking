from datetime import datetime, timedelta, timezone

import jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from app.config import settings
from app.expection import IncorrectEmailOrPasswordException
from app.users.repositories import UserRepository

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(
        to_encode, settings.SEKRET_KEY, algorithm=settings.ALGORITHM
    )
    return encode_jwt

async def authenticate_user(email: EmailStr, password: str) -> dict:
    user = await UserRepository.find_one_or_none(email=email)
    if not (user and verify_password(password, user.hash_password)):
        raise IncorrectEmailOrPasswordException
    return user