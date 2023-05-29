from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import Conditionnement
from ..schemas import ConditionnementSchema


def get_conditionnement(db: Session, conditionnement_id: int):
    conditionnement = db.query(Conditionnement).get(conditionnement_id)
    if not conditionnement:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conditionnement not found")
    return conditionnement


def get_all_conditionnements(db: Session):
    return db.query(Conditionnement).all()


def create_conditionnement(db: Session, conditionnement: ConditionnementSchema):
    db.add(conditionnement)
    db.commit()
    db.refresh(conditionnement)
    return conditionnement


def update_conditionnement(db: Session, conditionnement_id: int, updated_conditionnement: ConditionnementSchema):
    conditionnement = db.query(Conditionnement).get(conditionnement_id)
    if not conditionnement:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conditionnement not found")
    updated_data = updated_conditionnement.dict(exclude_unset=True)
    for attr, value in updated_data.items():
        setattr(conditionnement, attr, value)
    db.commit()
    db.refresh(conditionnement)
    return conditionnement


def delete_conditionnement(db: Session, conditionnement_id: int):
    conditionnement = db.query(Conditionnement).get(conditionnement_id)
    if not conditionnement:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conditionnement not found")
    db.delete(conditionnement)
    db.commit()
    return {"message": "Conditionnement deleted"}
