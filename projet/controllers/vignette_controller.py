from sqlalchemy.orm import Session
from ..models import Vignette


def get_vignette(db: Session, vignette_id: int):
    return db.query(Vignette).get(vignette_id)


def create_vignette(db: Session, vignette: Vignette):
    db.add(vignette)
    db.commit()
    db.refresh(vignette)
    return vignette


def update_vignette(db: Session, vignette: Vignette, updated_vignette: Vignette):
    for attr, value in updated_vignette.dict().items():
        setattr(vignette, attr, value)
    db.commit()
    db.refresh(vignette)
    return vignette


def delete_vignette(db: Session, vignette: Vignette):
    db.delete(vignette)
    db.commit()
    return {"message": "Vignette deleted"}
