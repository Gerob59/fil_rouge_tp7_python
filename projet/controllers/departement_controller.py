from sqlalchemy.orm import Session
from ..models import Departement


def get_departement(db: Session, code_dept: str):
    return db.query(Departement).get(code_dept)


def create_departement(db: Session, departement: Departement):
    db.add(departement)
    db.commit()
    db.refresh(departement)
    return departement


def update_departement(db: Session, departement: Departement, updated_departement: Departement):
    for attr, value in updated_departement.dict().items():
        setattr(departement, attr, value)
    db.commit()
    db.refresh(departement)
    return departement


def delete_departement(db: Session, departement: Departement):
    db.delete(departement)
    db.commit()
    return {"message": "Departement deleted"}
