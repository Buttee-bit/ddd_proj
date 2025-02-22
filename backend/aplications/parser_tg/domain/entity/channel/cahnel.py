from dataclasses import dataclass
from backend.aplications.parser_tg.domain.entity.base import BaseEntity



@dataclass
class Channel(BaseEntity):
    name: str
    description: str
    url: str

