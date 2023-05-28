from fastapi import HTTPException
from ..models import Objet
from ..controllers import objet_controller
from config.db import open_session
from .router import get_router

router = get_router()
session = open_session()


@router.get("/{objet_id}")
def get_objet(objet_id: int):
    objet = objet_controller.get_objet(session, objet_id)
    if not objet:
        raise HTTPException(status_code=404, detail="Objet not found")
    return objet


@router.post("/")
def create_objet(objet: Objet):
    return objet_controller.create_objet(session, objet)


@router.put("/{objet_id}")
def update_objet(objet_id: int, updated_objet: Objet):
    objet = objet_controller.get_objet(session, objet_id)
    if not objet:
        raise HTTPException(status_code=404, detail="Objet not found")
    return objet_controller.update_objet(session, objet, updated_objet)


@router.patch("/{objet_id}")
def update_objet(objet_id: int, updated_objet: Objet):
    objet = objet_controller.get_objet(session, objet_id)
    if not objet:
        raise HTTPException(status_code=404, detail="Objet not found")
    return objet_controller.update_objet(session, objet, updated_objet)


@router.delete("/{objet_id}")
def delete_objet(objet_id: int):
    objet = objet_controller.get_objet(session, objet_id)
    if not objet:
        raise HTTPException(status_code=404, detail="Objet not found")
    return objet_controller.delete_objet(session, objet)
