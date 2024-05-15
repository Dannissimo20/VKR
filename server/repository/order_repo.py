import uuid
from datetime import datetime

from sqlalchemy.orm import Session
from config import logger

from models.order_model import Order
from models.parts_model import Parts
from models.support_models.parts_orders_model import PartsOrders
from models.support_models.service_orders_model import ServicesOrders
from schemas.order_schema import OrderAddRequest, OrderAddWorkerRequest, OrderAddPartsRequest, OrderAddServicesRequest


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


def delete_from_record(order: Order, db: Session):
    try:
        db.query(Order).filter(Order.id == order.id).delete()
        # db.commit()
        # db.close()
        return 'ok'
    except Exception as e:
        logger.error(e)
        return str(e)


def add_worker(order: OrderAddWorkerRequest, db: Session):
    try:
        db.query(Order).filter(Order.id == order.order_id).update({Order.worker: order.worker_id})
        db.commit()
        db.close()
        return 'ok'
    except Exception as e:
        logger.error(e)
        return str(e)


def add_parts(order: OrderAddPartsRequest, db: Session):
    try:
        for part in order.parts:
            record = PartsOrders.insert().values(
                part=part.part_id,
                order=order.order_id,
                part_count=part.count
            )
            db.execute(record)
            db.query(Parts).filter(Parts.id == part.part_id).update({Parts.count: Parts.count - part.count})
            db.commit()
        db.close()
        return 'ok'
    except Exception as e:
        logger.error(e)
        return str(e)


def add_services(order: OrderAddServicesRequest, db: Session):
    try:
        for service in order.services:
            record = ServicesOrders.insert().values(
                service=service.service_id,
                order=order.order_id
            )
            db.execute(record)
        db.commit()
        db.close()
        return 'ok'
    except Exception as e:
        logger.error(e)
        return str(e)
