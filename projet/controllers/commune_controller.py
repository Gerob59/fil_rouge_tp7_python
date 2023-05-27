from sqlalchemy.orm import Session
from ..models import Commune


def get_commune(db: Session, commune_id: int):
    return db.query(Commune).get(commune_id)


def create_commune(db: Session, commune: Commune):
    db.add(commune)
    db.commit()
    db.refresh(commune)
    return commune


def update_commune(db: Session, commune: Commune, updated_commune: Commune):
    for attr, value in updated_commune.dict().items():
        setattr(commune, attr, value)
    db.commit()
    db.refresh(commune)
    return commune


def delete_commune(db: Session, commune: Commune):
    db.delete(commune)
    db.commit()
    return {"message": "Commune deleted"}
