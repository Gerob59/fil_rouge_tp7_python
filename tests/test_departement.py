from fastapi import status
from starlette.testclient import TestClient
from projet.main import app

URL: str = "/departements/"
departement_id: str = "99"
client = TestClient(app)


def test_get_all_departements():
    response = client.get(URL)
    assert response.status_code == status.HTTP_200_OK


def test_create_departement():
    departement = {
      "code_dept": departement_id,
      "nom_dept": "test"
    }
    response = client.post(URL, json=departement)
    assert response.status_code == status.HTTP_200_OK


def test_get_departement():
    response = client.get(f"{URL}{departement_id}")
    assert response.status_code == status.HTTP_200_OK


def test_update_departement():
    departement = {
      "code_dept": departement_id,
      "nom_dept": "plus un test",
      "ordre_aff_dept": 1
    }
    response = client.put(f"{URL}{departement_id}", json=departement)
    assert response.status_code == status.HTTP_200_OK


def test_delete_departement():
    response = client.delete(f"{URL}{departement_id}")
    assert response.status_code == status.HTTP_200_OK
