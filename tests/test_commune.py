from fastapi import status
from starlette.testclient import TestClient
from projet.main import app

URL: str = "/communes/"
commune_id: int = 99999
client = TestClient(app)


def test_get_all_communes():
    response = client.get(URL)
    assert response.status_code == status.HTTP_200_OK


def test_create_commune():
    commune = {
      "id": commune_id,
      "dep": "59"
    }
    response = client.post(URL, json=commune)
    assert response.status_code == status.HTTP_200_OK


def test_get_commune():
    response = client.get(f"{URL}{commune_id}")
    assert response.status_code == status.HTTP_200_OK


def test_update_commune():
    commune = {
      "id": commune_id,
      "dep": "59",
      "cp": "59999",
      "ville": "test-ville"
    }
    response = client.put(f"{URL}{commune_id}", json=commune)
    assert response.status_code == status.HTTP_200_OK


def test_delete_commune():
    response = client.delete(f"{URL}{commune_id}")
    assert response.status_code == status.HTTP_200_OK
