from fastapi import APIRouter, Depends

from app.auth.auth import get_password_hash
from app.auth.dependes import get_current_user
from app.expection import UserChangeEmailException
from app.users.models import Users
from app.users.repositories import UserRepository
from app.users.shemas import SUser


router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("")
async def get_all_users(user: Users = Depends(get_current_user)) -> list[SUser]:
    return await UserRepository.get_all()


@router.patch("/change/email")
async def change_email_user(
    new_email: str,
    user: Users = Depends(get_current_user)
    ):
    if user.email == new_email:
        raise UserChangeEmailException
    await UserRepository.update(user.id, email = new_email)
    return {"detail": "Почта изменена успешно"}

@router.patch("/change/password")
async def change_password_user( 
    new_password: str, 
    user: Users = Depends(get_current_user)
    ):
    hashed_password = get_password_hash(new_password)
    await UserRepository.update(user.id, hash_password = hashed_password)
    return {"detail": "Пароль изменен успешно"}
    

@router.delete("/delete")
async def delete_user(
    user: Users = Depends(get_current_user)
    ):
    await UserRepository.delete(id=user.id)
    return {"detail": "Пользователь удален успешно"}