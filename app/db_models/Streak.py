from sqlalchemy import Column, Integer, String, Date, LargeBinary, ForeignKey
from app.db_models.BaseModel import BaseModel
from sqlalchemy.orm import relationship

class Streak(BaseModel):
    __tablename__ = 'streak'

    id = Column(Integer, primary_key=True)
    user_email = Column(String, ForeignKey('user.email'))
    date = Column(Date)
    count = Column(Integer)

    user = relationship("User", back_populates="streak")