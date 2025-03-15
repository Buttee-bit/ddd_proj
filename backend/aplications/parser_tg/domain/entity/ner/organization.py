from dataclasses import dataclass
from backend.aplications.parser_tg.domain.entity.ner.person import NerPeople


@dataclass
class NerOrganization(NerPeople):
    ...