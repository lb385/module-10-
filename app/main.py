from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import Base, engine, get_db

app = FastAPI(title="Secure User API")


@app.on_event("startup")
def on_startup() -> None:
    Base.metadata.create_all(bind=engine)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/users", response_model=schemas.UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_user(db, user_in)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username or email already exists",
        )
