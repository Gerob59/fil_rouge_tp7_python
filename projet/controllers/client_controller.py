from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import Client
from ..schemas import ClientSchema


def get_client(db: Session, client_id: int) -> ClientSchema:
    with db:
        client_db = db.query(Client).get(client_id)
        if not client_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
    return ClientSchema.from_orm(client_db)


def get_all_clients(db: Session) -> [ClientSchema]:
    with db:
        res_db = db.query(Client).all()
        res = []
        for detail in res_db:
            res.append(ClientSchema.from_orm(detail))
    return res


def create_client(db: Session, client: ClientSchema) -> ClientSchema:
    with db:
        client_db = Client(**client.dict())
        db.add(client_db)
        db.commit()
        db.refresh(client_db)
    return ClientSchema.from_orm(client_db)


def update_client(db: Session, client_id: int, updated_client: ClientSchema) -> ClientSchema:
    with db:
        client_db = db.query(Client).get(client_id)
        if not client_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
        updated_data = updated_client.dict(exclude_unset=True)
        for attr, value in updated_data.items():
            setattr(client_db, attr, value)
        db.commit()
        db.refresh(client_db)
    return ClientSchema.from_orm(client_db)


def delete_client(db: Session, client_id: int) -> dict:
    with db:
        client_db = db.query(Client).get(client_id)
        if not client_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
        db.delete(client_db)
        db.commit()
    return {"message": "Client deleted"}
