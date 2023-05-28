from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import Utilisateur
from ..controllers import utilisateur_controller
from config.db import get_db

router = APIRouter()


@router.get("/{utilisateur_id}", response_model=Utilisateur)
def get_utilisateur(utilisateur_id: int, db: Session = Depends(get_db)):
    utilisateur = utilisateur_controller.get_utilisateur(db, utilisateur_id)
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur not found")
    return utilisateur


@router.get("/", response_model=list[Utilisateur])
def get_all_utilisateurs(db: Session = Depends(get_db)):
    return utilisateur_controller.get_all_utilisateurs(db)


@router.post("/", response_model=Utilisateur)
def create_utilisateur(utilisateur: Utilisateur, db: Session = Depends(get_db)):
    return utilisateur_controller.create_utilisateur(db, utilisateur)


@router.put("/{utilisateur_id}", response_model=Utilisateur)
def update_utilisateur(utilisateur_id: int, updated_utilisateur: Utilisateur, db: Session = Depends(get_db)):
    utilisateur = utilisateur_controller.get_utilisateur(db, utilisateur_id)
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur not found")
    return utilisateur_controller.update_utilisateur(db, utilisateur, updated_utilisateur)


@router.patch("/{utilisateur_id}", response_model=Utilisateur)
def update_utilisateur(utilisateur_id: int, updated_utilisateur: Utilisateur, db: Session = Depends(get_db)):
    utilisateur = utilisateur_controller.get_utilisateur(db, utilisateur_id)
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur not found")
    return utilisateur_controller.update_utilisateur(db, utilisateur, updated_utilisateur)


@router.delete("/{utilisateur_id}", response_model=dict)
def delete_utilisateur(utilisateur_id: int, db: Session = Depends(get_db)):
    utilisateur = utilisateur_controller.get_utilisateur(db, utilisateur_id)
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur not found")
    return utilisateur_controller.delete_utilisateur(db, utilisateur)
