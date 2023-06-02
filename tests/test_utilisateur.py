from fastapi import status
from starlette.testclient import TestClient
from projet.main import app

URL: str = "/utilisateurs/"
utilisateur_id: int = 9999
client = TestClient(app)


def test_get_all_utilisateurs():
    response = client.get(URL)
    assert response.status_code == status.HTTP_200_OK


def test_create_utilisateur():
    utilisateur = {
        "code_utilisateur": utilisateur_id,
        "nom_utilisateur": "hotton",
        "prenom_utilisateur": "robin",
        "username": "root",
        "password": "password"
    }
    response = client.post(URL, json=utilisateur)
    assert response.status_code == status.HTTP_200_OK


def test_get_utilisateur():
    response = client.get(f"{URL}{utilisateur_id}")
    assert response.status_code == status.HTTP_200_OK


def test_update_utilisateur():
    utilisateur = {
        "code_utilisateur": utilisateur_id,
        "nom_utilisateur": "guillon",
        "prenom_utilisateur": "antonin",
        "username": "root2",
        "password": "password"
    }
    response = client.put(f"{URL}{utilisateur_id}", json=utilisateur)
    assert response.status_code == status.HTTP_200_OK


def test_delete_utilisateur():
    response = client.delete(f"{URL}{utilisateur_id}")
    assert response.status_code == status.HTTP_200_OK
