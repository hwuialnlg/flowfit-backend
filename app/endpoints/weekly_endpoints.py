import datetime
from fastapi import APIRouter, HTTPException
from fastapi import Depends
import sqlalchemy
from sqlalchemy import and_
from app.database import SessionLocal
from sqlalchemy.orm import Session

from app.db_models.Day import Day
from app.db_models.Day import Daily
from app.endpoints.user_endpoints import get_current_user
from app.pydantic_models import Daily as DailyBody

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(dependencies=[Depends(get_db)])

@router.post("/addExerciseToDaily")
async def add_exercise_to_daily(daily: DailyBody, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        dayId = db.query(Day).filter(Day.name == daily.day).one()
        dailyAdd = Daily(
            email=current_user.get("email"),
            day=dayId.id,
            exercise_id=daily.exercise_id
        )
        db.add(dailyAdd)
        db.commit()

    except Exception:
        raise HTTPException(status_code=400, detail="Something went wrong...")
    
    return {**dailyAdd}

@router.post("/removeExerciseFromDaily")
async def remove_exercise_from_daily(daily: DailyBody, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        dayId = db.query(Day).filter(Day.name == daily.day).one()
        # exerciseToRemove = db.query(Daily).filter(Daily.email == current_user.get("email") and_ Daily.day == dayId.id and_ Daily.exercise_id == daily.exercise_id).one()
        exerciseToRemove = db.query(Daily).filter(
            and_(
                and_(Daily.email == current_user.get("email"), Daily.day == dayId.id),
                Daily.exercise_id == daily.exercise_id
            )
        )
        db.delete(exerciseToRemove)
        db.commit()

    except Exception:
        raise HTTPException(status_code=400, detail="Something went wrong...")
    
    return {**exerciseToRemove}

@router.post("/removeGroupFromDaily")
async def remove_group_from_daily(daily: DailyBody, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        dayId = db.query(Day).filter(Day.name == daily.day).one()
        # groupToRemove = db.query(Daily).filter(Daily.email == current_user.get("email") and_ Daily.day == dayId.id and_ Daily.group_id == daily.group_id).one()
        groupToRemove = db.query(Daily).filter(
            and_(and_(Daily.email == current_user.get("email"), Daily.day == dayId.id),
                Daily.group_id == daily.group_id
            )
        ).one()
        db.delete(groupToRemove)
        db.commit()

    except Exception:
        raise HTTPException(status_code=400, detail="Something went wrong...")
    
    return {**groupToRemove}

@router.post("/addGroupToDaily")
async def add_group_to_daily(daily: DailyBody, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        dayId = db.query(Day).filter(Day.name == daily.day).one()
        dailyAdd = Daily(
            email=current_user.get("email"),
            day=dayId.id,
            group_id=daily.group_id
        )
        db.add(dailyAdd)
        db.commit()

    except Exception:
        raise HTTPException(status_code=400, detail="Something went wrong...")
    
    return {**dailyAdd}

@router.get("/weekly")
async def get_weekly(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        res = {}
        days = db.query(Day).all()
        for day in days:
            res[day.name] = {}
            res[day.name]["groups"] = []
            res[day.name]["exercises"] = []
            # dailysOfDay = db.query(Daily).filter(Daily.day == day.id and_ Daily.email == current_user.get("email")).all()
            dailysOfDay = db.query(Daily).filter(and_(Daily.day == day.id, Daily.email == current_user.get("email"))).all()
            for daily in dailysOfDay:
                daily = daily.toDict()
                groupTest = daily.get("group", 0)
                exerciseTest = daily.get("exercise", 0)
                if groupTest != 0 and groupTest:
                    res[day.name]["groups"].append(daily["group"].toDict())
                if exerciseTest != 0 and exerciseTest:
                    res[day.name]["exercises"].append(daily["exercise"].toDict())

    except Exception:
        raise HTTPException(status_code=400, detail="Something went wrong...")
    
    return res

