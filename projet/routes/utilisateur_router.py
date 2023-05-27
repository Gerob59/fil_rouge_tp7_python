from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..models import Utilisateur
from ..controllers import utilisateur_controller
from config.sqlalchemy import bind_engine
from .router import get_router

router = get_router()


@router.get("/{utilisateur_id}")
def get_utilisateur(utilisateur_id: int, db: Session = bind_engine()):
    utilisateur = utilisateur_controller.get_utilisateur(db, utilisateur_id)
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur not found")
    return utilisateur


@router.post("/")
def create_utilisateur(utilisateur: Utilisateur, db: Session = bind_engine()):
    return utilisateur_controller.create_utilisateur(db, utilisateur)


@router.put("/{utilisateur_id}")
def update_utilisateur(utilisateur_id: int, updated_utilisateur: Utilisateur, db: Session = bind_engine()):
    utilisateur = utilisateur_controller.get_utilisateur(db, utilisateur_id)
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur not found")
    return utilisateur_controller.update_utilisateur(db, utilisateur, updated_utilisateur)


@router.delete("/{utilisateur_id}")
def delete_utilisateur(utilisateur_id: int, db: Session = bind_engine()):
    utilisateur = utilisateur_controller.get_utilisateur(db, utilisateur_id)
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur not found")
    return utilisateur_controller.delete_utilisateur(db, utilisateur)
