from dataclasses import dataclass, field
from datetime import datetime
from backend.aplications.parser_tg.domain.entity.base import BaseEntity
from backend.aplications.parser_tg.domain.entity.channel.channel import Channel

@dataclass
class News(BaseEntity):
    title: str
    text: str
    published_at: datetime
    media_url: set = field(default_factory=set, kw_only=True)
    oid_channel: str
    # channel_name: str = field(default_factory=set, kw_only=True)

    # def create_news_for_user(self, channel:Channel):
    #     self.channel_name = channel.url
    #     ...