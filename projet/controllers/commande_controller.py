from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import Commande
from ..schemas import CommandeSchema


def get_commande(db: Session, commande_id: int):
    commande = db.query(Commande).get(commande_id)
    if not commande:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Commande not found")
    return commande


def get_all_commandes(db: Session):
    return db.query(Commande).all()


def create_commande(db: Session, commande: CommandeSchema):
    db.add(commande)
    db.commit()
    db.refresh(commande)
    return commande


def update_commande(db: Session, commande_id: int, updated_commande: CommandeSchema):
    commande = db.query(Commande).get(commande_id)
    if not commande:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Commande not found")
    updated_data = updated_commande.dict(exclude_unset=True)
    for attr, value in updated_data.items():
        setattr(commande, attr, value)
    db.commit()
    db.refresh(commande)
    return commande


def delete_commande(db: Session, commande_id: int):
    commande = db.query(Commande).get(commande_id)
    if not commande:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Commande not found")
    db.delete(commande)
    db.commit()
    return {"message": "Commande deleted"}
