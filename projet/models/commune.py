from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from .commune_base import CommuneBase
from .departement_base import DepartementBase


class Commune(CommuneBase):
    dep: Mapped["DepartementBase"] = mapped_column(String(2), ForeignKey('t_dept.code_dept'))
