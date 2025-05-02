from dataclasses import dataclass
import logging
from typing import Iterable

from backend.aplications.parser_tg.domain.entity.ner.person import NerPeople
from backend.aplications.parser_tg.infra.repositoryes.base import (
    BaseMongoDBRepository,
    BaseNerPeopleRepository,
)
from backend.aplications.parser_tg.infra.repositoryes.ners.converters import (
    convert_ner_people_to_document,
    convert_one_ner_to_document,
)


@dataclass
class NerPeoplesRepository(BaseNerPeopleRepository, BaseMongoDBRepository):

    async def get_by_id_document(self, id_document: str) -> NerPeople:
        document = self._collection.find_one(filter={"id_document": id_document})

    async def add_ner_by_id_document(
        self, id_document: str, ner: list[NerPeople]
    ) -> None:
        if ner == []:
            return None
        await self._collection.insert_one(
            {"id_document": id_document, "ner": convert_ner_people_to_document(ner)}
        )

    async def add_unique_ner(self, ner: Iterable[NerPeople]) -> None:
        for ner_ in ner:
            exist_ner = self._collection.find(filter={"value": ner_.value})
            if exist_ner:
                ...
            else:
                await self._collection.insert_one(convert_ner_people_to_document(ner_))


@dataclass
class NerPeoplesUniqueRepository(BaseNerPeopleRepository, BaseMongoDBRepository):

    async def get_by_id_document(self, id_document: str) -> NerPeople:
        document = self._collection.find_one(filter={"id_document": id_document})

    async def add_ner_by_id_document(
        self, id_document: str, ner: list[NerPeople]
    ) -> None:
        if ner == []:
            return None
        await self._collection.insert_one(
            {"id_document": id_document, "ner": convert_ner_people_to_document(ner)}
        )

    async def add_unique_ner(self, ner: Iterable[NerPeople]) -> None:
        logging.warning(f'ner: {ner}')
        for ner_ in ner:
            document = await self._collection.find_one(filter={"value": ner_.value})
            if document:
                logging.warning(f'document: {document}')
                ...
            else:
                await self._collection.insert_one(convert_one_ner_to_document(ner_))
