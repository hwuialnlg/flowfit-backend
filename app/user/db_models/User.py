from sqlalchemy import Column, Integer, String, Date
from .BaseModel import BaseModel

class User(BaseModel):
    __tablename__ = 'users'

    username = Column(String)
    created_at = Column(Date)
    password = Column(String, nullable=False)
    dob = Column(Date, nullable=True)
    email = Column(String, primary_key=True)