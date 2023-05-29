from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import Enseigne
from ..schemas import EnseigneSchema


def get_enseigne(db: Session, enseigne_id: int):
    enseigne = db.query(Enseigne).get(enseigne_id)
    if not enseigne:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Enseigne not found")
    return enseigne


def get_all_enseignes(db: Session):
    return db.query(Enseigne).all()


def create_enseigne(db: Session, enseigne: EnseigneSchema):
    db.add(enseigne)
    db.commit()
    db.refresh(enseigne)
    return enseigne


def update_enseigne(db: Session, enseigne_id: int, updated_enseigne: EnseigneSchema):
    enseigne = db.query(Enseigne).get(enseigne_id)
    if not enseigne:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Enseigne not found")
    updated_data = updated_enseigne.dict(exclude_unset=True)
    for attr, value in updated_data.items():
        setattr(enseigne, attr, value)
    db.commit()
    db.refresh(enseigne)
    return enseigne


def delete_enseigne(db: Session, enseigne_id: int):
    enseigne = db.query(Enseigne).get(enseigne_id)
    if not enseigne:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Enseigne not found")
    db.delete(enseigne)
    db.commit()
    return {"message": "Enseigne deleted"}
