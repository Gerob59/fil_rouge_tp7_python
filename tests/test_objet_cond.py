from fastapi import status
from starlette.testclient import TestClient
from projet.main import app

URL: str = "/objet_cond/"
objet_cond_id: int = 99999
client = TestClient(app)


def test_get_all_objet_cond():
    response = client.get(URL)
    assert response.status_code == status.HTTP_200_OK


def test_create_objet_cond():
    objet_cond = {
        "idrelcond": objet_cond_id,
        "codobj": 1,
        "codcond": 1
      }
    response = client.post(URL, json=objet_cond)
    assert response.status_code == status.HTTP_200_OK


def test_get_objet_cond():
    response = client.get(f"{URL}{objet_cond_id}")
    assert response.status_code == status.HTTP_200_OK


def test_update_objet_cond():
    objet_cond = {
        "idrelcond": objet_cond_id,
        "qteobjdeb": 10,
        "qteobjfin": 100,
        "codobj": 1,
        "codcond": 1
      }
    response = client.put(f"{URL}{objet_cond_id}", json=objet_cond)
    assert response.status_code == status.HTTP_200_OK


def test_delete_objet_cond():
    response = client.delete(f"{URL}{objet_cond_id}")
    assert response.status_code == status.HTTP_200_OK


