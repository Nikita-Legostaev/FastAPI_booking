from sqlalchemy import Computed, Date, ForeignKey, Integer
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Bookings(Base):
    __tablename__ = 'booking'

    id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    date_from: Mapped[Date] = mapped_column(type_=Date)
    date_to: Mapped[Date] = mapped_column(type_=Date)
    price: Mapped[int] 
    total_cost: Mapped[int]
    total_days: Mapped[int] 
    
    rooms: Mapped["Rooms"] = relationship(back_populates="booking")
    user: Mapped["Users"] = relationship(back_populates="booking")
    
    def __str__(self) -> str:
        return f"Booking #{self.id}"
