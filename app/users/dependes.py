

from datetime import datetime, timezone
from fastapi import Depends, Request
import jwt

from app.config import settings
from app.users.repositories import UserRepository


def get_token(request: Request):
    token = request.cookies.get('booking_access_token')
    if not token:
        raise Exception('Authentication failed')
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, settings.SEKRET_KEY, algorithms=settings.ALGORITHM)
    except Exception as e:
        raise Exception('Authentication failed') from e
    expair: str = payload.get('exp')
    if int(expair) < int(datetime.now(timezone.utc).timestamp()) and not expair:
        raise Exception('Authentication failed')
    user = await UserRepository.find_by_id(id=int(payload['sub']))
    if not user:
        raise Exception('Authentication failed')
    
    return user
    