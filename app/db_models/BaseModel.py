from app.database import Base

class BaseModel(Base):
    __abstract__ = True

    def toDict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
