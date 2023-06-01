from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import Poids
from ..schemas import PoidsSchema


def get_poids(db: Session, poids_id: int) -> PoidsSchema:
    with db:
        poids_db = db.query(Poids).get(poids_id)
        if not poids_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Poids not found")
    return PoidsSchema.from_orm(poids_db)


def get_all_poids(db: Session) -> [PoidsSchema]:
    with db:
        res_db = db.query(Poids).all()
        res = []
        for poids in res_db:
            res.append(PoidsSchema.from_orm(poids))
    return res


def create_poids(db: Session, poids: PoidsSchema) -> PoidsSchema:
    with db:
        poids_db = Poids(**poids.dict())
        db.add(poids_db)
        db.commit()
        db.refresh(poids_db)
    return PoidsSchema.from_orm(poids_db)


def update_poids(db: Session, poids_id: int, updated_poids: PoidsSchema) -> PoidsSchema:
    with db:
        poids_db = db.query(Poids).get(poids_id)
        if not poids_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Poids not found")
        updated_data = updated_poids.dict(exclude_unset=True)
        for attr, value in updated_data.items():
            setattr(poids_db, attr, value)
        db.commit()
        db.refresh(poids_db)
    return PoidsSchema.from_orm(poids_db)


def delete_poids(db: Session, poids_id: int) -> dict:
    with db:
        poids_db = db.query(Poids).get(poids_id)
        if not poids_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Poids not found")
        db.delete(poids_db)
        db.commit()
    return {"message": "Poids deleted"}
