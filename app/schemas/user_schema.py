from pydantic import BaseModel

class UserResponseModel(BaseModel):
    name: str
    dob: str
    email: str

# include other response or body models