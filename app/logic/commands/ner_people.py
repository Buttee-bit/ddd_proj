from dataclasses import dataclass
import logging
from typing import List

from app.domain.entity.ner.entity import Ner
from app.domain.entity.ner.person import NerPeople
from app.infra.analizer.base import BaseAnalazer

from app.infra.repositoryes.ners.factory.base import NerFactory
from app.infra.repositoryes.news.base import BaseNewsRepository
from app.logic.commands.base import CommandHandler
from app.infra.analizer.converters import (
    convert_analysis_result,
)
from app.logic.commands.base import (
    BaseCommand,
    CommandHandler,
)
from app.infra.repositoryes.ners.people import PeopleNerRepository

@dataclass(frozen=True)
class AddNerPeopleToDocumentCommand(BaseCommand):
    document_oid: str


@dataclass(frozen=True)
class AddNerPeopleToDocumentHandler(
    CommandHandler[AddNerPeopleToDocumentCommand, NerPeople]
):
    ner_people_repository: PeopleNerRepository
    news_repository: BaseNewsRepository
    analizer: BaseAnalazer

    async def handle(self, command: AddNerPeopleToDocumentCommand) -> None:
        news = await self.news_repository.get_one_news(oid=command.document_oid)
        analis_result = self.analizer.get_result(text=news.text)
        list_ners = convert_analysis_result(result=analis_result)

        # await self.ner_people_repository.add_ner_by_id_document(
        #     id_document=command.document_oid,
        #     ner=[
        #         NerPeople(
        #             value=ner.value,
        #             props=ner.props,
        #             index=ner.index
        #         ) for ner in list_ners
        #     ]
        # )
        # return list_ners



@dataclass(frozen=True)
class NerAnalizeCommand(BaseCommand):
    oid: str
    text: str


@dataclass(frozen=True)
class NerAnalizeHandler(
    CommandHandler[NerAnalizeCommand, NerPeople]
):
    analizer: BaseAnalazer
    ner_factory: NerFactory

    async def handle(self, command: NerAnalizeCommand) -> List[Ner]:
        list_ner = []
        result = await self.analizer.get_result(text=command.text)
        for entity in convert_analysis_result(result=result):
            ner = await self.ner_factory.create_ner(data=entity)
            if ner:
                list_ner.append(ner)
        return list_ner