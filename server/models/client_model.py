from sqlalchemy import Column, String, DateTime, UUID
from sqlalchemy.orm import relationship

from database.database import Base


class Client(Base):
    __tablename__ = "clients"
    id = Column(UUID(as_uuid=True), primary_key=True)
    fio = Column(String)
    phone = Column(String)
    email = Column(String)
    dob = Column(DateTime)
    cars = relationship("Car")
    records = relationship("Record")
