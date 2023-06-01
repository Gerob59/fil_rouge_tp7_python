from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import Role
from ..schemas import RoleSchema, RoleBase


def get_role(db: Session, role_id: int) -> RoleBase:
    with db:
        role_db = db.query(Role).get(role_id)
        if not role_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found")
    return RoleBase.from_orm(role_db)


def get_all_roles(db: Session) -> [RoleBase]:
    with db:
        res_db = db.query(Role).all()
        res = []
        for role in res_db:
            res.append(RoleBase.from_orm(role))

    return res


def create_role(db: Session, role: RoleSchema) -> RoleBase:
    with db:
        role_db = Role(**role.dict())
        db.add(role_db)
        db.commit()
        db.refresh(role_db)
    return RoleBase.from_orm(role_db)


def update_role(db: Session, role_id: int, updated_role: RoleSchema) -> RoleSchema:
    with db:
        role_db = db.query(Role).get(role_id)
        if not role_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found")
        updated_data = updated_role.dict(exclude_unset=True)
        for attr, value in updated_data.items():
            setattr(role_db, attr, value)
        db.commit()
        db.refresh(role_db)
    return RoleSchema.from_orm(role_db)


def delete_role(db: Session, role_id: int) -> dict:
    with db:
        role_db = db.query(Role).get(role_id)
        if not role_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found")
        db.delete(role_db)
        db.commit()
    return {"message": "Role deleted"}
