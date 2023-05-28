from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import Commune
from ..controllers import commune_controller
from config.db import get_db

router = APIRouter()


@router.get("/{commune_id}", response_model=Commune)
def get_commune(commune_id: int, db: Session = Depends(get_db)):
    commune = commune_controller.get_commune(db, commune_id)
    if not commune:
        raise HTTPException(status_code=404, detail="Commune not found")
    return commune


@router.get("/", response_model=list[Commune])
def get_all_communes(db: Session = Depends(get_db)):
    return commune_controller.get_all_communes(db)


@router.post("/", response_model=Commune)
def create_commune(commune: Commune, db: Session = Depends(get_db)):
    return commune_controller.create_commune(db, commune)


@router.put("/{commune_id}", response_model=Commune)
def update_commune(commune_id: int, updated_commune: Commune, db: Session = Depends(get_db)):
    commune = commune_controller.get_commune(db, commune_id)
    if not commune:
        raise HTTPException(status_code=404, detail="Commune not found")
    return commune_controller.update_commune(db, commune, updated_commune)


@router.patch("/{commune_id}", response_model=Commune)
def update_commune(commune_id: int, updated_commune: Commune, db: Session = Depends(get_db)):
    commune = commune_controller.get_commune(db, commune_id)
    if not commune:
        raise HTTPException(status_code=404, detail="Commune not found")
    return commune_controller.update_commune(db, commune, updated_commune)


@router.delete("/{commune_id}", response_model=dict)
def delete_commune(commune_id: int, db: Session = Depends(get_db)):
    commune = commune_controller.get_commune(db, commune_id)
    if not commune:
        raise HTTPException(status_code=404, detail="Commune not found")
    return commune_controller.delete_commune(db, commune)
