from dataclasses import dataclass
import logging
from typing import Iterable
from app.domain.entity.news.news import News
from app.infra.repositoryes.base import BaseMongoDBRepository
from app.infra.repositoryes.converters import convert_news_entity_to_document, convert_news_document_to_entity
from app.infra.repositoryes.news.base import BaseNewsRepository


@dataclass
class NewsRepository(BaseNewsRepository, BaseMongoDBRepository):

    async def add_news(self, news: News) -> None:
        try:
            await self._collection.insert_one(
                convert_news_entity_to_document(news)
            )
        except Exception as e:
            logging.warning(f'e: {e}')
    async def get_one_news(self, oid:str) -> News:
        document = await self._collection.find_one(
            filter={'oid':oid}
        )
        return convert_news_document_to_entity(document)

    async def get_news(self, offset:int, limit:int) -> tuple[Iterable[News], int]:
        cursor = self._collection.find().limit(limit=limit).skip(skip=offset)
        news = [
            convert_news_document_to_entity(document=news_document)
            async for news_document in cursor
        ]
        count = await self._collection.count_documents(filter={})
        return news, count