from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.db_models.User import User
from app.db_models.Stats import Stats
from app.pydantic_models.User import User as UserBody
from app.pydantic_models.User import Login as Login
from app.response_models.UserResponse import UserResponse
import jwt
import datetime
import bcrypt
from app.database import SessionLocal
from fastapi import Depends
from sqlalchemy.orm import Session
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()

ALGORITHM = os.getenv("ALGORITHM")
SECRET_KEY = os.getenv("SECRET_KEY")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_access_token(data):
    to_encode = data.copy()
    expire = datetime.utcnow() + datetime.timedelta(minutes=30)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.exceptions.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

router = APIRouter(dependencies=[Depends(get_db)])

@router.post("/createUser", response_model=UserResponse)
async def create_user(user: UserBody, db: Session = Depends(get_db)) -> UserResponse:

    user_db = User(username=user.name, salt="", password=bcrypt.hashpw(user.password.encode(), bcrypt.gensalt()), dob=user.dob, email=user.email, created_at=datetime.datetime.now())
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

@router.post("/validateUser")
async def validate_user(user : Login, db: Session = Depends(get_db)):
    try:
        res = db.query(User).filter(User.email == user.email).one()
        if bcrypt.checkpw(user.password.encode(), res.password):
            token = create_access_token(data={"sub": user.email, "username": res.username})
            return {"access_token": token, "token_type": "bearer", "email": res.email, "username": res.username}
    except Exception:
        raise HTTPException(status_code=400, detail="Could not match user/password")

    raise HTTPException(status_code=404, detail='Could not match user/password')