from pydantic import BaseModel, Field

class User(BaseModel):
    name: str
    password: str
    dob: str
    email: str
    weight: int = Field(default=0)
    height: int = Field(default=0)

class Login(BaseModel):
    email: str
    password: str