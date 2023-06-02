from fastapi import status
from starlette.testclient import TestClient
from projet.main import app

URL: str = "/conditionnements/"
conditionnement_id: int = 99999
client = TestClient(app)


def test_get_all_conditionnements():
    response = client.get(URL)
    assert response.status_code == status.HTTP_200_OK


def test_create_conditionnement():
    conditionnement = {
      "idcondit": conditionnement_id,
      "poidscondit": 0
    }
    response = client.post(URL, json=conditionnement)
    assert response.status_code == status.HTTP_200_OK


def test_get_conditionnement():
    response = client.get(f"{URL}{conditionnement_id}")
    assert response.status_code == status.HTTP_200_OK


def test_update_conditionnement():
    conditionnement = {
      "idcondit": conditionnement_id,
      "libcondit": "quelque chose",
      "poidscondit": 1,
      "prixcond": 1,
      "ordreimp": 1
    }
    response = client.put(f"{URL}{conditionnement_id}", json=conditionnement)
    assert response.status_code == status.HTTP_200_OK


def test_delete_conditionnement():
    response = client.delete(f"{URL}{conditionnement_id}")
    assert response.status_code == status.HTTP_200_OK


