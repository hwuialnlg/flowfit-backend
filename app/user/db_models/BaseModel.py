from ...main import base

class BaseModel(base):
    def toDict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}