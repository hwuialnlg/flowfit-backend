from sqlalchemy import Column, String, Date, LargeBinary
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

    stats = relationship("Stats", back_populates='user')