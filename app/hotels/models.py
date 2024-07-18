from sqlalchemy import Integer, String
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column


class Hotels(Base):
    __tablename__ = "hotels"
    
    id: Mapped[int] = mapped_column(Integer ,primary_key=True)
    name: Mapped[str] = mapped_column(String)
    location: Mapped[str] = mapped_column(String)
    service: Mapped[str] = mapped_column(String)
    rooms_quantity: Mapped[int]= mapped_column(Integer)
    image_id: Mapped[int] = mapped_column(Integer)