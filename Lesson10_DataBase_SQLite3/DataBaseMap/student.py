from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
Base = declarative_base()
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    age = Column(Float)
    avg_grade = Column(Float)

    def __init__(self, name: String, age: Float, avg_grade: Float):
        self.name: String = name
        self.age: Float = age
        self.avg_grade: Float = avg_grade