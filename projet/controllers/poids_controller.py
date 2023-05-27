from sqlalchemy.orm import Session
from ..models import Poids


def get_poids(db: Session, poids_id: int):
    return db.query(Poids).get(poids_id)


def create_poids(db: Session, poids: Poids):
    db.add(poids)
    db.commit()
    db.refresh(poids)
    return poids


def update_poids(db: Session, poids: Poids, updated_poids: Poids):
    for attr, value in updated_poids.dict().items():
        setattr(poids, attr, value)
    db.commit()
    db.refresh(poids)
    return poids


def delete_poids(db: Session, poids: Poids):
    db.delete(poids)
    db.commit()
    return {"message": "Poids deleted"}
