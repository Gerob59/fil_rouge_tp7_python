from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import RoleUtilisateur
from ..schemas import RoleUtilisateurSchema


def get_role_utilisateur(db: Session, role_utilisateur_id: int) -> RoleUtilisateurSchema:
    with db:
        role_utilisateur_db = db.query(RoleUtilisateur).get(role_utilisateur_id)
        if not role_utilisateur_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="RoleUtilisateur not found")
    return RoleUtilisateurSchema.from_orm(role_utilisateur_db)


def get_all_role_utilisateurs(db: Session) -> [RoleUtilisateurSchema]:
    with db:
        resultat = db.query(RoleUtilisateur).all()
    return resultat


def create_role_utilisateur(db: Session, role_utilisateur: RoleUtilisateurSchema) -> RoleUtilisateurSchema:
    with db:
        role_utilisateur_db = RoleUtilisateur(**role_utilisateur.dict())
        db.add(role_utilisateur_db)
        db.commit()
        db.refresh(role_utilisateur_db)
    return RoleUtilisateurSchema.from_orm(role_utilisateur_db)


def update_role_utilisateur(db: Session, role_utilisateur_id: int, updated_role_utilisateur: RoleUtilisateurSchema) -> RoleUtilisateurSchema:
    with db:
        role_utilisateur_db = db.query(RoleUtilisateur).get(role_utilisateur_id)
        if not role_utilisateur_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="RoleUtilisateur not found")
        updated_data = updated_role_utilisateur.dict(exclude_unset=True)
        for attr, value in updated_data.items():
            setattr(role_utilisateur_db, attr, value)
        db.commit()
        db.refresh(role_utilisateur_db)
    return RoleUtilisateurSchema.from_orm(role_utilisateur_db)


def delete_role_utilisateur(db: Session, role_utilisateur_id: int) -> dict:
    with db:
        role_utilisateur_db = db.query(RoleUtilisateur).get(role_utilisateur_id)
        if not role_utilisateur_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="RoleUtilisateur not found")
        db.delete(role_utilisateur_db)
        db.commit()
    return {"message": "RoleUtilisateur deleted"}
