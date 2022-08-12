
from pydantic import BaseModel

class ImageBase(BaseModel):
    base64: str

class ImageCreate(ImageBase):
    pass

class ImageCreate2(BaseModel):
    base64: bytes

class Image(ImageBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
        
class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    images: list[ImageCreate] = []

class User(UserBase):
    id: int
    images: list[Image] = []

    class Config:
        orm_mode = True



