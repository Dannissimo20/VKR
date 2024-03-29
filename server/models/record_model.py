from sqlalchemy import Column, Integer, DateTime, UUID, ForeignKey

from database.database import Base


class Record(Base):
    __tablename__ = "record"
    car = Column(UUID(as_uuid=True), ForeignKey("cars.vin"))
    client = Column(UUID(as_uuid=True), ForeignKey("clients.id"))
    confirmation = Column(Integer)
    date = Column(DateTime)
