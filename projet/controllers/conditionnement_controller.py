from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import Conditionnement
from ..schemas import ConditionnementSchema


def get_conditionnement(db: Session, conditionnement_id: int) -> ConditionnementSchema:
    '''
        retourne un conditionnement en fonction d'un id donné
        :param db: Session
        :param conditionnement_id: int
        :return: ConditionnementSchema
        '''
    with db:
        conditionnement_db = db.query(Conditionnement).get(conditionnement_id)
        if not conditionnement_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conditionnement not found")
    return ConditionnementSchema.from_orm(conditionnement_db)


def get_all_conditionnements(db: Session) -> [ConditionnementSchema]:
    '''
        retourne tous les conditionnements de la bdd
        :param db: Session
        :return: [ConditionnementSchema]
    '''
    with db:
        resultat = db.query(Conditionnement).all()
    return resultat


def create_conditionnement(db: Session, conditionnement: ConditionnementSchema) -> ConditionnementSchema:
    '''
        ajoute un nouveau conditionnement en bdd
        :param db: Session
        :param conditionnement: ConditionnementSchema
        :return: ConditionnementSchema
    '''
    with db:
        conditionnement_db = Conditionnement(**conditionnement.dict())
        db.add(conditionnement_db)
        db.commit()
        db.refresh(conditionnement_db)
    return ConditionnementSchema.from_orm(conditionnement_db)


def update_conditionnement(db: Session, conditionnement_id: int,
                           updated_conditionnement: ConditionnementSchema) -> ConditionnementSchema:
    '''
        modifie un conditionnement en bdd
        :param db: Session
        :param conditionnement_id: int
        :param updated_conditionnement: ConditionnementSchema
        :return: ConditionnementSchema
    '''
    with db:
        conditionnement_db = db.query(Conditionnement).get(conditionnement_id)
        if not conditionnement_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conditionnement not found")
        updated_data = updated_conditionnement.dict(exclude_unset=True)
        for attr, value in updated_data.items():
            setattr(conditionnement_db, attr, value)
        db.commit()
        db.refresh(conditionnement_db)
    return ConditionnementSchema.from_orm(conditionnement_db)


def delete_conditionnement(db: Session, conditionnement_id: int) -> dict:
    '''
        supprime un conditionnement en bdd
        :param db: Session
        :param conditionnement_id: int
        :return: dict
    '''
    with db:
        conditionnement_db = db.query(Conditionnement).get(conditionnement_id)
        if not conditionnement_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conditionnement not found")
        db.delete(conditionnement_db)
        db.commit()
    return {"message": "Conditionnement deleted"}
