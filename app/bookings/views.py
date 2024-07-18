from fastapi import APIRouter

from app.bookings.repositories import BookingRepository

router = APIRouter(
    prefix="/hotels",
    tags=["hotels"]
)


@router.get("/")
async def get_hotels():
    return await BookingRepository.get_all()