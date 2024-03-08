from models.support_models.parts_orders_model import PartsOrders

from sqlalchemy.orm import relationship
from sqlalchemy import Column, UUID, String, Integer, Float

from database.database import Base


class Parts(Base):
    __tablename__ = "parts"
    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    count = Column(Integer)
    unit = Column(String)
    orders = relationship("Order", secondary=PartsOrders)
