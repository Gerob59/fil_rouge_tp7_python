from fastapi import status
from starlette.testclient import TestClient
from projet.main import app

URL: str = "/vignettes/"
detail_id: int = 99999
client = TestClient(app)


def test_get_all_vignettes():
    response = client.get(URL)
    assert response.status_code == status.HTTP_200_OK


def test_create_vignette():
    detail = {
      "id": detail_id,
      "codcde": 1
    }
    response = client.post(URL, json=detail)
    assert response.status_code == status.HTTP_200_OK


def test_get_vignette():
    response = client.get(f"{URL}{detail_id}")
    assert response.status_code == status.HTTP_200_OK


def test_update_vignette():
    detail = {
      "id": detail_id,
      "codcde": 1,
      "qte": 2,
      "colis": 2,
      "commentaire": "aucun commentaire"
    }
    response = client.put(f"{URL}{detail_id}", json=detail)
    assert response.status_code == status.HTTP_200_OK


def test_delete_vignette():
    response = client.delete(f"{URL}{detail_id}")
    assert response.status_code == status.HTTP_200_OK


