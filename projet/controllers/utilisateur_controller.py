from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import Utilisateur
from ..schemas import UtilisateurSchema, UtilisateurBase
from ..utils import hashing


def get_utilisateur(db: Session, utilisateur_id: int) -> UtilisateurBase:
    with db:
        utilisateur_db = db.query(Utilisateur).get(utilisateur_id)
        if not utilisateur_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Utilisateur not found")
    return UtilisateurBase.from_orm(utilisateur_db)


def get_utilisateur_by_username(db: Session, username: str) -> UtilisateurBase:
    with db:
        utilisateur_db = db.query(Utilisateur).filter(Utilisateur.username == username)
        if not utilisateur_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Utilisateur not found")
    return UtilisateurBase.from_orm(utilisateur_db)


def get_all_utilisateurs(db: Session) -> [UtilisateurBase]:
    with db:
        res_db = db.query(Utilisateur).all()
        res = []
        for user in res_db:
            res.append(UtilisateurBase.from_orm(user))
    return res


def create_utilisateur(db: Session, utilisateur: UtilisateurSchema) -> UtilisateurBase:
    with db:
        # create an utilisateur
        utilisateur_db = Utilisateur(**utilisateur.dict())

        # hash the password
        hashed_password = hashing(utilisateur.password)

        # modify utilisateur password with the hashed one
        utilisateur_db.password = hashed_password

        db.add(utilisateur_db)
        db.commit()
        db.refresh(utilisateur_db)
    return UtilisateurBase.from_orm(utilisateur_db)


def update_utilisateur(db: Session, utilisateur_id: int, updated_utilisateur: UtilisateurSchema) -> UtilisateurSchema:
    with db:
        utilisateur_db = db.query(Utilisateur).get(utilisateur_id)
        if not utilisateur_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Utilisateur not found")
        updated_data = updated_utilisateur.dict(exclude_unset=True)
        for attr, value in updated_data.items():
            setattr(utilisateur_db, attr, value)
        db.commit()
        db.refresh(utilisateur_db)
    return UtilisateurSchema.from_orm(utilisateur_db)


def delete_utilisateur(db: Session, utilisateur_id: int) -> dict:
    with db:
        utilisateur_db = db.query(Utilisateur).get(utilisateur_id)
        if not utilisateur_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Utilisateur not found")
        db.delete(utilisateur_db)
        db.commit()
    return {"message": "Utilisateur deleted"}
