from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import Enseigne
from ..schemas import EnseigneSchema


def get_enseigne(db: Session, enseigne_id: int) -> EnseigneSchema:
    with db:
        enseigne_db = db.query(Enseigne).get(enseigne_id)
        if not enseigne_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Enseigne not found")
    return EnseigneSchema.from_orm(enseigne_db)


def get_all_enseignes(db: Session) -> [EnseigneSchema]:
    with db:
        res_db = db.query(Enseigne).all()
        res = []
        for enseigne in res_db:
            res.append(EnseigneSchema.from_orm(enseigne))
    return res


def create_enseigne(db: Session, enseigne: EnseigneSchema) -> EnseigneSchema:
    with db:
        enseigne_db = Enseigne(**enseigne.dict())
        db.add(enseigne_db)
        db.commit()
        db.refresh(enseigne_db)
    return EnseigneSchema.from_orm(enseigne_db)


def update_enseigne(db: Session, enseigne_id: int, updated_enseigne: EnseigneSchema) -> EnseigneSchema:
    with db:
        enseigne_db = db.query(Enseigne).get(enseigne_id)
        if not enseigne_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Enseigne not found")
        updated_data = updated_enseigne.dict(exclude_unset=True)
        for attr, value in updated_data.items():
            setattr(enseigne_db, attr, value)
        db.commit()
        db.refresh(enseigne_db)
    return EnseigneSchema.from_orm(enseigne_db)


def delete_enseigne(db: Session, enseigne_id: int) -> dict:
    with db:
        enseigne_db = db.query(Enseigne).get(enseigne_id)
        if not enseigne_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Enseigne not found")
        db.delete(enseigne_db)
        db.commit()
    return {"message": "Enseigne deleted"}
