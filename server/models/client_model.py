from sqlalchemy import Column, String, DateTime
from database.database import Base


class Client(Base):
    __tablename__ = "clients"
    id = Column(String, primary_key=True)
    name = Column(String)
    dob = Column(DateTime)
