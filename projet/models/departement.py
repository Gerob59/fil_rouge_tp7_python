from .commune import Commune
from sqlalchemy.orm import relationship, Mapped

from .departement_base import DepartementBase


class Departement(DepartementBase):
    communes: Mapped[list["Commune"]] = relationship()
