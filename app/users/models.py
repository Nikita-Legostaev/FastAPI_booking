from sqlalchemy import Integer, String
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Users(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True)
    hash_password: Mapped[str]
    
    booking: Mapped["Bookings"] = relationship(back_populates="user")
    
    def __str__(self) -> str:
        return f"User #{self.id} - {self.email}"
    
    