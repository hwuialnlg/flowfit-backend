from pydantic import BaseModel, Field

class Exercise(BaseModel):
    email: str
    exercise_name: str

class AddExerciseStatModel(BaseModel):
    email: str
    exercise_id: int
    stat: int