from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import client_controller
from ..schemas import ClientSchema
from config import get_db

router = APIRouter()


@router.get("/{client_id}", response_model=ClientSchema)
def get_client(client_id: int, db: Session = Depends(get_db)):
    return client_controller.get_client(db, client_id)


@router.get("/", response_model=list[ClientSchema])
def get_all_clients(db: Session = Depends(get_db)):
    return client_controller.get_all_clients(db)


@router.post("/", response_model=ClientSchema)
def create_client(client: ClientSchema, db: Session = Depends(get_db)):
    return client_controller.create_client(db, client)


@router.put("/{client_id}", response_model=ClientSchema)
def update_client(client_id: int, updated_client: ClientSchema, db: Session = Depends(get_db)):
    return client_controller.update_client(db, client_id, updated_client)


@router.patch("/{client_id}", response_model=ClientSchema)
def patch_client(client_id: int, updated_client: ClientSchema, db: Session = Depends(get_db)):
    return client_controller.update_client(db, client_id, updated_client)


@router.delete("/{client_id}", response_model=dict)
def delete_client(client_id: int, db: Session = Depends(get_db)):
    return client_controller.delete_client(db, client_id)
