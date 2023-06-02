from fastapi import status
from starlette.testclient import TestClient
from projet.main import app

URL: str = "/clients/"
client_id: int = 99999
client = TestClient(app)


def test_get_all_clients():
    response = client.get(URL)
    assert response.status_code == status.HTTP_200_OK


def test_create_client():
    my_client = {
        "codcli": client_id,
        "genrecli": "M",
        "nomcli": "hotton",
        "prenomcli": "robin",
        "adresse1cli": "unknown",
        "villecli_id": 1,
        "telcli": "0600000000",
        "emailcli": "robin.hotton@hotmail.com",
    }
    response = client.post(URL, json=my_client)
    assert response.status_code == status.HTTP_200_OK


def test_get_client():
    response = client.get(f"{URL}{client_id}")
    assert response.status_code == status.HTTP_200_OK


def test_update_client():
    my_client = {
        "codcli": client_id,
        "genrecli": "M",
        "nomcli": "hotton",
        "prenomcli": "robin",
        "adresse1cli": "toujours unknown",
        "villecli_id": 1,
        "telcli": "0781293190",
        "emailcli": "robin.hotton@hotmail.com",
    }
    response = client.put(f"{URL}{client_id}", json=my_client)
    assert response.status_code == status.HTTP_200_OK


def test_delete_client():
    response = client.delete(f"{URL}{client_id}")
    assert response.status_code == status.HTTP_200_OK


