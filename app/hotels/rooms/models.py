from sqlalchemy import JSON, ForeignKey, Integer, String
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship



class Rooms(Base):
    __tablename__ = "rooms"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    hotel_id: Mapped[int] = mapped_column(ForeignKey('hotels.id'))
    name: Mapped[str]
    description: Mapped[dict[str] | None]
    price: Mapped[int] 
    services: Mapped[dict[str] | None]
    quantity: Mapped[int] 
    image_id: Mapped[int]
    
    hotel: Mapped["Hotels"] = relationship(back_populates="rooms")
    booking: Mapped["Bookings"] = relationship(back_populates="rooms")
    
    def __str__(self) -> str:
        return f"Room #{self.id} - {self.name}"