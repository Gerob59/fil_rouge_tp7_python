from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import vignette_controller
from ..schemas import VignetteSchema
from config import get_db

router = APIRouter()


@router.get("/{vignette_id}", response_model=VignetteSchema, status_code=200)
def get_vignette(vignette_id: int, db: Session = Depends(get_db)):
    return vignette_controller.get_vignette(db, vignette_id)


@router.get("/", response_model=list[VignetteSchema], status_code=200)
def get_all_vignettes(db: Session = Depends(get_db)):
    return vignette_controller.get_all_vignettes(db)


@router.post("/", response_model=VignetteSchema, status_code=201)
def create_vignette(vignette: VignetteSchema, db: Session = Depends(get_db)):
    return vignette_controller.create_vignette(db, vignette)


@router.put("/{vignette_id}", response_model=VignetteSchema, status_code=202)
def update_vignette(vignette_id: int, updated_vignette: VignetteSchema, db: Session = Depends(get_db)):
    return vignette_controller.update_vignette(db, vignette_id, updated_vignette)


@router.patch("/{vignette_id}", response_model=VignetteSchema, status_code=202)
def patch_vignette(vignette_id: int, updated_vignette: VignetteSchema, db: Session = Depends(get_db)):
    return vignette_controller.update_vignette(db, vignette_id, updated_vignette)


@router.delete("/{vignette_id}", response_model=dict, status_code=200)
def delete_vignette(vignette_id: int, db: Session = Depends(get_db)):
    return vignette_controller.delete_vignette(db, vignette_id)
