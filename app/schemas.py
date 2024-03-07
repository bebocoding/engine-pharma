from pydantic import BaseModel

class User(BaseModel):
    phone_number: str
    email: str
    password: str


