from dataclasses import dataclass
from typing import Iterable

from backend.aplications.parser_tg.domain.entity.channel.channel import Channel

from backend.aplications.parser_tg.infra.repositoryes.base import BaseChannelRepository
from backend.aplications.parser_tg.infra.repositoryes.filters.channels import GetAllChannelsFilters
from backend.aplications.parser_tg.infra.tracing.handler import trace_custom
from backend.aplications.parser_tg.logic.queries.base import BaseQuery, BaseQueryHandler

# from domain.entities.messages import (
#     Chat,
#     ChatListener,
#     Message,
# )
# from infra.repositories.filters.messages import (
#     GetAllChatsFilters,
#     GetMessagesFilters,
# )
# from infra.repositories.messages.base import (
#     BaseChatsRepository,
#     BaseMessagesRepository,
# )
# from logic.exceptions.messages import ChatNotFoundException
# from logic.queries.base import (
#     BaseQuery,
#     BaseQueryHandler,
# )




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