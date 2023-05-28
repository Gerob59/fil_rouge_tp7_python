from fastapi import HTTPException
from ..models import Commande
from ..controllers import commande_controller
from config.db import open_session
from .router import get_router

router = get_router()
session = open_session()


@router.get("/{commande_id}")
def get_commande(commande_id: int):
    commande = commande_controller.get_commande(session, commande_id)
    if not commande:
        raise HTTPException(status_code=404, detail="Commande not found")
    return commande


@router.post("/")
def create_commande(commande: Commande):

    return commande_controller.create_commande(session, commande)


@router.put("/{commande_id}")
def update_commande(commande_id: int, updated_commande: Commande):
    commande = commande_controller.get_commande(session, commande_id)
    if not commande:
        raise HTTPException(status_code=404, detail="Commande not found")
    return commande_controller.update_commande(session, commande, updated_commande)


@router.delete("/{commande_id}")
def delete_commande(commande_id: int):
    commande = commande_controller.get_commande(session, commande_id)
    if not commande:
        raise HTTPException(status_code=404, detail="Commande not found")
    return commande_controller.delete_commande(session, commande)
