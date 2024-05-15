from sqlalchemy import Column, UUID, String, Integer, Float
from sqlalchemy.orm import relationship

from database.database import Base
from models.support_models.service_orders_model import ServicesOrders


class Service(Base):
    __tablename__ = "service"
    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String)
    duration = Column(Integer)
    price = Column(Float)
    orders = relationship("Order", secondary=ServicesOrders)
