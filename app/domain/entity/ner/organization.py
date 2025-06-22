from dataclasses import dataclass
from app.domain.entity.ner.person import NerPeople

# TODO не использую нафиг с пляжа
@dataclass
class NerOrganization(NerPeople):
    ...