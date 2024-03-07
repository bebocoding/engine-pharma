from .database import Base
from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, text, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    phone_number = Column(String, nullable=False, unique=True)
    email = Column(String, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False,
                        server_default=text('now()'))
    