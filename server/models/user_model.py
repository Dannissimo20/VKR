from sqlalchemy import UUID, Column, String, LargeBinary, text
import bcrypt
import jwt

from config import SECRET_KEY
from database.database import Base


class User(Base):

    @staticmethod
    def hash_password(password) -> bytes:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def validate_password(self, password) -> bool:
        return bcrypt.checkpw(password.encode(), self.password)

    def generate_token(self) -> dict:
        return {
            "access_token": jwt.encode(
                {"login": self.login, "role": self.role},
                SECRET_KEY
            )
        }

    """Models a user table"""
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    login = Column(String(225), nullable=False)
    password = Column(LargeBinary, nullable=False)
    role = Column(String(225), nullable=False)
    email = Column(String(225))
    fio = Column(String(225))
    phone = Column(String(225))
