from sqlalchemy import Column, ForeignKey, String, Integer
from app.db_models.BaseModel import BaseModel
from sqlalchemy.orm import relationship

class Day(BaseModel):
    __tablename__ = 'day'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)

class Daily(BaseModel):
    __tablename__ = 'daily'

    id = Column(Integer, primary_key=True)
    email = Column(String, ForeignKey('user.email'), nullable=False)
    day = Column(Integer, ForeignKey('day.id'), nullable=False)
    exercise_id = Column(Integer, ForeignKey('exercise.id'), nullable=True)
    group_id = Column(Integer, ForeignKey('group.id'), nullable=True)

    group = relationship("Group", backref=None)
    exercise = relationship("Exercise", backref=None)

    