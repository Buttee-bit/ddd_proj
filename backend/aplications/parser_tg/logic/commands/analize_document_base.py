from dataclasses import dataclass
from backend.aplications.parser_tg.infra.analizer.base import BaseAnalazer
from backend.aplications.parser_tg.infra.repositoryes.base import BaseNerPeopleRepository, BaseNewsRepository
from backend.aplications.parser_tg.logic.commands.base import CommandHandler
from pullenti.ner.ServerService import ServerService
from pullenti.ner.AnalysisResult import AnalysisResult


@dataclass(frozen=True)
class AnalyzeDocumentBaseCommand:
    document_id: str
    analizer: ServerService



@dataclass(frozen=True)
class AnalyzeDocumentBaseCommandHandler(CommandHandler[AnalyzeDocumentBaseCommand]):
    news_repository: BaseNewsRepository

    async def handle(self, command: AnalyzeDocumentBaseCommand):
        ...
