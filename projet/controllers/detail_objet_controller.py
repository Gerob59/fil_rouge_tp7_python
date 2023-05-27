from sqlalchemy.orm import Session
from ..models import DetailObjet


def get_detail_objet(db: Session, detail_objet_id: int):
    return db.query(DetailObjet).get(detail_objet_id)


def create_detail_objet(db: Session, detail_objet: DetailObjet):
    db.add(detail_objet)
    db.commit()
    db.refresh(detail_objet)
    return detail_objet


def update_detail_objet(db: Session, detail_objet: DetailObjet, updated_detail_objet: DetailObjet):
    for attr, value in updated_detail_objet.dict().items():
        setattr(detail_objet, attr, value)
    db.commit()
    db.refresh(detail_objet)
    return detail_objet


def delete_detail_objet(db: Session, detail_objet: DetailObjet):
    db.delete(detail_objet)
    db.commit()
    return {"message": "DetailObjet deleted"}
