from pydantic import BaseModel

class UserResponseModel(BaseModel):
    name: str
    dob: str
    email: str

     