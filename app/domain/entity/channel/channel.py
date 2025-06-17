from dataclasses import dataclass, field
from app.domain.entity.base import BaseEntity



@dataclass
class Channel(BaseEntity):
    url: str
    news: set = field(default_factory=set, kw_only=True)
    id_channel: int = field(default_factory=int, kw_only=True)
    subscribers: int = field(default_factory=int, kw_only=True)
    title: str = field(default_factory=str, kw_only=True)