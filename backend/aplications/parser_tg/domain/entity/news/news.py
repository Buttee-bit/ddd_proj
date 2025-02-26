from dataclasses import dataclass, field
from datetime import datetime
from backend.aplications.parser_tg.domain.entity.base import BaseEntity
from backend.aplications.parser_tg.domain.values.title import Title


@dataclass
class News(BaseEntity):
    title: Title
    text: str
    media_url: set = field(default_factory=set, kw_only=True)
    published_at: datetime
