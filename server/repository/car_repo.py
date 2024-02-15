import re
from datetime import datetime

from sqlalchemy.orm import Session

from models.car_model import Car
from schemas.car_schema import CarAddRequest


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
