from fastapi import status
from starlette.testclient import TestClient
from projet.main import app

URL: str = "/login"
client = TestClient(app)


def test_create_vignette():
    login = {
        "username": "root",
        "password": "password"
    }
    response = client.post(URL, json=login)
    assert response.status_code == status.HTTP_200_OK
