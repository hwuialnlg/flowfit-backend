from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    name: str
    password: str
    dob: str
    email: str
    weight: Optional[int] = 0
    height: Optional[int] = 0

class Login(BaseModel):
    email: str
    password: str