from fastapi import HTTPException
from ..models import DetailObjet
from ..controllers import detail_objet_controller
from config.db import open_session
from .router import get_router

router = get_router()
session = open_session()


@router.get("/{detail_objet_id}")
def get_detail_objet(detail_objet_id: int):
    detail_objet = detail_objet_controller.get_detail_objet(session, detail_objet_id)
    if not detail_objet:
        raise HTTPException(status_code=404, detail="DetailObjet not found")
    return detail_objet


@router.post("/")
def create_detail_objet(detail_objet: DetailObjet):
    return detail_objet_controller.create_detail_objet(session, detail_objet)


@router.put("/{detail_objet_id}")
def update_detail_objet(detail_objet_id: int, updated_detail_objet: DetailObjet):
    detail_objet = detail_objet_controller.get_detail_objet(session, detail_objet_id)
    if not detail_objet:
        raise HTTPException(status_code=404, detail="DetailObjet not found")
    return detail_objet_controller.update_detail_objet(session, detail_objet, updated_detail_objet)


@router.patch("/{detail_objet_id}")
def update_detail_objet(detail_objet_id: int, updated_detail_objet: DetailObjet):
    detail_objet = detail_objet_controller.get_detail_objet(session, detail_objet_id)
    if not detail_objet:
        raise HTTPException(status_code=404, detail="DetailObjet not found")
    return detail_objet_controller.update_detail_objet(session, detail_objet, updated_detail_objet)


@router.delete("/{detail_objet_id}")
def delete_detail_objet(detail_objet_id: int):
    detail_objet = detail_objet_controller.get_detail_objet(session, detail_objet_id)
    if not detail_objet:
        raise HTTPException(status_code=404, detail="DetailObjet not found")
    return detail_objet_controller.delete_detail_objet(session, detail_objet)
