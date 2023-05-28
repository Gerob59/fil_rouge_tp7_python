from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..models import Commande
from ..controllers import commande_controller
from config.db import get_db

router = APIRouter()


@router.get("/{commande_id}", response_model=Commande)
def get_commande(commande_id: int, db: Session = Depends(get_db)):
    commande = commande_controller.get_commande(db, commande_id)
    if not commande:
        raise HTTPException(status_code=404, detail="Commande not found")
    return commande


@router.get("/", response_model=list[Commande])
def get_all_commandes(db: Session = Depends(get_db)):
    return commande_controller.get_all_commandes(db)


@router.post("/", response_model=Commande)
def create_commande(commande: Commande, db: Session = Depends(get_db)):
    return commande_controller.create_commande(db, commande)


@router.put("/{commande_id}", response_model=Commande)
def update_commande(commande_id: int, updated_commande: Commande, db: Session = Depends(get_db)):
    commande = commande_controller.get_commande(db, commande_id)
    if not commande:
        raise HTTPException(status_code=404, detail="Commande not found")
    return commande_controller.update_commande(db, commande, updated_commande)


@router.patch("/{commande_id}", response_model=Commande)
def update_commande(commande_id: int, updated_commande: Commande, db: Session = Depends(get_db)):
    commande = commande_controller.get_commande(db, commande_id)
    if not commande:
        raise HTTPException(status_code=404, detail="Commande not found")
    return commande_controller.update_commande(db, commande, updated_commande)


@router.delete("/{commande_id}", response_model=dict)
def delete_commande(commande_id: int, db: Session = Depends(get_db)):
    commande = commande_controller.get_commande(db, commande_id)
    if not commande:
        raise HTTPException(status_code=404, detail="Commande not found")
    return commande_controller.delete_commande(db, commande)
