from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models,schemas
from ..database import get_db


router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.get("/")
def get_users():
    return {"Message": "users"}

@router.post("/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(**user.model_dump())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user