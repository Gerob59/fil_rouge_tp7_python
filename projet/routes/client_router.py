from fastapi import HTTPException
from ..controllers import client_controller
from ..models import Client
from config.db import open_session
from .router import get_router


router = get_router()
session = open_session()


@router.get("/{client_id}")
def get_client(client_id: int):
    client = client_controller.get_client(session, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client


@router.post("/")
def create_client(client: Client):
    return client_controller.create_client(session, client)


@router.put("/{client_id}")
def update_client(client_id: int, updated_client: Client):
    client = client_controller.get_client(session, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client_controller.update_client(session, client, updated_client)


@router.patch("/{client_id}")
def patch_client(client_id: int, updated_client: Client):
    client = client_controller.get_client(session, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client_controller.update_client(session, client, updated_client)


@router.delete("/{client_id}")
def delete_client(client_id: int):
    client = client_controller.get_client(session, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client_controller.delete_client(session, client)
