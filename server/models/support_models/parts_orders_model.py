from sqlalchemy import Column, UUID, ForeignKey, Table, Integer

from database.database import Base

PartsOrders = Table(
    "parts_orders",
    Base.metadata,
    Column("part", UUID(as_uuid=True), ForeignKey("parts.id")),
    Column("order", UUID(as_uuid=True), ForeignKey("order.id")),
    Column("part_count", Integer)
)
# class PartsOrders(Base):
#     __tablename__ = "parts_orders"
#     part = Column(UUID(as_uuid=True), ForeignKey("parts.id"))
#     order = Column(UUID(as_uuid=True), ForeignKey("order.id"))
