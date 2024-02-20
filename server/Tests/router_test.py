from main import app
from fastapi.testclient import TestClient
import unittest

client = TestClient(app)


def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_get_all_cars():
    response = client.get("/car/get_all")
    assert response.status_code == 200
    assert len(response.json()["cars"]) > 0


def test_get_all_cars_for_client():
    response = client.get("/car/get_all_for_client?client_id=11111111-1111-1111-1111-111111111111")
    assert response.status_code == 200
    assert len(response.json()["cars"]) > 0


def test_get_all_clients():
    response = client.get("/client/get_all")
    assert response.status_code == 200
    assert len(response.json()["clients"]) > 0


if __name__ == '__main__':
    unittest.main()
