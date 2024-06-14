
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database import Base

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    haircut_choice = Column(String, nullable=False)
    appointment_date = Column(DateTime, nullable=False)
    payment_method = Column(String, nullable=False)

    appointments = relationship("Appointment", back_populates="customer")
