from sqlalchemy import Column, Integer, DateTime, UUID, ForeignKey
from sqlalchemy.orm import relationship

from database.database import Base


class Record(Base):
    __tablename__ = "record"
    id = Column(UUID(as_uuid=True), primary_key=True)
    client = Column(UUID(as_uuid=True), ForeignKey("clients.id"))
    confirmation = Column(Integer)
    date = Column(DateTime)
    order = relationship("Order", uselist=False)
