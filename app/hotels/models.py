from sqlalchemy import Integer, String
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship



class Hotels(Base):
    __tablename__ = "hotels"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] 
    location: Mapped[str] 
    service: Mapped[str] 
    rooms_quantity: Mapped[int]
    image_id: Mapped[int] 
    
    rooms: Mapped["Rooms"] = relationship(back_populates="hotel")
    
    def __str__(self) -> str:
        return f"Hotel #{self.name} - {self.location}"