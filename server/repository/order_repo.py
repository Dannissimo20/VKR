import uuid
from datetime import datetime

from sqlalchemy.orm import Session
from config import logger

from models.order_model import Order
from schemas.order_schema import OrderAddRequest


def add(order: OrderAddRequest, db: Session):
    try:
        db.order = Order(
            worker=order.worker,
            lifter=order.lifter,
            status=0,
            problem_description=order.problem_description,
            recommendation_description=order.recommendation_description,
            created_at=datetime.now(),
        )
        db.add(db.order)
        db.commit()
        db.close()
        return 'ok'
    except Exception as e:
        logger.error(e)
        return str(e)


def add_from_record(db: Session):
    try:
        db_order = Order(
            id=uuid.uuid4(),
            status=0,
            created_at=datetime.now(),
        )
        db.add(db_order)
        db.commit()
        return db_order
    except Exception as e:
        logger.error(e)
        return str(e)
