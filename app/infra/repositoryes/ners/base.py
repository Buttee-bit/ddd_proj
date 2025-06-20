from abc import ABC, abstractmethod
from dataclasses import dataclass
import dataclasses
import logging
from typing import Iterable

from app.domain.entity.ner.entity import Ner
from app.domain.entity.news.news import News
from app.infra.repositoryes.base import BaseMongoDBRepository
from app.infra.repositoryes.ners.converters import convert_document_to_ner, convert_ner_to_document

@dataclass
class BaseNerRepository(ABC):

    @abstractmethod
    async def add_ner(self, ner: Ner) -> None: ...

    @abstractmethod
    async def get_one_ner(self, oid: str) -> Ner: ...

    @abstractmethod
    async def get_one_ner_by_value(self, value: str) -> Ner: ...

    @abstractmethod
    async def get_ners(offset:int, limit:int) -> tuple[Iterable[Ner], int]: ...

    @abstractmethod
    async def update_ner_info(ner:Ner) -> Ner:
        ...

@dataclass
class DefaultNerRepository(BaseNerRepository, BaseMongoDBRepository):

    async def add_ner(self, ner: Ner) -> None:
        document = convert_ner_to_document(data=ner)
        await self._collection.insert_one(document=document)

    async def get_one_ner(self, oid: str) -> Ner: ...

    async def get_one_ner_by_value(self, value: str) -> Ner:
        filter = {
            'value':value
        }
        ner = await self._collection.find_one(filter=filter)
        if ner:
            return convert_document_to_ner(document=ner)
        else:
            return None

    async def get_ners(offset:int, limit:int) -> tuple[Iterable[Ner], int]: ...

    async def update_ner_info(self, ner:Ner):
        try:
            filter = {'oid': ner.oid}
            await self._collection.update_one(filter=filter, update={'$set':convert_ner_to_document(data=ner)})
        except Exception as e:
            logging.warning(f'e; {e}')