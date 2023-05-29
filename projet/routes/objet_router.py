from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas import ObjetSchema
from ..controllers import objet_controller
from config.db import get_db

router = APIRouter()


@router.get("/{objet_id}", response_model=ObjetSchema)
def get_objet(objet_id: int, db: Session = Depends(get_db)):
    objet = objet_controller.get_objet(db, objet_id)
    if not objet:
        raise HTTPException(status_code=404, detail="Objet not found")
    return objet


@router.get("/", response_model=list[ObjetSchema])
def get_all_objets(db: Session = Depends(get_db)):
    return objet_controller.get_all_objets(db)


@router.post("/", response_model=ObjetSchema)
def create_objet(objet: ObjetSchema, db: Session = Depends(get_db)):
    return objet_controller.create_objet(db, objet)


@router.put("/{objet_id}", response_model=ObjetSchema)
def update_objet(objet_id: int, updated_objet: ObjetSchema, db: Session = Depends(get_db)):
    objet = objet_controller.get_objet(db, objet_id)
    if not objet:
        raise HTTPException(status_code=404, detail="Objet not found")
    return objet_controller.update_objet(db, objet, updated_objet)


@router.patch("/{objet_id}", response_model=ObjetSchema)
def update_objet(objet_id: int, updated_objet: ObjetSchema, db: Session = Depends(get_db)):
    objet = objet_controller.get_objet(db, objet_id)
    if not objet:
        raise HTTPException(status_code=404, detail="Objet not found")
    return objet_controller.update_objet(db, objet, updated_objet)


@router.delete("/{objet_id}", response_model=dict)
def delete_objet(objet_id: int, db: Session = Depends(get_db)):
    objet = objet_controller.get_objet(db, objet_id)
    if not objet:
        raise HTTPException(status_code=404, detail="Objet not found")
    return objet_controller.delete_objet(db, objet)
