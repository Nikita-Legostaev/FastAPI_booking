from fastapi import APIRouter

from app.hotels.repositories import HotelsRepository


router = APIRouter(
    prefix="/hotels",
    tags=["hotels"]
)

@router.get('/id/{hotel_id}')
async def get_hotel_by_id(hotel_id: int):
    return await HotelsRepository.find_by_id(hotel_id)

@router.get('/')
async def get_hotels():
    return await HotelsRepository.get_all()


