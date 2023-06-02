from fastapi import status
from starlette.testclient import TestClient
from projet.main import app

URL: str = "/vignettes/"
vignette_id: int = 9999
client = TestClient(app)


def test_get_all_vignettes():
    response = client.get(URL)
    assert response.status_code == status.HTTP_200_OK


def test_create_vignette():
    vignette = {
        "id": vignette_id,
        "valmin": 10.49,
        "valtimbre": 2.99
    }
    response = client.post(URL, json=vignette)
    assert response.status_code == status.HTTP_201_CREATED


def test_get_vignette():
    response = client.get(f"{URL}{vignette_id}")
    assert response.status_code == status.HTTP_200_OK


def test_update_vignette():
    vignette = {
        "valmin": 19.99,
        "valtimbre": 6.99
    }
    response = client.put(f"{URL}{vignette_id}", json=vignette)
    assert response.status_code == status.HTTP_202_ACCEPTED


def test_delete_vignettes():
    response = client.delete(f"{URL}{vignette_id}")
    assert response.status_code == status.HTTP_200_OK
