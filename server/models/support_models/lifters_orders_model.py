from sqlalchemy import ForeignKey, UUID, Column, Table

from database.database import Base

LiftersOrders = Table(
    "lifters_orders",
    Base.metadata,
    Column("lifter", UUID(as_uuid=True), ForeignKey("lifter.id")),
    Column("order", UUID(as_uuid=True), ForeignKey("order.id")),
)
# class LiftersOrders(Base):
#    __tablename__ = 'lifters_orders'
#     lifter = Column(UUID(as_uuid=True), ForeignKey('lifter.id'), primary_key=True)
#     order = Column(UUID(as_uuid=True), ForeignKey('order.id'), primary_key=True)
