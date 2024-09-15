from pydantic import BaseModel

# define all models for the users in here

class TemplateUser(BaseModel):
    name: str
    dob: str
    weight: int
     