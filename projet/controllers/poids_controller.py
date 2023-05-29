from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import Poids
from ..schemas import PoidsSchema


def get_poids(db: Session, poids_id: int):
    poids = db.query(Poids).get(poids_id)
    if not poids:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Poids not found")
    return poids


def get_all_poids(db: Session):
    return db.query(Poids).all()


def create_poids(db: Session, poids: PoidsSchema):
    db.add(poids)
    db.commit()
    db.refresh(poids)
    return poids


def update_poids(db: Session, poids_id: int, updated_poids: PoidsSchema):
    poids = db.query(Poids).get(poids_id)
    if not poids:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Poids not found")
    updated_data = updated_poids.dict(exclude_unset=True)
    for attr, value in updated_data.items():
        setattr(poids, attr, value)
    db.commit()
    db.refresh(poids)
    return poids


def delete_poids(db: Session, poids_id: int):
    poids = db.query(Poids).get(poids_id)
    if not poids:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Poids not found")
    db.delete(poids)
    db.commit()
    return {"message": "Poids deleted"}
