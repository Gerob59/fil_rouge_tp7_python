from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import Objet
from ..schemas import ObjetSchema


def get_objet(db: Session, objet_id: int) -> ObjetSchema:
    with db:
        objet_db = db.query(Objet).get(objet_id)
        if not objet_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Objet not found")
    return ObjetSchema.from_orm(objet_db)


def get_all_objets(db: Session) -> [ObjetSchema]:
    with db:
        res_db = db.query(Objet).all()
        res = []
        for obj in res_db:
            res.append(ObjetSchema.from_orm(obj))
    return res


def create_objet(db: Session, objet: ObjetSchema) -> ObjetSchema:
    with db:
        objet_db = Objet(**objet.dict())
        db.add(objet_db)
        db.commit()
        db.refresh(objet_db)
    return ObjetSchema.from_orm(objet_db)


def update_objet(db: Session, objet_id: int, updated_objet: ObjetSchema) -> ObjetSchema:
    with db:
        objet_db = db.query(Objet).get(objet_id)
        if not objet_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Objet not found")
        updated_data = updated_objet.dict(exclude_unset=True)
        for attr, value in updated_data.items():
            setattr(objet_db, attr, value)
        db.commit()
        db.refresh(objet_db)
    return ObjetSchema.from_orm(objet_db)


def delete_objet(db: Session, objet_id: int) -> dict:
    with db:
        objet_db = db.query(Objet).get(objet_id)
        if not objet_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Objet not found")
        db.delete(objet_db)
        db.commit()
    return {"message": "Objet deleted"}
