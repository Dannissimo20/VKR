from sqlalchemy import Column, UUID, ForeignKey

from database.database import Base


class PartsOrders(Base):
    __tablename__ = "parts_orders"
    part = Column(UUID(as_uuid=True), ForeignKey("parts.id"))
    order = Column(UUID(as_uuid=True), ForeignKey("order.id"))
