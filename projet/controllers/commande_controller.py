from sqlalchemy.orm import Session
from ..models import Commande


def get_commande(db: Session, commande_id: int):
    return db.query(Commande).get(commande_id)


def create_commande(db: Session, commande: Commande):
    db.add(commande)
    db.commit()
    db.refresh(commande)
    return commande


def update_commande(db: Session, commande: Commande, updated_commande: Commande):
    for attr, value in updated_commande.dict().items():
        setattr(commande, attr, value)
    db.commit()
    db.refresh(commande)
    return commande


def delete_commande(db: Session, commande: Commande):
    db.delete(commande)
    db.commit()
    return {"message": "Commande deleted"}
