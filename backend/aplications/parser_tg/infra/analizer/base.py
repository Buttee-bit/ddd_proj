from abc import abstractmethod
from dataclasses import dataclass
from backend.pullenti.ner.ServerService import ServerService
from backend.pullenti.morph.MorphLang import MorphLang
from backend.pullenti.ner.ProcessorService import ProcessorService
from backend.pullenti.ner.Analyzer import Analyzer
from backend.pullenti.ner.AnalysisResult import AnalysisResult


@dataclass(frozen=True)
class BaseAnalazer:
    address_: str

    @property
    def _get_service(self) -> ServerService:
        return ServerService

    @abstractmethod
    def get_result(self, text:str) -> AnalysisResult:
        ...