from sqlalchemy import Column, String, Integer, DateTime

from database.database import Base


class Record(Base):
    __tablename__ = "record"
    fio = Column(String)
    confirmation = Column(Integer)
    date = Column(DateTime)
    phone = Column(String)
