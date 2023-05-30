from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import Commune
from ..schemas import CommuneSchema

def get_commune(db: Session, commune_id: int) -> CommuneSchema:
    with db:
        commune_db = db.query(Commune).get(commune_id)
        if not commune_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Commune not found")
    return CommuneSchema.from_orm(commune_db)


def get_all_communes(db: Session) -> [CommuneSchema]:
    with db:
        resultat = db.query(Commune).all()
    return resultat


def create_commune(db: Session, commune: CommuneSchema) -> CommuneSchema:
    with db:
        commune_db = Commune(**commune.dict())
        db.add(commune_db)
        db.commit()
        db.refresh(commune_db)
    return CommuneSchema.from_orm(commune_db)


def update_commune(db: Session, commune_id: int, updated_commune: CommuneSchema) -> CommuneSchema:
    with db:
        commune_db = db.query(Commune).get(commune_id)
        if not commune_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Commune not found")
        updated_data = updated_commune.dict(exclude_unset=True)
        for attr, value in updated_data.items():
            setattr(commune_db, attr, value)
        db.commit()
        db.refresh(commune_db)
    return CommuneSchema.from_orm(commune_db)


def delete_commune(db: Session, commune_id: int) -> dict:
    with db:
        commune_db = db.query(Commune).get(commune_id)
        if not commune_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Commune not found")
        db.delete(commune_db)
        db.commit()
    return {"message": "Commune deleted"}

