from dataclasses import dataclass
from datetime import datetime
import logging

from app.domain.entity.object.object import ObjectDomain
from app.infra.repositoryes.ners.base import BaseNerRepository
from app.infra.repositoryes.object.mongo_object import BaseObjectDomainRepository
from app.logic.commands.base import BaseCommand, CommandHandler

@dataclass(frozen=True)
class CreateObjectCommand(BaseCommand):
    name: str


@dataclass(frozen=True)
class CreateObjectCommandHandler(CommandHandler[CreateObjectCommand, ObjectDomain]):
    object_repository: BaseObjectDomainRepository

    async def handle(self, command: CreateObjectCommand) -> ObjectDomain:
        eixcst_object = await self.object_repository.get_by_name(name=command.name)
        if eixcst_object:
            return eixcst_object
        else:
            object_ = ObjectDomain(main_name=command.name)
            await self.object_repository.add(object_=object_)
            return object_


@dataclass(frozen=True)
class UpdateNerOrganizationObjectCommand(BaseCommand):
    type: str
    oid_domain_object: str
    oid_ner: str

@dataclass(frozen=True)
class UpdateNerOrganizationObjectCommandHandler(CommandHandler[UpdateNerOrganizationObjectCommand, ObjectDomain]):
    object_repository: BaseObjectDomainRepository
    ner_repository: BaseNerRepository

    async def handle(self, command: UpdateNerOrganizationObjectCommand):
        logging.warning(f'command: {command}')
        ner = await self.ner_repository.get_one_ner(oid=command.oid_ner)
        object_ = await self.object_repository.get_one(oid=command.oid_domain_object)
        # TODO Заменить
        if command.type =='add':
            object_.add_ner(ner)
            await self.object_repository.add_ner(ner_oid=command.oid_ner, object_oid=command.oid_domain_object)
            return object_

        # TODO Заменить
        if command.type == 'del':
            object_.delete_ner(ner=ner)
            return super().handle(command)