from fastapi import APIRouter, Depends, HTTPException, Response

from app.auth.auth import authenticate_user, create_access_token, get_password_hash
from app.auth.dependes import get_current_user
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
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    await UserRepository.add(email=user.email, hash_password=hashed_password)
    
    
@router.post("/login")
async def login_user(responce: Response, user: SUserAuth):
    try:
        user = await authenticate_user(user.email, user.password)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token({"sub": str(user.id)})
    responce.set_cookie(key="booking_access_token", value=access_token)
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/logout")
async def logout_user(responce: Response):
    responce.delete_cookie(key="booking_access_token")
    return {"message": "Logged out"}


