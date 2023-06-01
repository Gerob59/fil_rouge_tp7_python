from sqlalchemy import Column, String, Integer, Index, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from .departement import Departement

from config import Base


class Commune(Base):
    __tablename__ = "t_communes"

    id = Column(Integer, primary_key=True)
    dep: Mapped["Departement"] = mapped_column(String(2), ForeignKey('t_dept.code_dept'))
    cp = Column(String(5), default=None)
    ville = Column(String(50), default=None)

    __table_args__ = (Index('commune_index', "dep", "cp", "ville"),)
