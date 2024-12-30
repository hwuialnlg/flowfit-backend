import datetime
import calendar
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
        copy_start_range = None
        labels = []
        if (time == "ALL"):
            labels = list({i.date.year for i in res.exercisestats})
            return {"stats": [stat.toDict() for stat in res.exercisestats], "labels": labels}
        elif (time == "1M"):
            # need to cleanup returned calendar.monthrange stuff
            start_range = end_range - relativedelta(months=1)
            copy_start_range = start_range
            if start_range.month == end_range.month:
                labels = [i + 1 for i in range(calendar.monthrange(datetime.datetime.now().year, start_range.month)[1])]
            else:
                # iterate to get previous months dates
                while start_range.day <= calendar.monthrange(start_range.year, start_range.month)[1]:
                    labels.append(f"{start_range.year}-{start_range.month}-{start_range.day}")
                    if start_range.day != 31:
                        start_range += relativedelta(days=1)
                    else:
                        break
                labels.extend([f"{end_range.year}-{end_range.month}-{i+1}" for i in range(calendar.monthrange(end_range.year, end_range.month)[1]) if i + 1 <= end_range.day])
        elif (time == "3M"):
            start_range = end_range - relativedelta(months=2)
            copy_start_range = start_range
            if start_range.year == end_range.year:
                labels = [f"{end_range.year}-{i+1}" for i in range(end_range.month) if start_range.month <= i+1 <= end_range.month]
            else:
                while start_range.month <= 12:
                    labels.append(f"{start_range.year}-{start_range.month}")
                    start_range += datetime.timedelta(months=1)
                labels.extend([f"{end_range.year}-{i+1}" for i in range(end_range.month)])
        elif (time == "1Y"):
            start_range = end_range - relativedelta(years=1)
            copy_start_range = start_range
            if start_range.year == end_range.year:
                labels = [f"{start_range.year}-{i+1}" for i in range(12)]
            else:
                while start_range.month <= 12:
                    labels.append(f"{start_range.year}-{start_range.month}")
                    start_range += datetime.timedelta(months=1)
                labels.extend([f"{end_range.year}-{i+1}" for i in range(end_range.month)])

        return {"stats" : [stat.toDict() for stat in res.exercisestats if copy_start_range.date() <= stat.date <= end_range.date()], "labels": labels}

    except Exception as e:
        raise HTTPException(status_code=404, detail=e)