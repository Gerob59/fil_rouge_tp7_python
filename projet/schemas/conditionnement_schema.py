from projet.schemas.conditionnement_base_schema import ConditionnementBase
from projet.schemas.detail_base_schema import DetailBase


class ConditionnementSchema(ConditionnementBase):
    details: list[DetailBase]
