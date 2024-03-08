from sqlalchemy import UUID, Column, ForeignKey

from database.database import Base


class LiftersOrders(Base):
    __tablename__ = "parts_orders"
    lifter = Column(UUID(as_uuid=True), ForeignKey("lifter.id"))
    order = Column(UUID(as_uuid=True), ForeignKey("order.id"))
