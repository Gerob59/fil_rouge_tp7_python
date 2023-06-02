from fastapi import status
from starlette.testclient import TestClient
from projet.main import app

URL: str = "/poids/"
poids_id: int = 99999
client = TestClient(app)


def test_get_all_poids():
    response = client.get(URL)
    assert response.status_code == status.HTTP_200_OK


def test_create_poids():
    poids = {
        "id": poids_id,
        "valmin": 2,
        "valtimbre": 15
    }
    response = client.post(URL, json=poids)
    assert response.status_code == status.HTTP_200_OK


def test_get_poids():
    response = client.get(f"{URL}{poids_id}")
    assert response.status_code == status.HTTP_200_OK


def test_update_poids():
    poids = {
        "id": poids_id,
        "valmin": 2,
        "valtimbre": 15
    }
    response = client.put(f"{URL}{poids_id}", json=poids)
    assert response.status_code == status.HTTP_200_OK


def test_delete_poids():
    response = client.delete(f"{URL}{poids_id}")
    assert response.status_code == status.HTTP_200_OK


