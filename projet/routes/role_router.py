from fastapi import HTTPException
from ..models import Role
from ..controllers import role_controller
from config.db import open_session
from .router import get_router

router = get_router()
session = open_session()


@router.get("/{role_id}")
def get_role(role_id: int):
    role = role_controller.get_role(session, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role


@router.post("/")
def create_role(role: Role):
    return role_controller.create_role(session, role)


@router.put("/{role_id}")
def update_role(role_id: int, updated_role: Role):
    role = role_controller.get_role(session, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role_controller.update_role(session, role, updated_role)


@router.patch("/{role_id}")
def update_role(role_id: int, updated_role: Role):
    role = role_controller.get_role(session, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role_controller.update_role(session, role, updated_role)


@router.delete("/{role_id}")
def delete_role(role_id: int):
    role = role_controller.get_role(session, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role_controller.delete_role(session, role)
