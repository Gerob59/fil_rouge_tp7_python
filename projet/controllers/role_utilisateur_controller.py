from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import RoleUtilisateur
from ..schemas import RoleUtilisateurSchema


def get_role_utilisateur(db: Session, role_utilisateur_id: int):
    role_utilisateur = db.query(RoleUtilisateur).get(role_utilisateur_id)
    if not role_utilisateur:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="RoleUtilisateur not found")
    return role_utilisateur


def get_all_role_utilisateurs(db: Session):
    return db.query(RoleUtilisateur).all()


def create_role_utilisateur(db: Session, role_utilisateur: RoleUtilisateurSchema):
    db.add(role_utilisateur)
    db.commit()
    db.refresh(role_utilisateur)
    return role_utilisateur


def update_role_utilisateur(db: Session, role_utilisateur_id: int, updated_role_utilisateur: RoleUtilisateurSchema):
    role_utilisateur = db.query(RoleUtilisateur).get(role_utilisateur_id)
    if not role_utilisateur:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="RoleUtilisateur not found")
    updated_data = updated_role_utilisateur.dict(exclude_unset=True)
    for attr, value in updated_data.items():
        setattr(role_utilisateur, attr, value)
    db.commit()
    db.refresh(role_utilisateur)
    return role_utilisateur


def delete_role_utilisateur(db: Session, role_utilisateur_id: int):
    role_utilisateur = db.query(RoleUtilisateur).get(role_utilisateur_id)
    if not role_utilisateur:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="RoleUtilisateur not found")
    db.delete(role_utilisateur)
    db.commit()
    return {"message": "RoleUtilisateur deleted"}
