from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas import DepartementSchema
from ..controllers import departement_controller
from config import get_db

router = APIRouter()


@router.get("/{code_dept}", response_model=DepartementSchema)
def get_departement(code_dept: str, db: Session = Depends(get_db)):
    return departement_controller.get_departement(db, code_dept)


@router.get("/", response_model=list[DepartementSchema])
def get_all_departements(db: Session = Depends(get_db)):
    return departement_controller.get_all_departements(db)


@router.post("/", response_model=DepartementSchema)
def create_departement(departement: DepartementSchema, db: Session = Depends(get_db)):
    return departement_controller.create_departement(db, departement)


@router.put("/{code_dept}", response_model=DepartementSchema)
def update_departement(code_dept: str, updated_departement: DepartementSchema, db: Session = Depends(get_db)):
    return departement_controller.update_departement(db, code_dept, updated_departement)


@router.patch("/{code_dept}", response_model=DepartementSchema)
def update_departement(code_dept: str, updated_departement: DepartementSchema, db: Session = Depends(get_db)):
    return departement_controller.update_departement(db, code_dept, updated_departement)


@router.delete("/{code_dept}", response_model=dict)
def delete_departement(code_dept: str, db: Session = Depends(get_db)):
    return departement_controller.delete_departement(db, code_dept)
