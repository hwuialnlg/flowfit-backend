from sqlalchemy import Column, Integer, String
from datetime import datetime
from .BaseModel import BaseModel

class User(BaseModel):
    __tablename__ = 'users'

    username = Column(String)
    created_at = Column(datetime)
    password = Column(String, nullable=False)
    dob = Column(datetime, nullable=True)
    email = Column(String, primary_key=True)