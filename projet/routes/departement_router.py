from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import Departement
from ..controllers import departement_controller
from config.db import get_db

router = APIRouter()


@router.get("/{code_dept}", response_model=Departement)
def get_departement(code_dept: str, db: Session = Depends(get_db)):
    departement = departement_controller.get_departement(db, code_dept)
    if not departement:
        raise HTTPException(status_code=404, detail="Departement not found")
    return departement


@router.get("/", response_model=list[Departement])
def get_all_departements(db: Session = Depends(get_db)):
    return departement_controller.get_all_departements(db)


@router.post("/", response_model=Departement)
def create_departement(departement: Departement, db: Session = Depends(get_db)):
    return departement_controller.create_departement(db, departement)


@router.put("/{code_dept}", response_model=Departement)
def update_departement(code_dept: str, updated_departement: Departement, db: Session = Depends(get_db)):
    departement = departement_controller.get_departement(db, code_dept)
    if not departement:
        raise HTTPException(status_code=404, detail="Departement not found")
    return departement_controller.update_departement(db, departement, updated_departement)


@router.patch("/{code_dept}", response_model=Departement)
def update_departement(code_dept: str, updated_departement: Departement, db: Session = Depends(get_db)):
    departement = departement_controller.get_departement(db, code_dept)
    if not departement:
        raise HTTPException(status_code=404, detail="Departement not found")
    return departement_controller.update_departement(db, departement, updated_departement)


@router.delete("/{code_dept}", response_model=dict)
def delete_departement(code_dept: str, db: Session = Depends(get_db)):
    departement = departement_controller.get_departement(db, code_dept)
    if not departement:
        raise HTTPException(status_code=404, detail="Departement not found")
    return departement_controller.delete_departement(db, departement)
