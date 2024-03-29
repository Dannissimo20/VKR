import re
import uuid
from datetime import datetime

from sqlalchemy.orm import Session

from models.client_model import Client
from models.car_model import Car
from schemas.car_schema import CarSchema
from schemas.client_schema import ClientAddRequest, ClientSchema


def add(db: Session, client: ClientAddRequest):
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


def get_all(db: Session):
    clients = db.query(Client).all()
    clients_schema = []
    for client in clients:
        client_id = str(client.id)
        cars = db.query(Car).filter(Car.client == client_id).all()
        cars = [CarSchema(vin=car.vin,
                          marka=car.marka,
                          model=car.model,
                          color=car.color,
                          license_plate=car.license_plate,
                          body=car.body,
                          yob=car.yob,
                          engine=car.engine,
                          drive=car.drive,
                          transmission=car.transmission) for car in cars]
        client_schema = ClientSchema(name=client.name, dob=client.dob, cars=cars)
        clients_schema.append(client_schema)
    return clients_schema
