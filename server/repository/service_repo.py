from sqlalchemy.orm import Session

from models.service_model import Service
from schemas.service_schema import ServiceAddRequest


def add(service: ServiceAddRequest, db: Session):
    try:
        db_service = Service(name=service.name, description=service.description)
        db.add(db_service)
        db.commit()
        db.close()
        return 'ok'
    except Exception as e:
        return str(e)
