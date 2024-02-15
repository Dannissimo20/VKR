import re
import uuid

from sqlalchemy.orm import Session

from models.client_model import Client
from schemas.client_schema import ClientAddSchema


def add(db: Session, client: ClientAddSchema):
    try:
        pattern = r"^\w+\s\w+\s\w+$"
        if re.match(pattern, client.name):
            db_client = Client(id=uuid.uuid4(), name=client.name, dob=client.DoB)
            db.add(db_client)
            db.commit()
            db.close()
        else:
            return 'name error'
        return 'ok'
    except Exception as e:
        raise e
