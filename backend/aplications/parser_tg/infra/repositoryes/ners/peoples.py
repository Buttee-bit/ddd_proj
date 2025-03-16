from dataclasses import dataclass
import logging

from backend.aplications.parser_tg.domain.entity.ner.person import NerPeople
from backend.aplications.parser_tg.infra.repositoryes.base import BaseMongoDBRepository, BaseNerPeopleRepository
from backend.aplications.parser_tg.infra.repositoryes.ners.converters import convert_ner_people_to_document


@dataclass
class NerPeoplesRepository(BaseNerPeopleRepository, BaseMongoDBRepository):

    async def get_by_id_document(self, id_document: str) -> NerPeople:
        document = self._collection.find_one(
            filter={
                "id_document": id_document
            }
        )

    async def add_ner_by_id_document(self, id_document: str, ner: list[NerPeople]) -> None:
        logging.warning(f'id_document: {id_document}, ner: {ner}')
        if ner == []:
            return None
        await self._collection.insert_one(
            {
                "id_document": id_document,
                "ner": convert_ner_people_to_document(ner)
            }
        )


