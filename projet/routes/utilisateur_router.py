from fastapi import HTTPException
from ..models import Utilisateur
from ..controllers import utilisateur_controller
from config.db import open_session
from .router import get_router

router = get_router()
session = open_session()


@router.get("/{utilisateur_id}")
def get_utilisateur(utilisateur_id: int):
    utilisateur = utilisateur_controller.get_utilisateur(session, utilisateur_id)
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur not found")
    return utilisateur


@router.post("/")
def create_utilisateur(utilisateur: Utilisateur):
    return utilisateur_controller.create_utilisateur(session, utilisateur)


@router.put("/{utilisateur_id}")
def update_utilisateur(utilisateur_id: int, updated_utilisateur: Utilisateur):
    utilisateur = utilisateur_controller.get_utilisateur(session, utilisateur_id)
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur not found")
    return utilisateur_controller.update_utilisateur(session, utilisateur, updated_utilisateur)


@router.delete("/{utilisateur_id}")
def delete_utilisateur(utilisateur_id: int):
    utilisateur = utilisateur_controller.get_utilisateur(session, utilisateur_id)
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur not found")
    return utilisateur_controller.delete_utilisateur(session, utilisateur)
