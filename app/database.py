import os
from dotenv import load_dotenv, dotenv_values
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

load_dotenv()

engine = create_engine(f'postgresql+psycopg2://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_SERVER")}:5432/postgres', echo=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()