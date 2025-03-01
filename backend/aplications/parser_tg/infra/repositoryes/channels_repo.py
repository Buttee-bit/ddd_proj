from dataclasses import dataclass
from backend.aplications.parser_tg.domain.entity.channel.channel import Channel
from backend.aplications.parser_tg.domain.entity.news.news import News
from backend.aplications.parser_tg.infra.repositoryes.base import BaseMongoDBRepository, BaseChannelRepository
from backend.aplications.parser_tg.infra.repositoryes.converters import convert_channel_document_to_entity, convert_channel_entity_to_document


@dataclass
class ChannelsRepository(BaseChannelRepository, BaseMongoDBRepository):

    async def add_channel(self, channel: Channel) -> None:
        await self._collection.insert_one(
            convert_channel_entity_to_document(channel)
        )

    async def get_channel(self, oid:str) -> News:
        document = await self._collection.find_one(
            filter={'oid':oid}
        )
        return convert_channel_document_to_entity(document)