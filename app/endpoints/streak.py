from app.db_models.Streak import Streak
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

@router.get("/getStreak")
async def create_user(email: str, db: Session = Depends(get_db)) -> int:

    try:
        streak = db.query(Streak).filter(Streak.user_email == email).one()
        return streak.count
    except Exception as e:
        # return e
        return HTTPException(status_code=400, detail="Could not find user and user streaks")