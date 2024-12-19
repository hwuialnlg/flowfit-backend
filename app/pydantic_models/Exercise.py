from pydantic import BaseModel, Field

class Exercise(BaseModel):
    exercise_name: str

class AddExerciseStatModel(BaseModel):
    exercise_id: int
    stat: int