from fastapi import status
from fastapi.testclient import TestClient

from cargo_app.main import app

client = TestClient(app)


def test_load_ok(test_data_1, expected_result_1):
    response = client.post('/api/v1/cargos/load', json=test_data_1)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_result_1


def test_load_denied_all(test_data_2, expected_result_2):
    response = client.post('/api/v1/cargos/load', json=test_data_2)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_result_2


def test_load_best_with_overweight(test_data_3, expected_result_3):
    response = client.post('/api/v1/cargos/load', json=test_data_3)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_result_3


def test_load_best_with_overarea(test_data_4, expected_result_4):
    response = client.post('/api/v1/cargos/load', json=test_data_4)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_result_4
