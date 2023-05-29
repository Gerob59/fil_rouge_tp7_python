from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas import RoleSchema
from ..controllers import role_controller
from config.db import get_db

router = APIRouter()


@router.get("/{role_id}", response_model=RoleSchema)
def get_role(role_id: int, db: Session = Depends(get_db)):
    role = role_controller.get_role(db, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role


@router.get("/", response_model=list[RoleSchema])
def get_all_roles(db: Session = Depends(get_db)):
    return role_controller.get_all_roles(db)


@router.post("/", response_model=RoleSchema)
def create_role(role: RoleSchema, db: Session = Depends(get_db)):
    return role_controller.create_role(db, role)


@router.put("/{role_id}", response_model=RoleSchema)
def update_role(role_id: int, updated_role: RoleSchema, db: Session = Depends(get_db)):
    role = role_controller.get_role(db, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role_controller.update_role(db, role, updated_role)


@router.patch("/{role_id}", response_model=RoleSchema)
def update_role(role_id: int, updated_role: RoleSchema, db: Session = Depends(get_db)):
    role = role_controller.get_role(db, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role_controller.update_role(db, role, updated_role)


@router.delete("/{role_id}", response_model=dict)
def delete_role(role_id: int, db: Session = Depends(get_db)):
    role = role_controller.get_role(db, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role_controller.delete_role(db, role)
