import re
import uuid

from sqlalchemy.orm import Session
from config import logger

from models.client_model import Client
from models.car_model import Car
from schemas.car_schema import CarSchema
from schemas.client_schema import ClientAddRequest, ClientSchema


def add(db: Session, client: ClientAddRequest):
    try:
        pattern = r"^\w+\s\w+$"
        if not re.match(pattern, client.fio):
            logger.warning(f'Wrong name format: {client.fio} instead of "name surname"')
            return 'check name format'
        pattern = r'^7\d{10}$'
        if not re.match(pattern, client.phone):
            logger.warning(f'Wrong phone format: {client.phone} instead of "71234567890"')
            return 'check phone format'
        db_client = Client(id=uuid.uuid4(), fio=client.fio, phone=client.phone)
        db.add(db_client)
        db.commit()
        db.close()
        return 'ok'
    except Exception as e:
        logger.error(e)
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
        client_schema = ClientSchema(name=client.name, phone=client.phone, cars=cars)
        clients_schema.append(client_schema)
    return clients_schema
