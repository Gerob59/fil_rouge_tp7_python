from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas import VignetteSchema
from ..controllers import vignette_controller
from config.db import get_db

router = APIRouter()


@router.get("/{vignette_id}", response_model=VignetteSchema)
def get_vignette(vignette_id: int, db: Session = Depends(get_db)):
    vignette = vignette_controller.get_vignette(db, vignette_id)
    if not vignette:
        raise HTTPException(status_code=404, detail="Vignette not found")
    return vignette


@router.get("/", response_model=list[VignetteSchema])
def get_all_vignettes(db: Session = Depends(get_db)):
    return vignette_controller.get_all_vignettes(db)


@router.post("/", response_model=VignetteSchema)
def create_vignette(vignette: VignetteSchema, db: Session = Depends(get_db)):
    return vignette_controller.create_vignette(db, vignette)


@router.put("/{vignette_id}", response_model=VignetteSchema)
def update_vignette(vignette_id: int, updated_vignette: VignetteSchema, db: Session = Depends(get_db)):
    vignette = vignette_controller.get_vignette(db, vignette_id)
    if not vignette:
        raise HTTPException(status_code=404, detail="Vignette not found")
    return vignette_controller.update_vignette(db, vignette, updated_vignette)


@router.patch("/{vignette_id}", response_model=VignetteSchema)
def update_vignette(vignette_id: int, updated_vignette: VignetteSchema, db: Session = Depends(get_db)):
    vignette = vignette_controller.get_vignette(db, vignette_id)
    if not vignette:
        raise HTTPException(status_code=404, detail="Vignette not found")
    return vignette_controller.update_vignette(db, vignette, updated_vignette)


@router.delete("/{vignette_id}", response_model=dict)
def delete_vignette(vignette_id: int, db: Session = Depends(get_db)):
    vignette = vignette_controller.get_vignette(db, vignette_id)
    if not vignette:
        raise HTTPException(status_code=404, detail="Vignette not found")
    return vignette_controller.delete_vignette(db, vignette)
