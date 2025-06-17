from dataclasses import dataclass, field
from datetime import datetime
from app.domain.entity.base import BaseEntity
from app.domain.values.news.text import Text
from app.domain.values.news.title import Title

@dataclass
class News(BaseEntity):
    title: Title
    text: Text
    published_at: datetime
    media_url: set = field(default_factory=set, kw_only=True)
    id_channel: int
