from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Iterable
from motor.core import AgnosticClient

from backend.aplications.parser_tg.domain.entity.news.news import News
from backend.aplications.parser_tg.domain.entity.channel.channel import Channel
from backend.aplications.parser_tg.logic.queries.base import BaseQuery


class BaseChannelRepository(ABC):
    @abstractmethod
    async def add_channel(self, channel: Channel) -> None:
        ...

    @abstractmethod
    async def get_channel(self) -> Channel:
        ...

    @abstractmethod
    async def get_all_channels_with_filter(self, limit: int, offset: int) -> Iterable[Channel]:
        ...
    @abstractmethod
    async def get_all_channels(self) -> Iterable[Channel]:
        ...

class BaseNewsRepository(ABC):
    @abstractmethod
    async def add_news(self, news: str) -> None:
        ...

    @abstractmethod
    async def get_one_news(self) -> News:
        ...


@dataclass
class BaseMongoDBRepository(ABC):
    mongo_db_client: AgnosticClient
    mongo_db_db_name: str
    mongo_db_collection_name: str


    @property
    def _collection(self):
        return self.mongo_db_client[self.mongo_db_db_name][
            self.mongo_db_collection_name
        ]