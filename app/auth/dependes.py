

from datetime import datetime, timezone
from fastapi import Depends, Request
import jwt

from app.config import settings
from app.expection import IncorrentTokenFormatException, TokenAbsentException, TokenExpiredException, UserIsNotPresentException
from app.users.repositories import UserRepository


def get_token(request: Request):
    token = request.cookies.get('booking_access_token')
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, settings.SEKRET_KEY, algorithms=settings.ALGORITHM)
    except:
        raise IncorrentTokenFormatException
    expair: str = payload.get('exp')
    if int(expair) < int(datetime.now(timezone.utc).timestamp()) and not expair:
        raise TokenExpiredException
    user = await UserRepository.find_by_id(id=int(payload['sub']))
    if not user:
        raise UserIsNotPresentException
    
    return user
    