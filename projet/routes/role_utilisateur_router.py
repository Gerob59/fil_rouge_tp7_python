from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas import RoleUtilisateurSchema
from ..controllers import role_utilisateur_controller
from config.db import get_db

router = APIRouter()


@router.get("/{role_utilisateur_id}", response_model=RoleUtilisateurSchema)
def get_role_utilisateur(role_utilisateur_id: int, db: Session = Depends(get_db)):
    role_utilisateur = role_utilisateur_controller.get_role_utilisateur(db, role_utilisateur_id)
    if not role_utilisateur:
        raise HTTPException(status_code=404, detail="RoleUtilisateur not found")
    return role_utilisateur


@router.get("/", response_model=list[RoleUtilisateurSchema])
def get_all_role_utilisateurs(db: Session = Depends(get_db)):
    return role_utilisateur_controller.get_all_role_utilisateurs(db)


@router.post("/", response_model=RoleUtilisateurSchema)
def create_role_utilisateur(role_utilisateur: RoleUtilisateurSchema, db: Session = Depends(get_db)):
    return role_utilisateur_controller.create_role_utilisateur(db, role_utilisateur)


@router.put("/{role_utilisateur_id}", response_model=RoleUtilisateurSchema)
def update_role_utilisateur(role_utilisateur_id: int, updated_role_utilisateur: RoleUtilisateurSchema, db: Session = Depends(get_db)):
    role_utilisateur = role_utilisateur_controller.get_role_utilisateur(db, role_utilisateur_id)
    if not role_utilisateur:
        raise HTTPException(status_code=404, detail="RoleUtilisateur not found")
    return role_utilisateur_controller.update_role_utilisateur(db, role_utilisateur, updated_role_utilisateur)


@router.patch("/{role_utilisateur_id}", response_model=RoleUtilisateurSchema)
def update_role_utilisateur(role_utilisateur_id: int, updated_role_utilisateur: RoleUtilisateurSchema, db: Session = Depends(get_db)):
    role_utilisateur = role_utilisateur_controller.get_role_utilisateur(db, role_utilisateur_id)
    if not role_utilisateur:
        raise HTTPException(status_code=404, detail="RoleUtilisateur not found")
    return role_utilisateur_controller.update_role_utilisateur(db, role_utilisateur, updated_role_utilisateur)


@router.delete("/{role_utilisateur_id}", response_model=dict)
def delete_role_utilisateur(role_utilisateur_id: int, db: Session = Depends(get_db)):
    role_utilisateur = role_utilisateur_controller.get_role_utilisateur(db, role_utilisateur_id)
    if not role_utilisateur:
        raise HTTPException(status_code=404, detail="RoleUtilisateur not found")
    return role_utilisateur_controller.delete_role_utilisateur(db, role_utilisateur)
