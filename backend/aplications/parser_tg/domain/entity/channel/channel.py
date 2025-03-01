from dataclasses import dataclass, field
from backend.aplications.parser_tg.domain.entity.base import BaseEntity



@dataclass
class Channel(BaseEntity):
    url: str
    news: set = field(default_factory=set, kw_only=True)
