from datetime import date, datetime, timedelta
from fastapi import APIRouter, Depends, Query

from app.auth.dependes import get_current_user
from app.hotels.repositories import HotelsRepository
from app.hotels.shemas import SHotels, SHotelsInfo
from app.users.models import Users


router = APIRouter(
    prefix="/hotels",
    tags=["hotels"]
)

@router.get('/id/{hotel_id}')
async def get_hotel_by_id(hotel_id: int):
    return await HotelsRepository.find_by_id(hotel_id)

@router.get('/')
async def get_hotels_all() -> list[SHotelsInfo]:
    return await HotelsRepository.get_all()

@router.get("/{location}/hotels")
async def get_hotels_by_location(
    location: str,
    date_from: date = Query(description=f"{datetime.now().date()}"),
    date_to: date = Query(description=f"{(datetime.now() + timedelta(days=30)).date()}"),
    ):
    if date_from > date_to:
        raise ValueError("date_from must be less than or equal to date_to")
    if (date_to - date_from).days > 31:
        raise ValueError("Maximum allowed duration is 31 days")
    return await HotelsRepository.find_all(location, date_from, date_to)
    
@router.post('/')
async def add_hotel(SHotels: SHotels, users: Users = Depends(get_current_user)):
    await HotelsRepository.add(**SHotels.model_dump())
    return {"detail": "Hotel added successfully"}

@router.patch('/{hotel_id}')
async def update_hotel(hotel_id: int, SHotels: SHotels, users: Users = Depends(get_current_user)):
    await HotelsRepository.update(hotel_id, **SHotels.model_dump())
    return {"detail": "Hotel updated successfully"}
    
@router.delete('/{hotel_id}')
async def delete_hotel(hotel_id: int, users: Users = Depends(get_current_user)):
    await HotelsRepository.delete(hotel_id)
    return {"detail": "Hotel deleted successfully"}

