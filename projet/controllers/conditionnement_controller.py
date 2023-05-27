from sqlalchemy.orm import Session
from ..models import Conditionnement


def get_conditionnement(db: Session, conditionnement_id: int):
    return db.query(Conditionnement).get(conditionnement_id)


def create_conditionnement(db: Session, conditionnement: Conditionnement):
    db.add(conditionnement)
    db.commit()
    db.refresh(conditionnement)
    return conditionnement


def update_conditionnement(db: Session, conditionnement: Conditionnement, updated_conditionnement: Conditionnement):
    for attr, value in updated_conditionnement.dict().items():
        setattr(conditionnement, attr, value)
    db.commit()
    db.refresh(conditionnement)
    return conditionnement


def delete_conditionnement(db: Session, conditionnement: Conditionnement):
    db.delete(conditionnement)
    db.commit()
    return {"message": "Conditionnement deleted"}
