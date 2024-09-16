from fastapi import FastAPI
from user.router import user_router
from user.createUser import create_user
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv, dotenv_values
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()
app = FastAPI()
engine = create_engine(f'postgresql+psycopg2://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_SERVER")}:5432/postgres', echo=True)
base = declarative_base()
base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()

# HTTP Request Testing
# Open up the swagger/local server docs
# or use Insomnia/Postman

# include routers here

app.include_router(user_router)