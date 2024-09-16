from fastapi import APIRouter, HTTPException
from .response_models import UserResponseModel
from .db_models.User import User
import datetime
from .db_models.BaseModel import session

router = APIRouter()

@router.post("/createUser", response_model=UserResponseModel)
async def create_user(name: str, password: str, dob: str, email: str) -> UserResponseModel:

    user = User(username=name, password=hash(password), dob=dob, email=email, created_at=datetime.datetime.now())
    # do email validation
    # do dob validation

    try:
        session.add(user)
        session.commit()
    except Exception:
        pass
        # handle dupes

    return UserResponseModel(name=name, dob=dob, email=email)

@router.post("/validateUser")
async def validate_user(email: str, password: str):

    try:
        res = session.query(User).filter(User.email == email).one()
        if (str(hash(password)) == res.password):
            return res
    except Exception:
        pass

    raise HTTPException(status_code=404, detail='Could not match user/password')