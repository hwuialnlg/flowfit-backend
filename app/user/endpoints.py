from fastapi import APIRouter, HTTPException
from .response_models import UserResponseModel
from .db_models.User import User
import datetime
from .db_models.BaseModel import session
import bcrypt

router = APIRouter()

@router.post("/createUser", response_model=UserResponseModel)
async def create_user(name: str, password: str, dob: str, email: str) -> UserResponseModel:

    salt = bcrypt.gensalt()
    user = User(username=name, salt=salt, password=bcrypt.hashpw(password.encode(), salt), dob=dob, email=email, created_at=datetime.datetime.now())
    # do email validation (prob handled frontend instead)
    # do dob validation

    try:
        session.add(user)
        session.commit()
    except Exception as e:
        print(e)
        return HTTPException(status_code=400, detail="Could not create user")

    return UserResponseModel(name=name, dob=dob, email=email)

@router.post("/validateUser")
async def validate_user(email: str, password: str):

    try:
        res = session.query(User).filter(User.email == email).one()
        if (bcrypt.hashpw(password.encode(), res.salt) == res.password):
            return res
    except Exception:
        return HTTPException(status_code=400, detail="Could not match user/password")

    raise HTTPException(status_code=404, detail='Could not match user/password')