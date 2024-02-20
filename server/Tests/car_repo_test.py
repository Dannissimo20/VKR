import unittest
from copy import deepcopy

from sqlalchemy.orm import Session

from Tests.test_database import TestSessionLocal
from Tests.tests_fixture import cars_for_client
from repository import car_repo
from schemas.car_schema import CarAddRequest


car = CarAddRequest(vin='1',
                    marka='1',
                    model='1',
                    color='1',
                    license_plate='А111АА43',
                    body='1',
                    yob=1901,
                    engine='1.0/1/1',
                    drive='front',
                    transmission='auto',
                    client='11111111-1111-1111-1111-111111111111'
                    )


class AddCarTests(unittest.TestCase):

    def test_license_plate_error(self):
        test_car = deepcopy(car)
        test_car.license_plate = 'Hello'
        test_db: Session = TestSessionLocal()
        response = car_repo.add(test_db, test_car)
        self.assertEqual(response, 'check license_plate format')

    def test_right(self):
        test_db: Session = TestSessionLocal()
        response = car_repo.add(test_db, car)
        self.assertEqual(response, 'ok')

    def test_engine_error(self):
        test_car = deepcopy(car)
        test_car.engine = '1/1/1'
        test_db: Session = TestSessionLocal()
        response = car_repo.add(test_db, test_car)
        self.assertEqual(response, 'check engine format')

    def tes_drive_error(self):
        test_car = deepcopy(car)
        test_car.drive = 'Hello'
        test_db: Session = TestSessionLocal()
        response = car_repo.add(test_db, test_car)
        self.assertEqual(response, 'check drive format')

    def test_transmission_error(self):
        test_car = deepcopy(car)
        test_car.transmission = 'Hello'
        test_db: Session = TestSessionLocal()
        response = car_repo.add(test_db, test_car)
        self.assertEqual(response, 'check transmission format')

    def test_year_error(self):
        test_car = deepcopy(car)
        test_car.yob = 1000
        test_db: Session = TestSessionLocal()
        response = car_repo.add(test_db, test_car)
        self.assertEqual(response, 'check year input')


class GetCarForClientTests(unittest.TestCase):

    def test_right(self):
        test_db: Session = TestSessionLocal()
        response = car_repo.get_all_for_client(test_db, '11111111-1111-1111-1111-111111111111')
        self.assertEqual(response, cars_for_client)

    def test_client_id_error(self):
        test_db: Session = TestSessionLocal()
        response = car_repo.get_all_for_client(test_db, 'Hello')
        self.assertEqual(response, 'check client_id format')


if __name__ == '__main__':
    unittest.main()
