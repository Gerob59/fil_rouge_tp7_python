from fastapi import HTTPException
from ..models import Enseigne
from ..controllers import enseigne_controller
from config.db import open_session
from .router import get_router

router = get_router()
session = open_session()


@router.get("/{enseigne_id}")
def get_enseigne(enseigne_id: int):
    enseigne = enseigne_controller.get_enseigne(session, enseigne_id)
    if not enseigne:
        raise HTTPException(status_code=404, detail="Enseigne not found")
    return enseigne


@router.post("/")
def create_enseigne(enseigne: Enseigne):
    return enseigne_controller.create_enseigne(session, enseigne)


@router.put("/{enseigne_id}")
def update_enseigne(enseigne_id: int, updated_enseigne: Enseigne):
    enseigne = enseigne_controller.get_enseigne(session, enseigne_id)
    if not enseigne:
        raise HTTPException(status_code=404, detail="Enseigne not found")
    return enseigne_controller.update_enseigne(session, enseigne, updated_enseigne)


@router.patch("/{enseigne_id}")
def update_enseigne(enseigne_id: int, updated_enseigne: Enseigne):
    enseigne = enseigne_controller.get_enseigne(session, enseigne_id)
    if not enseigne:
        raise HTTPException(status_code=404, detail="Enseigne not found")
    return enseigne_controller.update_enseigne(session, enseigne, updated_enseigne)


@router.delete("/{enseigne_id}")
def delete_enseigne(enseigne_id: int):
    enseigne = enseigne_controller.get_enseigne(session, enseigne_id)
    if not enseigne:
        raise HTTPException(status_code=404, detail="Enseigne not found")
    return enseigne_controller.delete_enseigne(session, enseigne)
