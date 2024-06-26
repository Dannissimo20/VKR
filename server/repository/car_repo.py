import re
from datetime import datetime
from uuid import UUID

from sqlalchemy.orm import Session
from config import logger

from models.car_model import Car
from models.client_model import Client
from schemas.car_schema import CarAddRequest, CarGetSchema


def converter_car_car_schema(car, client):
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
        client=str(client.id)
    )
    return car_schema


def add(db: Session, car: CarAddRequest):
    try:
        if not re.match(r"^\d+\.\d+/\d+/\w+$", car.engine):
            logger.warning(f'Wrong engine format: {car.engine} instead of "1.0/100/petrol"')
            return 'check engine format'
        elif not re.match(r"^[АВЕКМНОРСТУХ]\d{3}(?<!000)[АВЕКМНОРСТУХ]{2}\d{2,3}$", car.license_plate):
            logger.warning(f'Wrong license_plate format: {car.license_plate} instead of "A000AA00"')
            return 'check license_plate format'
        elif car.drive != 'front' and car.drive != 'rear' and car.drive != 'all':
            logger.warning(f'Wrong drive format: {car.drive} instead of "front" or "rear" or "all"')
            return 'check drive format'
        elif car.transmission != 'auto' and car.transmission != 'manual':
            logger.warning(f'Wrong transmission format: {car.transmission} instead of "auto" or "manual"')
            return 'check transmission format'
        elif (datetime.strptime(str(car.yob), '%Y').year <= 1900 or
              datetime.strptime(str(car.yob), '%Y').year > datetime.now().year):
            logger.warning(f'Wrong year format: {car.yob} instead of year greater than 1900 and less than {datetime.now().year}')
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
        logger.error(e)
        return str(e)


def get_all(db: Session):
    cars = db.query(Car).all()
    cars_schema = []
    for car in cars:
        client = db.query(Client).get(car.client)
        car_schema = converter_car_car_schema(car, client)
        cars_schema.append(car_schema)
    return cars_schema


def get_all_for_client(db: Session, client_id: str):
    try:
        client_id = UUID(client_id)
    except ValueError:
        logger.warning(f'Wrong client_id format: {client_id} instead of "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"')
        return 'check client_id format'
    client = db.query(Client).filter(Client.id == client_id).first()
    cars = db.query(Car).filter(Car.client == client_id).all()
    cars_schema = []
    for car in cars:
        car_schema = converter_car_car_schema(car, client)
        cars_schema.append(car_schema)
    return cars_schema
