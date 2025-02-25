from dataclasses import dataclass, field
from backend.aplications.parser_tg.domain.entity.base import BaseEntity



@dataclass
class ChannelEntity(BaseEntity):
    name: str
    description: str
    url: str
    news: set = field(default_factory=lambda: set())
