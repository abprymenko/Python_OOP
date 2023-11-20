from sqlalchemy import create_engine, Engine
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
            if(not self.IsSessionOpen()):
                self.Session = Session(self.Engine)
        except:
            raise
    def IsSessionOpen(self):
        try:
            return self.Session.is_active if self.Session else False
        except:
            raise
    def CloseSession(self):
        try:
            self.Session.close()
        except:
            raise
    def AddMany(self, instances: list):
        try:
            self.Session.add_all(instances)
            self.Session.commit()
        except:
            raise
    def SelectAll(self, *enteties):
        return self.Session.query(*enteties).all()