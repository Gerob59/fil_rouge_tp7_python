from sqlalchemy.orm import Session
from ..models import Client


def get_client(db: Session, client_id: int):
    return db.query(Client).get(client_id)


def create_client(db: Session, client: Client):
    db.add(client)
    db.commit()
    db.refresh(client)
    return client


def update_client(db: Session, client: Client, updated_client: Client):
    for attr, value in updated_client.dict().items():
        setattr(client, attr, value)
    db.commit()
    db.refresh(client)
    return client


def delete_client(db: Session, client: Client):
    db.delete(client)
    db.commit()
    return {"message": "Client deleted"}
