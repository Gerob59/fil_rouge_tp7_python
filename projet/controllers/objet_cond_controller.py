from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import ObjetCond


def get_objet_cond(db: Session, objet_cond_id: int):
    objet_cond = db.query(ObjetCond).get(objet_cond_id)
    if not objet_cond:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ObjetCond not found")
    return objet_cond


def get_all_objet_cond(db: Session):
    return db.query(ObjetCond).all()


def create_objet_cond(db: Session, objet_cond: ObjetCond):
    db.add(objet_cond)
    db.commit()
    db.refresh(objet_cond)
    return objet_cond


def update_objet_cond(db: Session, objet_cond_id: ObjetCond, updated_objet_cond: ObjetCond):
    objet_cond = db.query(ObjetCond).get(objet_cond_id)
    if not objet_cond:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ObjetCond not found")
    updated_data = updated_objet_cond.dict(exclude_unset=True)
    for attr, value in updated_data.items():
        setattr(objet_cond, attr, value)
    db.commit()
    db.refresh(objet_cond)
    return objet_cond


def delete_objet_cond(db: Session, objet_cond_id: int):
    objet_cond = db.query(ObjetCond).get(objet_cond_id)
    if not objet_cond:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ObjetCond not found")
    db.delete(objet_cond)
    db.commit()
    return {"message": "ObjetCond deleted"}
