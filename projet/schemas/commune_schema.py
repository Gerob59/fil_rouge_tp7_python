from typing import Optional
from pydantic import BaseModel
from pydantic.types import constr
from .departement_schema import DepartementSchema


class CommuneSchema(BaseModel):
    id: Optional[int]
    dep: DepartementSchema
    cp: constr(max_length=5) = None
    ville: constr(max_length=50) = None

    class Config:
        orm_mode = True
