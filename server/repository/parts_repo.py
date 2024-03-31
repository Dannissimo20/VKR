import uuid

from sqlalchemy.orm import Session
from config import logger

from models.parts_model import Parts
from schemas.parts_schema import PartsAddRequest, PartsSchema


def add(part: PartsAddRequest, db: Session):
    try:
        db_part = Parts(id=uuid.uuid4(),
                        name=part.name,
                        description=part.description,
                        price=part.price,
                        count=part.count,
                        unit=part.unit)
        db.add(db_part)
        db.commit()
        db.close()
        return 'ok'
    except Exception as e:
        logger.error(e)
        return str(e)


def get_all(db: Session):
    try:
        parts = db.query(Parts).all()
        parts_schema = [PartsSchema(id=str(part.id),
                                    name=part.name,
                                    description=part.description,
                                    price=part.price,
                                    count=part.count,
                                    unit=part.unit) for part in parts]
    except Exception as e:
        logger.error(e)
        return str(e)
    if parts is None:
        logger.warning('parts not found')
        return 'parts not found'
    return parts_schema


def get_by_id(part_id, db: Session):
    try:
        part_id = uuid.UUID(part_id)
        part = db.query(Parts).filter(Parts.id == part_id).first()
    except Exception as e:
        logger.error(e)
        return str(e)
    if part is None:
        logger.warning(f'part for id {part_id} not found')
        return 'part not found'
    return PartsSchema(id=str(part.id),
                       name=part.name,
                       description=part.description,
                       price=part.price,
                       count=part.count,
                       unit=part.unit)


def update_for_count(part_id, count, db: Session):
    try:
        part_id = uuid.UUID(part_id)
        part = db.query(Parts).filter(Parts.id == part_id).first()
        if part is None:
            logger.warning(f'part for id {part_id} not found')
            return 'part not found'
        part.count = count
        db.commit()
        db.close()
        return 'ok'
    except Exception as e:
        logger.error(e)
        return str(e)
