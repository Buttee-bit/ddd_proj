from dataclasses import dataclass
from typing import Iterable

from app.domain.entity.news.news import News
from app.infra.repositoryes.channels.base import BaseChannelRepository
from app.infra.repositoryes.news.base import BaseNewsRepository
from app.logic.queries.base import BaseQuery, BaseQueryHandler


@dataclass(frozen=True)
class GetNewsLatestQuery(BaseQuery):
    offset: int
    limit: int
    ...


@dataclass(frozen=True)
class GetNewslatestHandler(BaseQueryHandler):
    channels_repository: BaseChannelRepository
    news_repository: BaseNewsRepository

    async def handle(self, query: GetNewsLatestQuery) -> tuple[Iterable[News], int]:
        return await self.news_repository.get_news(
            offset=query.offset,
            limit=query.limit)