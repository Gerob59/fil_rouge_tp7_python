from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..models import Departement
from ..controllers import departement_controller
from config.sqlalchemy import bind_engine
from .router import get_router

router = get_router()


@router.get("/{code_dept}")
def get_departement(code_dept: str, db: Session = bind_engine()):
    departement = departement_controller.get_departement(db, code_dept)
    if not departement:
        raise HTTPException(status_code=404, detail="Departement not found")
    return departement


@router.post("/")
def create_departement(departement: Departement, db: Session = bind_engine()):
    return departement_controller.create_departement(db, departement)


@router.put("/{code_dept}")
def update_departement(code_dept: str, updated_departement: Departement, db: Session = bind_engine()):
    departement = departement_controller.get_departement(db, code_dept)
    if not departement:
        raise HTTPException(status_code=404, detail="Departement not found")
    return departement_controller.update_departement(db, departement, updated_departement)


@router.delete("/{code_dept}")
def delete_departement(code_dept: str, db: Session = bind_engine()):
    departement = departement_controller.get_departement(db, code_dept)
    if not departement:
        raise HTTPException(status_code=404, detail="Departement not found")
    return departement_controller.delete_departement(db, departement)
