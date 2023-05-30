from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import DetailObjet
from ..schemas import DetailObjetSchema


def get_detail_objet(db: Session, detail_objet_id: int) -> DetailObjetSchema:
    with db:
        detail_objet_db = db.query(DetailObjet).get(detail_objet_id)
        if not detail_objet_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="DetailObjet not found")
    return DetailObjetSchema.from_orm(detail_objet_db)


def get_all_detail_objets(db: Session) -> [DetailObjetSchema]:
    with db:
        resultat = db.query(DetailObjet).all()
    return resultat


def create_detail_objet(db: Session, detail_objet: DetailObjetSchema) -> DetailObjetSchema:
    with db:
        detail_objet_db = DetailObjet(**detail_objet.dict())
        db.add(detail_objet_db)
        db.commit()
        db.refresh(detail_objet_db)
    return DetailObjetSchema.from_orm(detail_objet_db)


def update_detail_objet(db: Session, detail_objet_id: int, updated_detail_objet: DetailObjetSchema) -> DetailObjetSchema:
    with db:
        detail_objet_db = db.query(DetailObjet).get(detail_objet_id)
        if not detail_objet_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="DetailObjet not found")
        updated_data = updated_detail_objet.dict(exclude_unset=True)
        for attr, value in updated_data.items():
            setattr(detail_objet_db, attr, value)
        db.commit()
        db.refresh(detail_objet_db)
    return DetailObjetSchema.from_orm(detail_objet_db)


def delete_detail_objet(db: Session, detail_objet_id: int) -> dict:
    with db:
        detail_objet_db = db.query(DetailObjet).get(detail_objet_id)
        if not detail_objet_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="DetailObjet not found")
        db.delete(detail_objet_db)
        db.commit()
    return {"message": "DetailObjet deleted"}
