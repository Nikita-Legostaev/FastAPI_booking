from fastapi import APIRouter, Depends, HTTPException
from pydantic import TypeAdapter, parse_obj_as

from app.bookings.repositories import BookingRepository
from app.bookings.shemas import SBooking, SBookingInfo, SNewBooking
from app.auth.dependes import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["bookings"]
)


@router.get("")
async def get_bookings_with_image(user: Users = Depends(get_current_user)) -> list[SBookingInfo]:
    return await BookingRepository.find_all_with_images(user_id=user.id)

@router.get("/all")
async def get_all_bookings() -> list[SBooking]:
    return await BookingRepository.get_all()


@router.post("", status_code=201)
async def add_booking(
    booking: SNewBooking,
    user: Users = Depends(get_current_user),
):
    booking = await BookingRepository.add(
        user.id,
        booking.room_id,
        booking.date_from,
        booking.date_to,
    )
    return {"detail": "Booking created successfully"}


@router.delete("/{booking_id}")
async def remove_booking(
    booking_id: int,
    current_user: Users = Depends(get_current_user),
):
    await BookingRepository.delete(id=booking_id)
    return {"detail": "Booking deleted successfully"}
