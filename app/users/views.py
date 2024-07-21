from fastapi import APIRouter, Depends, HTTPException, Response
from pydantic import TypeAdapter

from app.auth.auth import get_password_hash
from app.auth.dependes import get_current_user
from app.users.models import Users
from app.users.repositories import UserRepository


router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("")
async def get_all_users(user: Users = Depends(get_current_user)):
    return await UserRepository.get_all()


@router.patch("/change/email")
async def change_email_user(
    new_email: str,
    user: Users = Depends(get_current_user)
    ):
    existing_user = await UserRepository.find_one_or_none(id=user.id)
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    if existing_user.email == new_email:
        raise HTTPException(status_code=400, detail="Email is already in use")

    await UserRepository.update(user.id, email = new_email)
    return {"detail": "Email updated successfully"}

@router.patch("/change/password")
async def change_password_user( 
    new_password: str, 
    user: Users = Depends(get_current_user)
    ):
    existing_user = await UserRepository.find_one_or_none(id=user.id)
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    hashed_password = get_password_hash(new_password)
    await UserRepository.update(user.id, hash_password = hashed_password)
    return {"detail": "Password updated successfully"}
    

@router.delete("/delete")
async def delete_user(
    user: Users = Depends(get_current_user)
    ):
    existing_user = await UserRepository.find_one_or_none(id=user.id)
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    await UserRepository.delete(id=user.id)
    return {"detail": "User deleted successfully"}