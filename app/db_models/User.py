from sqlalchemy import Column, Integer, String, Date, LargeBinary
from app.db_models.BaseModel import BaseModel

class User(BaseModel):
    __tablename__ = 'user'

    username = Column(String)
    created_at = Column(Date)
    salt = Column(LargeBinary)
    password = Column(LargeBinary, nullable=False)
    dob = Column(Date, nullable=True)
    email = Column(String, primary_key=True)