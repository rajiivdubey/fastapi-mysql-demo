from sqlalchemy import Column, Integer, String
from database import Base

class Employees(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    age = Column(String(50))
    salary = Column(String(50))
    department_id = Column(String(50))


