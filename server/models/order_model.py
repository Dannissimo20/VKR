from models.support_models.lifters_orders_model import LiftersOrders
from models.support_models.service_orders_model import ServicesOrders
from models.support_models.parts_orders_model import PartsOrders

from sqlalchemy.orm import relationship
from sqlalchemy import Column, UUID, ForeignKey, Integer, Float, String, DateTime

from database.database import Base


class Order(Base):
    __tablename__ = "order"
    id = Column(UUID(as_uuid=True), primary_key=True)
    record = Column(UUID(as_uuid=True), ForeignKey("record.id"))
    worker = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    parts = relationship("Parts", secondary=PartsOrders)
    part_count = Column(Integer)
    service = relationship("Service", secondary=ServicesOrders)
    summa = Column(Float)
    lifter = relationship("Lifter", secondary=LiftersOrders)
    status = Column(Integer)
    problem_description = Column(String)
    recommendation_description = Column(String)
    created_at = Column(DateTime)
    begined_at = Column(DateTime)
    finished_at = Column(DateTime)
