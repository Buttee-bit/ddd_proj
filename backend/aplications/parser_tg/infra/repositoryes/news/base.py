from abc import ABC, abstractmethod
from typing import Iterable

from backend.aplications.parser_tg.domain.entity.news.news import News


class BaseNewsRepository(ABC):
    @abstractmethod
    async def add_news(self, news: str) -> None: ...

    @abstractmethod
    async def get_one_news(self, oid: str) -> News: ...

    @abstractmethod
    async def get_news(offset:int, limit:int) -> tuple[Iterable[News], int]: ...