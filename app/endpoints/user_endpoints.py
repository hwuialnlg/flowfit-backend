from fastapi import APIRouter, HTTPException
from app.db_models.User import User
from app.db_models.Stats import Stats
from app.pydantic_models.User import User as UserBody
from app.pydantic_models.User import Login as Login
from app.response_models.UserResponse import UserResponse
import datetime
import bcrypt
from app.database import SessionLocal
from fastapi import Depends
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(dependencies=[Depends(get_db)])

@router.post("/createUser", response_model=UserResponse)
async def create_user(user: UserBody, db: Session = Depends(get_db)) -> UserResponse:

    salt = bcrypt.gensalt()
    user_db = User(username=user.name, salt=salt, password=bcrypt.hashpw(user.password.encode(), salt), dob=user.dob, email=user.email, created_at=datetime.datetime.now())
    stats = Stats(email=user.email, weight=user.weight, height=user.height, date=datetime.datetime.now())
    # do email validation (prob handled frontend instead)
    # do dob validation

    try:
        db.add(user_db)
        db.add(stats)
        db.commit()
    except Exception as e:
        # return e
        raise HTTPException(status_code=400, detail="Could not create user")

    return UserResponse(email=user.email, name=user.name)

@router.post("/validateUser", response_model=UserResponse)
async def validate_user(user : Login, db: Session = Depends(get_db)):
    try:
        res = db.query(User).filter(User.email == user.email).one()
        if (bcrypt.hashpw(user.password.encode(), res.salt) == res.password):
            return {"email": res.email, "name": res.username}
    except Exception:
        raise HTTPException(status_code=400, detail="Could not match user/password")

    raise HTTPException(status_code=404, detail='Could not match user/password')