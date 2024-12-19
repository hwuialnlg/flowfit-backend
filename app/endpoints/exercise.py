import datetime
from fastapi import APIRouter, HTTPException
from fastapi import Depends
from app.database import SessionLocal
from sqlalchemy.orm import Session

from app.db_models.Exercise import Exercise
from app.db_models.Exercise import ExerciseStats
from app.endpoints.user_endpoints import get_current_user
from app.pydantic_models.Exercise import Exercise as ExerciseBody
from app.pydantic_models.Exercise import AddExerciseStatModel

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(dependencies=[Depends(get_db)])

@router.post("/createExercise")
async def create_exercise(exercise_body: ExerciseBody, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        res = db.query(Exercise).filter(Exercise.name == exercise_body.exercise_name and Exercise.email == current_user.get("email")).one()
        if res:
            raise HTTPException(status_code=400, detail="Exercise already exists")
        exercise_db = Exercise(email=current_user.get("email"), exercise_name=exercise_body.exercise_name)
        db.add(exercise_db)
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)
    
    return {"exercise_name": exercise_db.exercise_name, "email": exercise_db.email}

@router.get("/exercises")
async def get_exercises(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):

    try:
        res = db.query(Exercise).filter(Exercise.email == current_user.get("email")).all()

    except Exception as e:
        raise HTTPException(status_code=404, detail=e)
    
    return {"email": current_user.get("email"), "exercises": [exercise.toDict() for exercise in res]}

@router.get("/exercise_stats")
async def get_exercise_stats(exercise_id : int, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):

    try:
        res = db.query(Exercise).filter(Exercise.email == current_user.get("email") and Exercise.id == exercise_id).one()
    except Exception as e:
        raise HTTPException(status_code=404, detail=e)
    
    return {"email": current_user.get("email"), "exercise_name": res.exercise_name, "exercise_id": res.id, "exercise_stats": [stat.toDict() for stat in res.exercisestats]}

@router.post("/add_exercise_stats")
async def add_exercise_stats(add_exercise_stat : AddExerciseStatModel, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):

    try:
        res = db.query(Exercise).filter(Exercise.email == current_user.get("email") and Exercise.id == add_exercise_stat.get("exercise_id")).one()
        exercise_stats = ExerciseStats(exercise_id=res.id, date=datetime.datetime.now(), weight=add_exercise_stat.stat)
        db.add(exercise_stats)
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=404, detail=e)
    
    return {"email": current_user.get("email"), "exercise_name": res.exercise_name, "exercise_id": res.id, "exercise_stats": exercise_stats.toDict()}

