from datetime import datetime
from pydantic import BaseModel

class UserCreate(BaseModel):
    phone_number: str
    password: str

class UserOut(BaseModel):
    id:int
    created_at: datetime




