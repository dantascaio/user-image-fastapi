from sqlalchemy import BLOB, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(
        String(50),
        # unique=True,
        index=True,
    )
    images = relationship("Image", back_populates="owner")


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    base64 = Column(BLOB(100000))
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="images")
