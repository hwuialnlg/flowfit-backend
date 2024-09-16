from .router import user_router as router
from .response_models import UserResponseModel

@router.post("/createUser", response_model=UserResponseModel)
async def create_user(name: str, password: str, dob: str, email: str) -> UserResponseModel:
    return {name: name, dob: dob, email: email}