from sqlalchemy.orm import Session

from ..models import schemas

from . import models


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_image(db: Session, image: schemas.ImageCreate2, user_id: int):
    db_image = models.Image(**image.dict(), user_id=user_id)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image
