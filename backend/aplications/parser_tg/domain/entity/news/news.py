from dataclasses import dataclass, field
from datetime import datetime
from backend.aplications.parser_tg.domain.entity.base import BaseEntity
from backend.aplications.parser_tg.domain.values.news.text import Text
from backend.aplications.parser_tg.domain.values.news.title import Title

@dataclass
class News(BaseEntity):
    title: Title
    text: Text
    published_at: datetime
    media_url: set = field(default_factory=set, kw_only=True)
    id_channel: int
