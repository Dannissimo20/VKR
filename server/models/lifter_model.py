from sqlalchemy import Column, UUID, String
from sqlalchemy.orm import relationship

from database.database import Base
from models.support_models.lifters_orders_model import LiftersOrders


class Lifter(Base):
    __tablename__ = "lifter"
    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String)
    description = Column(String)
    purpose = Column(String)
    orders = relationship("Order", secondary=LiftersOrders)
