from fastapi import HTTPException
from ..models import Conditionnement
from ..controllers import conditionnement_controller
from config.db import open_session
from .router import get_router

router = get_router()
session = open_session()


@router.get("/{conditionnement_id}")
def get_conditionnement(conditionnement_id: int):
    conditionnement = conditionnement_controller.get_conditionnement(session, conditionnement_id)
    if not conditionnement:
        raise HTTPException(status_code=404, detail="Conditionnement not found")
    return conditionnement


@router.post("/")
def create_conditionnement(conditionnement: Conditionnement):
    return conditionnement_controller.create_conditionnement(session, conditionnement)


@router.put("/{conditionnement_id}")
def update_conditionnement(conditionnement_id: int, updated_conditionnement: Conditionnement):
    conditionnement = conditionnement_controller.get_conditionnement(session, conditionnement_id)
    if not conditionnement:
        raise HTTPException(status_code=404, detail="Conditionnement not found")
    return conditionnement_controller.update_conditionnement(session, conditionnement, updated_conditionnement)


@router.patch("/{conditionnement_id}")
def update_conditionnement(conditionnement_id: int, updated_conditionnement: Conditionnement):
    conditionnement = conditionnement_controller.get_conditionnement(session, conditionnement_id)
    if not conditionnement:
        raise HTTPException(status_code=404, detail="Conditionnement not found")
    return conditionnement_controller.update_conditionnement(session, conditionnement, updated_conditionnement)


@router.delete("/{conditionnement_id}")
def delete_conditionnement(conditionnement_id: int):
    conditionnement = conditionnement_controller.get_conditionnement(session, conditionnement_id)
    if not conditionnement:
        raise HTTPException(status_code=404, detail="Conditionnement not found")
    return conditionnement_controller.delete_conditionnement(session, conditionnement)
