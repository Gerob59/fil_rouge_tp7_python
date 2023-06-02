from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import Departement
from ..schemas import DepartementSchema


def get_departement(db: Session, code_dept: str) -> DepartementSchema:
    '''
        retourne un departement en fonction d'un id donné
        :param db: Session
        :param code_dept: str
        :return: DepartementSchema
    '''
    with db:
        departement_db = db.query(Departement).get(code_dept)
        if not departement_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Departement not found")
    return DepartementSchema.from_orm(departement_db)


def get_all_departements(db: Session) -> [DepartementSchema]:
    '''
        retourne tous les departements de la bdd
        :param db: Session
        :return: [DepartementSchema]
    '''
    with db:
        resultat = db.query(Departement).all()
    return resultat


def create_departement(db: Session, departement: DepartementSchema) -> DepartementSchema:
    '''
        ajoute un nouveau departement en bdd
        :param db: Session
        :param departement: DepartementSchema
        :return: DepartementSchema
    '''
    with db:
        departement_db = Departement(**departement.dict())
        db.add(departement_db)
        db.commit()  # pas forcément obligatoire
        db.refresh(departement_db)
    return DepartementSchema.from_orm(departement_db)


def update_departement(db: Session, code_dept: str, updated_departement: DepartementSchema) -> DepartementSchema:
    '''
        modifie un client en bdd
        :param db: Session
        :param code_dept: int
        :param updated_departement: ClientSchema
        :return: DepartementSchema
    '''
    with db:
        departement_db = db.query(Departement).get(code_dept)
        if not departement_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Departement not found")
        updated_data = updated_departement.dict(exclude_unset=True)
        for attr, value in updated_data.items():
            if hasattr(departement_db, attr):
                setattr(departement_db, attr, value)
        db.commit()
        db.refresh(departement_db)
    return DepartementSchema.from_orm(departement_db)


def delete_departement(db: Session, code_dept: str) -> dict:
    '''
        supprime un departement en bdd
        :param db: Session
        :param code_dept: str
        :return: dict
    '''
    with db:
        departement_db = db.query(Departement).get(code_dept)
        if not departement_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Departement not found")
        db.delete(departement_db)
        db.commit()
    return {"message": f"Departement deleted"}
