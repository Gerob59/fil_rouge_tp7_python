from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import Objet


def get_objet(db: Session, objet_id: int):
    objet = db.query(Objet).get(objet_id)
    if not objet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Objet not found")
    return objet


def get_all_objets(db: Session):
    return db.query(Objet).all()


def create_objet(db: Session, objet: Objet):
    db.add(objet)
    db.commit()
    db.refresh(objet)
    return objet


def update_objet(db: Session, objet_id: int, updated_objet: Objet):
    objet = db.query(Objet).get(objet_id)
    if not objet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Objet not found")
    updated_data = updated_objet.dict(exclude_unset=True)
    for attr, value in updated_data.items():
        setattr(objet, attr, value)
    db.commit()
    db.refresh(objet)
    return objet


def delete_objet(db: Session, objet_id: int):
    objet = db.query(Objet).get(objet_id)
    if not objet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Objet not found")
    db.delete(objet)
    db.commit()
    return {"message": "Objet deleted"}
