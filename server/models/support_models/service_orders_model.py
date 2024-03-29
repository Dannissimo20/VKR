from sqlalchemy import ForeignKey, Column, UUID, Table

from database.database import Base

ServicesOrders = Table(
    "services_orders",
    Base.metadata,
    Column("service", UUID(as_uuid=True), ForeignKey("service.id")),
    Column("order", UUID(as_uuid=True), ForeignKey("order.id")),
)
# class ServicesOrders(Base):
#     __tablename__ = "services_orders"
#     service = Column(UUID(as_uuid=True), ForeignKey("service.id"))
#     order = Column(UUID(as_uuid=True), ForeignKey("order.id"))
