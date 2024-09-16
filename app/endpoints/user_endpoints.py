from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserResponseModel
from app.db_models.User import User
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

@router.post("/createUser", response_model=UserResponseModel)
async def create_user(name: str, password: str, dob: str, email: str, db: Session = Depends(get_db)) -> UserResponseModel:

    salt = bcrypt.gensalt()
    user = User(username=name, salt=salt, password=bcrypt.hashpw(password.encode(), salt), dob=dob, email=email, created_at=datetime.datetime.now())
    # do email validation (prob handled frontend instead)
    # do dob validation

    try:
        db.add(user)
        db.commit()
    except Exception as e:
        # return e
        return HTTPException(status_code=400, detail="Could not create user")

    return UserResponseModel(name=name, dob=dob, email=email)

@router.post("/validateUser")
async def validate_user(email: str, password: str, db: Session = Depends(get_db)):

    try:
        res = db.query(User).filter(User.email == email).one()
        if (bcrypt.hashpw(password.encode(), res.salt) == res.password):
            return {res.username, res.email, res.email}
    except Exception:
        return HTTPException(status_code=400, detail="Could not match user/password")

    raise HTTPException(status_code=404, detail='Could not match user/password')