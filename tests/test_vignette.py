from fastapi import status
from starlette.testclient import TestClient
from projet.main import app

URL: str = "/vignettes/"
vignette_id: int = 99999
client = TestClient(app)


def test_get_all_vignettes():
    response = client.get(URL)
    assert response.status_code == status.HTTP_200_OK


def test_create_vignette():
    vignette = {
        "id": vignette_id,
        "valmin": 11,
        "valtimbre": 3
    }
    response = client.post(URL, json=vignette)
    assert response.status_code == status.HTTP_200_OK


def test_get_vignette():
    response = client.get(f"{URL}{vignette_id}")
    assert response.status_code == status.HTTP_200_OK


def test_update_vignette():
    vignette = {
        "id": vignette_id,
        "valmin": 19.99,
        "valtimbre": 6.99
    }
    response = client.put(f"{URL}{vignette_id}", json=vignette)
    assert response.status_code == status.HTTP_200_OK


def test_delete_vignette():
    response = client.delete(f"{URL}{vignette_id}")
    assert response.status_code == status.HTTP_200_OK


