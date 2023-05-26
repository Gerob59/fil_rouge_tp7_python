from sqlalchemy import Column, Integer, Numeric
from config.sqlalchemy import Base


class Vignette(Base):
    __tablename__ = "t_poidsv"

    id = Column(Integer, primary_key=True)
    valmin = Column(Numeric, default=0)
    valtimbre = Column(Numeric, default=0)
