import datetime
from fastapi import APIRouter, HTTPException
from fastapi import Depends
import sqlalchemy
from app.database import SessionLocal
from sqlalchemy.orm import Session

from app.endpoints.user_endpoints import get_current_user

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(dependencies=[Depends(get_db)])

@router.post("/addExerciseToDaily")
async def add_exercise_to_daily(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    pass

@router.post("/removeExerciseFromDaily")
async def remove_exercise_from_daily(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    pass

@router.post("/removeGroupFromDaily")
async def remove_group_from_daily(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    pass

@router.post("/addGroupToDaily")
async def add_group_to_daily(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    pass