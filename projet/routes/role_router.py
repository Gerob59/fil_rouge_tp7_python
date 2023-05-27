from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..models import Role
from ..controllers import role_controller
from config.sqlalchemy import bind_engine
from .router import get_router

router = get_router()


@router.get("/{role_id}")
def get_role(role_id: int, db: Session = bind_engine()):
    role = role_controller.get_role(db, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role


@router.post("/")
def create_role(role: Role, db: Session = bind_engine()):
    return role_controller.create_role(db, role)


@router.put("/{role_id}")
def update_role(role_id: int, updated_role: Role, db: Session = bind_engine()):
    role = role_controller.get_role(db, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role_controller.update_role(db, role, updated_role)


@router.delete("/{role_id}")
def delete_role(role_id: int, db: Session = bind_engine()):
    role = role_controller.get_role(db, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role_controller.delete_role(db, role)
