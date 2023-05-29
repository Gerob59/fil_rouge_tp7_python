from sqlalchemy import Column, Integer, String
from config.db import Base


class Role(Base):
    __tablename__ = "t_role"

    codrole = Column(Integer, primary_key=True)
    librole = Column(String(25), default=None)
    