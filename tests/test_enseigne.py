from fastapi import status
from starlette.testclient import TestClient
from projet.main import app

URL: str = "/enseignes/"
enseigne_id: int = 99999
client = TestClient(app)


def test_get_all_enseignes():
    response = client.get(URL)
    assert response.status_code == status.HTTP_200_OK


def test_create_enseigne():
    enseigne = {
        "id_enseigne": enseigne_id,
        "lb_enseigne": "DSD",
        "ville_enseigne": "Wervicq-sud",
        "dept_enseigne": 0
    }
    response = client.post(URL, json=enseigne)
    assert response.status_code == status.HTTP_200_OK


def test_get_enseigne():
    response = client.get(f"{URL}{enseigne_id}")
    assert response.status_code == status.HTTP_200_OK


def test_update_enseigne():
    enseigne = {
        "id_enseigne": enseigne_id,
        "lb_enseigne": "car-wash",
        "ville_enseigne": "Wervicq-sud",
        "dept_enseigne": 59
    }
    response = client.put(f"{URL}{enseigne_id}", json=enseigne)
    assert response.status_code == status.HTTP_200_OK


def test_delete_enseigne():
    response = client.delete(f"{URL}{enseigne_id}")
    assert response.status_code == status.HTTP_200_OK


