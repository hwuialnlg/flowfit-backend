from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine

# routers
from app.endpoints.user_endpoints import router as user_router
# import more routers

Base.metadata.create_all(engine)
app = FastAPI()

# add other origins here / cors
# domain name of frontend needs to be added eventually....
origins = [
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include other routers here
app.include_router(user_router)
# app.include_router(...router)