import uuid
from datetime import datetime

from sqlalchemy.orm import Session

from models.client_model import Client
from models.record_model import Record
from repository import order_repo
from schemas.record_schema import RecordAddRequest


def add(record: RecordAddRequest, db: Session):
    try:
        client = db.query(Client).filter(Client.phone == record.client_phone, Client.fio == record.client_fio).first()
        if client is None:
            client = Client(id=uuid.uuid4(), fio=record.client_fio, phone=record.client_phone)
            db.add(client)
        record_id = uuid.uuid4()
        db_record = Record(id=record_id, confirmation=record.confirmation, date=datetime.strptime(record.date, '%d.%m.%Y'), client=client.id)
        db.add(db_record)
        order_repo.add_from_record(record=db_record.id, db=db)
        db.commit()
        db.close()
        return 'ok'
    except Exception as e:
        return str(e)
