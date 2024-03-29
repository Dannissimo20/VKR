from sqlalchemy import Column, String, UUID, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database.database import Base


class Car(Base):
    __tablename__ = "cars"
    vin = Column(String, primary_key=True)
    marka = Column(String)
    model = Column(String)
    color = Column(String)
    license_plate = Column(String)
    body = Column(String)
    yob = Column(Integer)
    engine = Column(String)
    drive = Column(String)
    transmission = Column(String)
    client = Column(UUID(as_uuid=True), ForeignKey("clients.id"))
    records = relationship("Record")
