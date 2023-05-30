from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..schemas import CommandeSchema
from ..controllers import commande_controller
from config.db import get_db

router = APIRouter()


@router.get("/{commande_id}", response_model=CommandeSchema)
def get_commande(commande_id: int, db: Session = Depends(get_db)):
    commande = commande_controller.get_commande(db, commande_id)
    if not commande:
        raise HTTPException(status_code=404, detail="Commande not found")
    return commande


@router.get("/", response_model=list[CommandeSchema])
def get_all_commandes(db: Session = Depends(get_db)):
    return commande_controller.get_all_commandes(db)


@router.post("/", response_model=CommandeSchema)
def create_commande(commande: CommandeSchema, db: Session = Depends(get_db)):
    return commande_controller.create_commande(db, commande)


@router.put("/{commande_id}", response_model=CommandeSchema)
def update_commande(commande_id: int, updated_commande: CommandeSchema, db: Session = Depends(get_db)):
    commande = commande_controller.get_commande(db, commande_id)
    if not commande:
        raise HTTPException(status_code=404, detail="Commande not found")
    return commande_controller.update_commande(db, commande, updated_commande)


@router.patch("/{commande_id}", response_model=CommandeSchema)
def update_commande(commande_id: int, updated_commande: CommandeSchema, db: Session = Depends(get_db)):
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
