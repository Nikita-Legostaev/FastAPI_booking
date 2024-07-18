

from app.bookings.models import Bookings
from app.repositories.base import BaseRepositories


class BookingRepository(BaseRepositories):
    model = Bookings