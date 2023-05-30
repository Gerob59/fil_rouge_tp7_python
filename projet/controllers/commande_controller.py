from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import Commande
from ..schemas import CommandeSchema


def get_commande(db: Session, commande_id: int) -> CommandeSchema:
    with db:
        commande_db = db.query(Commande).get(commande_id)
        if not commande_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Commande not found")
    return CommandeSchema.from_orm(commande_db)


def get_all_commandes(db: Session) -> [CommandeSchema]:
    with db:
        resultat = db.query(Commande).all()
    return resultat


def create_commande(db: Session, commande: CommandeSchema) -> CommandeSchema:
    with db:
        commande_db = Commande(**commande.dict())
        db.add(commande_db)
        db.commit()
        db.refresh(commande_db)
    return CommandeSchema.from_orm(commande_db)


def update_commande(db: Session, commande_id: int, updated_commande: CommandeSchema) -> CommandeSchema:
    with db:
        commande_db = db.query(Commande).get(commande_id)
        if not commande_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Commande not found")
        updated_data = updated_commande.dict(exclude_unset=True)
        for attr, value in updated_data.items():
            setattr(commande_db, attr, value)
        db.commit()
        db.refresh(commande_db)
    return CommandeSchema.from_orm(commande_db)


def delete_commande(db: Session, commande_id: int) -> dict:
    with db:
        commande_db = db.query(Commande).get(commande_id)
        if not commande_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Commande not found")
        db.delete(commande_db)
        db.commit()
    return {"message": "Commande deleted"}
