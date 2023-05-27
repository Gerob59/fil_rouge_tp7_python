from sqlalchemy.orm import Session
from ..models import Enseigne


def get_enseigne(db: Session, enseigne_id: int):
    return db.query(Enseigne).get(enseigne_id)


def create_enseigne(db: Session, enseigne: Enseigne):
    db.add(enseigne)
    db.commit()
    db.refresh(enseigne)
    return enseigne


def update_enseigne(db: Session, enseigne: Enseigne, updated_enseigne: Enseigne):
    for attr, value in updated_enseigne.dict().items():
        setattr(enseigne, attr, value)
    db.commit()
    db.refresh(enseigne)
    return enseigne


def delete_enseigne(db: Session, enseigne: Enseigne):
    db.delete(enseigne)
    db.commit()
    return {"message": "Enseigne deleted"}
