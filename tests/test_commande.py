from fastapi import status
from starlette.testclient import TestClient
from projet.main import app

URL: str = "/commandes/"
commande_id: int = 99999
client = TestClient(app)


def test_get_all_commandes():
    response = client.get(URL)
    assert response.status_code == status.HTTP_200_OK


def test_create_commande():
    commande = {
      "codcde": commande_id,
      "codcli": 1,
    }
    response = client.post(URL, json=commande)
    assert response.status_code == status.HTTP_200_OK


def test_get_commande():
    response = client.get(f"{URL}{commande_id}")
    assert response.status_code == status.HTTP_200_OK


def test_update_commande():
    commande = {
      "codcde": commande_id,
      "datcde": "2023-06-02",
      "codcli": 1,
      "timbrecli": 1,
      "timbrecde": 1,
      "nbcolis": 2,
      "cheqcli": 1,
      "idcondit": 1,
      "cdeComt": "je ne sais pas",
      "barchive": 1,
      "bstock": 1
    }
    response = client.put(f"{URL}{commande_id}", json=commande)
    assert response.status_code == status.HTTP_200_OK


def test_delete_commande():
    response = client.delete(f"{URL}{commande_id}")
    assert response.status_code == status.HTTP_200_OK
