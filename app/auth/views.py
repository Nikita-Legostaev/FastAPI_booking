from fastapi import APIRouter, Depends, Response

from app.auth.auth import authenticate_user, create_access_token, get_password_hash
from app.auth.dependes import get_current_user
from app.expection import UserAlreadyExistsException
from app.users.models import Users
from app.users.repositories import UserRepository
from app.auth.shemas import SUserAuth

router = APIRouter(
    prefix="/auth",
    tags=["authentication"],
)


@router.post("/register")
async def register_user(user: SUserAuth):
    existing_user = await UserRepository.find_one_or_none(email=user.email)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user.password)
    await UserRepository.add(email=user.email, hash_password=hashed_password)
    
    
@router.post("/login")
async def login_user(responce: Response, user: SUserAuth):
    user = await authenticate_user(user.email, user.password)
    access_token = create_access_token({"sub": str(user.id)})
    responce.set_cookie(key="booking_access_token", value=access_token)
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/logout")
async def logout_user(responce: Response, user: Users = Depends(get_current_user)):
    responce.delete_cookie(key="booking_access_token")
    return {"message": "Logged out"}


