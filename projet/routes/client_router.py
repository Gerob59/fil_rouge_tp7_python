from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..controllers import client_controller
from ..models import Client
from config.sqlalchemy import bind_engine
from .router import get_router

router = get_router()


@router.get("/{client_id}")
def get_client(client_id: int, db: Session = bind_engine()):
    client = client_controller.get_client(db, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client


@router.post("/")
def create_client(client: Client, db: Session = bind_engine()):
    return client_controller.create_client(db, client)


@router.put("/{client_id}")
def update_client(client_id: int, updated_client: Client, db: Session = bind_engine()):
    client = client_controller.get_client(db, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client_controller.update_client(db, client, updated_client)


@router.delete("/{client_id}")
def delete_client(client_id: int, db: Session = bind_engine()):
    client = client_controller.get_client(db, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client_controller.delete_client(db, client)
