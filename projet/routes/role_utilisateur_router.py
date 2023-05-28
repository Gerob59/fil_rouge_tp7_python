from fastapi import HTTPException
from ..models import RoleUtilisateur
from ..controllers import role_utilisateur_controller
from config.db import open_session
from .router import get_router

router = get_router()
session = open_session()


@router.get("/{role_utilisateur_id}")
def get_role_utilisateur(role_utilisateur_id: int):
    role_utilisateur = role_utilisateur_controller.get_role_utilisateur(session, role_utilisateur_id)
    if not role_utilisateur:
        raise HTTPException(status_code=404, detail="RoleUtilisateur not found")
    return role_utilisateur


@router.post("/")
def create_role_utilisateur(role_utilisateur: RoleUtilisateur):
    return role_utilisateur_controller.create_role_utilisateur(session, role_utilisateur)


@router.put("/{role_utilisateur_id}")
def update_role_utilisateur(role_utilisateur_id: int, updated_role_utilisateur: RoleUtilisateur):
    role_utilisateur = role_utilisateur_controller.get_role_utilisateur(session, role_utilisateur_id)
    if not role_utilisateur:
        raise HTTPException(status_code=404, detail="RoleUtilisateur not found")
    return role_utilisateur_controller.update_role_utilisateur(session, role_utilisateur, updated_role_utilisateur)


@router.patch("/{role_utilisateur_id}")
def update_role_utilisateur(role_utilisateur_id: int, updated_role_utilisateur: RoleUtilisateur):
    role_utilisateur = role_utilisateur_controller.get_role_utilisateur(session, role_utilisateur_id)
    if not role_utilisateur:
        raise HTTPException(status_code=404, detail="RoleUtilisateur not found")
    return role_utilisateur_controller.update_role_utilisateur(session, role_utilisateur, updated_role_utilisateur)


@router.delete("/{role_utilisateur_id}")
def delete_role_utilisateur(role_utilisateur_id: int):
    role_utilisateur = role_utilisateur_controller.get_role_utilisateur(session, role_utilisateur_id)
    if not role_utilisateur:
        raise HTTPException(status_code=404, detail="RoleUtilisateur not found")
    return role_utilisateur_controller.delete_role_utilisateur(session, role_utilisateur)
