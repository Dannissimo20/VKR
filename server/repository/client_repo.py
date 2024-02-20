import re
import uuid
from datetime import datetime

from sqlalchemy.orm import Session

from models.client_model import Client
from models.car_model import Car
from schemas.client_schema import ClientAddSchema


def add(db: Session, client: ClientAddSchema):
    try:
        pattern = r"^\w+\s\w+\s\w+$"
        if not re.match(pattern, client.name):
            return 'check name format'
        try:
            dob = datetime.strptime(client.dob, '%Y-%m-%d')
        except ValueError:
            return 'check DoB format'
        db_client = Client(id=uuid.uuid4(), name=client.name, dob=dob)
        if db_client.name != "test test test":
            db.add(db_client)
            db.commit()
            db.close()
        return 'ok'
    except Exception as e:
        raise e
