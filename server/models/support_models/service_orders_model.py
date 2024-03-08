from sqlalchemy import ForeignKey, Column, UUID

from database.database import Base


class ServicesOrders(Base):
    __tablename__ = "services_orders"
    service = Column(UUID(as_uuid=True), ForeignKey("service.id"))
    order = Column(UUID(as_uuid=True), ForeignKey("order.id"))
