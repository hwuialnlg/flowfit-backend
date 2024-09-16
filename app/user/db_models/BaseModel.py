from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv, dotenv_values
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# DO NOT CHANGE
load_dotenv()
engine = create_engine(f'postgresql+psycopg2://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_SERVER")}:5432/postgres', echo=True)
Base = declarative_base()
Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()

class BaseModel(Base):
    __abstract__ = True

    def toDict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}