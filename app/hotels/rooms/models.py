from sqlalchemy import JSON, ForeignKey, Integer, String
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column


class Rooms(Base):
    __tablename__ = "rooms"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    hotel_id: Mapped[int] = mapped_column(Integer, ForeignKey('hotels.id'))
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String, nullable=True)
    price: Mapped[int] = mapped_column(Integer)
    services: Mapped[dict] = mapped_column(JSON, nullable=True)
    quantity: Mapped[int] = mapped_column(Integer)
    image_id: Mapped[int] = mapped_column(Integer)