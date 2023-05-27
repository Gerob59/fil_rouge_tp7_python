from sqlalchemy.orm import Session
from ..models import RoleUtilisateur


def get_role_utilisateur(db: Session, role_utilisateur_id: int):
    return db.query(RoleUtilisateur).get(role_utilisateur_id)


def create_role_utilisateur(db: Session, role_utilisateur: RoleUtilisateur):
    db.add(role_utilisateur)
    db.commit()
    db.refresh(role_utilisateur)
    return role_utilisateur


def update_role_utilisateur(db: Session, role_utilisateur: RoleUtilisateur, updated_role_utilisateur: RoleUtilisateur):
    for attr, value in updated_role_utilisateur.dict().items():
        setattr(role_utilisateur, attr, value)
    db.commit()
    db.refresh(role_utilisateur)
    return role_utilisateur


def delete_role_utilisateur(db: Session, role_utilisateur: RoleUtilisateur):
    db.delete(role_utilisateur)
    db.commit()
    return {"message": "RoleUtilisateur deleted"}
