from abc import ABC, abstractmethod
from typing import Iterable

from app.domain.entity.object.object import ObjectDomain


class BaseObjectDomainRepository(ABC):
    @abstractmethod
    async def add(self, news: str) -> ObjectDomain: ...

    @abstractmethod
    async def get_one(self, oid: str) -> ObjectDomain: ...

    @abstractmethod
    async def get_many(offset:int, limit:int) -> tuple[Iterable[ObjectDomain], int]: ...