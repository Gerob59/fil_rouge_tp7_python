from fastapi import HTTPException
from ..models import Departement
from ..controllers import departement_controller
from config.db import open_session
from .router import get_router

router = get_router()
session = open_session()


@router.get("/{code_dept}")
def get_departement(code_dept: str):
    departement = departement_controller.get_departement(session, code_dept)
    if not departement:
        raise HTTPException(status_code=404, detail="Departement not found")
    return departement


@router.post("/")
def create_departement(departement: Departement):
    return departement_controller.create_departement(session, departement)


@router.put("/{code_dept}")
def update_departement(code_dept: str, updated_departement: Departement):
    departement = departement_controller.get_departement(session, code_dept)
    if not departement:
        raise HTTPException(status_code=404, detail="Departement not found")
    return departement_controller.update_departement(session, departement, updated_departement)


@router.delete("/{code_dept}")
def delete_departement(code_dept: str):
    departement = departement_controller.get_departement(session, code_dept)
    if not departement:
        raise HTTPException(status_code=404, detail="Departement not found")
    return departement_controller.delete_departement(session, departement)
