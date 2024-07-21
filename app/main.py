from fastapi import FastAPI
from sqladmin import Admin

from app.admin.views import BookingAdmin, HotelAdmin, RoomAdmin, UserAdmin
from app.bookings.views import router as bookings_router
from app.hotels.views import router as hotels_router
from app.users.views import router as users_router
from app.auth.views import router as auth_router
from app.hotels.rooms.views import router as rooms_router
from app.database import engine
from app.admin.auth import authentication_backend

app = FastAPI(
    title="Бронирование"
)

admin = Admin(app, engine, authentication_backend=authentication_backend)
admin.add_view(UserAdmin)
admin.add_view(HotelAdmin)
admin.add_view(RoomAdmin)
admin.add_view(BookingAdmin)

app.include_router(bookings_router)
app.include_router(hotels_router)
app.include_router(users_router)
app.include_router(auth_router)
app.include_router(rooms_router)

