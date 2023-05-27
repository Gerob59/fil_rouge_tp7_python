from sqlalchemy.orm import Session
from ..models import Utilisateur


def get_utilisateur(db: Session, utilisateur_id: int):
    return db.query(Utilisateur).get(utilisateur_id)


def create_utilisateur(db: Session, utilisateur: Utilisateur):
    db.add(utilisateur)
    db.commit()
    db.refresh(utilisateur)
    return utilisateur


def update_utilisateur(db: Session, utilisateur: Utilisateur, updated_utilisateur: Utilisateur):
    for attr, value in updated_utilisateur.dict().items():
        setattr(utilisateur, attr, value)
    db.commit()
    db.refresh(utilisateur)
    return utilisateur


def delete_utilisateur(db: Session, utilisateur: Utilisateur):
    db.delete(utilisateur)
    db.commit()
    return {"message": "Utilisateur deleted"}
