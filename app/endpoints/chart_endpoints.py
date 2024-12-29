import datetime
from dateutil.relativedelta import relativedelta
from fastapi import APIRouter, HTTPException
from fastapi import Depends
import sqlalchemy
from app.database import SessionLocal
from sqlalchemy.orm import Session

from app.db_models.Exercise import Exercise
from app.endpoints.user_endpoints import get_current_user

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(dependencies=[Depends(get_db)])

@router.get("/chart")
async def get_chart(exercise_id: int, time: str = "1M", current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    # allowed times are 1M, 3M, 1Y, ALL
    try:
        res = db.query(Exercise).filter(sqlalchemy.and_(Exercise.email == current_user.get("email"), Exercise.id == exercise_id)).one()
        end_range = datetime.datetime.now()
        start_range = None
        if (time == "ALL"):
            return {"stats": [stat.toDict() for stat in res.exercisestats]}
        elif (time == "1M"):
            start_range = end_range - relativedelta(months=1)
        elif (time == "3M"):
            start_range = end_range - relativedelta(months=3)
        elif (time == "1Y"):
            start_range = end_range - relativedelta(years=1)

        return {"stats" : [stat.toDict() for stat in res.exercisestats if start_range.date() <= stat.date <= end_range.date()]}

    except Exception as e:
        raise HTTPException(status_code=404, detail=e)