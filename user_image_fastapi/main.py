import base64
from enum import Enum
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import null
from sqlalchemy.orm import Session
import uvicorn


from app.models.schemas import UserCreate
from app.database import crud, models
from app.models import schemas
from app.database.database import SessionLocal, engine
from app.models.schemas import Image
from app.models.schemas import ImageCreate
from app.models.schemas import ImageCreate2

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


users = []
last_id = 0


class Model(Enum):
    shufflenet = "Shufflenet"
    densenet = "Densenet"
    tf = "tensorflow"


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/echo/{id}")
async def echo(id: int):
    return {"id": id}


@app.get("/model/{model}")
async def model(model: Model):
    return {"model_name": model, "Description": f"Thats is the {model.value}"}


@app.post("/client")
async def insert_client(user: UserCreate):
    last_id = len(users) + 1
    # user.id = last_id
    users.append(user)
    return {"user": users}


@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # db_user = crud.get_user_by_email(db, email=user.email)
    new_user = crud.create_user(db=db, user=user)
    novas_imagens = [Image]
    if user.images is not None:
        for image in user.images:
            image.base64 = base64.decodebytes(image.base64.encode("ascii"))
            crud.create_user_image(
                db=db, image=ImageCreate2(**image.dict()), user_id=new_user.id
            )

    # if db_user:
    #    raise HTTPException(status_code=400, detail="Email already registered")
    # novo_usuario = schemas.User(id=123, name="forcado", images=[])
    return new_user


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
