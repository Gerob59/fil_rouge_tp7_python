from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import commande_controller
from ..schemas import CommandeSchema
from config import get_db

router = APIRouter()


@router.get("/{commande_id}", response_model=CommandeSchema)
def get_commande(commande_id: int, db: Session = Depends(get_db)):
    return commande_controller.get_commande(db, commande_id)


@router.get("/", response_model=list[CommandeSchema])
def get_all_commandes(db: Session = Depends(get_db)):
    return commande_controller.get_all_commandes(db)


@router.post("/", response_model=CommandeSchema)
def create_commande(commande: CommandeSchema, db: Session = Depends(get_db)):
    return commande_controller.create_commande(db, commande)


@router.put("/{commande_id}", response_model=CommandeSchema)
def update_commande(commande_id: int, updated_commande: CommandeSchema, db: Session = Depends(get_db)):
    return commande_controller.update_commande(db, commande_id, updated_commande)


@router.patch("/{commande_id}", response_model=CommandeSchema)
def patch_commande(commande_id: int, updated_commande: CommandeSchema, db: Session = Depends(get_db)):
    return commande_controller.update_commande(db, commande_id, updated_commande)


@router.delete("/{commande_id}", response_model=dict)
def delete_commande(commande_id: int, db: Session = Depends(get_db)):
    return commande_controller.delete_commande(db, commande_id)
