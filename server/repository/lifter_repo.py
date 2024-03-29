import uuid
from uuid import UUID

from sqlalchemy.orm import Session
from config import logger

from models.lifter_model import Lifter
from schemas.lifter_schema import LifterAddRequest, LifterSchema


def add(lifter: LifterAddRequest, db: Session):
    try:
        db_lifter = Lifter(id=uuid.uuid4(), name=lifter.name, description=lifter.description, purpose=lifter.purpose)
        db.add(db_lifter)
        db.commit()
        db.close()
        return 'ok'
    except Exception as e:
        logger.error(e)
        return str(e)


def get_all(db: Session):
    try:
        lifters = db.query(Lifter).all()
        lifters_schema = [LifterSchema(name=lifter.name, description=lifter.description, purpose=lifter.purpose)
                          for lifter in lifters]
    except Exception as e:
        logger.error(e)
        return str(e)
    if lifters is None:
        logger.warning('lifters not found')
        return 'lifters not found'
    return lifters_schema


def get_by_id(lifter_id, db: Session):
    try:
        lifter_id = UUID(lifter_id)
        lifter = db.query(Lifter).filter(Lifter.id == lifter_id).first()
    except Exception as e:
        logger.error(e)
        return str(e)
    if lifter is None:
        logger.warning(f'lifter for id {lifter_id} not found')
        return 'lifter not found'
    return LifterSchema(name=lifter.name, description=lifter.description, purpose=lifter.purpose)
