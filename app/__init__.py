from sqlalchemy import create_engine
import os
from dotenv import load_dotenv, dotenv_values
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


load_dotenv()

# DO NOT CHANGE
engine = create_engine(f'postgresql+psycopg2://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_SERVER")}:5432/postgres', echo=True)
Base = declarative_base()
Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()
