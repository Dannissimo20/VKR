import uuid
from datetime import datetime
from typing import cast

from sqlalchemy.orm import Session
from config import logger

from models.client_model import Client
from models.order_model import Order
from models.record_model import Record
from repository import order_repo
from schemas.record_schema import RecordAddRequest, RecordConfirmRequest


def add(record: RecordAddRequest, db: Session):
    try:
        client = db.query(Client).filter(cast('ColumnElement[bool]', Client.phone == record.client_phone), cast('ColumnElement[bool]', Client.fio == record.client_fio)).first()
        if client is None:
            client = Client(id=uuid.uuid4(), fio=record.client_fio, phone=record.client_phone)
            db.add(client)
        record_id = uuid.uuid4()
        order = order_repo.add_from_record(db=db)
        db_record = Record(id=record_id, order=order, confirmation=record.confirmation, date=datetime.strptime(record.date, '%d.%m.%Y'), client=client.id)
        db.add(db_record)
        db.commit()
        db.close()
        return 'ok'
    except Exception as e:
        logger.error(e)
        return str(e)


def confirm(record: RecordConfirmRequest, db: Session):
    try:
        db_record = db.query(Record).filter(Record.id == record.id).first()
        db_record.confirmation = 1
        db.commit()
        db.close()
        return 'ok'
    except Exception as e:
        logger.error(e)
        return str(e)


def cancel(record: RecordConfirmRequest, db: Session):
    try:
        db_record = db.query(Record).filter(Record.id == record.id).first()
        db_record.confirmation = 2
        order_repo.delete_from_record(db_record.order, db)
        db.commit()
        db.close()
        return 'ok'
    except Exception as e:
        logger.error(e)
        return str(e)
