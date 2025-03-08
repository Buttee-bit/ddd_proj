from dataclasses import dataclass, field
from datetime import datetime
from backend.aplications.parser_tg.domain.entity.base import BaseEntity

@dataclass
class News(BaseEntity):
    title: str
    text: str
    published_at: datetime
    media_url: set = field(default_factory=set, kw_only=True)
    oid_channel: str