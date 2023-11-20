from sqlalchemy import create_engine, Engine, ColumnElement
from sqlalchemy.orm import Session
from student import Base

class DbContext:
    def __init__(self, url: str):
        self.Session: Session = None
        self.Url: str = url
        self.Engine: Engine = create_engine(self.Url)
    def CreateTables(self):
        try:
            Base.metadata.create_all(self.Engine)
        except:
            raise
    def OpenSession(self):
        try:
            if(not self.__IsSessionOpen()):
                self.Session = Session(self.Engine)
        except:
            raise
    def CloseSession(self):
        try:
            if (self.__IsSessionOpen()):
                self.Session.close()
        except:
            raise
    def AddAll(self, instances: list):
        try:
            self.Session.add_all(instances)
            self.Session.commit()
        except:
            raise
    def AddInstance(self, instance: object):
        try:
            self.Session.add(instance)
            self.Session.commit()
        except:
            raise
    def QueryAll(self, filter: ColumnElement[bool] = None, *enteties):
        try:
            query = self.Session.query(*enteties)
            if filter is not  None:
                query = query.filter(filter)
            return query.all()
        except:
            raise
    def __IsSessionOpen(self):
        try:
            return self.Session.is_active if self.Session else False
        except:
            raise