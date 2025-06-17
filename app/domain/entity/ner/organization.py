from dataclasses import dataclass
from app.domain.entity.ner.person import NerPeople


@dataclass
class NerOrganization(NerPeople):
    ...