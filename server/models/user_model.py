from sqlalchemy import UUID, Column, String
from sqlalchemy.orm import relationship

from database.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True)
    login = Column(String)
    password = Column(String)
    email = Column(String)
    role = Column(String)
    fio = Column(String)
    phone = Column(String)
    orders = relationship("Order")
