import unittest

from Tests.car_repo_test import AddCarTests
from Tests.car_repo_test import GetCarForClientTests
from Tests.client_repo_test import AddClientTest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(AddCarTests))
    suite.addTests(loader.loadTestsFromTestCase(GetCarForClientTests))
    suite.addTests(loader.loadTestsFromTestCase(AddClientTest))
    runner = unittest.TextTestRunner()
    runner.run(suite)
