from abc import ABC, abstractmethod
from typing import Iterable

from app.domain.entity.object.object import ObjectDomain


class BaseObjectDomainRepository(ABC):
    @abstractmethod
    async def add(self, object_: ObjectDomain) -> ObjectDomain: ...


    @abstractmethod
    async def add_ner(self, object_oid: str, ner_oid:str) -> None: ...

    @abstractmethod
    async def get_one(self, oid: str) -> ObjectDomain: ...

    @abstractmethod
    async def get_by_name(self, name:str) -> ObjectDomain: ...

    @abstractmethod
    async def get_many(offset:int, limit:int) -> tuple[Iterable[ObjectDomain], int]: ...