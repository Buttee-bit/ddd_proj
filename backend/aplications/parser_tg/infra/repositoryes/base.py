from dataclasses import dataclass
from abc import ABC, abstractmethod
from backend.aplications.parser_tg.domain.entity.news.news import News
from backend.aplications.parser_tg.domain.entity.channel.entity import ChannelEntity


class BaseChannelRepository(ABC):
    @abstractmethod
    def add_channel(self, channel: str) -> None:
        ...

    @abstractmethod
    def get_channel(self) -> ChannelEntity:
        ...

class BaseNewsRepository(ABC):
    @abstractmethod
    def add_news(self, news: str) -> None:
        ...

    @abstractmethod
    def get_one_news(self) -> News:
        ...