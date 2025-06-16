from dataclasses import dataclass
import logging

from backend.aplications.parser_tg.domain.entity.ner.person import NerPeople
from backend.aplications.parser_tg.infra.analizer.base import BaseAnalazer
from backend.aplications.parser_tg.infra.repositoryes.base import (
    BaseNerPeopleRepository,
    BaseNewsRepository,
)
from backend.aplications.parser_tg.logic.commands.base import CommandHandler
from backend.aplications.parser_tg.infra.analizer.converters import (
    convert_analysis_result_to_ners,
)
from backend.aplications.parser_tg.logic.commands.base import (
    BaseCommand,
    CommandHandler,
)


@dataclass(frozen=True)
class AddNerPeopleToDocumentCommand(BaseCommand):
    document_oid: str


@dataclass(frozen=True)
class AddNerPeopleToDocumentHandler(
    CommandHandler[AddNerPeopleToDocumentCommand, NerPeople]
):
    ner_people_repository: BaseNerPeopleRepository
    news_repository: BaseNewsRepository
    analizer: BaseAnalazer

    async def handle(self, command: AddNerPeopleToDocumentCommand) -> None:
        news = await self.news_repository.get_one_news(oid=command.document_oid)
        analis_result = self.analizer.get_result(text=news.text)
        list_ners = convert_analysis_result_to_ners(result=analis_result)

        await self.ner_people_repository.add_ner_by_id_document(
            id_document=command.document_oid,
            ner=[
                NerPeople(
                    value=ner.value,
                    props=ner.props,
                    index=ner.index
                ) for ner in list_ners
            ]
        )
        return list_ners



@dataclass(frozen=True)
class FindPeopleCommand(BaseCommand):
    oid: str
    text: str


@dataclass(frozen=True)
class FindPeopleHandler(
    CommandHandler[FindPeopleCommand, NerPeople]
):
    ner_people_repository: BaseNerPeopleRepository
    news_repository: BaseNewsRepository
    unique_ner_repository: BaseNerPeopleRepository
    analizer: BaseAnalazer

    async def handle(self, command: FindPeopleCommand) -> None:
        result = self.analizer.get_result(text=command.text)
        logging.warning(f'result: {result}')
        list_ners = convert_analysis_result_to_ners(result=result)
        # await self.ner_people_repository.add_ner_by_id_document(
        #     id_document=command.oid,
        #     ner=[
        #         NerPeople(
        #             value=ner.value,
        #             props=ner.props,
        #             index=ner.index
        #         ) for ner in list_ners
        #     ]
        # )
        await self.unique_ner_repository.add_unique_ner(ner=list_ners)
        return list_ners