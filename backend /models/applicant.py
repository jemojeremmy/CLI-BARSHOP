from sqlalchemy import Column, Integer, String
from database import Base

class Applicant(Base):
    __tablename__ = "applicants"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    years_worked = Column(Integer, nullable=False)
    age = Column(Integer, nullable=False)
