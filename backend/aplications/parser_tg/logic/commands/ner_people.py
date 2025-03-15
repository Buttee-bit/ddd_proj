from dataclasses import dataclass

from backend.aplications.parser_tg.domain.entity.ner.person import NerPeople
from backend.aplications.parser_tg.infra.analizer.base import BaseAnalazer
from backend.aplications.parser_tg.infra.repositoryes.base import (
    BaseNerPeopleRepository,
    BaseNewsRepository,
)
from backend.aplications.parser_tg.logic.commands.base import CommandHandler


@dataclass(frozen=True)
class AddNerPeopleToDocumentCommand:
    document_oid: str
    ner_value: str
    props: list[str]
    index: list[list[int]]


dataclass(frozen=True)
class AddNerPeopleToDocumenthandler(CommandHandler[AddNerPeopleToDocumentCommand]):
    ner_people_repository: BaseNerPeopleRepository
    news_repository: BaseNewsRepository
    analizer: BaseAnalazer

    async def handle(self, command: AddNerPeopleToDocumentCommand) -> None:
        news = await self.news_repository.get_one_news(oid=command.document_oid)
        text = news.text

        await self.ner_people_repository.add_ner_by_id_document(
            id_document=command.document_id,
            ner=NerPeople(
                value=command.ner_value, props=command.props, index=command.index
            ),
        )