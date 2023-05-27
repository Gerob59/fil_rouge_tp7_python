from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..models import Commande
from ..controllers import commande_controller
from config.sqlalchemy import bind_engine
from .router import get_router

router = get_router()


@router.get("/{commande_id}")
def get_commande(commande_id: int, db: Session = bind_engine()):
    commande = commande_controller.get_commande(db, commande_id)
    if not commande:
        raise HTTPException(status_code=404, detail="Commande not found")
    return commande


@router.post("/")
def create_commande(commande: Commande, db: Session = bind_engine()):
    return commande_controller.create_commande(db, commande)


@router.put("/{commande_id}")
def update_commande(commande_id: int, updated_commande: Commande, db: Session = bind_engine()):
    commande = commande_controller.get_commande(db, commande_id)
    if not commande:
        raise HTTPException(status_code=404, detail="Commande not found")
    return commande_controller.update_commande(db, commande, updated_commande)


@router.delete("/{commande_id}")
def delete_commande(commande_id: int, db: Session = bind_engine()):
    commande = commande_controller.get_commande(db, commande_id)
    if not commande:
        raise HTTPException(status_code=404, detail="Commande not found")
    return commande_controller.delete_commande(db, commande)
