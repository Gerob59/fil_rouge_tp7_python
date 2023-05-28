from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import Departement


def get_departement(db: Session, code_dept: str):
    departement = db.query(Departement).get(code_dept)
    if not departement:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Departement not found")
    return departement


def get_all_departements(db: Session):
    return db.query(Departement).all()


def create_departement(db: Session, departement: Departement):
    db.add(departement)
    db.commit()
    db.refresh(departement)
    return departement


def update_departement(db: Session, code_dept: Departement, updated_departement: Departement):
    departement = db.query(Departement).get(code_dept)
    if not departement:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Departement not found")
    updated_data = updated_departement.dict(exclude_unset=True)
    for attr, value in updated_data.items():
        setattr(departement, attr, value)
    db.commit()
    db.refresh(departement)
    return departement


def delete_departement(db: Session, code_dept: Departement):
    departement = db.query(Departement).get(code_dept)
    if not departement:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Departement not found")
    db.delete(departement)
    db.commit()
    return {"message": "Departement deleted"}
