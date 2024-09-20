import os
from dotenv import load_dotenv, dotenv_values
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

load_dotenv()

if (os.getenv("TYPE") == "DOCKER"):
    engine = create_engine(f'{os.getenv("DB_TYPE")}+{os.getenv("DB_DRIVER")}://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DOCKER_LINK")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}', echo=True)
else:
    engine = create_engine(f'{os.getenv("DB_TYPE")}+{os.getenv("DB_DRIVER")}://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_SERVER")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}', echo=True)


# if not using docker replace environment variables
# also, replace the database type + database API driver + last name
# engine = create_engine(f'postgresql+psycopg2://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_SERVER")}:5432/postgres', echo=True)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()