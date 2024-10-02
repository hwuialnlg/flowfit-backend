from sqlalchemy import Column, Integer, String, Date, LargeBinary, ForeignKey
from app.db_models.BaseModel import BaseModel
from sqlalchemy.orm import relationship

class Stats(BaseModel):
    __tablename__ = 'stats'

    id = Column(Integer, primary_key=True)
    # when the stats were last updated
    date = Column(Date)
    weight = Column(Integer, nullable=True)
    # most likely going to convert to inches...?
    height = Column(Integer, nullable=True)
    email = Column(String, ForeignKey("user.email"))

    user = relationship("User", back_populates="stats")
