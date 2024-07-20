from datetime import date, datetime, timedelta
from fastapi import APIRouter, Depends, Query

from app.auth.dependes import get_current_user
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
    return await RoomsRepository.add(**room_info.model_dump())

@router.patch("/{room_id}")
async def update_room(room_id: int, room_info: SRoom, users: Users = Depends(get_current_user)):
    return await RoomsRepository.update(room_id, **room_info.model_dump())

@router.delete("/{room_id}")
async def delete_room(room_id: int, users: Users = Depends(get_current_user)):
    return await RoomsRepository.delete(room_id)