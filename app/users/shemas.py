

from pydantic import BaseModel, ConfigDict, EmailStr


class SUser(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    email: EmailStr
    