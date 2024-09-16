from fastapi import FastAPI
from user.endpoints import router as user_router

app = FastAPI()

# include other routers here
app.include_router(user_router)
# app.include_router(...router)