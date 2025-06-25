from datetime import datetime
import logging

from dataclasses import dataclass, asdict

from app.infra.repositoryes.base import BaseMongoDBRepository
from app.infra.repositoryes.object.base import BaseObjectDomainRepository


from app.infra.repositoryes.errors.exist import ExisInDBError
from app.domain.entity.object.object import ObjectDomain
from app.infra.repositoryes.errors.exist import ExisInDBError
from app.infra.repositoryes.object.converters import convert_document_to_Main_Object


@dataclass
class ObjectsRepository(BaseObjectDomainRepository, BaseMongoDBRepository):

    async def add(self, object_: ObjectDomain) -> ObjectDomain:
        await self._collection.insert_one(document=asdict(object_))
        return object_

    async def get_one(self, oid) -> ObjectDomain:
        filter = {"oid": oid}
        document = await self._collection.find_one(filter=filter)
        if document:
            return convert_document_to_Main_Object(document=document)
        else:
            ExisInDBError(value=oid)

    async def get_by_name(self, name: str) -> ObjectDomain|None:
        filter_ = {"main_name": name}
        document = await self._collection.find_one(filter=filter_)
        if document:
            return convert_document_to_Main_Object(document=document)
        else:
            logging.warning(f"ничерта нет")

    async def add_ner(self, object_oid, ner_oid):
        filter = {'oid':object_oid}
        await self._collection.update_one(filter=filter,
                                          update={'$set':{'ners':ner_oid, 'updatet_at':datetime.now()}})


    async def get_many(offset, limit):
        return await super().get_many(limit)
