from datetime import date, datetime, timedelta
from fastapi import APIRouter, Depends, Query

from app.auth.dependes import get_current_user
from app.expection import NotFoundHotelsException, NotFoundRoomsException
from app.hotels.repositories import HotelsRepository
from app.hotels.rooms.repositories import RoomsRepository
from app.hotels.rooms.shemas import SRoom, SRoomAll, SRoomInfo
from app.users.models import Users


router = APIRouter(
    prefix="/rooms",
    tags=["rooms"]
)


@router.get("/{hotel_id}/rooms")
async def get_rooms_by_time(
    hotel_id: int,
    date_from: date = Query(description=f"{datetime.now().date()}"),
    date_to: date = Query(description=f"{(datetime.now() + timedelta(days=14)).date()}"),
) -> list[SRoomInfo]:
    rooms = await RoomsRepository.find_all(hotel_id, date_from, date_to)
    return rooms

@router.get("")
async def get_rooms_all() -> list[SRoomAll]:
    return await RoomsRepository.get_all()

@router.post("/")
async def create_room(room_info: SRoom, users: Users = Depends(get_current_user)):
    hotels = await HotelsRepository.find_one_or_none(hotel_id=room_info.hotel_id)
    if not hotels:
        raise NotFoundHotelsException
    await RoomsRepository.add(**room_info.model_dump())
    return {"detail": "Комната создана успешно"}

@router.patch("/{room_id}")
async def update_room(room_id: int, room_info: SRoom, users: Users = Depends(get_current_user)):
    roooms = RoomsRepository.find_one_or_none(id=room_id)
    if not roooms:
        raise NotFoundRoomsException
    await RoomsRepository.update(room_id, **room_info.model_dump())
    return {"detail": "Комната изменена успешно"}

@router.delete("/{room_id}")
async def delete_room(room_id: int, users: Users = Depends(get_current_user)):
    roooms = RoomsRepository.find_one_or_none(id=room_id)
    if not roooms:
        raise NotFoundRoomsException
    await RoomsRepository.delete(room_id)
    return {"detail": "Комната удалена успешно"}