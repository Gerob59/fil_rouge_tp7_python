from projet.schemas.detail_base_schema import DetailBase
from projet.schemas.objet_base_schema import ObjetBase


class ObjetSchema(ObjetBase):
    details: list[DetailBase]
