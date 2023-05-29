from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import Vignette
from ..schemas import VignetteSchema


def get_vignette(db: Session, vignette_id: int):
    vignette = db.query(Vignette).get(vignette_id)
    if not vignette:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vignette not found")
    return vignette


def get_all_vignettes(db: Session):
    return db.query(Vignette).all()


def create_vignette(db: Session, vignette: VignetteSchema):
    db.add(vignette)
    db.commit()
    db.refresh(vignette)
    return vignette


def update_vignette(db: Session, vignette_id: int, updated_vignette: VignetteSchema):
    vignette = db.query(Vignette).get(vignette_id)
    if not vignette:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vignette not found")
    updated_data = updated_vignette.dict(exclude_unset=True)
    for attr, value in updated_data.items():
        setattr(vignette, attr, value)
    db.commit()
    db.refresh(vignette)
    return vignette


def delete_vignette(db: Session, vignette_id: int):
    vignette = db.query(Vignette).get(vignette_id)
    if not vignette:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vignette not found")
    db.delete(vignette)
    db.commit()
    return {"message": "Vignette deleted"}
