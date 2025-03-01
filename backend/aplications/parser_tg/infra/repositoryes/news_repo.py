from dataclasses import dataclass
from backend.aplications.parser_tg.domain.entity.news.news import News
from backend.aplications.parser_tg.infra.repositoryes.base import BaseMongoDBRepository, BaseNewsRepository
from backend.aplications.parser_tg.infra.repositoryes.converters import convert_news_entity_to_document, convert_news_document_to_entity


@dataclass
class NewsRepository(BaseNewsRepository, BaseMongoDBRepository):

    async def add_news(self, news: News) -> None:
        await self._collection.insert_one(
            convert_news_entity_to_document(news)
        )

    async def get_one_news(self, oid:str) -> News:
        document = await self._collection.find_one(
            filter={'oid':oid}
        )
        return convert_news_document_to_entity(document)