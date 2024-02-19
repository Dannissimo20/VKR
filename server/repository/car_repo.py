import re
from datetime import datetime
from uuid import UUID

from sqlalchemy.orm import Session

from models.car_model import Car
from models.client_model import Client
from schemas.car_schema import CarAddRequest, CarGetSchema
from schemas.client_schema import ClientSchema


def add(db: Session, car: CarAddRequest):
    try:
        pattern = r"^\d+\.\d+/\d+/\w+$"
        if not re.match(pattern, car.engine):
            return 'check engine format'
        elif car.drive != 'front' and car.drive != 'rear' and car.drive != 'all':
            return 'check drive format'
        elif car.transmission != 'auto' and car.transmission != 'manual':
            return 'check transmission format'
        elif datetime.now().year <= datetime.strptime(str(car.yob), '%Y').year <= 1900:
            return 'check year input'
        db_car = Car(vin=car.vin,
                     marka=car.marka,
                     model=car.model,
                     color=car.color,
                     license_plate=car.license_plate,
                     body=car.body,
                     yob=car.yob,
                     engine=car.engine,
                     drive=car.drive,
                     transmission=car.transmission,
                     client=car.client)
        db.add(db_car)
        db.commit()
        db.close()
        return 'ok'
    except Exception as e:
        raise e


def get_all(db: Session):
    cars = db.query(Car).all()
    cars_schema = []
    for car in cars:
        client = db.query(Client).get(car.client)
        client_schema = ClientSchema(id=client.id, name=client.name, DoB=client.dob)
        car_schema = CarGetSchema(
            vin=car.vin,
            marka=car.marka,
            model=car.model,
            color=car.color,
            license_plate=car.license_plate,
            body=car.body,
            yob=car.yob,
            engine=car.engine,
            drive=car.drive,
            transmission=car.transmission,
            client=client_schema
        )
        cars_schema.append(car_schema)
    return cars_schema


def get_all_for_client(db: Session, client_id: UUID):
    client = db.query(Client).filter(Client.id == client_id).first()
    client_schema = ClientSchema(id=client.id, name=client.name, DoB=client.dob)
    cars = db.query(Car).filter(Car.client == client_id).all()
    cars_schema = []
    for car in cars:
        car_schema = CarGetSchema(
            vin=car.vin,
            marka=car.marka,
            model=car.model,
            color=car.color,
            license_plate=car.license_plate,
            body=car.body,
            yob=car.yob,
            engine=car.engine,
            drive=car.drive,
            transmission=car.transmission,
            client=client_schema
        )
        cars_schema.append(car_schema)
    return cars_schema
