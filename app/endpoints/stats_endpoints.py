from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserResponseModel
from app.db_models.User import User
from app.db_models.Stats import Stats
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

@router.post("/addStats")
async def addStat(email: str, weight: int = 0, height: int = 0, db: Session = Depends(get_db)):

    try:
        user = db.query(User).filter(User.email == email).one()
        stats = sorted(user.stats, key=lambda stat: stat.date)

        if (not height):
            height = (stats[-1].height if len(stats) > 0 else 0)
        if (not weight):
            weight = (stats[-1].weight if len(stats) > 0 else 0)

        stats = Stats(email=email, height=height, weight=weight, date=datetime.datetime.now())
        db.add(stats)
        db.commit()

        return {"email": email, "weight": weight, "height": height, "date": datetime.datetime.now()}

    except Exception as e:
        # return e
        return HTTPException(status_code=400, detail="Could not find user")
    
@router.get("/getStats")
async def getStats(email: str, db: Session = Depends(get_db)):

    try:
        stats = db.query(Stats).filter(Stats.email == email)
        stats = sorted(stats, key=lambda stat: stat.date)
        if (not height):
            height = (stats[-1].height if len(stats) > 0 else 0)
        if (not weight):
            weight = (stats[-1].weight if len(stats) > 0 else 0)

        return {"email": email, "height": height, "weight": weight, "date": stats.date}
    
    except Exception as e:
        # return e
        return HTTPException(status_code=400, detail="Could not find user")
