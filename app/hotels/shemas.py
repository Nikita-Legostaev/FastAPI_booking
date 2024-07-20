

from pydantic import BaseModel, ConfigDict


class SHotels(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    name: str
    location: str
    service: str
    rooms_quantity: int
    image_id: int
    
    
class SHotelsInfo(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    name: str
    location: str
    service: str
    rooms_quantity: int
    image_id: int