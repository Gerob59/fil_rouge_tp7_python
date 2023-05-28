from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import client_controller
from ..models import Client
from config.db import get_db

router = APIRouter()


@router.get("/{client_id}", response_model=Client)
def get_client(client_id: int, db: Session = Depends(get_db)):
    client = client_controller.get_client(db, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client


@router.get("/", response_model=list[Client])
def get_all_clients(db: Session = Depends(get_db)):
    return client_controller.get_all_clients(db)


@router.post("/", response_model=Client)
def create_client(client: Client, db: Session = Depends(get_db)):
    return client_controller.create_client(db, client)


@router.put("/{client_id}", response_model=Client)
def update_client(client_id: int, updated_client: Client, db: Session = Depends(get_db)):
    client = client_controller.get_client(db, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client_controller.update_client(db, client, updated_client)


@router.patch("/{client_id}", response_model=Client)
def patch_client(client_id: int, updated_client: Client, db: Session = Depends(get_db)):
    client = client_controller.get_client(db, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client_controller.update_client(db, client, updated_client)


@router.delete("/{client_id}", response_model=dict)
def delete_client(client_id: int, db: Session = Depends(get_db)):
    client = client_controller.get_client(db, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client_controller.delete_client(db, client)
