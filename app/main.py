from fastapi import FastAPI

from app.bookings.views import router as bookings_router
from app.hotels.views import router as hotels_router
from app.users.views import router as users_router

app = FastAPI(
    title="Бронирование"
)

app.include_router(bookings_router)
app.include_router(hotels_router)
app.include_router(users_router)