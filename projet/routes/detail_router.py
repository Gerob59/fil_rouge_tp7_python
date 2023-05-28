from fastapi import HTTPException
from ..models import Detail
from ..controllers import detail_controller
from config.db import open_session
from .router import get_router

router = get_router()
session = open_session()


@router.get("/{detail_id}")
def get_detail(detail_id: int):
    detail = detail_controller.get_detail(session, detail_id)
    if not detail:
        raise HTTPException(status_code=404, detail="Detail not found")
    return detail


@router.post("/")
def create_detail(detail: Detail):
    return detail_controller.create_detail(session, detail)


@router.put("/{detail_id}")
def update_detail(detail_id: int, updated_detail: Detail):
    detail = detail_controller.get_detail(session, detail_id)
    if not detail:
        raise HTTPException(status_code=404, detail="Detail not found")
    return detail_controller.update_detail(session, detail, updated_detail)


@router.patch("/{detail_id}")
def update_detail(detail_id: int, updated_detail: Detail):
    detail = detail_controller.get_detail(session, detail_id)
    if not detail:
        raise HTTPException(status_code=404, detail="Detail not found")
    return detail_controller.update_detail(session, detail, updated_detail)


@router.delete("/{detail_id}")
def delete_detail(detail_id: int):
    detail = detail_controller.get_detail(session, detail_id)
    if not detail:
        raise HTTPException(status_code=404, detail="Detail not found")
    return detail_controller.delete_detail(session, detail)
