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

    @classmethod
    def create_news(cls, data:dict) -> "News":
        return cls(
            oid = data['oid'],
            created_at = data['created_at'],
            title = Title(value=data['title']).as_generic_type(),
            text = Text(value=data['text']).as_generic_type(),
            published_at = data['published_at'],
            media_url = data['media_url'],
            id_channel = data['id_channel'],
        )