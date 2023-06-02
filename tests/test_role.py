from fastapi import status
from starlette.testclient import TestClient
from projet.main import app

URL: str = "/roles/"
role_id: int = 99999
client = TestClient(app)


def test_get_all_roles():
    response = client.get(URL)
    assert response.status_code == status.HTTP_200_OK


def test_create_role():
    role = {
        "codrole": role_id,
        "librole": "test_role"
    }
    response = client.post(URL, json=role)
    assert response.status_code == status.HTTP_200_OK


def test_get_role():
    response = client.get(f"{URL}{role_id}")
    assert response.status_code == status.HTTP_200_OK


def test_update_role():
    role = {
        "codrole": role_id,
        "librole": "autre_test_role"
    }
    response = client.put(f"{URL}{role_id}", json=role)
    assert response.status_code == status.HTTP_200_OK


def test_delete_role():
    response = client.delete(f"{URL}{role_id}")
    assert response.status_code == status.HTTP_200_OK


