from fastapi import status
from starlette.testclient import TestClient
from projet.main import app

URL: str = "/objets/"
objet_id: int = 99999
client = TestClient(app)


def test_get_all_objets():
    response = client.get(URL)
    assert response.status_code == status.HTTP_200_OK


def test_create_objet():
    objet = {
        "codobj": objet_id,
        "libobj": "téléphone",
        "tailleobj": "20 cm x 5 cm",
        "puobj": 1000,
        "poidsobj": 400
    }
    response = client.post(URL, json=objet)
    assert response.status_code == status.HTTP_200_OK


def test_get_objet():
    response = client.get(f"{URL}{objet_id}")
    assert response.status_code == status.HTTP_200_OK


def test_update_objet():
    objet = {
        "codobj": objet_id,
        "libobj": "brique",
        "tailleobj": "40 cm x 20 cm",
        "puobj": 1,
        "poidsobj": 400
    }
    response = client.put(f"{URL}{objet_id}", json=objet)
    assert response.status_code == status.HTTP_200_OK


def test_delete_objet():
    response = client.delete(f"{URL}{objet_id}")
    assert response.status_code == status.HTTP_200_OK


