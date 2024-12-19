from sqlalchemy import Column, ForeignKey, String, Date, LargeBinary, Integer
from app.db_models.BaseModel import BaseModel
from sqlalchemy.orm import relationship

class ExerciseStats(BaseModel):
    __tablename__ = 'exercisestats'

    id = Column(Integer, primary_key=True, autoincrement=True)
    exercise_id = Column(Integer, ForeignKey('exercise.id'))
    date = Column(Date, nullable=False)
    weight = Column(Integer, nullable=False)

    exercise = relationship("Exercise", back_populates="exercisestats")

class Exercise(BaseModel):
    __tablename__ = 'exercise'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, ForeignKey('user.email'))
    exercise_name = Column(String, nullable=False)

    exercisestats = relationship("ExerciseStats", back_populates="exercise")