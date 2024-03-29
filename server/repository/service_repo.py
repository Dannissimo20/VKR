import uuid

from sqlalchemy.orm import Session
from config import logger

from models.service_model import Service
from schemas.service_schema import ServiceAddRequest


def add(service: ServiceAddRequest, db: Session):
    try:
        db_service = Service(id=uuid.uuid4(), name=service.name, duration=service.duration)
        db.add(db_service)
        db.commit()
        db.close()
        return 'ok'
    except Exception as e:
        logger.error(e)
        return str(e)
