from .conditionnement_base_schema import ConditionnementBase
from .detail_base_schema import DetailBase
from .objet_schema import ObjetBase


class DetailSchema(DetailBase):
    objets: list[ObjetBase]
    conditionnements: list[ConditionnementBase]

