from sqlalchemy import Column, ForeignKey, String, Integer
from app.db_models.BaseModel import BaseModel

class Groups(BaseModel):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)