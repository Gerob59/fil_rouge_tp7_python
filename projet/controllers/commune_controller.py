from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import Commune
from ..schemas import CommuneSchema


def get_commune(db: Session, commune_id: int):
    commune = db.query(Commune).get(commune_id)
    if not commune:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Commune not found")
    return commune


def get_all_communes(db: Session):
    return db.query(Commune).all()


def create_commune(db: Session, commune: CommuneSchema):
    db.add(commune)
    db.commit()
    db.refresh(commune)
    return commune


def update_commune(db: Session, commune_id: int, updated_commune: CommuneSchema):
    commune = db.query(Commune).get(commune_id)
    if not commune:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Commune not found")
    updated_data = updated_commune.dict(exclude_unset=True)
    for attr, value in updated_data.items():
        setattr(commune, attr, value)
    db.commit()
    db.refresh(commune)
    return commune


def delete_commune(db: Session, commune_id: int):
    commune = db.query(Commune).get(commune_id)
    if not commune:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Commune not found")
    db.delete(commune)
    db.commit()
    return {"message": "Commune deleted"}
