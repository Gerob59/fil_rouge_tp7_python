from fastapi import HTTPException
from ..models import Vignette
from ..controllers import vignette_controller
from config.db import open_session
from .router import get_router

router = get_router()
session = open_session()


@router.get("/{vignette_id}")
def get_vignette(vignette_id: int):
    vignette = vignette_controller.get_vignette(session, vignette_id)
    if not vignette:
        raise HTTPException(status_code=404, detail="Vignette not found")
    return vignette


@router.post("/")
def create_vignette(vignette: Vignette):
    return vignette_controller.create_vignette(session, vignette)


@router.put("/{vignette_id}")
def update_vignette(vignette_id: int, updated_vignette: Vignette):
    vignette = vignette_controller.get_vignette(session, vignette_id)
    if not vignette:
        raise HTTPException(status_code=404, detail="Vignette not found")
    return vignette_controller.update_vignette(session, vignette, updated_vignette)


@router.patch("/{vignette_id}")
def update_vignette(vignette_id: int, updated_vignette: Vignette):
    vignette = vignette_controller.get_vignette(session, vignette_id)
    if not vignette:
        raise HTTPException(status_code=404, detail="Vignette not found")
    return vignette_controller.update_vignette(session, vignette, updated_vignette)


@router.delete("/{vignette_id}")
def delete_vignette(vignette_id: int):
    vignette = vignette_controller.get_vignette(session, vignette_id)
    if not vignette:
        raise HTTPException(status_code=404, detail="Vignette not found")
    return vignette_controller.delete_vignette(session, vignette)
