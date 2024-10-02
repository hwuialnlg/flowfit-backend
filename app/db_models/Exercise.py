from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db_models.BaseModel import BaseModel

class Exercise(BaseModel):
    __tablename__ = "exercise"

    # 1 user to many exercises
    id = Column(Integer, primary_key=True)
    email = Column(String, ForeignKey("user.email"))
    name = Column(String, nullable=False)

    user = relationship("User", back_populates="exercise")