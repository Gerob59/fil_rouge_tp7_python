from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import DetailObjet
from ..schemas import DetailObjetSchema


def get_detail_objet(db: Session, detail_objet_id: int):
    detail_objet = db.query(DetailObjet).get(detail_objet_id)
    if not detail_objet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="DetailObjet not found")
    return detail_objet


def get_all_detail_objets(db: Session):
    return db.query(DetailObjet).all()


def create_detail_objet(db: Session, detail_objet: DetailObjetSchema):
    db.add(detail_objet)
    db.commit()
    db.refresh(detail_objet)
    return detail_objet


def update_detail_objet(db: Session, detail_objet_id: int, updated_detail_objet: DetailObjetSchema):
    detail_objet = db.query(DetailObjet).get(detail_objet_id)
    if not detail_objet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="DetailObjet not found")
    updated_data = updated_detail_objet.dict(exclude_unset=True)
    for attr, value in updated_data.items():
        setattr(detail_objet, attr, value)
    db.commit()
    db.refresh(detail_objet)
    return detail_objet


def delete_detail_objet(db: Session, detail_objet_id: int):
    detail_objet = db.query(DetailObjet).get(detail_objet_id)
    if not detail_objet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="DetailObjet not found")
    db.delete(detail_objet)
    db.commit()
    return {"message": "DetailObjet deleted"}
