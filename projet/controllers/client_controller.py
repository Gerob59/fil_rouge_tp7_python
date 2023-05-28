from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import Client


def get_client(db: Session, client_id: int):
    client = db.query(Client).get(client_id)
    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
    return client


def get_all_clients(db: Session):
    return db.query(Client).all()


def create_client(db: Session, client: Client):
    db.add(client)
    db.commit()
    db.refresh(client)
    return client


def update_client(db: Session, client_id: int, updated_client: Client):
    client = db.query(Client).get(client_id)
    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
    updated_data = updated_client.dict(exclude_unset=True)
    for attr, value in updated_data.items():
        setattr(client, attr, value)
    db.commit()
    db.refresh(client)
    return client


def delete_client(db: Session, client_id: int):
    client = db.query(Client).get(client_id)
    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
    db.delete(client)
    db.commit()
    return {"message": "Client deleted"}
