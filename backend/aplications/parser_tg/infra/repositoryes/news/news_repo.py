from dataclasses import dataclass
from backend.aplications.parser_tg.domain.entity.news.news import News
from backend.aplications.parser_tg.infra.repositoryes.base import BaseMongoDBRepository, BaseNewsRepository
from backend.aplications.parser_tg.infra.repositoryes.news.converters import convert_document_to_entity, convert_entity_to_document


@dataclass
class NewsRepository(BaseNewsRepository, BaseMongoDBRepository):

    async def add_one_news(self, news: News) -> None:
        await self._collection.insert_one(
            convert_entity_to_document(news)
        )

    async def get_one_document(self, oid:str) -> News:
        document = await self._collection.find_one(
            filter={'oid':oid}
        )
        return convert_document_to_entity(document)