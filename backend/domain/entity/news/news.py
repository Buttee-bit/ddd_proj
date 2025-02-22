from dataclasses import dataclass, field
from datetime import datetime
from backend.domain.entity.base import BaseEntity
from backend.domain.values.title import Title



@dataclass
class News(BaseEntity):
    title: Title
    text: str
    media_url: list = field(default_factory=lambda: [])
    published_at: datetime
    chanel: str
