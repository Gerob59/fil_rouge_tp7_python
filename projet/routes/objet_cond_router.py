from fastapi import HTTPException
from ..models import ObjetCond
from ..controllers import objet_cond_controller
from config.db import open_session
from .router import get_router

router = get_router()
session = open_session()


@router.get("/{objet_cond_id}")
def get_objet_cond(objet_cond_id: int):
    objet_cond = objet_cond_controller.get_objet_cond(session, objet_cond_id)
    if not objet_cond:
        raise HTTPException(status_code=404, detail="ObjetCond not found")
    return objet_cond


@router.post("/")
def create_objet_cond(objet_cond: ObjetCond):
    return objet_cond_controller.create_objet_cond(session, objet_cond)


@router.put("/{objet_cond_id}")
def update_objet_cond(objet_cond_id: int, updated_objet_cond: ObjetCond):
    objet_cond = objet_cond_controller.get_objet_cond(session, objet_cond_id)
    if not objet_cond:
        raise HTTPException(status_code=404, detail="ObjetCond not found")
    return objet_cond_controller.update_objet_cond(session, objet_cond, updated_objet_cond)


@router.patch("/{objet_cond_id}")
def update_objet_cond(objet_cond_id: int, updated_objet_cond: ObjetCond):
    objet_cond = objet_cond_controller.get_objet_cond(session, objet_cond_id)
    if not objet_cond:
        raise HTTPException(status_code=404, detail="ObjetCond not found")
    return objet_cond_controller.update_objet_cond(session, objet_cond, updated_objet_cond)


@router.delete("/{objet_cond_id}")
def delete_objet_cond(objet_cond_id: int):
    objet_cond = objet_cond_controller.get_objet_cond(session, objet_cond_id)
    if not objet_cond:
        raise HTTPException(status_code=404, detail="ObjetCond not found")
    return objet_cond_controller.delete_objet_cond(session, objet_cond)
