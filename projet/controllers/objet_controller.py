from sqlalchemy.orm import Session
from ..models import Objet


def get_objet(db: Session, objet_id: int):
    return db.query(Objet).get(objet_id)


def create_objet(db: Session, objet: Objet):
    db.add(objet)
    db.commit()
    db.refresh(objet)
    return objet


def update_objet(db: Session, objet: Objet, updated_objet: Objet):
    for attr, value in updated_objet.dict().items():
        setattr(objet, attr, value)
    db.commit()
    db.refresh(objet)
    return objet


def delete_objet(db: Session, objet: Objet):
    db.delete(objet)
    db.commit()
    return {"message": "Objet deleted"}
