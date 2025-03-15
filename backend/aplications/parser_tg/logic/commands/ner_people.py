from dataclasses import dataclass
import logging

from backend.aplications.parser_tg.domain.entity.ner.person import NerPeople
from backend.aplications.parser_tg.infra.analizer.base import BaseAnalazer
from backend.aplications.parser_tg.infra.repositoryes.base import (
    BaseNerPeopleRepository,
    BaseNewsRepository,
)
from backend.aplications.parser_tg.logic.commands.base import CommandHandler
from backend.aplications.parser_tg.infra.analizer.converters import convert_analysis_result_to_ners

@dataclass(frozen=True)
class AddNerPeopleToDocumentCommand:
    document_oid: str


dataclass(frozen=True)
class AddNerPeopleToDocumenthandler(CommandHandler[AddNerPeopleToDocumentCommand]):
    ner_people_repository: BaseNerPeopleRepository
    news_repository: BaseNewsRepository
    analizer: BaseAnalazer

    async def handle(self, command: AddNerPeopleToDocumentCommand) -> None:
        news = await self.news_repository.get_one_news(oid=command.document_oid)
        analis_result = self.analizer.get_result(text=news.text)
        list_ners = convert_analysis_result_to_ners(analis_result=analis_result)
        logging.warning(f'list_ners: {list_ners}')

        await self.ner_people_repository.add_ner_by_id_document(
            id_document=command.document_oid,
            ner=NerPeople(
                value=command.ner_value, props=command.props, index=command.index
            ),
        )