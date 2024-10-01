from sqlalchemy import Column, Integer, String, Date, LargeBinary, ForeignKey
from app.db_models.BaseModel import BaseModel
from sqlalchemy.orm import relationship

class User(BaseModel):
    __tablename__ = 'user'

    username = Column(String)
    created_at = Column(Date)
    salt = Column(LargeBinary)
    password = Column(LargeBinary, nullable=False)
    dob = Column(Date, nullable=True)
    email = Column(String, primary_key=True)

    streak = relationship("Streak", back_populates="user")