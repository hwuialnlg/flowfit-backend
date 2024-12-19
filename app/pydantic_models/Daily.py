from typing import Optional
from pydantic import BaseModel, Field

class Daily(BaseModel):
    day: str
    exercise_id: Optional[int] = Field(default=None)
    group_id: Optional[int] = Field(default=None)

