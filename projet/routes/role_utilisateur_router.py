from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..models import RoleUtilisateur
from ..controllers import role_utilisateur_controller
from config.sqlalchemy import bind_engine
from .router import get_router

router = get_router()


@router.get("/{role_utilisateur_id}")
def get_role_utilisateur(role_utilisateur_id: int, db: Session = bind_engine()):
    role_utilisateur = role_utilisateur_controller.get_role_utilisateur(db, role_utilisateur_id)
    if not role_utilisateur:
        raise HTTPException(status_code=404, detail="RoleUtilisateur not found")
    return role_utilisateur


@router.post("/")
def create_role_utilisateur(role_utilisateur: RoleUtilisateur, db: Session = bind_engine()):
    return role_utilisateur_controller.create_role_utilisateur(db, role_utilisateur)


@router.put("/{role_utilisateur_id}")
def update_role_utilisateur(role_utilisateur_id: int, updated_role_utilisateur: RoleUtilisateur, db: Session = bind_engine()):
    role_utilisateur = role_utilisateur_controller.get_role_utilisateur(db, role_utilisateur_id)
    if not role_utilisateur:
        raise HTTPException(status_code=404, detail="RoleUtilisateur not found")
    return role_utilisateur_controller.update_role_utilisateur(db, role_utilisateur, updated_role_utilisateur)


@router.delete("/{role_utilisateur_id}")
def delete_role_utilisateur(role_utilisateur_id: int, db: Session = bind_engine()):
    role_utilisateur = role_utilisateur_controller.get_role_utilisateur(db, role_utilisateur_id)
    if not role_utilisateur:
        raise HTTPException(status_code=404, detail="RoleUtilisateur not found")
    return role_utilisateur_controller.delete_role_utilisateur(db, role_utilisateur)
