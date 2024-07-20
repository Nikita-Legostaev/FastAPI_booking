from fastapi import APIRouter

from app.bookings.repositories import BookingRepository

router = APIRouter(
    prefix="/bookings",
    tags=["bookings"]
)


@router.get("/")
async def get_bookings():
    return await BookingRepository.get_all()