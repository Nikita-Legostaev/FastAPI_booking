from fastapi import FastAPI

from app.bookings.views import router as bookings_router

app = FastAPI(
    title="Бронирование"
)

app.include_router(bookings_router)