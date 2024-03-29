from sqlalchemy.orm import Session

from models.parts_model import Parts
from schemas.parts_schema import PartsAddRequest


def add(part: PartsAddRequest, db: Session):
    try:
        db_part = Parts(name=part.name, description=part.description, price=part.price, count=part.count, unit=part.unit)
        db.add(db_part)
        db.commit()
        db.close()
        return 'ok'
    except Exception as e:
        return str(e)