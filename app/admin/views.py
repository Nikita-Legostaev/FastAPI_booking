from sqladmin import ModelView

from app.bookings.models import Bookings
from app.hotels.models import Hotels
from app.hotels.rooms.models import Rooms
from app.users.models import Users


class UserAdmin(ModelView, model=Users):
    column_list = [Users.email]
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"
    category = "Аккаунты"
    column_details_exclude_list = [Users.hash_password]
    can_delete = False
    
    
class HotelAdmin(ModelView, model=Hotels):
    column_list = [Hotels.name, Hotels.location]
    name = "Отель"
    name_plural = "Отели"
    icon = "fa-solid fa-hotel"
    category = "Отели"
    

class RoomAdmin(ModelView, model=Rooms):
    column_list = [Rooms.name, Rooms.price, Rooms.quantity]
    name = "Номер"
    name_plural = "Номера"
    icon = "fa-solid fa-bed"
    category = "Отели"
    

class BookingAdmin(ModelView, model=Bookings):
    column_list = [Bookings.id, Bookings.date_from, Bookings.date_to, Bookings.price]
    name = "Бронирование"
    name_plural = "Бронирования"
    icon = "fa-solid fa-calendar-alt"
    category = "Бронирования"
    
    
    