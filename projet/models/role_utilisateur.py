from sqlalchemy import Column, Integer, ForeignKey
from config.db import Base


class RoleUtilisateur(Base):
    __tablename__ = "t_utilisateur_role"

    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey('t_utilisateur.code_utilisateur'))
    role_id = Column(Integer, ForeignKey('t_role.codrole'))
