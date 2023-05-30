from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import ObjetCond
from ..schemas import ObjetCondSchema


def get_objet_cond(db: Session, objet_cond_id: int) -> ObjetCondSchema:
    with db:
        objet_cond_db = db.query(ObjetCond).get(objet_cond_id)
        if not objet_cond_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ObjetCond not found")
    return ObjetCondSchema.from_orm(objet_cond_db)


def get_all_objet_conds(db: Session) -> [ObjetCondSchema]:
    with db:
        resultat = db.query(ObjetCond).all()
    return resultat


def create_objet_cond(db: Session, objet_cond: ObjetCondSchema) -> ObjetCondSchema:
    with db:
        objet_cond_db = ObjetCond(**objet_cond.dict())
        db.add(objet_cond_db)
        db.commit()
        db.refresh(objet_cond_db)
    return ObjetCondSchema.from_orm(objet_cond_db)


def update_objet_cond(db: Session, objet_cond_id: int, updated_objet_cond: ObjetCondSchema) -> ObjetCondSchema:
    with db:
        objet_cond_db = db.query(ObjetCond).get(objet_cond_id)
        if not objet_cond_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ObjetCond not found")
        updated_data = updated_objet_cond.dict(exclude_unset=True)
        for attr, value in updated_data.items():
            setattr(objet_cond_db, attr, value)
        db.commit()
        db.refresh(objet_cond_db)
    return ObjetCondSchema.from_orm(objet_cond_db)


def delete_objet_cond(db: Session, objet_cond_id: int) -> dict:
    with db:
        objet_cond_db = db.query(ObjetCond).get(objet_cond_id)
        if not objet_cond_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ObjetCond not found")
        db.delete(objet_cond_db)
        db.commit()
    return {"message": "ObjetCond deleted"}
