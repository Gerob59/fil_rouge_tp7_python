from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas import UtilisateurSchema
from ..controllers import utilisateur_controller
from config.db import get_db

router = APIRouter()


@router.get("/{utilisateur_id}", response_model=UtilisateurSchema)
def get_utilisateur(utilisateur_id: int, db: Session = Depends(get_db)):
    utilisateur = utilisateur_controller.get_utilisateur(db, utilisateur_id)
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur not found")
    return utilisateur


@router.get("/", response_model=list[UtilisateurSchema])
def get_all_utilisateurs(db: Session = Depends(get_db)):
    return utilisateur_controller.get_all_utilisateurs(db)


@router.post("/", response_model=UtilisateurSchema)
def create_utilisateur(utilisateur: UtilisateurSchema, db: Session = Depends(get_db)):
    return utilisateur_controller.create_utilisateur(db, utilisateur)


@router.put("/{utilisateur_id}", response_model=UtilisateurSchema)
def update_utilisateur(utilisateur_id: int, updated_utilisateur: UtilisateurSchema, db: Session = Depends(get_db)):
    utilisateur = utilisateur_controller.get_utilisateur(db, utilisateur_id)
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur not found")
    return utilisateur_controller.update_utilisateur(db, utilisateur, updated_utilisateur)


@router.patch("/{utilisateur_id}", response_model=UtilisateurSchema)
def update_utilisateur(utilisateur_id: int, updated_utilisateur: UtilisateurSchema, db: Session = Depends(get_db)):
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
