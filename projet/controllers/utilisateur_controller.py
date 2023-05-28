from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import Utilisateur


def get_utilisateur(db: Session, utilisateur_id: int):
    utilisateur = db.query(Utilisateur).get(utilisateur_id)
    if not utilisateur:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Utilisateur not found")
    return utilisateur


def get_all_utilisateurs(db: Session):
    return db.query(Utilisateur).all()


def create_utilisateur(db: Session, utilisateur: Utilisateur):
    db.add(utilisateur)
    db.commit()
    db.refresh(utilisateur)
    return utilisateur


def update_utilisateur(db: Session, utilisateur_id: int, updated_utilisateur: Utilisateur):
    utilisateur = db.query(Utilisateur).get(utilisateur_id)
    if not utilisateur:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Utilisateur not found")
    updated_data = updated_utilisateur.dict(exclude_unset=True)
    for attr, value in updated_data.items():
        setattr(utilisateur, attr, value)
    db.commit()
    db.refresh(utilisateur)
    return utilisateur


def delete_utilisateur(db: Session, utilisateur_id: int):
    utilisateur = db.query(Utilisateur).get(utilisateur_id)
    if not utilisateur:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Utilisateur not found")
    db.delete(utilisateur)
    db.commit()
    return {"message": "Utilisateur deleted"}
