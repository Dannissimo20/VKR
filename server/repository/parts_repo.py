import uuid

from sqlalchemy.orm import Session
from config import logger

from models.parts_model import Parts
from schemas.parts_schema import PartsAddRequest


def add(part: PartsAddRequest, db: Session):
    try:
        db_part = Parts(id=uuid.uuid4(), name=part.name, description=part.description, price=part.price, count=part.count, unit=part.unit)
        db.add(db_part)
        db.commit()
        db.close()
        return 'ok'
    except Exception as e:
        logger.error(e)
        return str(e)
