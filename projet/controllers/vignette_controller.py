from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import Vignette
from ..schemas import VignetteSchema


def get_vignette(db: Session, vignette_id: int) -> VignetteSchema:
    with db:
        vignette_db = db.query(Vignette).get(vignette_id)
        if not vignette_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vignette not found")
    return VignetteSchema.from_orm(vignette_db)


def get_all_vignettes(db: Session) -> [VignetteSchema]:
    with db:
        resultat = db.query(Vignette).all()
    return resultat


def create_vignette(db: Session, vignette: VignetteSchema) -> VignetteSchema:
    with db:
        vignette_db = Vignette(**vignette.dict())
        db.add(vignette_db)
        db.commit()
        db.refresh(vignette_db)
    return VignetteSchema.from_orm(vignette_db)


def update_vignette(db: Session, vignette_id: int, updated_vignette: VignetteSchema) -> VignetteSchema:
    with db:
        vignette_db = db.query(Vignette).get(vignette_id)
        if not vignette_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vignette not found")
        updated_data = updated_vignette.dict(exclude_unset=True)
        for attr, value in updated_data.items():
            setattr(vignette_db, attr, value)
        db.commit()
        db.refresh(vignette_db)
    return VignetteSchema.from_orm(vignette_db)


def delete_vignette(db: Session, vignette_id: int) -> dict:
    with db:
        vignette_db = db.query(Vignette).get(vignette_id)
        if not vignette_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vignette not found")
        db.delete(vignette_db)
        db.commit()
    return {"message": "Vignette deleted"}
