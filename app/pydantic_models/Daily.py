from pydantic import BaseModel, Field

class Daily(BaseModel):
    day: str
    exercise_id: int = Field(default=None)
    group_id: int = Field(default=None)

