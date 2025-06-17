import logging
from dataclasses import dataclass
from app.domain.entity.channel.channel import Channel
from app.domain.entity.news.news import News
from app.infra.repositoryes.base import BaseMongoDBRepository
from app.infra.repositoryes.channels.base import BaseChannelRepository
from app.infra.repositoryes.channels.converter import convert_channel_document_to_entity, convert_channel_entity_to_document
from app.infra.repositoryes.errors.exist import ExisInDBError
from app.infra.repositoryes.filters.channels import GetAllChannelsFilters
from app.infra.repositoryes.errors.exist import ExisInDBError


@dataclass
class ChannelsRepository(BaseChannelRepository, BaseMongoDBRepository):

    async def add_channel(self, url: str, subscribers:int, title:str, id_channel:int) -> Channel:
        channel = await self.chek_exis_channel(url=url)
        if channel:
            raise ExisInDBError(value=channel.url)
        else:
            channel = Channel(url=url, id_channel=id_channel, subscribers=subscribers, title=title)
            await self._collection.insert_one(convert_channel_entity_to_document(channel))
            return channel

    async def chek_exis_channel(self, url) -> Channel|bool:
        filter = {
            'url':url,
        }
        channel = await self._collection.find_one(
            filter=filter
        )
        if channel: return convert_channel_document_to_entity(channel)
        else: return False

    async def get_channel(self, oid:str) -> News:
        document = await self._collection.find_one(
            filter={'oid':oid}
        )
        return convert_channel_document_to_entity(document)

    async def get_all_channels_with_filter(self, filters: GetAllChannelsFilters) -> list[Channel]:
        documents = self._collection.find().skip(filters.offset).limit(filters.limit)
        return [convert_channel_document_to_entity(document) async for document in documents]

    async def get_all_channels(self) -> list[Channel]:
        documents = self._collection.find()
        return [convert_channel_document_to_entity(document) async for document in documents]

    async def update_channel_info(self, url_channel: str, data:dict):
        filter = {
            'url':url_channel
        }
        await self._collection.update_one(
            filter=filter,
            update={'$set': data}
        )