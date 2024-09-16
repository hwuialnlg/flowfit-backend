import os
from fastapi import FastAPI
from app.database import Base, engine
# routers
from app.endpoints.user_endpoints import router as user_router

Base.metadata.create_all(engine)
app = FastAPI()

# include other routers here
app.include_router(user_router)
# app.include_router(...router)