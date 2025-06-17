from dataclasses import dataclass
from typing import Iterable

from app.domain.entity.channel.channel import Channel

from app.infra.repositoryes.channels.base import BaseChannelRepository
from app.infra.repositoryes.filters.channels import GetAllChannelsFilters
from app.infra.tracing.handler import trace_custom
from app.logic.queries.base import BaseQuery, BaseQueryHandler


@dataclass(frozen=True)
class GetChannelsQueryWithFilter(BaseQuery):
    filters: GetAllChannelsFilters


@dataclass(frozen=True)
class GetChannelQueryWithilterHandler(BaseQueryHandler):
    channels_repository: BaseChannelRepository

    @trace_custom(name="GetChannelQueryWithilterHandler")
    async def handle(self, query: GetChannelsQueryWithFilter) -> Iterable[Channel]:
        channels = await self.channels_repository.get_all_channels_with_filter(filters=query.filters)
        return channels


@dataclass(frozen=True)
class GetChannelsQuery(BaseQuery):
    ...


@dataclass(frozen=True)
class GetChannelQueryHandler(BaseQueryHandler):
    channels_repository: BaseChannelRepository

    @trace_custom(name="GetChannelQueryHandler")
    async def handle(self, query: GetChannelsQuery) -> Iterable[Channel]:
        channels = await self.channels_repository.get_all_channels()
        return channels