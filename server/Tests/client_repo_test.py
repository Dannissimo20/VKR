import unittest
from copy import deepcopy

from sqlalchemy.orm import Session

from Tests.test_database import TestSessionLocal
from repository import client_repo
from schemas.client_schema import ClientAddSchema

client = ClientAddSchema(name='test test test', dob='1970-01-01')


class AddClientTest(unittest.TestCase):
    def test_right(self):
        test_db: Session = TestSessionLocal()
        response = client_repo.add(test_db, client)
        self.assertEqual(response, 'ok')

    def test_name_error(self):
        test_client = deepcopy(client)
        test_client.name = 'test test'
        test_db: Session = TestSessionLocal()
        response = client_repo.add(test_db, test_client)
        self.assertEqual(response, 'check name format')


if __name__ == '__main__':
    unittest.main()
