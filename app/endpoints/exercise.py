import datetime
from fastapi import APIRouter, HTTPException
from fastapi import Depends
from app.database import SessionLocal
from sqlalchemy.orm import Session

from app.db_models.Exercise import Exercise
from app.db_models.Exercise import ExerciseStats
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
async def create_exercise(exercise_body: ExerciseBody, db: Session = Depends(get_db)):

    try:
        exercise_db = Exercise(email=exercise_body.email, exercise_name=exercise_body.exercise_name)
        db.add(exercise_db)
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)
    
    return {"exercise_name": exercise_db.exercise_name, "email": exercise_db.email}

@router.get("/exercises")
async def get_exercises(email: str, db: Session = Depends(get_db)):

    try:
        res = db.query(Exercise).filter(Exercise.email == email).all()

    except Exception as e:
        raise HTTPException(status_code=404, detail=e)
    
    return {"email": email, "exercises": [exercise.toDict() for exercise in res]}

@router.get("/exercise_stats")
async def get_exercise_stats(email: str, exercise_id : int, db: Session = Depends(get_db)):

    try:
        res = db.query(Exercise).filter(Exercise.email == email and Exercise.id == exercise_id).one()
    except Exception as e:
        raise HTTPException(status_code=404, detail=e)
    
    return {"email": email, "exercise_name": res.exercise_name, "exercise_id": res.id, "exercise_stats": [stat.toDict() for stat in res.exercisestats]}

@router.post("/add_exercise_stats")
async def add_exercise_stats(add_exercise_stat : AddExerciseStatModel, db: Session = Depends(get_db)):

    try:
        res = db.query(Exercise).filter(Exercise.email == add_exercise_stat.email and Exercise.id == add_exercise_stat.exercise_id).one()
        exercise_stats = ExerciseStats(exercise_id=res.id, date=datetime.datetime.now(), weight=add_exercise_stat.stat)
        db.add(exercise_stats)
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=404, detail=e)
    
    return {"email": add_exercise_stat.email, "exercise_name": res.exercise_name, "exercise_id": res.id, "exercise_stats": exercise_stats.toDict()}

