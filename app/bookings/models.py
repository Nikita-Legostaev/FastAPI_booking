from sqlalchemy import Computed, Date, ForeignKey, Integer
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column

class Bookings(Base):
    __tablename__ = 'booking'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    room_id: Mapped[int] = mapped_column(Integer, ForeignKey("rooms.id"))
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    date_from: Mapped[Date] = mapped_column(Date)
    date_to: Mapped[Date] = mapped_column(Date)
    price: Mapped[int] = mapped_column(Integer)
    total_cost: Mapped[int] = mapped_column(Integer, Computed("(date_to - date_from) * price"))
    total_days: Mapped[int] = mapped_column(Integer, Computed("(date_to - date_from)"))
