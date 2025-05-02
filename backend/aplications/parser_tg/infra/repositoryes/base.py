from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Iterable
from motor.core import AgnosticClient

from backend.aplications.parser_tg.domain.entity.ner.person import NerPeople
from backend.aplications.parser_tg.domain.entity.news.news import News
from backend.aplications.parser_tg.domain.entity.channel.channel import Channel
from backend.aplications.parser_tg.logic.queries.base import BaseQuery


class BaseNerPeopleRepository(ABC):
    @abstractmethod
    async def get_by_id_document(self, text: str) -> NerPeople: ...

    @abstractmethod
    async def add_ner_by_id_document(self, id_document: str, ner: NerPeople) -> None: ...


    @abstractmethod
    async def add_unique_ner(self, ner: Iterable[NerPeople]) -> None:
        ...

class BaseChannelRepository(ABC):
    @abstractmethod
    async def add_channel(self, channel: Channel) -> None: ...

    @abstractmethod
    async def get_channel(self) -> Channel: ...

    @abstractmethod
    async def get_all_channels_with_filter(
        self, limit: int, offset: int
    ) -> Iterable[Channel]: ...

    @abstractmethod
    async def get_all_channels(self) -> Iterable[Channel]: ...


class BaseNewsRepository(ABC):
    @abstractmethod
    async def add_news(self, news: str) -> None: ...

    @abstractmethod
    async def get_one_news(self, oid: str) -> News: ...


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
